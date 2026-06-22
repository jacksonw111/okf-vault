---
type: "Playbook"
title: "SPA 内嵌 PDF 查看器（react-pdf + Hono 代理）"
description: "在前端 SPA 中以翻页 / 缩放 / 下载的方式逐页渲染第三方 PDF（如东方财富研报、巨潮资讯公告）的端到端实现规范：前端 react-pdf + 后端鉴权代理 + byte-range 透传 + 东财失效链兜底解析。"
tags: "[frontend, pdf, react-pdf, hono, proxy, ssrf, byte-range]"
timestamp: "2026-06-22T07:00:00Z"
---

# SPA 内嵌 PDF 查看器（react-pdf + Hono 代理）

## 适用场景

需要把**第三方**（非自托管）的 PDF 资源——典型如东方财富研报（`pdf.dfcfw.com`）、巨潮资讯公告（`static.cninfo.com.cn`）——**嵌入到自家 SPA 里逐页渲染**，用户不跳出应用、不触发浏览器下载、支持翻页 / 缩放 / 下载。本规范**横跨前后端**：缺前端查看器无法渲染，缺后端代理无法鉴权和绕 CORS。

## 前置条件

- 目标 app 是 **React SPA**（Vite 构建，TanStack Router）。
- 后端框架：**Hono**（落 `apps/server/src/routes/pdf-proxy.ts`）。
- 数据库能查到 `daily_report_item.raw->>'encodeUrl'`（用于东财兜底解析）。
- 用户登录态走 **cookie session**（better-auth 风格），前端 `authClient.useSession()`。
- 依赖版本（pnpm catalog 已固定）：`react-pdf` `10.4.1`、`pdfjs-dist` `5.4.296`。

## 它不是 / 它是

- **不是** PDF 的**生成 / 导出**：本系统不生成 PDF，没有 puppeteer / pdfkit / @react-pdf/renderer 等渲染器；只**消费**远端已有的 PDF。
- **是** 在 SPA 中**逐页渲染** + **下载 / 跳转**远端 PDF 的查看器。

## 关键约束（动机）

1. **CORS**：`pdf.dfcfw.com` / `static.cninfo.com.cn` 不带跨域头，浏览器里 pdfjs 的 fetch（尤其 byte-range 流式请求）会被拦。
2. **东方财富的直链会失效**：`H3_{infoCode}_1.pdf` 形式的直链常返回空 body，需要回到详情页用 `encodeUrl` 解析出真实 `attach_url`——这套解析必须在服务端做（要读 DB + 抓 HTML）。
3. **SSRF**：代理必须限定白名单 host + 强制 https，不能被当成任意 URL 抓取器。

## 全景数据流

```
┌─ 前端 ───────────────────────────────────────────────────────────────┐
│ 入口组件 (路由页 / ReportPdfDialog)                                    │
│   <PdfViewer url={远端PDF直链} />                                       │
│     proxyUrl(url):  命中白名单 host → 改写成                            │
│        {VITE_SERVER_URL}/api/pdf-proxy?url=<encodeURIComponent(原链)>   │
│        否则原样返回                                                     │
│     <Document file={fetchUrl} options={{withCredentials:true}}>        │
│        pdfjs worker 发起 fetch（含 cookie）+ byte-range 请求            │
└──────────────────────────────────┬────────────────────────────────────┘
                                    │ GET /api/pdf-proxy?url=...  (cookie)
┌──────────────────────────────────▼────────────────────────────────────┐
│ 后端 apps/server  pdfProxyHandler                                       │
│   1. auth.api.getSession → 未登录 401                                   │
│   2. 校验 url：必须 https + host ∈ ALLOWED_HOSTS，否则 400              │
│   3. fetchUpstream(url, range)  透传 Range 头                           │
│   4. 若 body 为空(content-length:0) → resolveViaEncodeUrl 兜底：        │
│        从 url 抽 infoCode → DB 查 encodeUrl → 抓东财详情页 →            │
│        正则取 attach_url → 再 fetch（结果缓存 1h）                       │
│   5. 透传 content-type/length/range/etag... + cache-control:private     │
│   6. 回流 upstream.body（支持 206 Partial Content）                     │
└─────────────────────────────────────────────────────────────────────────┘
```

## 步骤

### 1. 前端查看器 `PdfViewer`

#### 1.1 pdfjs worker 配置（模块顶部，必做）

```ts
import { Document, Page, pdfjs } from "react-pdf";
import "react-pdf/dist/Page/AnnotationLayer.css";   // 注释/链接层样式
import "react-pdf/dist/Page/TextLayer.css";          // 文本选择层样式

pdfjs.GlobalWorkerOptions.workerSrc = new URL(
  "pdfjs-dist/build/pdf.worker.min.mjs",
  import.meta.url
).toString();
```

- **worker 必须配置**，否则 pdfjs 在主线程跑会报错 / 卡顿。用 `new URL(..., import.meta.url)` 让 Vite 把 worker 作为资源打包并产出正确 URL——**不需要**在 `vite.config` 里加额外配置（已验证）。
- 两个 CSS 必须 import，否则文本层 / 注释层错位。

