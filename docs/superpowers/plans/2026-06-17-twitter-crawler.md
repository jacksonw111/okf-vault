# X/Twitter 定时爬虫 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 一个独立的 GitHub Action，每小时爬取预定义 X 账号的推文（原创/长文/线程/引用/转载，不含回复），取**全文**与媒体 URL，渲染成 Markdown 落到 `content/inbox/twitter/<账号>/`，交现有 OKF agent 每天整理一次。

**Architecture:** 自建子项目 `twitter-crawler/`（Node 22 + TypeScript，运行时 `tsx`），基于 `twitter-openapi-typescript` 调 X 内部 GraphQL。鉴权用单个 secret `X_AUTH_TOKEN`，运行时自动换 `ct0`。用 `getUserTweets`（天然不含回复；线程续条在 `.replies` 里）。产出文件名含 `tweet_id`，文件存在即去重。Action 用默认 `GITHUB_TOKEN` 推送（不触发 okf.yml），仅每日定时 agent 处理一次。

**Tech Stack:** Node 22, TypeScript, `tsx`, `twitter-openapi-typescript@^0.0.51`, `node:test`（内置测试，零额外依赖）。

## Global Constraints

- 仓库已是 git 仓库，主分支 `main`，git user `johnwen`。
- 纯函数禁止读时钟/随机/网络（`created` 日期等需由调用方注入，保证可测）。
- **绝不**把 `X_AUTH_TOKEN` / cookie / `ct0` 写入日志或异常消息。
- Markdown frontmatter 的 `title`/`description`/`source` 必须**双引号包裹**并转义内部双引号（Quartz YAML 规范，见 `content/PRODUCER.md`）。
- 产出路径固定：`content/inbox/twitter/<screenName>/<YYYY-MM-DD>-<tweetId>.md`，`screenName` 为不带 `@` 的小写用户名。
- 推文 ID（snowflake）可作字符串字典序比较排序（同长度）。
- 依赖最小化：生产依赖只有 `twitter-openapi-typescript`；manifest 请求用 Node 22 内置 `fetch`（不引 axios）。

## Spec refinements（实现期对 spec 的事实性修正，已在 API 源码核实）

1. 长推文全文路径 = `tweet.noteTweet.noteTweetResults.result.text`（spec 写的 `notetweetResult` 过时）。
2. 用 `getUserTweets`（非 `...AndReplies`）→ 天然不含回复（满足"不抓回复"），且线程续条在返回的 `tweet.replies[]` 里 → thread 重建无需启发式。
3. 类型枚举收敛为 5 类：`original | thread | quote | retweet | article`。spec 里的 `note` 折叠进 `original`（长文也是 original，全文照样取到）。`article`（X Premium 独立富文本）V1 不做专门检测（正文不在 `UserTweets` 返回里），会以 `original` 形态渲染其标题+链接+note 文本；完整正文列 V2。

## File Structure

| 文件 | 职责 |
|---|---|
| `twitter-crawler/package.json` | 依赖、`test`/`start` 脚本，`"type":"module"` |
| `twitter-crawler/tsconfig.json` | TS 配置 |
| `twitter-crawler/.gitignore` | 忽略 `node_modules/`、`dist/` |
| `twitter-crawler/accounts.json` | 账号清单 + `max_per_run` |
| `twitter-crawler/src/types.ts` | 本地最小类型（`RawTweet` 等），与库解耦 |
| `twitter-crawler/src/map.ts` | `toRawTweet`：库 `TweetApiUtilsData` → `RawTweet` |
| `twitter-crawler/src/text.ts` | `expandTco`（t.co 还原 + 媒体 t.co 剥离），纯 |
| `twitter-crawler/src/media.ts` | `extractMedia`（图片/最佳码率视频），纯 |
| `twitter-crawler/src/classify.ts` | `classifyTweet`，纯 |
| `twitter-crawler/src/render.ts` | `renderMarkdown`（frontmatter + 正文），纯 |
| `twitter-crawler/src/io.ts` | `formatDate`/`tweetFilePath`/`alreadySaved`，纯（existsSync） |
| `twitter-crawler/src/auth.ts` | `buildClient(authToken)`：fetch manifest → 取 ct0 → getClientFromCookies |
| `twitter-crawler/src/fetch.ts` | `fetchTweetsForAccount`：getUserByScreenName + getUserTweets 分页 |
| `twitter-crawler/src/index.ts` | 主流程：config → client → 逐账号 → map/classify/render/io → 写文件 |
| `twitter-crawler/test/fixtures.ts` | 形状准确的合成 `TweetApiUtilsData` 夹具 |
| `twitter-crawler/test/*.test.ts` | `node:test` 单测 |
| `twitter-crawler/README.md` | 如何取 auth_token、加账号、如何集成 |
| `.github/workflows/twitter-crawl.yml` | 每小时 cron workflow |
| `content/PRODUCER.md`（改） | 新增"媒体保留"硬规则 |
| `.claude/prompt.txt`（改） | 第 3 步加媒体保留提醒 |

---

### Task 1: Scaffold crawler project + test harness

**Files:**
- Create: `twitter-crawler/package.json`
- Create: `twitter-crawler/tsconfig.json`
- Create: `twitter-crawler/.gitignore`
- Create: `twitter-crawler/accounts.json`
- Create: `twitter-crawler/test/sanity.test.ts`

**Interfaces:**
- Produces: 一个可 `npm ci` + `npm test` 跑通的空骨架，供后续任务挂代码。

- [ ] **Step 1: 写 `twitter-crawler/package.json`**

```json
{
  "name": "twitter-crawler",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "test": "node --import tsx --test test/*.test.ts",
    "start": "tsx src/index.ts"
  },
  "dependencies": {
    "twitter-openapi-typescript": "^0.0.51"
  },
  "devDependencies": {
    "@types/node": "^22.0.0",
    "tsx": "^4.19.0",
    "typescript": "^5.6.0"
  }
}
```

- [ ] **Step 2: 写 `twitter-crawler/tsconfig.json`**

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "lib": ["ES2022"],
    "types": ["node"],
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "resolveJsonModule": true,
    "noEmit": true
  },
  "include": ["src", "test"]
}
```

- [ ] **Step 3: 写 `twitter-crawler/.gitignore`**

```
node_modules/
dist/
```

- [ ] **Step 4: 写 `twitter-crawler/accounts.json`**

```json
{
  "accounts": ["Wen_Zw"],
  "max_per_run": 20
}
```

- [ ] **Step 5: 写一个 sanity 测试 `twitter-crawler/test/sanity.test.ts`**

```ts
import { test } from "node:test";
import assert from "node:assert/strict";

test("sanity: test harness works", () => {
  assert.equal(1 + 1, 2);
});
```

- [ ] **Step 6: 安装依赖并生成 lockfile**

Run（在仓库根）:
```bash
cd twitter-crawler && npm install
```
Expected: 生成 `twitter-crawler/node_modules/` 和 `twitter-crawler/package-lock.json`。

- [ ] **Step 7: 跑测试确认绿灯**

Run:
```bash
cd twitter-crawler && npm test
```
Expected: 1 passing（`sanity: test harness works`）。

- [ ] **Step 8: Commit**

```bash
git add twitter-crawler/package.json twitter-crawler/package-lock.json twitter-crawler/tsconfig.json twitter-crawler/.gitignore twitter-crawler/accounts.json twitter-crawler/test/sanity.test.ts
git commit -m "feat(twitter-crawler): scaffold project + test harness"
```

---

### Task 2: 本地类型层 `types.ts`

**Files:**
- Create: `twitter-crawler/src/types.ts`
- Test: `twitter-crawler/test/types.test.ts`

**Interfaces:**
- Produces: `RawTweet`、`TweetType`、`MediaEntity`、`UrlEntity`、`MediaInfo` 等本地类型，后续所有纯函数只依赖这些（不直接依赖库类型）。

- [ ] **Step 1: 写 `twitter-crawler/src/types.ts`**

```ts
// 本地最小类型层：只描述我们消费的字段，与 twitter-openapi-typescript 的重类型解耦。
// 库的 TweetApiUtilsData → toRawTweet(map.ts) → RawTweet。库字段名变了只改 map.ts。

