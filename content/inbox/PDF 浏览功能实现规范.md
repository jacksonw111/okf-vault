# PDF 浏览功能实现规范

> 目标：任何 agent 读完本文档，**不看现有代码也能复刻整套"站内 PDF 浏览"能力**（前端查看器 + 后端代理），并知道如何接新的 PDF 源、加新入口。
>
> 与 `docs/frontend/sidebar.md` / `theming.md` 同源同风格。注意本功能**横跨前后端**：前端 `PdfViewer`（react-pdf）+ 后端 `pdf-proxy`（Hono 路由）。两者缺一不可。

---

## 1. 这是什么 / 不是什么

- **是**：把第三方（东方财富、巨潮资讯）的研报/公告 PDF **内嵌在 SPA 里逐页渲染**的查看器——不跳出应用、不触发浏览器下载、支持翻页/缩放/下载。
- **不是**：PDF 的**生成/导出**。本系统不生成 PDF（没有 puppeteer/pdfkit/@react-pdf 渲染器），只**消费**远端已有的 PDF。
- 依赖：`react-pdf`（catalog `10.4.1`）封装 + `pdfjs-dist`（catalog `5.4.296`）做实际解析渲染。

为什么需要后端代理而不能直接喂 URL 给 pdfjs：

1. **CORS**：`pdf.dfcfw.com` / `static.cninfo.com.cn` 不带跨域头，浏览器里 pdfjs 的 fetch（尤其 byte-range 流式请求）会被拦。
2. **东方财富的 PDF 链接会失效**：`H3_{infoCode}_1.pdf` 形式的直链常返回空 body，需要回到详情页用 `encodeUrl` 解析出真实 `attach_url`。这套解析逻辑必须在服务端做（要读 DB + 抓 HTML）。

---

## 2. 全景数据流

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

---

## 3. 文件清单与职责

```
apps/web/src/
  components/research/pdf-viewer.tsx              查看器（web 版：两 host 代理 + http→https）
  components/stock-detail/report-pdf-dialog.tsx   财报公告入口：按钮 → Dialog 内嵌 PdfViewer
  components/stock-detail/financial-reports-section.tsx  表格行里用 ReportPdfDialog
  routes/app.research.a-stock.$id.$infoCode.tsx   研报全页查看路由
apps/admin/src/
  components/research-reports/pdf-viewer.tsx      查看器（admin 版：只代理 pdf.dfcfw.com）
  routes/admin.data.daily-reports.$id.$infoCode.tsx  admin 研报查看路由
apps/server/src/
  routes/pdf-proxy.ts                             代理 handler（核心）
  index.ts                                        挂载 app.get("/api/pdf-proxy", ...) + CORS
packages/db/src/
  repositories/research-report-repository.ts      findEncodeUrlByInfoCode（兜底解析用）
```

> **现状提示（技术债）**：`apps/web` 和 `apps/admin` 各有一份 `PdfViewer`，**几乎完全重复**，只有 `proxyUrl` 的白名单不同（见 §6）。复刻新 app 时应优先**抽到 `packages/ui`** 共享，而不是再 copy 一份。

---

## 4. 前端查看器 `PdfViewer`

### 4.1 pdfjs worker 配置（模块顶部，必做）

```ts
import { Document, Page, pdfjs } from "react-pdf";
import "react-pdf/dist/Page/AnnotationLayer.css";   // 注释/链接层样式
import "react-pdf/dist/Page/TextLayer.css";          // 文本选择层样式

pdfjs.GlobalWorkerOptions.workerSrc = new URL(
  "pdfjs-dist/build/pdf.worker.min.mjs",
  import.meta.url
).toString();
```

- **worker 必须配置**，否则 pdfjs 在主线程跑会报错/卡顿。用 `new URL(..., import.meta.url)` 让 Vite 把 worker 作为资源打包并产出正确 URL——**不需要**在 `vite.config` 里加额外配置（本项目两 app 的 vite.config 都没有 PDF 相关设置，验证过）。
- 两个 CSS 必须 import，否则文本层/注释层错位。

