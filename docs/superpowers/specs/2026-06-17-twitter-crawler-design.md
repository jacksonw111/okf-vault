# 设计文档：X/Twitter 定时爬虫 GitHub Action

- 日期：2026-06-17
- 状态：待评审
- 作者：brainstorming 产出

## 1. 目标

新建一个**独立的** GitHub Action，每小时自动爬取预定义 X/Twitter 账号的推文，保存为 Markdown 落到本仓库的 `content/inbox/twitter/` 下，交给现有的 OKF agent 每天自动整理一次。

- 用户在仓库 Secrets 自行配置 X 的 `auth_token`。
- 第一批测试账号：`@Wen_Zw`。
- 保留的推文类型：**原创、长文、线程(thread)、引用(quote)、转载(retweet)**。**不抓回复(reply)**。
- 正文必须取**全文**（含长推文），媒体以远程 URL 附在正文里。

## 2. 背景

### 2.1 现有仓库（okf-vault）

- Quartz 知识库，遵循 "Open Knowledge Format (OKF)"。
- `content/inbox/`：原始资料 → 由 Claude Code agent 处理成 `content/concepts/{term,tool,playbook,note}` 下的概念文件 → 原始资料移到 `content/inbox/_done/`。
- 现有 inbox 剪藏 frontmatter 约定：`title` / `source` / `author: [[@user]]` / `published` / `created` / `description` / `tags: [clippings]`。
- 现有 workflow `.github/workflows/okf.yml`：
  - 触发：每天 UTC 19:00（北京 03:00）定时 / 手动 / push 到 `content/inbox/**`。
  - `process` job：跑 Claude Code agent 整理 inbox → 提交（`[skip ci]`）。
  - `publish` job：生成 `overview.md` + 构建 Quartz → GitHub Pages。
  - agent 扫描范围（见 `.claude/prompt.txt` 第 2 步）：遍历 `inbox/` 下所有文件，**只跳过 `inbox/README.md` 和 `inbox/_done/`**。
  - 已用 secret：`MINIMAX_API_KEY`、`GLM_API_KEY`。
- 本地同步脚本 `~/.local/bin/okf-sync.sh`（launchd `com.user.okf-sync.plist`，约每 30 分钟）：`git pull --rebase --autostash` → `git add -A` → `commit` → `git push`。
- `githooks/pre-commit`：对 `content/inbox/*.md` 跑 `scripts/format_clippings.py`（best-effort，不阻断）。仅匹配 `content/inbox/*.md` 一层，**不匹配** `content/inbox/twitter/**`。

### 2.2 x-kit 调研结论

参考仓库 `xiaoxiunique/x-kit`（Bun/TS，MIT）。结论：**是好参考，但不能直接 fork**——

- 它的 `fetch-tweets.ts` **明确丢弃 retweet/quote/reply**（我们要保留这些）。
- 无分页、无 thread/article 处理。
- 会把 `auth_token` 打到 stdout（安全隐患）。
- 不是 npm 库，靠 clone 消费。