export type TweetType = "original" | "thread" | "quote" | "retweet" | "article";

export interface UrlEntity {
  url: string;          // t.co 短链
  expandedUrl?: string; // 真实地址
}

export interface MediaVariant {
  bitrate?: number;
  contentType: string;
  url: string;
}

export interface MediaEntity {
  type: "photo" | "video" | "animated_gif";
  mediaUrlHttps: string;
  videoInfo?: { variants: MediaVariant[] };
}

export interface MediaInfo {
  images: string[];
  videos: string[];
}

export interface RawTweet {
  id: string;                  // restId
  text: string;                // 全文（noteTweet 优先），t.co 已还原，媒体 t.co 已剥离
  createdAt: string;           // 原始串，如 "Mon Jan 01 12:00:00 +0000 2024"
  lang?: string;
  urls: UrlEntity[];
  media: MediaInfo;
  screenName: string;          // 不带 @
  displayName: string;
  quoted?: RawTweet;           // 引用推文
  retweeted?: RawTweet;        // 被转载推文
  threadParts: RawTweet[];     // 线程续条（root 之外），id 升序
  promoted: boolean;           // 广告
}
```

- [ ] **Step 2: 写类型自检测试 `twitter-crawler/test/types.test.ts`**

```ts
import { test } from "node:test";
import assert from "node:assert/strict";
import type { RawTweet } from "../src/types.js";

test("RawTweet 可以构造一个最小合法对象", () => {
  const rt: RawTweet = {
    id: "1",
    text: "hi",
    createdAt: "Mon Jan 01 12:00:00 +0000 2024",
    urls: [],
    media: { images: [], videos: [] },
    screenName: "wen",
    displayName: "Wen",
    threadParts: [],
    promoted: false,
  };
  assert.equal(rt.id, "1");
});
```

- [ ] **Step 3: 跑测试**

Run:
```bash
cd twitter-crawler && npm test
```
Expected: 2 passing。

- [ ] **Step 4: Commit**

```bash
git add twitter-crawler/src/types.ts twitter-crawler/test/types.test.ts
git commit -m "feat(twitter-crawler): add RawTweet anti-corruption type layer"
```

---

### Task 3: `text.ts` — t.co 还原（纯）

**Files:**
- Create: `twitter-crawler/src/text.ts`
- Test: `twitter-crawler/test/text.test.ts`

**Interfaces:**
- Consumes: `UrlEntity[]`、`MediaInfo`（来自 types.ts）
- Produces: `expandTco(text, urls, media)`，被 map.ts 调用。

- [ ] **Step 1: 写失败测试 `twitter-crawler/test/text.test.ts`**

```ts
import { test } from "node:test";
import assert from "node:assert/strict";
import { expandTco } from "../src/text.js";

test("expandTco: 把 t.co 短链还原成 expandedUrl", () => {
  const out = expandTco(
    "see https://t.co/abc1 now",
    [{ url: "https://t.co/abc1", expandedUrl: "https://example.com/page" }],
    { images: [], videos: [] }
  );
  assert.equal(out, "see https://example.com/page now");
});

test("expandTco: 没有 expandedUrl 时保留原短链", () => {
  const out = expandTco("x https://t.co/zz", [{ url: "https://t.co/zz" }], {
    images: [],
    videos: [],
  });
  assert.equal(out, "x https://t.co/zz");
});

test("expandTco: 剥离尾部媒体 t.co（图片）", () => {
  const out = expandTco(
    "hello https://t.co/media1",
    [],
    { images: ["https://t.co/media1"], videos: [] }
  );
  assert.equal(out, "hello");
});

test("expandTco: 多个 url 都还原", () => {
  const out = expandTco(
    "a https://t.co/a b https://t.co/b",
    [
      { url: "https://t.co/a", expandedUrl: "https://a.com" },
      { url: "https://t.co/b", expandedUrl: "https://b.com" },
    ],
    { images: [], videos: [] }
  );
  assert.equal(out, "a https://a.com b https://b.com");
});
```

- [ ] **Step 2: 跑测试确认失败**

Run:
```bash
cd twitter-crawler && npm test 2>&1 | grep -A3 expandTco
```
Expected: FAIL（`Cannot find module '../src/text.js'`）。

- [ ] **Step 3: 写 `twitter-crawler/src/text.ts`**

```ts
import type { UrlEntity, MediaInfo } from "./types.js";

/**
 * 把正文里的 t.co 短链还原成真实 URL，并剥离末尾的媒体 t.co。
 * 纯函数：不读时钟/网络。
 */
export function expandTco(
  text: string,
  urls: UrlEntity[],
  media: MediaInfo
): string {
  let out = text;

  // 1) 还原 url 实体里的短链
  for (const u of urls) {
    if (u.expandedUrl && u.url && u.url !== u.expandedUrl) {
      out = out.split(u.url).join(u.expandedUrl);
    }
  }

  // 2) 剥离媒体 t.co（图片/视频附在末尾的占位短链）
  const mediaTcos = [...media.images, ...media.videos].filter(
    (s) => typeof s === "string" && s.includes("t.co")
  );
  for (const m of mediaTcos) {
    // 去掉短链及其前面的一个空格
    out = out.replace(new RegExp("\\s*" + escapeReg(m), "g"), "");
  }

  return out.trim();
}

function escapeReg(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}
```

- [ ] **Step 4: 跑测试确认通过**

Run:
```bash
cd twitter-crawler && npm test 2>&1 | grep -E "expandTco|passing|failing"
```
Expected: 4 个 expandTco 测试 passing。

- [ ] **Step 5: Commit**

```bash
git add twitter-crawler/src/text.ts twitter-crawler/test/text.test.ts
git commit -m "feat(twitter-crawler): t.co url expansion + media strip"
```

---

### Task 4: `media.ts` — 媒体抽取（纯）

**Files:**
- Create: `twitter-crawler/src/media.ts`
- Test: `twitter-crawler/test/media.test.ts`

**Interfaces:**
- Consumes: `MediaEntity[]`（types.ts）
- Produces: `extractMedia(entities): MediaInfo`

- [ ] **Step 1: 写失败测试 `twitter-crawler/test/media.test.ts`**

```ts
import { test } from "node:test";
import assert from "node:assert/strict";
import { extractMedia } from "../src/media.js";

test("extractMedia: 图片", () => {
  const m = extractMedia([
    { type: "photo", mediaUrlHttps: "https://pbs.twimg.com/a.jpg" },
  ]);
  assert.deepEqual(m, { images: ["https://pbs.twimg.com/a.jpg"], videos: [] });
});

test("extractMedia: 视频取最高码率 mp4", () => {
  const m = extractMedia([
    {
      type: "video",
      mediaUrlHttps: "https://pbs.twimg.com/thumb.jpg",
      videoInfo: {
        variants: [
          { contentType: "application/x-mpegURL", url: "https://v/hls.m3u8" },
          { contentType: "video/mp4", bitrate: 832000, url: "https://v/832.mp4" },
          { contentType: "video/mp4", bitrate: 2160000, url: "https://v/2160.mp4" },
        ],
      },
    },
  ]);
  assert.deepEqual(m, {
    images: [],
    videos: ["https://v/2160.mp4"],
  });
});

test("extractMedia: animated_gif 也算视频", () => {
  const m = extractMedia([
    {
      type: "animated_gif",
      mediaUrlHttps: "https://pbs.twimg.com/g.jpg",
      videoInfo: {
        variants: [{ contentType: "video/mp4", bitrate: 0, url: "https://g.mp4" }],
      },
    },
  ]);
  assert.deepEqual(m, { images: [], videos: ["https://g.mp4"] });
});

test("extractMedia: 空数组", () => {
  assert.deepEqual(extractMedia([]), { images: [], videos: [] });
});
```

- [ ] **Step 2: 跑测试确认失败**

Run:
```bash
cd twitter-crawler && npm test 2>&1 | grep -A2 extractMedia
```
Expected: FAIL（模块不存在）。

- [ ] **Step 3: 写 `twitter-crawler/src/media.ts`**

```ts
import type { MediaEntity, MediaInfo } from "./types.js";