#### 1.2 `proxyUrl` —— 决定是否走代理

```ts
const PROXIED_HOSTS = new Set(["pdf.dfcfw.com", "static.cninfo.com.cn"]);
function proxyUrl(target: string): string {
  try {
    const url = new URL(target);
    if (!PROXIED_HOSTS.has(url.hostname)) return target;     // 非白名单直连
    if (url.protocol === "http:") url.protocol = "https:";   // 强制 https（proxy 只收 https）
    return `${env.VITE_SERVER_URL}/api/pdf-proxy?url=${encodeURIComponent(url.toString())}`;
  } catch { return target; }
}
```

- 只有白名单 host 才改写成代理 URL；其他直接喂给 pdfjs。
- **http→https 升级**：历史数据里 cninfo 链接可能是 http，而 proxy 只接受 https；这些旧链可能还躺在前端 TanStack Query 缓存里（1h staleTime）。
- `env.VITE_SERVER_URL` 走 `@ai-financial/env/web`，禁止直接读 `import.meta.env`。

#### 1.3 渲染结构

```tsx
const PDF_OPTIONS = { withCredentials: true };   // 关键：fetch 带 cookie（proxy 要鉴权）

<Document
  file={fetchUrl}
  options={PDF_OPTIONS}
  onLoadSuccess={({ numPages }) => setPages(numPages)}
  onLoadError={(err) => setError(`该研报暂不可用：${err.message}`)}
  loading={<div>加载中...</div>}
>
  {Array.from({ length: pages }, (_, i) => i + 1).map((num) => (
    <div data-page={num} ref={收集到 pageRefs Map}>
      <Page pageNumber={num} scale={scale} renderTextLayer renderAnnotationLayer />
    </div>
  ))}
</Document>
```

- `withCredentials: true` 让 pdfjs 的请求带上 cookie → 后端 `getSession` 才能鉴权（配合 CORS `credentials:true`）。
- 一次性渲染全部页（不是懒加载单页），用一个滚动容器纵向排列。
- 加载 / 错误状态都在 `<Document>` 上处理；错误时整块换成提示文案。

#### 1.4 交互：滚动监听 + 翻页 + 缩放

- **当前页跟踪**：`pages` 就绪后建 `IntersectionObserver`（`root` 是滚动容器，`threshold:[0.25,0.5,0.75]`），取可见比例最高的页设为 `currentPage`。这是项目里少数被允许的 `useEffect`（与非 React 的 IO API 交互）。
- **翻页**：底部悬浮控制条的上 / 下按钮调 `scrollToPage(n)` → `el.scrollIntoView({behavior:"smooth"})`（用 `pageRefs` Map 按页号取 DOM）。
- **缩放**：`scale` state，步长 0.2，区间 `[0.4, 3]`，初值 1.2。
- **下载**：`<a href={fetchUrl} target="_blank">`（指向代理 URL，仍受鉴权保护）。
- 控制条样式：`absolute bottom-4 left-1/2 -translate-x-1/2` 的圆角胶囊，`backdrop-blur`，按钮 `size="icon-sm" variant="ghost"`，图标 `size-4`。

### 2. 后端代理 `pdf-proxy.ts`

#### 2.1 安全闸门（顺序固定）

```ts
const ALLOWED_HOSTS = new Set(["pdf.dfcfw.com", "static.cninfo.com.cn"]);

1. session = auth.api.getSession({ headers });  if (!user) → 401
2. raw = query("url");  if (!raw) → 400 "missing url"
3. new URL(raw) 解析失败 → 400 "invalid url"
4. protocol !== "https:" || !ALLOWED_HOSTS.has(host) → 400 "host not allowed"
```

- **白名单 + 仅 https** 是防 SSRF 的关键：代理只能拉这两个已知主机。新增 PDF 源**必须**同时改前端 `PROXIED_HOSTS` 和后端 `ALLOWED_HOSTS`。

#### 2.2 抓取 + 东财兜底 + 透传

```ts
range = header("range");                          // 透传 byte-range
effectiveUrl = 命中 resolvedCache 且未过期 ? cached.url : raw;
upstream = fetchUpstream(effectiveUrl, range);    // GET, redirect:follow, 带 range

if (isEmptyResponse(upstream)) {                  // content-length === "0"
  resolved = await resolveViaEncodeUrl(raw);      // 见 §2.4
  if (resolved && resolved !== effectiveUrl) upstream = fetchUpstream(resolved, range);
}

if (!upstream.ok && upstream.status !== 206) → 502 "upstream {status}";  // 206 是正常的部分内容

// 透传这些响应头（缺 content-type 时补 application/pdf）：
//   content-type / content-length / content-range / accept-ranges / last-modified / etag
headers.set("cache-control", "private, max-age=300");
return new Response(upstream.body, { status: upstream.status, headers });
```

- **byte-range 透传**是 pdfjs 流式加载大 PDF 的前提（`accept-ranges` + `content-range` + `206`）。删了它大文件会很慢甚至失败。
- `upstream.body` 直接回流（streaming），不在内存里 buffer。

