---
type: "Tool"
title: "Claude Code"
description: "Anthropic 官方的终端原生 AI 编码 agent；支持自动批准工具调用（--permission-mode auto）、非交互 print 模式（-p）、JSON/Text 输出；可通过 ANTHROPIC_BASE_URL / ANTHROPIC_AUTH_TOKEN / ANTHROPIC_MODEL 环境变量接入任意兼容 Anthropic 协议的第三方端点。"
tags: "[ai, coding-agent, cli, anthropic, claude]"
timestamp: 2026-06-17T00:00:00Z
resource: "https://docs.claude.com/en/docs/claude-code/overview"
---

# Claude Code

## 它是什么

`Claude Code` 是 Anthropic 官方推出的 **终端原生 AI 编码 agent**——不是聊天框，是一个直接住进你 shell 里的同事：能读仓库、跑命令、改文件、提 PR、解释报错，连续多轮地把一个模糊任务推进到能合的代码。

它通过 Anthropic 协议与底层模型对话，但同时支持**任何兼容该协议的第三方端点**（如自部署的 [Claude API 兼容网关](https://github.com/anthropics/anthropic-sdk-python)、企业内网代理、国内中转），只需要环境变量指过去。

## 为什么用它 / 适合什么场景

- **直接在仓库里干活**：cwd 是项目根，能 `Read` / `Edit` / `Write` / `Bash` / `Grep` 任何文件，不像 chat UI 只能贴片段。
- **长任务可接力**：通过 Plan / Todo 机制把大任务拆小，跨多轮保留上下文。
- **CI / 脚本友好**：用 `-p`（非交互）和 `--output-format json` 就能把它当一次性 subprocess 跑。
- **白盒可控**：所有动作都是显式工具调用，能审计、能 hook、能 dry-run。
- **协议开放**：通过环境变量可换模型、换 provider，适合「Claude Code + 任意后端」组合。

## 关键能力

| 能力 | 说明 |
|------|------|
| 终端原生 | 装在 `PATH` 里，叫 `claude`；不依赖 IDE / 编辑器插件 |
| 多模型 / 多后端 | 默认 Claude 全系；`ANTHROPIC_MODEL` 切模型，`ANTHROPIC_BASE_URL` + `ANTHROPIC_AUTH_TOKEN` 切端点 |
| 工具调用 | 内置 Read / Edit / Write / Bash / Grep / Glob / NotebookEdit 等，权限可按模式批准 |
| 权限模式 | `--permission-mode auto` 全自动批准；`acceptEdits` 自动批准文件改动；plan 先出方案再执行 |
| 非交互模式 | `-p "<prompt>"` 单次提问即退出；`--output-format json\|stream-json\|text` 控制输出 |
| Skills 机制 | 通过 `/<skill-name>` 加载 slash command / 复用 prompt，与 [agent skills 生态](../term/term-agent-skills.md) 衔接 |
| 项目记忆 | `CLAUDE.md`（项目级）和 `~/.claude/CLAUDE.md`（用户级）注入系统提示 |
| MCP | 通过 Model Context Protocol 接外部工具 / 数据源（数据库、GitHub、Notion…） |
| Hooks | PreToolUse / PostToolUse 钩子，可串脚本做自动化门禁 |

## 常用环境变量

| 变量 | 作用 | 例子 |
|------|------|------|
| `ANTHROPIC_BASE_URL` | 改 API 端点（指向第三方网关 / 代理） | `https://api.your-gateway.com` |
| `ANTHROPIC_AUTH_TOKEN` | 鉴权 token | `sk-xxx` |
| `ANTHROPIC_MODEL` | 默认模型 | `claude-opus-4-8`、`claude-sonnet-4-6`、`claude-haiku-4-5-20251001` |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | 轻量任务单独指定 |  |
| `CLAUDE_CODE_MAX_TURNS` | 限制 agent 最大轮次 | `30` |
| `DISABLE_TELEMETRY` | 关闭遥测 | `1` |

## 典型调用模式

```bash
# 交互式启动
claude

# 单次提问（脚本/CI 友好）
claude -p "把 /home/user/work 里的 *.tmp 找出来列出来" --output-format json

# 全自动模式（CI 修代码用）
claude --permission-mode auto -p "升级 dependencies，破坏性变更修掉，跑测试到通过"

# 切到第三方端点 + 切模型
ANTHROPIC_BASE_URL=https://my-proxy.example.com \
ANTHROPIC_AUTH_TOKEN=sk-xxx \
ANTHROPIC_MODEL=claude-sonnet-4-6 \
claude
```

## 它催生的生态

Claude Code 的 Skills 机制（`/<skill-name>` + `.claude/commands/` + `.claude/skills/`）让社区贡献了大量复用包：

- [@mattpocock 整理的 skills 合集](tool-mattpocock-skills.md) — `/grill-me` `/zoom-out` `/caveman` `/hand-off` 等
- [shadcn/improve](tool-shadcn-improve.md) — 让最强模型审计代码、出实施计划
- [Hyperagent 的设计网格 skill](tool-hyperagent-design-skill.md) — 教代理遵循 Müller-Brockmann 网格做设计
- [Archify](tool-archify.md) — LLM→JSON→SVG 的架构图 skill
- [JSON-Render / HarnessAgent](tool-json-render.md) — 让代理在沙盒里渲染真实 UI

## 关键能力（与 OKF 体系的关系）

Claude Code 是本知识库的**默认生产环境**——`PRODUCER.md` 协议就是写给它（或类似 agent）看的：`PRODUCER.md` 把它当作 inbox 消费者，能读文件、能写文件、能改 frontmatter、能归档，已经在 [在 Obsidian 里开始用 OKF](../playbook/playbook-okf-obsidian-start.md) 的「自动同步」一节里被推荐。

## 相关概念

- [Agent Skills 是什么](../term/term-agent-skills.md)
- [mattpocock/skills 合集](tool-mattpocock-skills.md)
- [shadcn/improve](tool-shadcn-improve.md)
- [Archify](tool-archify.md)
- [JSON-Render / 生成式 UI](tool-json-render.md)
- [OKF 是什么](../term/term-okf.md) — 本知识库的整理 agent（生产者），按 PRODUCER.md 把资料转成 OKF 概念
- [在 Obsidian 里开始用 OKF](../playbook/playbook-okf-obsidian-start.md)
- `PRODUCER.md 协议`