其底层依赖 [`twitter-openapi-typescript`](https://github.com/fa0311/twitter-openapi-typescript)（fa0311）才是真正的构建块：反向工程 X 内部 web GraphQL 的 TS 客户端，用账号 cookie 鉴权。**本设计直接基于它**，自写一层薄封装。

**已确认的技术事实**：用仓库默认 `GITHUB_TOKEN` 推送的 commit **不会**触发同一仓库其它 workflow 的 `push` 事件（GitHub 防递归机制）。这是"每小时爬取不触发 agent"的关键。

## 3. 需求

### 功能性

- F1. 每小时（cron）自动运行；支持手动触发（含回填参数）。
- F2. 读取账号清单配置文件，逐个爬取。
- F3. 鉴权：仅用 1 个 secret `X_AUTH_TOKEN`；`ct0`（CSRF）运行时自动获取。
- F4. 捕获类型：原创 original / 长文 note tweet / 线程 thread / 引用 quote / 转载 retweet。**排除 reply**。
- F5. **取全文**：长推文用 `noteTweetResult`（非被截断的 `legacy.fullText`）；`t.co` 短链还原为真实 URL。
- F6. 引用推文：附被引用推文的**全文** + 归属 + 链接。
- F7. 媒体：图片以 `![](remote_url)` 嵌入；视频以链接列出。**V1 不下载**。
- F8. 产出 Markdown 落到 `content/inbox/twitter/<账号>/<发布日期>-<推文id>.md`。
- F9. 去重：按 `tweet_id` 文件存在性判断，已抓则跳过。
- F10. 新增推文才提交；commit message 带 `[skip ci]`；用 `GITHUB_TOKEN` 推送。
- F11. 现有每日定时 agent run 会扫到这些推文并整理（无需改扫描范围）。

### 非功能性

- N1. **绝不**把 `auth_token`/cookie/`ct0` 写入日志。
- N2. token 失效（401/403）或限流（429）时给出清晰错误，不静默失败。
- N3. 与本地同步脚本不产生文件级冲突（唯一文件名 + 无共享状态文件）。
- N4. 仓库建议 private（兜底安全）。
- N5. 不污染 Quartz 构建 / 现有 okf.yml。

## 4. 架构

```
twitter-crawler/                 # 新增独立子项目（不与 Quartz/OKF 混）
├── package.json                 # 依赖：twitter-openapi-typescript
├── tsconfig.json
├── accounts.json                # 账号清单（用户改这里加账号）
└── src/
    ├── index.ts                 # 主流程：读 accounts → 逐账号爬 → 写 md → 退出
    ├── auth.ts                  # auth_token → GET manifest.json 取 ct0 → getClientFromCookies
    ├── fetch.ts                 # getUserByScreenName → getUserTweets 分页（停止=命中已存在）
    ├── render.ts                # 推文对象 → markdown（按类型）
    └── types.ts                 # 类型定义

content/inbox/twitter/<账号>/    # 产出落点（agent 每天扫 inbox 会处理）
└── 2026-06-01-2061426518333571576.md

.github/workflows/twitter-crawl.yml   # 新增独立 workflow（不动 okf.yml）
```

**数据流**：

```
schedule(每小时) / workflow_dispatch
  → checkout(GITHUB_TOKEN, fetch-depth:0)
  → setup-node + npm ci
  → node 跑 crawler：对每个账号
        getUserByScreenName → userId
        → getUserTweets 分页
        → 逐条：reply 跳过；否则取全文+媒体 → 渲染 md
        → 文件已存在则跳过(并作为分页停止信号)；否则写入
  → git pull --rebase --autostash  (防与本地脚本撞车)
  → git add content/inbox/twitter
  → 有新文件才 commit + push (GITHUB_TOKEN, [skip ci])
```

**与现有系统的交互**：

- 推文落 `content/inbox/twitter/**` → 触发 okf.yml 的 `push` handler 吗？**不触发**（GITHUB_TOKEN 推送）。✓ 满足"每小时不触发 agent"。
- 但 okf.yml **每天定时 run** 会扫到 `inbox/twitter/**`（agent 只跳过 README 和 _done/）→ 每天自动整理一次。✓ 符合用户选择。
- 本地脚本 `git pull --rebase` 拉到这些推文，`add -A` 无新改动则不 commit。✓

## 5. 详细设计

### 5.1 鉴权（`auth.ts`）

镜像 x-kit 的 `_xClient()`，去掉日志：

1. 用 `auth_token` cookie `GET https://x.com/manifest.json`，从响应 `Set-Cookie` 取 `ct0` 及其它会话 cookie。
2. 构造 cookie 对象 → `TwitterOpenApi.getClientFromCookies(cookies)` 得到已鉴权客户端。
3. 后续请求由库自动注入 `x-csrf-token`、`authorization: Bearer <web bearer>`、cookie jar。

secret：`X_AUTH_TOKEN`（用户在仓库 Secrets 配置）。无第二个 token。

### 5.2 爬取（`fetch.ts`）

对每个账号：

1. `client.getUserApi().getUserByScreenName({ screenName })` → 取 `userId`。
2. `client.getTweetApi().getUserTweets({ userId, count: 20, cursor })` 分页。
3. 停止条件：某条推文的目标文件已存在（见 5.5 去重）。
4. `max_per_run` 控制单次上限（默认 20；回填时可调大）。

**类型过滤**：根据推文对象的字段判断，**reply 一律跳过**：

| 类型 | 判定 | 处理 |
|---|---|---|
| reply | `legacy.in_reply_to_status_id_str` 存在 **且** 不是自回复（线程续条） | 跳过 |
| retweet | `legacy.retweeted_status_result` 存在 | 渲染 retweet |
| quote | `quoted_status_result` 存在 / `legacy.isQuoteStatus` | 渲染 quote（含被引用全文） |
| thread 续条 | `in_reply_to_status_id_str` == 同账号上一条 | 折叠进线程首条 |
| article | card/独立 article 实体 | 渲染 article（见 5.3 限制） |
| original | 以上皆非 | 渲染 original |

### 5.3 全文提取（`render.ts`，关键技术点）

- 优先取 `note.noteTweetResult.result.text`（长推文完整全文）。
- 否则回退 `legacy.fullText`（短推文）。
- **URL 还原**：用 `legacy.entities.urls` 把 `t.co` 短链替换成 `expanded_url`；末尾媒体链接的 `t.co` 也还原。
- **媒体**：`legacy.entities.media` / `extendedEntities.media` → 图片 `![](media_url_https)`；视频/gif 列出 variant URL。
- **thread**：自回复链按时间顺序拼接进首条文件，正文标 `1/N`、`2/N`…。
- **quote**：附 `> 被引用 @用户：` + 其全文（同样优先 noteTweet）。
- **retweet**：附 `> 转载 @用户：` + 原文全文。
- **article 限制（诚实声明）**：X Premium 独立 "Article"（富文本长文）正文不在 `UserTweets` 返回里，V1 只能抓「标题 + 链接 + 任意 note 文本」；完整正文列为 V2（需额外抓取 article 页面）。普通长推文（note tweet）无此限制，全文可取。

### 5.4 Markdown 产出

文件名：`<YYYY-MM-DD 发布日>-<tweet_id>.md`。

frontmatter（沿用现有 inbox 剪藏约定 + 推文字段；`title`/`description`/`source` 一律双引号，符合 Quartz YAML 规范）：

```yaml
---
title: "推文前约 80 字…"
source: "https://x.com/Wen_Zw/status/2061426518333571576"
author:
  - "[[@Wen_Zw]]"
tweet_type: "original"          # original | note | thread | quote | retweet | article
tweet_id: "2061426518333571576"
published: 2026-06-01
created: "2026-06-17"
description: "推文全文或截断（双引号）"
tags:
  - "clippings"
  - "twitter"
media_count: 2                  # 可选，便于 agent/检索
---
```

正文结构：

```markdown
<全文正文>

<!-- 媒体 -->
![图片](https://pbs.twimg.com/media/....jpg)

<!-- 视频（无法直接嵌入） -->
视频：<https://video.twimg.com/...mp4>

<!-- 引用/转载时 -->
> 引用 @xxx：<被引用全文>

## 来源
<https://x.com/Wen_Zw/status/...>
```

### 5.5 去重

- 文件名含 `tweet_id`（雪花 ID 全局唯一）→ **文件存在即已抓**。
- 每条推文先 `fs.existsSync(target)` 判断：存在则跳过；分页遇到已存在即停止翻页。
- 无独立状态文件 → 无本地脚本与 Action 争抢同一文件的冲突面。

### 5.6 配置（`accounts.json`）

```json
{
  "accounts": ["Wen_Zw"],
  "max_per_run": 20
}
```

加账号只改此文件。`accounts` 为 screen_name（不含 `@`）。

### 5.7 Workflow（`.github/workflows/twitter-crawl.yml`）

```yaml
name: X/Twitter Crawl
on:
  schedule:
    - cron: "7 * * * *"        # 每小时 :07（避开 :00 全网高峰）
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
          token: ${{ secrets.GITHUB_TOKEN }}   # 关键：用它推 → 不触发 okf.yml
          fetch-depth: 0
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
          cache-dependency-path: twitter-crawler/package-lock.json
      - run: npm ci
        working-directory: twitter-crawler
      - name: 爬取
        working-directory: twitter-crawler
        env:
          X_AUTH_TOKEN: ${{ secrets.X_AUTH_TOKEN }}
          MAX_PER_RUN: ${{ github.event.inputs.max_per_run || '20' }}
        run: node dist/index.js
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

注：`node dist/index.js`——实现时用 `tsc` 编译到 `dist/`（或 `npx tsx src/index.ts`，实现期定）。token 未配置时前置校验直接 `exit 0`（不报红）。

### 5.8 agent 协议改动（`content/PRODUCER.md` + `.claude/prompt.txt`）

**新增一条硬规则**（PRODUCER.md「标准生产循环」内）：

> **媒体保留**：若 inbox 资料（尤其推文剪藏）含图片/视频，产出的概念文件**必须**保留这些媒体 URL——以 Markdown 图片 `![](url)` 或链接形式附在正文相关位置。不得丢弃媒体。

对应在 `.claude/prompt.txt` 第 3 步 b 里加一句提醒。

### 5.9 本地同步脚本（review，不改逻辑）

`~/.local/bin/okf-sync.sh` 已 `git pull --rebase --autostash` 再 push，本身能拉到 Action 的推文提交。本设计用 `tweet_id` 唯一命名 + 无共享状态文件，与本地 `git add -A` 不冲突。**不改脚本逻辑**；仅在 spec 记录：若未来 push 频率上升导致偶发 non-fast-forward，`--rebase --autostash` 是既有兜底。

## 6. 安全与可靠性

- token 绝不进日志（所有 `console.log` 经审查）。
- 401/403 → Action 失败并提示"X_AUTH_TOKEN 失效，请更换"；429 → 指数退避重试 1 次后失败提示限流。
- 单账号单次有 `max_per_run` 上限，降低被风控概率。
- 用 burner 账号的 token（有封号风险）。
- 仓库建议 private。

## 7. 决策记录

| 决策 | 选择 | 理由 |
|---|---|---|
| 存储去向 | `content/inbox/twitter/`，走每日 agent | 用户选"进 inbox + 每天 1 次自动整理" |
| 是否每小时触发 agent | 否 | 用 GITHUB_TOKEN 推送，push 不触发；仅每日定时 run 处理 |
| 爬取底层 | `twitter-openapi-typescript` | x-kit 过滤掉了要保留的类型；其底层库才是正解 |
| 回复 | 不抓 | 用户指定 |
| 引用 | 抓（含被引用全文） | 用户指定 |
| 全文 | noteTweet 优先 + t.co 还原 | 用户强调"不是简单短文" |
| 媒体 V1 | 远程 URL，不下载 | 轻量；下载列 V2 |
| 去重 | 文件存在性（tweet_id） | 无状态文件，天然避冲突 |
| runtime | Node 22 + TS | 复用 okf.yml 既有 Node 环境，不引 Bun |
| 落点路径 | `content/inbox/twitter/<账号>/` | 用户确认 |

## 8. 不在本次范围（V2 候选）

- 媒体下载到本地（耐用但膨胀仓库）。
- X 独立 Article 富文本正文完整抓取。
- 多 token 轮换 / 代理（抗风控）。
- 推文互动数（点赞/转发）快照、变更追踪。
- 按账号/类型的 Quartz 专属展示页。

## 9. 风险

- **ToS 风险**：用账号 cookie 调内部 API 属违反 X ToS；token 账号有封禁可能。缓解：burner 账号、`max_per_run` 限速、仓库 private。
- **API 漂移**：X 改 GraphQL `doc_id` 会导致 `twitter-openapi-typescript` 临时失效（上游通常几天内修）。缓解：锁版本 + 监控 Action 失败。
- **token 失效**：`auth_token` 数周可能过期，需手动更换。缓解：401 清晰报错。
- **Article 正文不全**：V1 已诚实声明限制。
- **每日 agent 处理压力**：多账号/高频推文时每日 run 要处理较多剪藏。缓解：retweet/quote 渲染精简；后续可加每日挑选机制。