/** 从 extendedEntities.media 抽图片 URL 和最佳码率视频 URL。 */
export function extractMedia(entities: MediaEntity[]): MediaInfo {
  const images: string[] = [];
  const videos: string[] = [];

  for (const e of entities ?? []) {
    if (e.type === "photo") {
      if (e.mediaUrlHttps) images.push(e.mediaUrlHttps);
    } else {
      // video | animated_gif
      const variants = e.videoInfo?.variants ?? [];
      const mp4s = variants.filter(
        (v) => v.contentType === "video/mp4" && typeof v.bitrate === "number"
      );
      const best =
        mp4s.length > 0
          ? mp4s.sort((a, b) => (b.bitrate ?? 0) - (a.bitrate ?? 0))[0]
          : variants.find((v) => v.contentType === "video/mp4");
      if (best?.url) videos.push(best.url);
    }
  }

  return { images, videos };
}
```

- [ ] **Step 4: 跑测试确认通过**

Run:
```bash
cd twitter-crawler && npm test 2>&1 | grep -E "extractMedia|passing|failing"
```
Expected: 4 个 extractMedia 测试 passing。

- [ ] **Step 5: Commit**

```bash
git add twitter-crawler/src/media.ts twitter-crawler/test/media.test.ts
git commit -m "feat(twitter-crawler): media extraction (images + best-bitrate video)"
```

---

### Task 5: `classify.ts`（纯）

**Files:**
- Create: `twitter-crawler/src/classify.ts`
- Test: `twitter-crawler/test/classify.test.ts`

**Interfaces:**
- Consumes: `RawTweet`（types.ts）
- Produces: `classifyTweet(rt): TweetType`

- [ ] **Step 1: 写失败测试 `twitter-crawler/test/classify.test.ts`**

```ts
import { test } from "node:test";
import assert from "node:assert/strict";
import { classifyTweet } from "../src/classify.js";
import type { RawTweet } from "../src/types.js";

function base(over: Partial<RawTweet> = {}): RawTweet {
  return {
    id: "1",
    text: "x",
    createdAt: "Mon Jan 01 12:00:00 +0000 2024",
    urls: [],
    media: { images: [], videos: [] },
    screenName: "wen",
    displayName: "Wen",
    threadParts: [],
    promoted: false,
    ...over,
  };
}

test("classify: retweet 优先", () => {
  assert.equal(
    classifyTweet(base({ retweeted: base({ id: "9" }) })),
    "retweet"
  );
});

test("classify: quote", () => {
  assert.equal(classifyTweet(base({ quoted: base({ id: "9" }) })), "quote");
});

test("classify: thread（有续条）", () => {
  assert.equal(
    classifyTweet(base({ threadParts: [base({ id: "2" })] })),
    "thread"
  );
});

test("classify: original", () => {
  assert.equal(classifyTweet(base()), "original");
});
```

- [ ] **Step 2: 跑测试确认失败**

Run:
```bash
cd twitter-crawler && npm test 2>&1 | grep -A2 classifyTweet
```
Expected: FAIL（模块不存在）。

- [ ] **Step 3: 写 `twitter-crawler/src/classify.ts`**

```ts
import type { RawTweet, TweetType } from "./types.js";

/**
 * 判定推文类型。注意：getUserTweets 已排除回复，故这里不处理 reply。
 * 优先级：retweet > quote > thread > original。
 * （article 类型 V1 不主动产出，保留在枚举里供未来。）
 */
export function classifyTweet(rt: RawTweet): TweetType {
  if (rt.retweeted) return "retweet";
  if (rt.quoted) return "quote";
  if (rt.threadParts.length > 0) return "thread";
  return "original";
}
```

- [ ] **Step 4: 跑测试确认通过**

Run:
```bash
cd twitter-crawler && npm test 2>&1 | grep -E "classify|passing|failing"
```
Expected: 4 个 classify 测试 passing。

- [ ] **Step 5: Commit**

```bash
git add twitter-crawler/src/classify.ts twitter-crawler/test/classify.test.ts
git commit -m "feat(twitter-crawler): tweet type classification"
```

---

### Task 6: `render.ts` — Markdown 渲染（纯）

**Files:**
- Create: `twitter-crawler/src/render.ts`
- Test: `twitter-crawler/test/render.test.ts`

**Interfaces:**
- Consumes: `RawTweet`、`classifyTweet`、`TweetType`
- Produces: `renderMarkdown(rt, type, createdDate): string`

- [ ] **Step 1: 写失败测试 `twitter-crawler/test/render.test.ts`**

```ts
import { test } from "node:test";
import assert from "node:assert/strict";
import { renderMarkdown } from "../src/render.js";
import { classifyTweet } from "../src/classify.js";
import type { RawTweet } from "../src/types.js";

function base(over: Partial<RawTweet> = {}): RawTweet {
  return {
    id: "100",
    text: "hello world",
    createdAt: "Sat Jun 01 08:00:00 +0000 2024",
    urls: [],
    media: { images: [], videos: [] },
    screenName: "Wen_Zw",
    displayName: "Wen",
    threadParts: [],
    promoted: false,
    ...over,
  };
}

test("render: original 基本结构 + frontmatter", () => {
  const md = renderMarkdown(base(), "original", "2024-06-17");
  assert.match(md, /title: "hello world"/);
  assert.match(md, /source: "https:\/\/x\.com\/Wen_Zw\/status\/100"/);
  assert.match(md, /tweet_type: "original"/);
  assert.match(md, /tweet_id: "100"/);
  assert.match(md, /published: 2024-06-01/);
  assert.match(md, /created: "2024-06-17"/);
  assert.match(md, /\[\[@Wen_Zw\]\]/);
  assert.match(md, /\- "clippings"/);
  assert.match(md, /\- "twitter"/);
});

test("render: 媒体附在正文", () => {
  const md = renderMarkdown(
    base({ media: { images: ["https://pbs/a.jpg"], videos: ["https://v/x.mp4"] } }),
    "original",
    "2024-06-17"
  );
  assert.match(md, /!\[\]\(https:\/\/pbs\/a\.jpg\)/);
  assert.match(md, /视频：.*https:\/\/v\/x\.mp4/);
});

test("render: thread 拼接续条", () => {
  const rt = base({
    text: "part1",
    threadParts: [base({ id: "101", text: "part2" })],
  });
  const md = renderMarkdown(rt, "thread", "2024-06-17");
  assert.match(md, /part1/);
  assert.match(md, /2\/2/);
  assert.match(md, /part2/);
});

test("render: quote 含被引用全文", () => {
  const rt = base({
    text: "my comment",
    quoted: base({ id: "9", text: "the quoted full text", screenName: "other" }),
  });
  const md = renderMarkdown(rt, "quote", "2024-06-17");
  assert.match(md, /my comment/);
  assert.match(md, /引用 @other：/);
  assert.match(md, /the quoted full text/);
});

test("render: retweet 含被转载全文", () => {
  const rt = base({
    retweeted: base({ id: "9", text: "original body", screenName: "other" }),
  });
  const md = renderMarkdown(rt, "retweet", "2024-06-17");
  assert.match(md, /转载 @other：/);
  assert.match(md, /original body/);
});