#### 2.3 在 `apps/server/src/index.ts` 挂载 + CORS

```ts
app.use("/*", cors({
  origin: (origin) => env.CORS_ORIGIN.includes(origin) ? origin : env.CORS_ORIGIN[0],
  allowMethods: ["GET", "POST", "OPTIONS"],
  allowHeaders: ["Content-Type", "Authorization"],
  credentials: true,                 // ← 必须 true，否则前端 withCredentials 的 cookie 不被接受
}));
app.get("/api/pdf-proxy", (c) => pdfProxyHandler(c));
```

`credentials:true` ↔ 前端 `withCredentials:true` 是一对，缺一边鉴权就 401。

#### 2.4 东方财富 `encodeUrl` 兜底解析 `resolveViaEncodeUrl`

东财直链 `https://pdf.dfcfw.com/pdf/H3_{infoCode}_1.pdf` 常返回空 body。兜底流程：

```
1. 查 resolvedCache（1h TTL），命中直接返回
2. 从 url path 正则 /\/pdf\/H3_([A-Za-z0-9]+)_1\.pdf$/ 抽 infoCode
3. findEncodeUrlByInfoCode(infoCode)  ← DB：dailyReportItem.raw->>'encodeUrl'
4. 抓详情页 https://data.eastmoney.com/report/zw_macresearch.jshtml?encodeUrl=...
     带 user-agent + referer: https://data.eastmoney.com/
5. 正则 /"attach_url"\s*:\s*"([^"]+)"/ 取真实 PDF URL
6. 校验 attach_url 仍是 https + 白名单 host
7. 写 resolvedCache 后返回
```

- `findEncodeUrlByInfoCode`（`research-report-repository.ts`）从 `daily_report_item.raw` 这个 jsonb 列里取 `encodeUrl`。
- 缓存是**进程内 Map**（`resolvedCache`，TTL 1h）——多实例部署各自缓存，可接受（只是省一次抓取）。

### 3. 入口接法（两种）

**A. 全页路由**（研报）——`app.research.a-stock.$id.$infoCode.tsx`：
用 `useQuery` 按 `infoCode` 拉元数据拿到 `pdfUrl`，`item ? <PdfViewer url={item.pdfUrl}/> : null`，外层固定高度容器 `h-[calc(100vh-6rem)]`。

**B. Dialog 弹层**（财报公告）——`ReportPdfDialog`：
表格行里一个「PDF」文字按钮 → `<Dialog>` 内 `h-[90vh] w-[min(96vw,1100px)]` 的卡片，头部放 `DialogTitle`（期间标签），body `{open ? <PdfViewer url={url}/> : null}`。**`open` 守卫**保证关闭时卸载查看器、不预渲染（省 worker 开销）。

## 验证 / 自检

- [ ] 登录态下打开能逐页渲染；未登录请求代理返回 401。
- [ ] 滚动时底部「当前页 / 总页数」实时更新；上下按钮平滑跳页。
- [ ] 缩放在 0.4–3 之间生效；下载按钮新标签打开（仍鉴权）。
- [ ] 东财空 body 链接经兜底后能正常显示（若接东财）。
- [ ] 大 PDF 走 byte-range 流式加载（network 里看到 206 + Range）。
- [ ] 非白名单 host 的 PDF 直连不经代理；http 链接被升级成 https。

## 拓展速查

| 想做的事 | 怎么做 |
|---|---|
| 接一个新 PDF 源（新 host） | ① 前端 `PdfViewer` 的 `PROXIED_HOSTS` 加 host；② 后端 `ALLOWED_HOSTS` 加同一 host。两处必须一致，否则前端转发了但后端 400。 |
| 消除 web / admin 重复 | 把 `PdfViewer` 抽到 `packages/ui/src/components/`，白名单 / 是否升级 https 作为 prop 传入。 |
| 新增"直链可用"源（无需兜底） | 同上加白名单即可，不用碰 `resolveViaEncodeUrl`（那段只为东财失效链）。 |
| 支持单页懒加载（大文档优化） | 改 `PdfViewer` 渲染逻辑：只渲染视口附近 ±N 页（结合现有 IntersectionObserver）。 |
| 加文字搜索 / 高亮 | pdfjs 已渲染 TextLayer，可在其上做查找；属于较大改动，建议先抽共享组件再做。 |
| PDF 生成 / 导出（全新方向） | 当前**不存在**该能力。需新引入渲染器（如服务端 puppeteer 截 HTML，或 @react-pdf/renderer）。 |
| 调代理缓存时长 | 改 `pdf-proxy.ts` 的 `cache-control max-age`（响应缓存）与 `CACHE_TTL_MS`（encodeUrl 解析缓存）。 |

## 相关概念

- [应用外壳侧边栏](playbook-app-shell-sidebar.md) — 同源风格的多 app 共享组件实现规范
- [双轴主题系统](playbook-dual-axis-theming.md) — 同源风格的 next-themes + shadcn 主题实现规范
- [Monorepo 代码质量体系搭建](playbook-monorepo-code-quality-setup.md) — 前端工程化基础