### 4.2 `proxyUrl` —— 决定是否走代理

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
- **http→https 升级**：历史数据里 cninfo 链接可能是 http，而 proxy 只接受 https；且这些旧链可能还躺在前端 TanStack Query 缓存里（1h staleTime）。
- `env.VITE_SERVER_URL` 走 `@ai-financial/env/web`，禁止直接读 `import.meta.env`。

### 4.3 渲染结构

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

- `withCredentials: true` 让 pdfjs 的请求带上 cookie → 后端 `getSession` 才能鉴权（配合 CORS `credentials:true`，见 §5.3）。
- 一次性渲染全部页（不是懒加载单页），用一个滚动容器纵向排列。
- 加载/错误状态都在 `<Document>` 上处理；错误时整块换成提示文案。

### 4.4 交互：滚动监听 + 翻页 + 缩放

- **当前页跟踪**：`pages` 就绪后建 `IntersectionObserver`（`root` 是滚动容器，`threshold:[0.25,0.5,0.75]`），取可见比例最高的页设为 `currentPage`。这是项目里少数被允许的 `useEffect`（与非 React 的 IO API 交互）。
- **翻页**：底部悬浮控制条的上/下按钮调 `scrollToPage(n)` → `el.scrollIntoView({behavior:"smooth"})`（用 `pageRefs` Map 按页号取 DOM）。
- **缩放**：`scale` state，步长 0.2，区间 `[0.4, 3]`，初值 1.2。
- **下载**：`<a href={fetchUrl} target="_blank">`（指向代理 URL，仍受鉴权保护）。
- 控制条样式：`absolute bottom-4 left-1/2 -translate-x-1/2` 的圆角胶囊，`backdrop-blur`，按钮 `size="icon-sm" variant="ghost"`，图标 `size-4`（符合全局图标 `size-4` 约定）。

---

## 5. 后端代理 `pdf-proxy.ts`

### 5.1 安全闸门（顺序固定）

```ts
const ALLOWED_HOSTS = new Set(["pdf.dfcfw.com", "static.cninfo.com.cn"]);

1. session = auth.api.getSession({ headers });  if (!user) → 401
2. raw = query("url");  if (!raw) → 400 "missing url"
3. new URL(raw) 解析失败 → 400 "invalid url"
4. protocol !== "https:" || !ALLOWED_HOSTS.has(host) → 400 "host not allowed"
```

- **白名单 + 仅 https** 是防 SSRF 的关键：代理只能拉这两个已知主机，杜绝被当成任意 URL 抓取器。新增 PDF 源**必须**同时改前端 `PROXIED_HOSTS` 和后端 `ALLOWED_HOSTS`。

### 5.2 抓取 + 东财兜底 + 透传