test("render: title/description 双引号转义", () => {
  const md = renderMarkdown(
    base({ text: 'she said "hi": http://x.com' }),
    "original",
    "2024-06-17"
  );
  // 不应出现裸冒号破坏 YAML（双引号包裹内已转义）
  assert.match(md, /title: "she said \\"hi\\".*/);
});
```

- [ ] **Step 2: 跑测试确认失败**

Run:
```bash
cd twitter-crawler && npm test 2>&1 | grep -A2 renderMarkdown
```
Expected: FAIL（模块不存在）。

- [ ] **Step 3: 写 `twitter-crawler/src/render.ts`**

```ts
import type { RawTweet, MediaInfo } from "./types.js";

/** YAML 双引号安全包裹：转义反斜杠/双引号，换行→空格。 */
export function yamlQuote(s: string): string {
  const safe = (s ?? "")
    .replace(/\\/g, "\\\\")
    .replace(/"/g, '\\"')
    .replace(/\r?\n/g, " ")
    .trim();
  return `"${safe}"`;
}

function titleFor(rt: RawTweet): string {
  const t = rt.text ?? "";
  const head = t.split(/\r?\n/)[0] ?? "";
  if (head.length <= 80) return head;
  return head.slice(0, 77) + "…";
}

function descriptionFor(rt: RawTweet): string {
  return (rt.text ?? "").slice(0, 280);
}

function mediaBlock(media: MediaInfo): string {
  const lines: string[] = [];
  for (const img of media.images) lines.push(`![](${img})`);
  if (media.videos.length > 0) {
    lines.push("");
    lines.push("视频：");
    for (const v of media.videos) lines.push(`- <${v}>`);
  }
  return lines.join("\n");
}

function bodyFor(rt: RawTweet, type: string): string {
  const parts: string[] = [];

  if (type === "retweet" && rt.retweeted) {
    const r = rt.retweeted;
    parts.push(`> 转载 @${r.screenName}：`);
    parts.push("");
    parts.push(quoteBlock(r.text));
    parts.push("");
    parts.push(`> 来源：<https://x.com/${r.screenName}/status/${r.id}>`);
    if (hasMedia(r.media)) {
      parts.push("");
      parts.push(mediaBlock(r.media));
    }
    return parts.join("\n");
  }

  // 自身正文
  parts.push(rt.text);

  if (type === "thread" && rt.threadParts.length > 0) {
    const total = rt.threadParts.length + 1;
    let i = 2;
    for (const p of rt.threadParts) {
      parts.push("");
      parts.push(`--- ${i}/${total} ---`);
      parts.push("");
      parts.push(p.text);
      if (hasMedia(p.media)) {
        parts.push("");
        parts.push(mediaBlock(p.media));
      }
      i++;
    }
  }

  if (type === "quote" && rt.quoted) {
    const q = rt.quoted;
    parts.push("");
    parts.push(`> 引用 @${q.screenName}：`);
    parts.push("");
    parts.push(quoteBlock(q.text));
    parts.push("");
    parts.push(`> 来源：<https://x.com/${q.screenName}/status/${q.id}>`);
    if (hasMedia(q.media)) {
      parts.push("");
      parts.push(mediaBlock(q.media));
    }
  }

  if (hasMedia(rt.media)) {
    parts.push("");
    parts.push(mediaBlock(rt.media));
  }

  return parts.join("\n");
}

function quoteBlock(text: string): string {
  return (text ?? "")
    .split(/\r?\n/)
    .map((l) => `> ${l}`)
    .join("\n");
}

function hasMedia(m: MediaInfo): boolean {
  return m.images.length > 0 || m.videos.length > 0;
}

export function renderMarkdown(
  rt: RawTweet,
  type: string,
  createdDate: string
): string {
  const fm = [
    "---",
    `title: ${yamlQuote(titleFor(rt))}`,
    `source: ${yamlQuote(`https://x.com/${rt.screenName}/status/${rt.id}`)}`,
    "author:",
    `  - "[[@${rt.screenName}]]"`,
    `tweet_type: ${yamlQuote(type)}`,
    `tweet_id: ${yamlQuote(rt.id)}`,
    `published: ${formatPublished(rt.createdAt)}`,
    `created: ${yamlQuote(createdDate)}`,
    `description: ${yamlQuote(descriptionFor(rt))}`,
    "tags:",
    `  - "clippings"`,
    `  - "twitter"`,
    "---",
  ].join("\n");

  const body = bodyFor(rt, type);

  const tail = [
    "",
    "## 来源",
    `<https://x.com/${rt.screenName}/status/${rt.id}>`,
    "",
  ].join("\n");

  return `${fm}\n\n${body}\n${tail}`;
}

// published 日期：createdAt "Sat Jun 01 08:00:00 +0000 2024" → "2024-06-01"
function formatPublished(createdAt: string): string {
  const d = new Date(createdAt);
  if (isNaN(d.getTime())) return "1970-01-01";
  const y = d.getUTCFullYear();
  const m = String(d.getUTCMonth() + 1).padStart(2, "0");
  const day = String(d.getUTCDate()).padStart(2, "0");
  return `${y}-${m}-${day}`;
}
```

- [ ] **Step 4: 跑测试确认通过**

Run:
```bash
cd twitter-crawler && npm test 2>&1 | grep -E "render|passing|failing"
```
Expected: 6 个 render 测试 passing。若有失败，对照断言微调（特别是 title 转义与媒体块格式）。

- [ ] **Step 5: Commit**

```bash
git add twitter-crawler/src/render.ts twitter-crawler/test/render.test.ts
git commit -m "feat(twitter-crawler): markdown rendering (all tweet types + media)"
```

---

### Task 7: `io.ts` — 路径与去重（纯 + existsSync）

**Files:**
- Create: `twitter-crawler/src/io.ts`
- Test: `twitter-crawler/test/io.test.ts`

**Interfaces:**
- Produces: `formatDate`、`tweetFilePath(dir, rt)`、`alreadySaved(path)`

- [ ] **Step 1: 写失败测试 `twitter-crawler/test/io.test.ts`**

```ts
import { test } from "node:test";
import assert from "node:assert/strict";
import { formatDate, tweetFilePath, alreadySaved } from "../src/io.js";
import type { RawTweet } from "../src/types.js";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

test("formatDate: 解析 X 时间串", () => {
  assert.equal(
    formatDate("Sat Jun 01 08:00:00 +0000 2024"),
    "2024-06-01"
  );
});

test("formatDate: 非法串返回 unknown-date", () => {
  assert.equal(formatDate("garbage"), "unknown-date");
});

test("tweetFilePath: 格式 <date>-<id>.md", () => {
  const rt: RawTweet = {
    id: "123",
    text: "x",
    createdAt: "Sat Jun 01 08:00:00 +0000 2024",
    urls: [],
    media: { images: [], videos: [] },
    screenName: "Wen_Zw",
    displayName: "Wen",
    threadParts: [],
    promoted: false,
  };
  assert.equal(
    tweetFilePath("content/inbox/twitter/Wen_Zw", rt),
    "content/inbox/twitter/Wen_Zw/2024-06-01-123.md"
  );
});

test("alreadySaved: 文件存在返回 true", () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "tc-"));
  const f = path.join(dir, "x.md");
  fs.writeFileSync(f, "hi");
  assert.equal(alreadySaved(f), true);
  assert.equal(alreadySaved(path.join(dir, "nope.md")), false);
});
```

- [ ] **Step 2: 跑测试确认失败**

Run:
```bash
cd twitter-crawler && npm test 2>&1 | grep -A2 formatDate
```
Expected: FAIL（模块不存在）。

- [ ] **Step 3: 写 `twitter-crawler/src/io.ts`**

```ts
import fs from "node:fs";
import type { RawTweet } from "./types.js";

/** X 时间串 "Sat Jun 01 08:00:00 +0000 2024" → "2024-06-01"；非法 → "unknown-date"。 */
export function formatDate(createdAt: string): string {
  const d = new Date(createdAt);
  if (isNaN(d.getTime())) return "unknown-date";
  const y = d.getUTCFullYear();
  const m = String(d.getUTCMonth() + 1).padStart(2, "0");
  const day = String(d.getUTCDate()).padStart(2, "0");
  return `${y}-${m}-${day}`;
}

export function tweetFilePath(dir: string, rt: RawTweet): string {
  return `${dir}/${formatDate(rt.createdAt)}-${rt.id}.md`;
}

export function alreadySaved(filePath: string): boolean {
  return fs.existsSync(filePath);
}
```

- [ ] **Step 4: 跑测试确认通过**

Run:
```bash
cd twitter-crawler && npm test
```
Expected: 全部 passing（到此应 20+ 个测试）。

- [ ] **Step 5: Commit**

```bash
git add twitter-crawler/src/io.ts twitter-crawler/test/io.test.ts
git commit -m "feat(twitter-crawler): path formatting + file-existence dedup"
```

---

### Task 8: 夹具 `fixtures.ts`（形状准确的合成 TweetApiUtilsData）

**Files:**
- Create: `twitter-crawler/test/fixtures.ts`

**Interfaces:**
- Produces: `fxOriginal`、`fxNoteLong`、`fxThread`、`fxQuote`、`fxRetweet`、`fxPromoted`——镜像库 `TweetApiUtilsData` 形状（用于 map.ts 单测）。

- [ ] **Step 1: 写 `twitter-crawler/test/fixtures.ts`**

```ts
// 形状准确的合成夹具，镜像 twitter-openapi-typescript 的 TweetApiUtilsData（字段路径经源码核实）。
// 真实返回结构在 Task 13 用真实 token 抓一条做对照校验；如字段名漂移则在此修正。
import type { TweetApiUtilsData } from "twitter-openapi-typescript";

