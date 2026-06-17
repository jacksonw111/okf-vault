# OKF 知识库（自动整理 + 自动发布）

这是一个 **Open Knowledge Format (OKF)** 知识库：把资料丢进 `content/inbox/`，**Claude Code + GLM-5.2** 每天定时自动整理成结构化的 Markdown 概念文件，并用 **Quartz** 自动发布成公开网站。

> 设计依据：Google Cloud《How the Open Knowledge Format can improve data sharing》。一个概念 = 一个 Markdown 文件 + YAML frontmatter（`type` 是唯一必填字段），文件之间用链接连成图谱。

## 目录结构

```
okf-vault/
├── content/              ← OKF bundle = Obsidian vault（把 Obsidian 开在这里）
│   ├── index.md          ← 知识库入口
│   ├── PRODUCER.md       ← agent 的工作协议（整理规则）
│   ├── inbox/            ← 📥 把资料扔这里；agent 处理完移到 _done/
│   ├── concepts/         ← agent 产出的概念文件落点
│   ├── templates/        ← 概念输出模板（schema）
│   ├── _dashboards/      ← 仪表盘
│   └── log.md            ← 变更记录
├── .github/workflows/okf.yml   ← 唯一的自动化管线（定时整理 + 发布）
├── .claude/prompt.txt          ← 喂给 Claude Code 的生产者提示词
└── （其余是 Quartz 引擎文件，不用动）
```

## 它怎么工作（全自动闭环）

1. **你投喂**：把资料（PDF / 文章 / 一段话）放进 `content/inbox/`，push（Obsidian Git 插件或手动）。
2. **每天定时**：`.github/workflows/okf.yml` 在 UTC 19:00（北京次日 03:00）自动跑：
   - 起 Claude Code，`--permission-mode auto`，经 GLM 原生 Anthropic 端点（`open.bigmodel.cn/api/anthropic`）用 **GLM-5.2**；
   - 按 `.claude/prompt.txt` + `PRODUCER.md` 读 inbox → 产出 `concepts/` → 更新 index/log → 归档资料；
   - 把结果 commit & push 到 main（`[skip ci]`）。
3. **同一管线紧接着**：Quartz 构建站点 → 部署到 GitHub Pages。

> **为什么不会死循环**：唯一触发器是 `schedule`。agent 自己的 push 既不会触发 schedule，用 `GITHUB_TOKEN` 推的 commit 也不会触发其它 workflow —— 结构上不可能循环。

## 你只需要做 2 件事（一次性）

### 1. 添加 GLM API Key
仓库 **Settings → Secrets and variables → Actions → New repository secret**
- Name：`GLM_API_KEY`
- Value：你的智谱 / Z.ai API key（`ANTHROPIC_AUTH_TOKEN` 用的是它）

> 配置端点：`ANTHROPIC_BASE_URL = https://open.bigmodel.cn/api/anthropic`，模型 `glm-5.2`。GLM Coding Plan 走的就是原生 Anthropic 协议，**无需任何代理 / 翻译层**。

### 2. （已由本仓库预置）确认 GitHub Pages 已开启
**Settings → Pages → Build and deployment → Source = GitHub Actions**（应当已开启；若没开，选这项即可）。

## 手动触发一次（首次验证 / 临时整理）

**Actions → "OKF Pipeline" → Run workflow**。
加好 key 后先手动跑一次，观察 `Agent 整理 inbox` 这一 job 的日志，确认 GLM 调用成功、`concepts/` 有产出。

## 日常使用

- **投喂**：资料丢 `content/inbox/` → push（或等下次定时）。
- **想立即整理**：Actions 里手动 Run workflow。
- **浏览**：打开 GitHub Pages 站点（`Actions` 里 `publish` job 完成后会显示部署 URL）。
- **本地看图谱**：用 Obsidian 打开 `content/` 文件夹，打开 Graph View。

## 角色与协议速查

- `content/PRODUCER.md`：agent 的生产协议（去重 / 命名 / frontmatter / 链接 / 索引 / 日志 / 归档）。
- `.claude/prompt.txt`：把这份 prompt 喂给 Claude Code（`-p` 模式）。
- 概念类型词表：`Term` / `Tool` / `Playbook` / `Note` / `Index`（可自行扩展为 `Dataset`/`Table`/`Metric`/`API` 等）。