```ts
range = header("range");                          // 透传 byte-range
effectiveUrl = 命中 resolvedCache 且未过期 ? cached.url : raw;
upstream = fetchUpstream(effectiveUrl, range);    // GET, redirect:follow, 带 range

if (isEmptyResponse(upstream)) {                  // content-length === "0"
  resolved = await resolveViaEncodeUrl(raw);      // 见 §5.4
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

### 5.3 在 `apps/server/src/index.ts` 挂载 + CORS

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

### 5.4 东方财富 `encodeUrl` 兜底解析 `resolveViaEncodeUrl`

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

---

## 6. 两个 app 的差异（务必知道）

| | web `PdfViewer` | admin `PdfViewer` |
|---|---|---|
| 代理白名单 | `pdf.dfcfw.com` **和** `static.cninfo.com.cn` | **仅** `pdf.dfcfw.com` |
| http→https 升级 | 有 | 无 |
| 其余（worker/渲染/交互） | 完全相同 | 完全相同 |

原因：admin 只看东财研报，不涉及巨潮公告；web 的财报公告模块要看 cninfo。后端 `ALLOWED_HOSTS` 是两者并集。

---

## 7. 入口接法（两种）

**A. 全页路由**（研报）——`app.research.a-stock.$id.$infoCode.tsx`：
用 `useQuery` 按 `infoCode` 拉元数据拿到 `pdfUrl`，`item ? <PdfViewer url={item.pdfUrl}/> : null`，外层固定高度容器 `h-[calc(100vh-6rem)]`。

**B. Dialog 弹层**（财报公告）——`ReportPdfDialog`：
表格行里一个「PDF」文字按钮 → `<Dialog>` 内 `h-[90vh] w-[min(96vw,1100px)]` 的卡片，头部放 `DialogTitle`（期间标签），body `{open ? <PdfViewer url={url}/> : null}`。**`open` 守卫**保证关闭时卸载查看器、不预渲染（省 worker 开销）。

> 两种入口都遵循 sidebar/列表页规则：Dialog 走 `@ai-financial/ui` 的 `Dialog`，不自造 modal。

---

## 8. 复刻 checklist

1. **依赖**：目标 app `package.json` 加 `"react-pdf": "catalog:"` + `"pdfjs-dist": "catalog:"`（catalog 已有 `10.4.1` / `5.4.296`）。
2. **查看器**：落 `PdfViewer`——顶部配 worker + import 两个 CSS；`proxyUrl` 白名单；`<Document withCredentials>` + 全页 `<Page>`；IntersectionObserver 跟踪当前页；底部控制条（翻页/缩放/下载）。**优先抽到 `packages/ui` 共享**，避免再 copy。
3. **后端代理**：落 `apps/server/src/routes/pdf-proxy.ts`——鉴权 401 / https+白名单 400 / range 透传 / 空 body 兜底 / 头透传 / `cache-control: private`。
4. **挂载 + CORS**：`index.ts` `app.get("/api/pdf-proxy", ...)`，CORS `credentials:true`。
5. **东财兜底（可选）**：若接东财，实现 `resolveViaEncodeUrl` + `findEncodeUrlByInfoCode`（依赖 `daily_report_item.raw.encodeUrl`）。只接 cninfo 等"直链可用"源可跳过。
6. **入口**：全页路由或 `Dialog`，把远端 `pdfUrl` 传给 `PdfViewer`，记得 Dialog 用 `open` 守卫懒挂载。

### 验收点

- [ ] 登录态下打开能逐页渲染；未登录请求代理返回 401。
- [ ] 滚动时底部 `当前页 / 总页数` 实时更新；上下按钮平滑跳页。
- [ ] 缩放在 0.4–3 之间生效；下载按钮新标签打开（仍鉴权）。
- [ ] 东财空 body 链接经兜底后能正常显示（若接东财）。
- [ ] 大 PDF 走 byte-range 流式加载（network 里看到 206 + Range）。
- [ ] 非白名单 host 的 PDF 直连不经代理；http 链接被升级成 https。

---

## 9. 如何拓展

| 想做的事 | 怎么做 |
|---|---|
| **接一个新 PDF 源（新 host）** | ① 前端 `PdfViewer` 的 `PROXIED_HOSTS` 加 host；② 后端 `ALLOWED_HOSTS` 加同一 host。两处必须一致，否则前端转发了但后端 400。 |
| **消除 web/admin 重复** | 把 `PdfViewer` 抽到 `packages/ui/src/components/`，白名单/是否升级 https 作为 prop 传入；两 app 改成引用。 |
| **新增"直链可用"源（无需兜底）** | 同上加白名单即可，不用碰 `resolveViaEncodeUrl`（那段只为东财失效链）。 |
| **支持单页懒加载（大文档优化）** | 改 `PdfViewer` 渲染逻辑：只渲染视口附近 ±N 页（结合现有 IntersectionObserver），其余占位。 |
| **加文字搜索/高亮** | pdfjs 已渲染 TextLayer，可在其上做查找；属于较大改动，建议先抽共享组件再做。 |
| **PDF 生成/导出（全新方向）** | 当前**不存在**该能力。需新引入渲染器（如服务端 puppeteer 截 HTML，或 @react-pdf/renderer），与本查看器无关，应另建模块。 |
| **调代理缓存时长** | 改 `pdf-proxy.ts` 的 `cache-control max-age`（响应缓存）与 `CACHE_TTL_MS`（encodeUrl 解析缓存）。 |