const user = (screenName: string, name = screenName) => ({
  restId: "1",
  isBlueVerified: false,
  core: { screenName, name },
  legacy: { screenName, name, description: "", followersCount: 1, friendsCount: 1 },
});

const legacy = (over: Record<string, unknown> = {}) => ({
  fullText: "short text",
  idStr: "100",
  createdAt: "Sat Jun 01 08:00:00 +0000 2024",
  lang: "en",
  conversationIdStr: "100",
  favoriteCount: 0,
  replyCount: 0,
  retweetCount: 0,
  entities: { urls: [] as any[], media: [] as any[] },
  extendedEntities: { media: [] as any[] },
  ...over,
});

const tweet = (over: Record<string, unknown> = {}) => ({
  restId: "100",
  legacy: legacy(over["legacy"] as Record<string, unknown>),
  ...over,
});

const base = (over: Record<string, unknown> = {}): TweetApiUtilsData =>
  ({
    raw: {} as any,
    tweet: tweet(),
    user: user("Wen_Zw"),
    replies: [],
    ...over,
  }) as unknown as TweetApiUtilsData;

/** 原创（短） */
export const fxOriginal = base();

/** 长推文（noteTweet 提供全文） */
export const fxNoteLong = base({
  tweet: tweet({
    legacy: legacy({
      fullText: "truncated… https://t.co/x",
      entities: { urls: [{ url: "https://t.co/x", expandedUrl: "https://real.example", displayUrl: "real", indices: [0, 0] }] as any[], media: [] as any[] },
    }),
    noteTweet: {
      noteTweetResults: { result: { text: "这是一条很长的推文全文，不会被截断，包含完整内容。" } },
    },
  }),
});

/** 线程：root + 1 条自回复 */
export const fxThread = base({
  tweet: tweet({
    restId: "100",
    legacy: legacy({ fullText: "thread start", conversationIdStr: "100", idStr: "100" }),
  }),
  replies: [
    {
      raw: {} as any,
      tweet: tweet({ restId: "101", legacy: legacy({ fullText: "thread cont", conversationIdStr: "100", idStr: "101", inReplyToStatusIdStr: "100" }) }),
      user: user("Wen_Zw"),
      replies: [],
    } as unknown as TweetApiUtilsData,
  ],
});

/** 引用 */
export const fxQuote = base({
  tweet: tweet({ legacy: legacy({ fullText: "my comment", isQuoteStatus: true, quotedStatusIdStr: "9" }) }),
  quoted: {
    raw: {} as any,
    tweet: tweet({ restId: "9", legacy: legacy({ fullText: "quoted full text" }) }),
    user: user("someoneelse"),
    replies: [],
  } as unknown as TweetApiUtilsData,
});

/** 转载 */
export const fxRetweet = base({
  tweet: tweet({ legacy: legacy({ fullText: "RT @someoneelse: body", retweeted: true }) }),
  retweeted: {
    raw: {} as any,
    tweet: tweet({ restId: "9", legacy: legacy({ fullText: "retweeted body" }) }),
    user: user("someoneelse"),
    replies: [],
  } as unknown as TweetApiUtilsData,
});

/** 广告（应被跳过） */
export const fxPromoted = base({ promotedMetadata: { advertiser: "x" } as any });
```

- [ ] **Step 2: 类型检查（确认夹具能赋给 TweetApiUtilsData）**

Run:
```bash
cd twitter-crawler && npx tsc --noEmit
```
Expected: 无类型错误（`as unknown as TweetApiUtilsData` 兜底，应通过）。若有报错，按提示修夹具字段。

- [ ] **Step 3: Commit**

```bash
git add twitter-crawler/test/fixtures.ts
git commit -m "test(twitter-crawler): shape-accurate TweetApiUtilsData fixtures"
```

---

### Task 9: `map.ts` — 库类型 → RawTweet（含 toRawTweet 单测）

**Files:**
- Create: `twitter-crawler/src/map.ts`
- Test: `twitter-crawler/test/map.test.ts`

**Interfaces:**
- Consumes: `TweetApiUtilsData`（库）、`expandTco`、`extractMedia`、types
- Produces: `toRawTweet(t): RawTweet | null`（被 fetch.ts 调用）

- [ ] **Step 1: 写失败测试 `twitter-crawler/test/map.test.ts`**

```ts
import { test } from "node:test";
import assert from "node:assert/strict";
import { toRawTweet } from "../src/map.js";
import {
  fxOriginal,
  fxNoteLong,
  fxThread,
  fxQuote,
  fxRetweet,
  fxPromoted,
} from "./fixtures.js";

test("toRawTweet: 原创", () => {
  const rt = toRawTweet(fxOriginal)!;
  assert.equal(rt.id, "100");
  assert.equal(rt.screenName, "Wen_Zw");
  assert.equal(rt.promoted, false);
  assert.equal(rt.threadParts.length, 0);
});

test("toRawTweet: 长推文取 noteTweet 全文 + t.co 还原", () => {
  const rt = toRawTweet(fxNoteLong)!;
  assert.equal(rt.text, "这是一条很长的推文全文，不会被截断，包含完整内容。 https://real.example");
});

test("toRawTweet: 线程续条进 threadParts 且升序", () => {
  const rt = toRawTweet(fxThread)!;
  assert.equal(rt.threadParts.length, 1);
  assert.equal(rt.threadParts[0].id, "101");
});

test("toRawTweet: quote 映射", () => {
  const rt = toRawTweet(fxQuote)!;
  assert.ok(rt.quoted);
  assert.equal(rt.quoted!.text, "quoted full text");
  assert.equal(rt.quoted!.screenName, "someoneelse");
});

test("toRawTweet: retweet 映射", () => {
  const rt = toRawTweet(fxRetweet)!;
  assert.ok(rt.retweeted);
  assert.equal(rt.retweeted!.text, "retweeted body");
});

test("toRawTweet: promoted 标记", () => {
  assert.equal(toRawTweet(fxPromoted)!.promoted, true);
});
```

- [ ] **Step 2: 跑测试确认失败**

Run:
```bash
cd twitter-crawler && npm test 2>&1 | grep -A2 toRawTweet
```
Expected: FAIL（模块不存在）。

- [ ] **Step 3: 写 `twitter-crawler/src/map.ts`**

```ts
import type { TweetApiUtilsData } from "twitter-openapi-typescript";
import type { RawTweet, MediaEntity, UrlEntity } from "./types.js";
import { expandTco } from "./text.js";
import { extractMedia } from "./media.js";

/** 库 TweetApiUtilsData → 本地 RawTweet。库字段名漂移只改这里。返回 null 表示无可用数据。 */
export function toRawTweet(t: TweetApiUtilsData | undefined | null): RawTweet | null {
  if (!t || !t.tweet) return null;
  const tw = t.tweet as any;
  const legacy = tw.legacy ?? {};
  const fullText: string = legacy.fullText ?? "";

  const noteText: string | undefined = tw.noteTweet?.noteTweetResults?.result?.text;
  const baseText = noteText ?? fullText;

  const urlEntities: UrlEntity[] = (legacy.entities?.urls ?? []).map((u: any) => ({
    url: u.url,
    expandedUrl: u.expandedUrl,
  }));

  const mediaEntities: MediaEntity[] = (legacy.extendedEntities?.media ?? []) as MediaEntity[];
  const media = extractMedia(mediaEntities);

  const screenName: string =
    t.user?.core?.screenName ?? t.user?.legacy?.screenName ?? "";
  const displayName: string =
    t.user?.legacy?.name ?? t.user?.core?.name ?? "";

  const threadParts = (t.replies ?? [])
    .map((r) => toRawTweet(r))
    .filter((x): x is RawTweet => x !== null)
    .sort((a, b) => (a.id < b.id ? -1 : a.id > b.id ? 1 : 0));

  return {
    id: tw.restId ?? legacy.idStr ?? "",
    text: expandTco(baseText, urlEntities, media),
    createdAt: legacy.createdAt ?? "",
    lang: legacy.lang,
    urls: urlEntities,
    media,
    screenName,
    displayName,
    quoted: t.quoted ? toRawTweet(t.quoted) ?? undefined : undefined,
    retweeted: t.retweeted ? toRawTweet(t.retweeted) ?? undefined : undefined,
    threadParts,
    promoted: !!t.promotedMetadata,
  };
}
```

- [ ] **Step 4: 跑测试确认通过**

Run:
```bash
cd twitter-crawler && npm test
```
Expected: 全部 passing（含 6 个 toRawTweet）。

- [ ] **Step 5: Commit**

```bash
git add twitter-crawler/src/map.ts twitter-crawler/test/map.test.ts
git commit -m "feat(twitter-crawler): map TweetApiUtilsData -> RawTweet"
```

---

### Task 10: `auth.ts` — 鉴权（薄、含干跑校验）

**Files:**
- Create: `twitter-crawler/src/auth.ts`

**Interfaces:**
- Produces: `buildClient(authToken): Promise<TwitterOpenApiClient>`

> 说明：此函数含网络副作用，不做单测；用 Task 13 的真实 token 干跑校验。**严禁**把 token/ct0 写日志。

- [ ] **Step 1: 写 `twitter-crawler/src/auth.ts`**

```ts
import { TwitterOpenApi } from "twitter-openapi-typescript";

/**
 * 用 auth_token cookie 换 ct0（CSRF），建已鉴权客户端。
 * 镜像 x-kit 的 _xClient，但绝不打印 token/cookie。
 */
export async function buildClient(authToken: string) {
  if (!authToken) throw new Error("X_AUTH_TOKEN is empty");

  // 1) GET manifest.json 带 auth_token cookie，从 set-cookie 收 ct0 等会话 cookie
  const resp = await fetch("https://x.com/manifest.json", {
    headers: { cookie: `auth_token=${authToken}` },
  });
  if (!resp.ok && resp.status !== 200 && resp.status !== 304) {
    // manifest 可能返回非 200 仍带 set-cookie；只在彻底失败时报错
  }

  const setCookies = resp.headers.getSetCookie?.() ?? [];
  const cookies: Record<string, string> = {};
  for (const sc of setCookies) {
    const pair = sc.split(";")[0];
    const idx = pair.indexOf("=");
    if (idx <= 0) continue;
    const name = pair.slice(0, idx).trim();
    const value = pair.slice(idx + 1).trim();
    if (name) cookies[name] = value;
  }
  cookies["auth_token"] = authToken;

  if (!cookies["ct0"]) {
    throw new Error(
      "Failed to harvest ct0 from x.com (token may be invalid/expired)"
    );
  }

  const api = new TwitterOpenApi();
  const client = await api.getClientFromCookies(cookies);
  return client;
}
```

- [ ] **Step 2: 类型检查**

Run:
```bash
cd twitter-crawler && npx tsc --noEmit
```
Expected: 无错误。`getSetCookie` 是 Node 22 undici 的 Headers 方法（`lib.dom` 里没有，但 `@types/node` 提供）。

- [ ] **Step 3: Commit**

```bash
git add twitter-crawler/src/auth.ts
git commit -m "feat(twitter-crawler): auth client from auth_token cookie"
```

---

### Task 11: `fetch.ts` — 分页抓取（依赖注入可测）

**Files:**
- Create: `twitter-crawler/src/fetch.ts`
- Test: `twitter-crawler/test/fetch.test.ts`

**Interfaces:**
- Consumes: 一个最小 client 接口 `{ getUserByScreenName, getUserTweets }`、`toRawTweet`、`RawTweet`
- Produces: `fetchTweetsForAccount({ client, screenName, maxPerRun, exists })` → `{ tweets: RawTweet[]; stoppedAtKnown: boolean }`

- [ ] **Step 1: 写失败测试 `twitter-crawler/test/fetch.test.ts`**

```ts
import { test } from "node:test";
import assert from "node:assert/strict";
import { fetchTweetsForAccount } from "../src/fetch.js";
import type { RawTweet } from "../src/types.js";

// 造一个假 client：返回预置页，cursor 为 undefined 表示最后一页。
function fakeClient(pages: any[][]) {
  let i = 0;
  return {
    async getUserByScreenName({ screenName }: { screenName: string }) {
      return { data: { user: { restId: "u1" } } };
    },
    async getUserTweets({ cursor }: { cursor?: string }) {
      const page = pages[Math.min(i, pages.length - 1)];
      i++;
      return { data: { data: page, cursor: { bottom: undefined } } };
    },
  };
}

const mk = (id: string): RawTweet => ({
  id,
  text: "t " + id,
  createdAt: "Sat Jun 01 08:00:00 +0000 2024",
  urls: [],
  media: { images: [], videos: [] },
  screenName: "wen",
  displayName: "Wen",
  threadParts: [],
  promoted: false,
});

test("fetch: 命中已存在文件则停止，不再翻页", async () => {
  const page = [{ promotedMetadata: undefined, __id: "100" }, { __id: "99" }];
  // 用最小桩：直接给 toRawTweet 友好的结构
  const client = {
    async getUserByScreenName() {
      return { data: { user: { restId: "u1" } } };
    },
    async getUserTweets() {
      return {
        data: {
          data: [
            { tweet: { restId: "200", legacy: { fullText: "a", createdAt: "Sat Jun 01 08:00:00 +0000 2024" } }, user: { core: { screenName: "wen" }, legacy: {} }, replies: [] },
            { tweet: { restId: "100", legacy: { fullText: "b", createdAt: "Sat Jun 01 08:00:00 +0000 2024" } }, user: { core: { screenName: "wen" }, legacy: {} }, replies: [] },
          ],
          cursor: { bottom: { value: "next-cursor" } },
        },
      };
    },
  };
  // 100 已存在
  const exists = (p: string) => p.endsWith("100.md");
  const { tweets, stoppedAtKnown } = await fetchTweetsForAccount({
    // @ts-ignore 只用我们消费的方法
    client,
    screenName: "wen",
    maxPerRun: 50,
    exists,
  });
  assert.equal(stoppedAtKnown, true);
  // 100 已存在被跳过；只产 200
  assert.equal(tweets.length, 1);
  assert.equal(tweets[0].id, "200");
});

test("fetch: maxPerRun 限制条数", async () => {
  const client = {
    async getUserByScreenName() {
      return { data: { user: { restId: "u1" } } };
    },
    async getUserTweets() {
      return {
        data: {
          data: [
            { tweet: { restId: "5", legacy: { fullText: "x", createdAt: "Sat Jun 01 08:00:00 +0000 2024" } }, user: { core: { screenName: "wen" }, legacy: {} }, replies: [] },
            { tweet: { restId: "4", legacy: { fullText: "x", createdAt: "Sat Jun 01 08:00:00 +0000 2024" } }, user: { core: { screenName: "wen" }, legacy: {} }, replies: [] },
            { tweet: { restId: "3", legacy: { fullText: "x", createdAt: "Sat Jun 01 08:00:00 +0000 2024" } }, user: { core: { screenName: "wen" }, legacy: {} }, replies: [] },
          ],
          cursor: { bottom: { value: "more" } },
        },
      };
    },
  };
  const { tweets } = await fetchTweetsForAccount({
    // @ts-ignore
    client,
    screenName: "wen",
    maxPerRun: 2,
    exists: () => false,
  });
  assert.equal(tweets.length, 2);
});
```

- [ ] **Step 2: 跑测试确认失败**

Run:
```bash
cd twitter-crawler && npm test 2>&1 | grep -A2 fetchTweetsForAccount
```
Expected: FAIL（模块不存在）。

- [ ] **Step 3: 写 `twitter-crawler/src/fetch.ts`**

```ts
import type { RawTweet } from "./types.js";
import { toRawTweet } from "./map.js";

// 最小 client 接口（与 twitter-openapi-typescript 的 client 子集兼容）
export interface MinClient {
  getUserApi(): {
    getUserByScreenName(p: { screenName: string }): Promise<{
      data: { user?: { restId?: string } | undefined };
    }>;
  };
  getTweetApi(): {
    getUserTweets(p: {
      userId: string;
      count?: number;
      cursor?: string;
    }): Promise<{
      data: {
        data: any[];
        cursor?: { bottom?: { value?: string } };
      };
    }>;
  };
}

export interface FetchOpts {
  client: MinClient;
  screenName: string;
  maxPerRun: number;
  exists: (filePathForTweetId: (id: string) => string) => boolean; // 见下，更实用：直接传 tweetId→是否已存
}

export interface FetchResult {
  tweets: RawTweet[];
  stoppedAtKnown: boolean;
}

/**
 * 抓某账号推文，分页直到：命中已存在推文、拿满 maxPerRun、或到底。
 */
export async function fetchTweetsForAccount(args: {
  client: MinClient;
  screenName: string;
  maxPerRun: number;
  isSaved: (tweetId: string) => boolean;
}): Promise<FetchResult> {
  const { client, screenName, maxPerRun, isSaved } = args;

  const userResp = await client.getUserApi().getUserByScreenName({ screenName });
  const userId = userResp.data.user?.restId;
  if (!userId) throw new Error(`account @${screenName} not found`);

  const out: RawTweet[] = [];
  let cursor: string | undefined;
  let stoppedAtKnown = false;

  for (;;) {
    const resp = await client.getTweetApi().getUserTweets({ userId, count: 40, cursor });
    for (const item of resp.data.data ?? []) {
      if (item?.promotedMetadata) continue; // 跳过广告
      const rt = toRawTweet(item);
      if (!rt) continue;

      if (isSaved(rt.id)) {
        stoppedAtKnown = true;
        return { tweets: out, stoppedAtKnown };
      }

      out.push(rt);
      if (out.length >= maxPerRun) {
        return { tweets: out, stoppedAtKnown };
      }
    }

    cursor = resp.data.cursor?.bottom?.value;
    if (!cursor) break;
  }

  return { tweets: out, stoppedAtKnown };
}
```

> 注：实现里把 `exists` 改成了更易测的 `isSaved(tweetId)`，单测里对应传 `(id) => id === "100"`。下面 Step 4 调整断言。

- [ ] **Step 4: 修正 Step 1 测试里的 `exists` 调用为 `isSaved`**

把 `test/fetch.test.ts` 里两处：
```ts
const exists = (p: string) => p.endsWith("100.md");
...
exists,
```
改为：
```ts
const isSaved = (id: string) => id === "100";
...
isSaved,
```
并把第二处 `exists: () => false` 改为 `isSaved: () => false`。

- [ ] **Step 5: 跑测试确认通过**

Run:
```bash
cd twitter-crawler && npm test
```
Expected: 全部 passing。

- [ ] **Step 6: Commit**

```bash
git add twitter-crawler/src/fetch.ts twitter-crawler/test/fetch.test.ts
git commit -m "feat(twitter-crawler): paginated account fetch with dedup stop"
```

---

### Task 12: `index.ts` — 主流程

**Files:**
- Create: `twitter-crawler/src/index.ts`
- Test: 手动干跑（Task 13）

**Interfaces:**
- Consumes: config（accounts.json + env）、buildClient、fetchTweetsForAccount、classifyTweet、renderMarkdown、io
- Produces: 读账号→抓→渲染→落盘；打印汇总（无敏感信息）；缺失 token 时 exit 0。

- [ ] **Step 1: 写 `twitter-crawler/src/config.ts`**

> 关键：爬虫在 `twitter-crawler/` 下运行，但产出必须落到**仓库根**的 `content/inbox/twitter/`（workflow 的 `git add` 在根执行）。故用 `import.meta.url` 算出仓库根，与 CWD 无关。

```ts
import path from "node:path";
import { fileURLToPath } from "node:url";
import accountsJson from "../accounts.json" with { type: "json" };

export interface Config {
  accounts: string[];
  maxPerRun: number;
  authToken: string;
  outDir: string; // 绝对路径：<repoRoot>/content/inbox/twitter
}

export function loadConfig(): Config {
  const raw = accountsJson as { accounts: string[]; max_per_run?: number };
  const accounts = (raw.accounts ?? []).map((a) => a.replace(/^@/, ""));
  const maxPerRun = Number(process.env.MAX_PER_RUN || raw.max_per_run || 20);
  const authToken = process.env.X_AUTH_TOKEN || "";

  // src/config.ts → 上两级 = 仓库根
  const here = path.dirname(fileURLToPath(import.meta.url));
  const repoRoot = path.resolve(here, "..", "..");
  const outDir = path.join(repoRoot, "content", "inbox", "twitter");

  return { accounts, maxPerRun, authToken, outDir };
}
```

- [ ] **Step 2: 写 `twitter-crawler/src/index.ts`**

```ts
import fs from "node:fs";
import path from "node:path";
import { loadConfig } from "./config.js";
import { buildClient } from "./auth.js";
import { fetchTweetsForAccount } from "./fetch.js";
import { classifyTweet } from "./classify.js";
import { renderMarkdown } from "./render.js";
import { tweetFilePath, alreadySaved } from "./io.js";

function todayUTC(): string {
  const d = new Date();
  const y = d.getUTCFullYear();
  const m = String(d.getUTCMonth() + 1).padStart(2, "0");
  const day = String(d.getUTCDate()).padStart(2, "0");
  return `${y}-${m}-${day}`;
}

async function main() {
  const cfg = loadConfig();

  if (!cfg.authToken) {
    console.log("::warning::X_AUTH_TOKEN 未配置，跳过爬取（exit 0，不报红）。");
    process.exit(0);
  }

  if (cfg.accounts.length === 0) {
    console.log("accounts.json 无账号，退出。");
    process.exit(0);
  }

  const client = await buildClient(cfg.authToken);
  const today = todayUTC();
  let totalWritten = 0;

  for (const screenName of cfg.accounts) {
    const dir = path.join(cfg.outDir, screenName);
    fs.mkdirSync(dir, { recursive: true });

    const isSaved = (id: string) =>
      alreadySaved(tweetFilePath(dir, { id } as any));

    let result;
    try {
      result = await fetchTweetsForAccount({
        client,
        screenName,
        maxPerRun: cfg.maxPerRun,
        isSaved,
      });
    } catch (err: any) {
      // 不打印 err 里可能夹带的请求细节；只给状态
      const msg = String(err?.message || err);
      if (/401|403|unauthor|ct0|invalid|expired/i.test(msg)) {
        console.error(`::error::@${screenName} 鉴权失败，X_AUTH_TOKEN 可能失效，请更换。`);
      } else if (/429|rate/i.test(msg)) {
        console.error(`::error::@${screenName} 被限流(429)，稍后再试。`);
      } else {
        console.error(`::error::@${screenName} 抓取失败：${msg}`);
      }
      continue;
    }

    let written = 0;
    for (const rt of result.tweets) {
      const type = classifyTweet(rt);
      const md = renderMarkdown(rt, type, today);
      const fp = tweetFilePath(dir, rt);
      fs.writeFileSync(fp, md, "utf8");
      written++;
    }
    totalWritten += written;
    console.log(
      `@${screenName}: fetched ${result.tweets.length}, written ${written}` +
        (result.stoppedAtKnown ? " (stopped at known)" : "")
    );
  }

  console.log(`done. total written: ${totalWritten}`);
}

main().catch((err) => {
  console.error("::error::crawler crashed:", String(err?.message || err));
  process.exit(1);
});
```

> 注：`isSaved` 里 `{ id } as any` 只用 id 算路径——可接受，但更干净是给 io 加一个 `idFilePath(dir, createdAt, id)`。为保 Task 7 接口稳定，此处用 cast。若 reviewer 要求，可在 io.ts 加 `tweetIdFilePath(dir, createdAt, id)` 复用。

- [ ] **Step 3: 类型检查 + 全量测试**

Run:
```bash
cd twitter-crawler && npx tsc --noEmit && npm test
```
Expected: 类型无误，全部测试 passing。

- [ ] **Step 4: Commit**

```bash
git add twitter-crawler/src/config.ts twitter-crawler/src/index.ts
git commit -m "feat(twitter-crawler): main wiring (config -> crawl -> render -> write)"
```

---

### Task 13: Workflow + README + 真实干跑校验

**Files:**
- Create: `.github/workflows/twitter-crawl.yml`
- Create: `twitter-crawler/README.md`
- 手动验证：配 secret、触发 workflow_dispatch、对照真实返回修夹具。

- [ ] **Step 1: 写 `.github/workflows/twitter-crawl.yml`**

```yaml
name: X/Twitter Crawl

on:
  schedule:
    - cron: "7 * * * *"        # 每小时 :07（避开 :00 高峰）
  workflow_dispatch:
    inputs:
      max_per_run:
        description: "单账号单次最大抓取数（回填用）"
        default: "20"

permissions:
  contents: write

concurrency:
  group: twitter-crawl
  cancel-in-progress: false

jobs:
  crawl:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}   # 用它推 → 不触发 okf.yml
          fetch-depth: 0

      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
          cache-dependency-path: twitter-crawler/package-lock.json

      - name: 安装依赖
        working-directory: twitter-crawler
        run: npm ci

      - name: 爬取
        working-directory: twitter-crawler
        env:
          X_AUTH_TOKEN: ${{ secrets.X_AUTH_TOKEN }}
          MAX_PER_RUN: ${{ github.event.inputs.max_per_run || '20' }}
        run: node --import tsx src/index.ts

      - name: 提交并推送
        run: |
          git config user.name  "twitter-bot"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git pull --rebase --autostash origin main || true
          git add content/inbox/twitter
          if git diff --cached --quiet; then
            echo "无新推文"
          else
            git commit -m "chore(twitter): hourly crawl [skip ci]"
            git push
          fi
```

- [ ] **Step 2: 写 `twitter-crawler/README.md`**

````markdown
# twitter-crawler

每小时抓取指定 X 账号推文（原创/长文/线程/引用/转载，不含回复），渲染成 Markdown 落到 `content/inbox/twitter/<账号>/`，交 OKF agent 每天整理。

## 配置 auth token

1. 浏览器登录 x.com。
2. DevTools → Application → Cookies → `https://x.com` → 复制 `auth_token` 的值。
3. 仓库 Settings → Secrets and variables → Actions → New repository secret：
   - Name: `X_AUTH_TOKEN`
   - Value: 上一步的值
4. （建议）仓库设为 private。

> `ct0`（CSRF）由爬虫运行时自动获取，无需配置。token 可能数周失效，401 时更换即可。建议用 burner 账号。

## 加账号

编辑 `twitter-crawler/accounts.json`：

```json
{ "accounts": ["Wen_Zw", "anotherAccount"], "max_per_run": 20 }
```

## 本地手动跑

```bash
cd twitter-crawler
npm ci
X_AUTH_TOKEN=xxx tsx src/index.ts
```

## 回填历史

Actions 页面 → X/Twitter Crawl → Run workflow → `max_per_run` 填大数（如 200）。

## 产出

- 路径：`content/inbox/twitter/<账号>/<YYYY-MM-DD>-<tweetId>.md`
- 去重：文件名含 tweetId，已存在即跳过。
- 不触发 agent：用 GITHUB_TOKEN 推送；okf.yml 每天定时 run 才整理。
````

- [ ] **Step 3: 本地干跑校验（需真实 token）**

让用户在本地执行（或自己在配好 secret 后）：
```bash
cd twitter-crawler && npm ci && X_AUTH_TOKEN=<your_token> tsx src/index.ts
```
Expected: 打印 `@Wen_Zw: fetched N, written M`，并在 `content/inbox/twitter/Wen_Zw/` 生成 md 文件。

- [ ] **Step 4: 对照真实返回校验夹具字段名**

打开生成的 md，确认正文是**全文**（长推文未被截断）、媒体 URL 附上、引用/转载含对方全文。若某类渲染异常，多半是字段路径漂移——抓一条真实 `getUserTweets` 返回（在 fetch.ts 临时 `console.log(JSON.stringify(item.raw))`，跑完删掉），对照修 `test/fixtures.ts` 和 `src/map.ts`。

- [ ] **Step 5: 在 GitHub 触发一次 workflow_dispatch 验证**

到仓库 Actions → X/Twitter Crawl → Run workflow。确认：
- 步骤全绿（或仅 token 未配时的 warning + exit 0）。
- 推送了 `content/inbox/twitter/Wen_Zw/*.md` 的 commit（commit author = twitter-bot）。
- 该 commit **没有**触发 OKF Pipeline（验证 GITHUB_TOKEN 防递归）。

- [ ] **Step 6: Commit workflow + README**

```bash
git add .github/workflows/twitter-crawl.yml twitter-crawler/README.md
git commit -m "feat(twitter-crawler): hourly workflow + usage docs"
```

---

### Task 14: OKF agent 协议——媒体保留规则

**Files:**
- Modify: `content/PRODUCER.md`（在「标准生产循环」末尾加一条）
- Modify: `.claude/prompt.txt`（第 3 步 b 加一句）

**Interfaces:** 无代码接口；改 agent 行为，使处理含媒体剪藏时保留媒体 URL。

- [ ] **Step 1: 读 `content/PRODUCER.md`「2. 标准生产循环」段，定位第 9 步后**

Run:
```bash
grep -n "处理 inbox" content/PRODUCER.md
```

- [ ] **Step 2: 在 `content/PRODUCER.md` 标准生产循环里新增第 10 条**

在「9. 处理 inbox」之后插入：

```markdown
10. **保留媒体**：若资料含图片/视频（尤其推文剪藏的 `![](url)` 或「视频：」链接），产出的概念文件**必须**保留这些媒体 URL——以 Markdown 图片 `![](url)` 或链接形式附在正文相关位置。**不得丢弃媒体**。
```

- [ ] **Step 3: 在 `.claude/prompt.txt` 第 3 步 b 末尾加一句**

定位：
```bash
grep -n "templates/ 下对应类型的模板" .claude/prompt.txt
```
在该行末尾追加：

```text
若资料含图片/视频，产出的概念文件必须保留媒体 URL（图片用 ![](url)、视频用链接），不得丢弃。
```

- [ ] **Step 4: Commit**

```bash
git add content/PRODUCER.md .claude/prompt.txt
git commit -m "feat(okf): producer protocol — preserve media URLs from clippings"
```

---

## Self-Review（plan 写完后自查，已修正）

1. **Spec 覆盖**：F1(workflow cron)→T13；F2(accounts.json)→T1/T12；F3(auth)→T10；F4(类型，排除 reply)→T5 + Spec refinement#2；F5(全文+t.co)→T3/T9；F6(quote 全文)→T6/T9；F7(媒体远程 URL)→T4/T6；F8(路径)→T7/T12；F9(去重)→T7/T11；F10(GITHUB_TOKEN+[skip ci])→T13；F11(每日 agent 扫到)→无需改扫描范围（agent 默认扫 inbox 子目录）；agent 媒体保留→T14。全覆盖。
2. **Placeholder 扫描**：无 TBD/TODO；每步都有可执行代码或命令。Step 12 的 `{ id } as any` 已加注并给出可选清理路径，非占位。
3. **类型一致性**：`RawTweet`、`toRawTweet`、`classifyTweet(rt)`、`renderMarkdown(rt,type,date)`、`fetchTweetsForAccount({client,screenName,maxPerRun,isSaved})`、`tweetFilePath(dir,rt)`、`extractMedia(entities)`、`expandTco(text,urls,media)`——签名在各 Task 间一致。Task 11 把 `exists` 改为 `isSaved(id)`，已在 Step 4 同步更新测试。
4. **风险点诚实标注**：article V1 限制、夹具真实校验（T13 Step 4）、token 失效处理（T12）均显式。

## 执行交付

Plan 已保存到 `docs/superpowers/plans/2026-06-17-twitter-crawler.md`。
