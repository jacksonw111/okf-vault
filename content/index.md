---
type: Index
title: "我的 OKF 知识库"
description: "基于 Open Knowledge Format v0.1 的个人知识库根入口。本目录即一个 OKF bundle——一个由 Markdown + YAML frontmatter 组成、可被人和 AI agent 共同消费的知识目录。"
tags: "[okf, root]"
timestamp: "2026-06-26T16:50:00Z"
---

# 我的 OKF 知识库

> **一句话**：OKF = 一个目录里一堆 Markdown 文件，每个文件 = 一个「概念」；文件路径就是概念的身份证；用 YAML frontmatter 放结构化字段（`type` 是唯一必填项），用正文放其余内容，文件之间用链接互相连接，形成一个知识图谱。

## 目录约定（OKF v0.1）

| 规则                | 说明                                                                 |
| ------------------- | -------------------------------------------------------------------- |
| 一个概念 = 一个文件 | 文件路径 = 概念的唯一身份，路径要稳定、不要乱改                      |
| `type` 必填         | 其余字段（title / description / resource / tags / timestamp）都可选  |
| 链接互联            | 用 Markdown 链接把概念连起来 → 形成图谱（Obsidian 图谱视图直接可用） |
| `index.md`          | 每个子目录可选放一个，用于「渐进式披露」（agent 浏览层级时的导航页） |
| `log.md`            | 可选，按时间记录变更                                                 |

## 本 bundle 的概念类型（自定义，OKF 不强制）

- `Term` — 术语 / 概念定义
- `Tool` — 工具 / 软件
- `Playbook` — 操作手册 / 流程
- `Note` — 普通笔记
- `Index` — 目录导航页

## 浏览起点

- [📊 知识库仪表盘](./overview.md) ← 实时统计 / 类型分布 / 标签 / 最近更新（**从这里开始**）
- [日报](./daily/index.md) ← 每天的概念发现、新闻和数据概览
- [新闻](./news/index.md) ← 公开新闻流，只用于网站展示
- [📑 概念目录](./concepts/index.md) ← 全量概念导航
- [📥 inbox 投递区](./inbox/README.md) ← 把资料扔这里

## 核心概念

- [OKF 是什么](concepts/term-okf.md)
- [Agent Skills（代理技能包）](concepts/term-agent-skills.md)
- [LLM Wiki 模式](concepts/term-llm-wiki.md)
- [Conventional Commits](concepts/term-conventional-commits.md)

## 工具

- [Obsidian](concepts/tool-obsidian.md)
- [Cabinet](concepts/tool-cabinet.md)
- [Field Theory](concepts/tool-field-theory.md)
- [Claude Code](concepts/tool-claude-code.md)
- [Mira（Agent-native 投研）](concepts/tool-mira.md)
- [WechatOnCloud / 云微](concepts/tool-wechat-on-cloud.md)
- [OKF Enrichment Agent](concepts/tool-okf-enrichment-agent.md)
- [OKF Static HTML Visualizer](concepts/tool-okf-static-html-visualizer.md)
- [OKF 参考示例 Bundles](concepts/tool-okf-sample-bundles.md)

## 网络 / NAS 工具

- [3X-UI](concepts/tool-3x-ui.md)
- [Lucky](concepts/tool-lucky.md)

## 代码质量 / Monorepo

- [Monorepo 代码质量体系搭建](concepts/playbook-monorepo-code-quality-setup.md)
- [Biome](concepts/tool-biome.md)
- [Ultracite](concepts/tool-ultracite.md)
- [Lefthook](concepts/tool-lefthook.md)
- [Turborepo](concepts/tool-turbo.md)
- [ESLint](concepts/tool-eslint.md)

## Agent Skills 生态

- [mattpocock/skills](concepts/tool-mattpocock-skills.md)
- [shadcn/improve](concepts/tool-shadcn-improve.md)
- [Archify](concepts/tool-archify.md)
- [JSON-Render / 生成式 UI](concepts/tool-json-render.md)
- [Hyperagent 设计网格 Skill](concepts/tool-hyperagent-design-skill.md)
- [BuilderIO / agent-native](concepts/tool-builder-io-agent-native.md)
- [Niamos](concepts/tool-niamos.md)
- [loops.elorm.xyz](concepts/tool-loops-elorm-xyz.md)

## 前端 / 设计资源

- [transitions.dev](concepts/tool-transitions-dev.md)
- [textmotion.dev](concepts/tool-textmotion-dev.md)
- [index.how/to/articulate](concepts/tool-index-how-articulate.md)
- [animations.dev/vocabulary](concepts/tool-animations-dev-vocabulary.md)
- [Trees（IDE 风格文件树组件）](concepts/tool-trees-rammcodes.md)
- [Vercel Design System](concepts/tool-vercel-design-system.md)
- [前端 / 创客 资源合集](concepts/note-front-end-resources.md)
- [DESIGN.md 最佳实践](concepts/note-design-md-best-practices.md)
- [Vibecoded Design Tells（AI 生成网站的设计特征排名）](concepts/tool-vibecoded-design-tells.md) — 320 万条 Reddit 帖子总结的「AI 网站视觉痕迹」排行
- [liquid-glass](concepts/tool-liquid-glass.md) — React 零依赖液态玻璃折射组件
- [Astro 7](concepts/tool-astro-7.md) — 内容驱动 Web 框架第 7 主版本
- [sitecheck](concepts/tool-sitecheck.md) — 浏览器扩展嗅探网站技术栈 + Geo / DNS / WHOIS
- [Web 图标库精选合集](concepts/tool-icon-libraries.md) — 20 万+ 图标 / 动效 / 多风格 / 品牌 / 导出 React & SVG
- [beUI Animated Select](concepts/tool-beui-select.md) — shadcn 风格动效 Select，面板从 trigger 处「捏合」成 pill + 弹簧回弹
- [heroicons-animated（316 个动效 Heroicons）](concepts/tool-heroicons-animated.md) — Tailwind Labs Heroicons 的动效版合集，Vercel 托管
- [Solar Wanderer](concepts/tool-solar-wanderer.md) — 浏览器内 NASA JPL 精度的实时太阳系 3D 模拟器（Three.js + WebGL2），gzip 后 ~200KB
- [Clarify](concepts/tool-clarify.md) — 面向 MDX + OpenAPI 的开源文档发布工具，本地优先 CLI + AI 可读 llms.txt
- [article-tools](concepts/tool-article-tools.md) — 纯前端 HTML 工具集：封面 / 二维码 / MD 转微信公众号 / MD 转 X 排版
- [Penpot](concepts/tool-penpot.md) — 开源自托管 Figma 替代，SVG/CSS/HTML 开放标准 + MCP + 实时协作
- [shadcn themes on 21st.dev](concepts/tool-shadcn-themes-21st.md) — 21st.dev 聚合所有 shadcn 社区主题，浏览器实时预览 + 一键 ship
- [gradient-shimmer-swiftui](concepts/tool-gradient-shimmer-swiftui.md) — SwiftUI 渐变闪光效果库，给 Apple 平台 UI 加高级感
- [Astryx](concepts/tool-astryx.md) — Meta 开源设计系统，StyleX 样式底层、150+ 可访问组件、CSS 变量级换肤
- [matrix-swift](concepts/tool-matrix-swift.md) — dot-matrix 移植到 SwiftUI 的点阵动画 View
- [Number Stepper UX](concepts/note-number-stepper-ux.md) — 长按 + 滚动数字 + 渐变遮罩的步进器动效原则
- [Kinetics](concepts/tool-kinetics.md) — 开源运动效果动画库，99 个动画同时提供 CSS + React + AI Prompt 三种版本
- [Cloudflare Kumo](concepts/tool-kumo.md) — Cloudflare 官方开源 UI 组件库与文档框架（TypeScript + React），面向 dashboard / 工单 / 监控
- [Toolcraft](concepts/tool-toolcraft.md) — pixel-point 出的创意类应用 starter kit，自带 canvas + 工具栏 + 滑块 + 曲线 + 拾色器，配套 AI 指令让 agent 直接出视觉工具
- [Componentry](concepts/tool-componentry.md) — componentry.dev 上的组件目录站，按类别聚合高质量交互组件，每组件 demo + 源码 + 复制按钮

## 听写 / 语音输入

- [Verenu](concepts/tool-verenu.md) — Tauri + Svelte 按住说话听写，本地优先 + 可换转写 API
- [Purr](concepts/tool-purr.md) — macOS Apple Silicon 菜单栏按住说话听写，全程本地推理

## 终端 / 系统管理

- [wlctl](concepts/tool-wlctl.md) — Rust 终端网络 TUI：WiFi / 热点 / 网卡 / VPN / WireGuard / doctor 排查
- [hush](concepts/tool-hush.md) — 密钥按名注入子进程环境的 Bash 工具，杜绝密钥进聊天记录
- [tmux-workbench](concepts/tool-tmux-workbench.md) — Rust 写的 tmux 会话记忆管理器，本地 + SSH 会话统一索引，CLI + TUI 一入口
- [GAM（GitHub 账号管理器）](concepts/tool-gam.md) — TypeScript CLI，OAuth 设备流程管理多个 GitHub 账号，无密码 / PAT / SSH 配置
- [pushcv-cli](concepts/tool-pushcv-cli.md) — 终端求职看板 CLI，四列流程 + AI 定制简历 + LinkedIn 抓取 + 薪资估算
- [noodle](concepts/tool-noodle.md) — 终端 REST 客户端（TUI），请求存 YAML 方便 Git 版本管理

## 电商 / 自动化

- [xianyu-super-butler](concepts/tool-xianyu-super-butler.md) — 闲鱼店铺管理平台：自动回复 / AI 议价 / 自动发货 / 多账号

## AI / Agent 生态

- [CopilotKit](concepts/tool-copilotkit.md)
- [ShipSwift](concepts/tool-shipswift.md)
- [forkd](concepts/tool-forkd.md)
- [Sophon](concepts/tool-sophon-at.md)
- [云端 Agent 基础设施的设计教训（CREAO）](concepts/note-cloud-agent-infrastructure.md)

### Agent 框架 / Skills / MCP 工具

- [agentcn（shadcn 的 AI Agent UI）](concepts/tool-agentcn.md)
- [Vercel Eve 框架](concepts/tool-vercel-eve-framework.md)
- [Vercel Labs Personal AI Template](concepts/tool-vercel-personal-ai-template.md)
- [ORGII](concepts/tool-orgii.md)
- [Repo→Agent](concepts/tool-repo-agent-generator.md)
- [CodexPro](concepts/tool-codexpro.md)
- [DevSpace](concepts/tool-devspace-mcp.md)
- [Codex Control Plane MCP](concepts/tool-codex-control-plane-mcp.md)
- [DeepSeek MCP WebSearch](concepts/tool-deepseek-mcp-websearch.md)
- [Obscura（Rust 无头浏览器）](concepts/tool-obscura-headless-browser.md)
- [GPT Image Skills](concepts/tool-gpt-image-skills.md)
- [Datalab LIFT（视觉文档 JSON 抽取模型）](concepts/tool-datalab-lift.md) — 9B VLM，给 JSON Schema 直接吐出符合格式的 JSON
- [Loops（jwangkun/loops）](concepts/tool-loops-jwangkun.md) — 100 个 AI 自动化循环模板
- [cognee](concepts/tool-cognee.md) — 可自托管的 AI 智能体持久长期记忆（知识图谱 + 向量检索）
- [DeepSpec](concepts/tool-deepspec.md) — DeepSeek 开源投机解码全栈框架（Eagle3 / DFlash / DSpark）
- [ai-brand-monitor-mcp](concepts/tool-ai-brand-monitor-mcp.md) — 品牌在四大 AI 平台可见性的 MCP 监测工具
- [Loopy](concepts/tool-loopy.md) — Forward Future 的带自我验证代理循环工作流模板
- [OpenTag](concepts/tool-opentag.md) — CopilotKit 开源自托管 Slack AI 代理
- [AI 视频广告提示词库](concepts/tool-ai-video-ad-prompts.md)
- [AI Humanizer Handbook](concepts/tool-ai-humanizer-handbook.md)
- [pi-task](concepts/tool-pi-task-delegation.md) — Pi Agent 子任务委派扩展（前台 / 后台 + TUI 进度条）
- [Proxide](concepts/tool-proxide.md) — 任意 Agent 经 MCP / 浏览器接 ChatGPT Pro 网页强模型
- [Claude Code 微醺创意 Skill](concepts/tool-claude-code-tipsy-skill.md) — 模拟「微醺」状态做创意头脑风暴
- [Yozu Web](concepts/tool-yozu-web.md) — 企业差旅 AI 的前端 MVP
- [Soul Grader Skill（SOUL.md 结构化评分）](concepts/tool-soul-grader-skill.md) — Hermes Agent 社区技能，9 维度量化 SOUL.md 身份文件质量
- [PeakCode（AI 编码代理的图形界面）](concepts/tool-peakcode.md) — 多代理会话统一 GUI + Git 工作流整合
- [Brigade](concepts/tool-brigade.md) — 本地 AI 代理团队 + Tideline 共享长期记忆
- [AgentStalker](concepts/tool-agent-stalker.md) — 把 LLM Agent 当系统而非模型来审计
- [motion-skills](concepts/tool-motion-skills.md) — iart 发布的 50 个运动图形 Skill
- [Light-skills](concepts/tool-light-skills.md) — 28 个科研全流程 AI Skill
- [AgentCrew](concepts/tool-agent-crew.md) — 多智能体协作聊天应用
- [Aura-IDE](concepts/tool-aura-ide.md) — Planner/Worker 双智能体本地编码工作台
- [Evano Studio](concepts/tool-evano-studio.md) — Electron + Python 本地 AI 桌面工作台
- [Lumina](concepts/tool-lumina-agent-runtime.md) — 端侧 AI Agent 轻量运行时
- [Nemos](concepts/tool-nemos-memory.md) — 带分层记忆的 AI 陪伴聊天
- [GameDesignOS](concepts/tool-game-design-os.md) — 本地 AI 辅助游戏设计 OS
- [happy-figure-skill](concepts/tool-happy-figure-skill.md) — 科研绘图 prompt 生成 Skill
- [Casting-Workflow](concepts/tool-casting-workflow.md) — 番茄小说短篇生成：5 篇指纹互消绕查重
- [Qwen-AgentWorld](concepts/tool-qwen-agentworld.md) — 通义千问原生语言世界模型
- [Skill_MAS](concepts/tool-skill-mas.md) — 元技能进化自动设计多智能体系统
- [zu-article-image-skill](concepts/tool-zu-article-image-skill.md) — Markdown 文章配图 Skill
- [speaker（学术演讲 PPTX 备注 Skill）](concepts/tool-speaker-pptx-skill.md) — 文本提取 + 渲染 + OCR + 视觉审查
- [MemGUI-Agent](concepts/tool-memgui-agent.md) — 快手开源移动端 GUI Agent，ConAct 把上下文管理塞进模型输出
- [paper-lifecycle](concepts/tool-paper-lifecycle.md) — 论文写作 Codex skills 套件，审稿式体检 + Rebuttal 策略
- [EchoesVault（OpenCode 持久记忆）](concepts/tool-echoes-vault-opencode.md) — OpenCode 插件，会话结束自动记决策
- [Age of Agents](concepts/tool-age-of-agents.md) — 把 AI 编码会话渲染成像素艺术王国
- [backend-agent-resume-scout（牛肉项目雷达）](concepts/tool-backend-agent-resume-scout.md) — Codex 用的简历项目发现 Skill
- [LilBot Agent](concepts/tool-lilbot-agent.md) — Python + prompt_toolkit 全屏 TUI 编码代理
- [claude-code-best-practice](concepts/tool-claude-code-best-practice.md) — 60k+ 星 Claude Code 资源合集
- [page-agent（阿里浏览器端 GUI Agent）](concepts/tool-page-agent.md) — 纯 TS 文本操作 DOM，四种接入
- [12-Factor Agents](concepts/tool-12-factor-agents.md) — HumanLayer 23.5k 星，12 条 Agent 工程原则
- [EverOS](concepts/tool-everos.md) — 统一本地长期记忆层，多 agent 共享与进化
- [Recall](concepts/tool-recall-claude-code.md) — Claude Code 离线持久化项目记忆插件
- [pi-web-agent](concepts/tool-pi-web-agent.md) — Pi 编码代理的网页工具包，老实上网
- [pi-fusion](concepts/tool-pi-fusion.md) — Pi 多模型并行扇出 + 汇总扩展
- [browser-search](concepts/tool-browser-search-agent.md) — SearXNG + Camofox + CloakBrowser 自托管搜索栈
- [Fable 5 World Demo](concepts/tool-fable5-world-demo.md) — 浏览器内 4×4km 完全程序化开放世界
- [Heartmorrow](concepts/tool-heartmorrow.md) — 本地 LLM 约会 + 世界模拟器
- [obsidian-knowledge-agent](concepts/tool-obsidian-knowledge-agent.md) — 六阶段 AI 管道自动整理 Obsidian 笔记
- [NVIDIA Skills](concepts/tool-nvidia-skills.md) — NVIDIA 官方 Agent Skills 合集，覆盖 CUDA / Jetson / NeMo 等 200+ 技能
- [llmaker](concepts/tool-llmaker.md) — Go 写的私有 LLM 应用栈编排器，一条命令拉起 RAG / Agent / 监控
- [pi-claude-bridge](concepts/tool-pi-claude-bridge.md) — Pi 扩展，把 Claude Code 作为 provider 或 AskClaude 工具接入
- [Open Knowledge（Inkeep）](concepts/tool-open-knowledge.md) — WYSIWYG Markdown 编辑器 + LLM 知识库，AI 直接读写文档
- [AgentSpace](concepts/tool-agentspace.md) — HKUDS 出品的人 + AI 代理团队协作平台
- [Loop Engineering](concepts/tool-loop-engineering.md) — 把 AI agent 编成自动循环的方法论 + 三个 CLI（loop-audit / loop-init / loop-cost）
- [Flounder](concepts/tool-flounder.md) — 把编码 agent 包装为端到端白帽安全审计系统，每步沙箱隔离
- [Floci](concepts/tool-floci.md) — LocalStack 的免费开源替代，本地 AWS 模拟器
- [MCO（多 AI 编程代理编排层）](concepts/tool-mco.md) — 中立的代理编排层，同时调度 Claude Code / Codex CLI / Gemini CLI 等多种 CLI 代理
- [second-brain-cloudflare](concepts/tool-second-brain-cloudflare.md) — Cloudflare Workers 上的开源共享记忆层，MCP 协议让 Claude/Codex/Cursor 共用一份长期记忆
- [OpenSeek（MoonBit DeepSeek 编程助手框架）](concepts/tool-openseek-moonbit.md) — MoonBit 写的编程助手基础库 + CLI，数据/网络/Agent/CLI 四层解耦
- [Study Dost AI](concepts/tool-study-dost-ai.md) — STEM 学习助手，每个概念同时给分步走 / 生活类比 / 视觉提示三种讲法
- [AI Media Assistant](concepts/tool-ai-media-assistant.md) — 中文创作者本地短视频生成 Web 工具，文案/字幕/配图/TTS/导出全流程
- [Cinema Manager](concepts/tool-cinema-manager.md) — 找片 Skill，多源搜索 + 质量评分 + 自动转存 + 整理成 Infuse/Plex/Jellyfin 目录
- [OpenMontage](concepts/tool-openmontage.md) — 首个开源 agentic 视频制作系统，自然语言到成片，Remotion 编程式渲染
- [codebase-memory-mcp](concepts/tool-codebase-memory-mcp.md) — 基于知识图谱的代码结构索引 MCP（tree-sitter + Hybrid LSP）
- [Cotal](concepts/tool-cotal.md) — 多智能体开放协议框架，拓扑可配（对等/经理制/指挥链/混搭）
- [AIGX](concepts/tool-aigx.md) — 开放的 AI 编程代理上下文格式，per-file 边界索引 + 零源码注入
- [grove（Entelligentsia）](concepts/tool-grove-tree-sitter.md) — tree-sitter 结构化代码访问工具，CLI + MCP 双面，27 语言 / 7 工具
- [cocoindex-code](concepts/tool-cocoindex-code.md) — AST 语义代码搜索引擎，省 70% token，30+ 语言
- [Orca（stablyai）](concepts/tool-orca-coding-ide.md) — 开源 Coding IDE 套壳，跨 Mac/Win/Linux，CC/Codex/pi/opencode 全兼容
- [mux（Claude Code tmux 插件）](concepts/tool-mux-claude-tmux.md) — tmux 浮动面板管理多个 Claude Code 会话
- [Amber（offchainthoughts）](concepts/tool-amber-vector-commitment.md) — 向量嵌入自验证便携文件，整哈希 + 抽样审计
- [Dating Coach Skill（HowToGetAlongWithGirls）](concepts/tool-dating-coach-skill.md) — Claude 用的恋爱教练技能包，聊记录分析 + 阶段诊断 + 道德底线
- [12306-mcp](concepts/tool-12306-mcp.md) — 12306 购票查询 MCP 服务器，让 AI 助手直接查车票/列车/中转
- [brain2qwerty](concepts/tool-brain2qwerty.md) — Meta + BCBL 开源项目，从 MEG/EEG 脑电信号里还原人正在打的字
- [animarouter](concepts/tool-animarouter.md) — 聚合 16+ LLM 提供商免费额度到单一 OpenAI 兼容接口，9 种路由策略含 Auto 元老虎机
- [opencode-cc](concepts/tool-opencode-cc.md) — 高性能 API 代理，把 OpenCode Zen 协议桥接为 Anthropic / OpenAI 兼容，让 Claude Code / Codex CLI 透明用国产模型
- [clearCore](concepts/tool-clearcore.md) — C++20 写的 MIPS CPU 模拟器，TUI + Qt6 双前端，单周期与 5 级流水线可运行时切换
- [sim-use](concepts/tool-sim-use.md) — CLI 让 AI Agent 观察与操作 iOS 模拟器与 Android 设备屏幕，读无障碍树省 16× tokens
- [Fundamental-Ava](concepts/tool-fundamental-ava.md) — Python 大规模多智能体模拟框架，能跑上千智能体观察涌现，含统计检验涌现检测器与 BFT 共识等文明层组件
- [hermes-desktop](concepts/tool-hermes-desktop.md) — Hermes Agent 的原生桌面 GUI 客户端
- [Ornith-1](concepts/tool-ornith-1.md) — DeepReinforce 开源编程智能体模型系列，9B/35B/397B 三规格，RL 同时优化解决方案与 scaffold
- [paper2anything](concepts/tool-paper2anything.md) — Claude Code 技能包，给论文 PDF 自动生成 PPT / 海报 / 项目主页 / 小红书 / 公众号 5 种宣传物料
- [patent-disclosure-skill](concepts/tool-patent-disclosure-skill.md) — AgentSkills 技能，从项目文档与代码自动生成中国专利技术交底书
- [agent-lock](concepts/tool-agent-lock.md) — eBPF LSM 把 AI 代理限制在指定目录，实时显示打开的每个文件
- [OpenWiki](concepts/tool-openwiki.md) — LangChain 团队 CLI，扫描代码库生成 wiki 并写入 AGENTS.md / CLAUDE.md
- [happier](concepts/tool-happier.md) — 端到端加密跨设备 AI 编码客户端，电脑跑编码会话手机接着干
- [tokenscope](concepts/tool-tokenscope.md) — macOS / Windows 菜单栏实时显示 Claude CLI token 用量与分解
- [integrations.sh](concepts/tool-integrations-sh.md) — 开源第三方集成目录，收录 MCP / API / CLI / GraphQL 服务器
- [Agent-Reach](concepts/tool-agent-reach.md) — 一行命令给 AI 编码 agent 装上互联网能力（Twitter / Reddit / YouTube 转录 / GitHub / 小红书 / B 站），无 API key 无需账号
- [anysearch-skill](concepts/tool-anysearch-skill.md) — 给 AI agent 用的统一实时搜索 Skill，多家搜索引擎聚合 + 重排序
- [agent-sphere](concepts/tool-agent-sphere.md) — Java 21 + Spring Boot 3.4 的 AI Agent 编排平台，多模型路由 + ReAct + 多级记忆 + MCP + SSE
- [kcap-cli](concepts/tool-kcap-cli.md) — AI 编码助手的可观测性 CLI，捕获会话生命周期 / 对话 / 子代理树 / 工具调用 / token 用量并仪表盘展示
- [SkillSpec](concepts/tool-skillspec.md) — 把 AI Agent 的 Skills 当成可遵守 / 可测试 / 可验证的契约，一条命令跑完整风险评估
- [firstmate](concepts/tool-firstmate.md) — 目录结构 + 规则组合，把终端编码 AI 变「大副」，自动派多个 crewmate 并行干活
- [Strix](concepts/tool-strix.md) — 自主 AI 渗透测试 agent，输出可直接复现的 PoC 而不是误报清单
- [Cliare](concepts/tool-cliare.md) — Rust 写的 CLI 黑盒审计工具，给 CLI 打 Agent 就绪评分 + 安全报告
- [claude-real-video](concepts/tool-claude-real-video.md) — Python 工具，按场景变化 + 字幕智能抽帧，让 AI 真正看懂视频
- [marketing-studio](concepts/tool-marketing-studio.md) — Claude Code 营销工作室，`/marketing` 一条指令渲染品牌全套素材
- [agentic-mercy-10x](concepts/tool-agentic-mercy-10x.md) — Claude Code 发行版：单一路由器派单 + 写入钩子强制规范 / 测试 / 安全门禁
- [unsnooze](concepts/tool-unsnooze.md) — Claude Code / Codex / Grok / Qwen / Kimi / OpenCode / Antigravity 用量墙恢复工具
- [loop.js](concepts/tool-loop-js.md) — 目标 + 执行 + 验证三件事同一种 prompt，独立只读 Verify agent 判定达标

### 编程语言 / 工具链

- [Node.js All-in-One](concepts/tool-node-all-in-one.md)
- [PHP 8.5 零依赖微型框架](concepts/tool-php85-micro-framework.md)
- [LaTeX→MathML 编译器](concepts/tool-latex-mathml-compiler.md) — 7.69KB 构建期编译器，比 KaTeX 快 3 倍
- [Haskell 反应式交互式笔记本](concepts/tool-haskell-reactive-notebook.md) — Markdown 嵌入 Haskell 代码块
- [Nefoin](concepts/tool-nefoin-nerdfont.md) — 一键安装 Nerd Font 的轻量 CLI
- [PP-OCRv6 Studio](concepts/tool-ppocrv6-studio.md) — 飞桨 PP-OCRv6 三档模型本地 OCR
- [Rust + QUIC 高性能 IM 后端](concepts/tool-rust-quic-im.md) — Actix-web + QUIC + P2P NAT 打洞
- [laravel-zero-console](concepts/tool-laravel-zero-console.md) — Laravel Zero CLI 通用 trait（表格 / 错误码 / 路径）
- [pon](concepts/tool-pon-python.md) — Rust 写的 Python 3.14 原生编译器（JIT + AOT），目标 Python 版的 bun / v8
- [QwenAI-Webapp](concepts/tool-qwenai-webapp.md) — FastAPI + Vue 3 + DashScope 接入通义千问，流式 + 多模态

### 后端 / 部署 / 自托管

- [Single Server](concepts/tool-single-server.md) — 一台 Linux 服务器串 Cloudflare + Tailscale + Kamal 一键部署
- [OPG](concepts/tool-opg-backend.md) — 一人公司多 app 后端控制面（账号 / AI 网关 / 视频 / 支付）
- [NasberryPi](concepts/tool-nasberry-pi.md) — 树莓派轻量 NAS CLI，一条命令配 Samba
- [docker-android](concepts/tool-docker-android.md) — Docker 镜像封装 Android 模拟器
- [DataBuff](concepts/tool-databuff.md) — AI Native OpenTelemetry APM，链路追踪 + AI 智能分析
- [cfnew-deployer](concepts/tool-cfnew-deployer.md) — Cloudflare Pages 部署器面板，邮箱 + API Key 一键 Worker / Pages + KV
- [MediaCrawler](concepts/tool-mediacrawler.md) — 七平台自媒体数据采集（小红书 / 抖音 / 快手 / B 站等），Playwright + JS 表达式签名
- [Gorest](concepts/tool-gorest.md) — Codex 驱动的 2D 动画精灵表生成器与场景合成工作台
- [Open GENAI](concepts/tool-open-genai.md) — 日本数字厅 GENAI 的本地化开源版，Keycloak + FastAPI + SQLite + Qdrant + faster-whisper
- [dbosify-py](concepts/tool-dbosify-py.md) — Temporal Python 的 Postgres 平替，零额外基础设施的持久化工作流
- [FlareMo](concepts/tool-flaremo.md) — Cloudflare Workers + D1 + R2 上的 Flomo 风格时间线笔记，兼容 Memos API
- [dd（JIT 容器）](concepts/tool-dd-jit-container.md) — Rust + C + JIT 在 macOS 上直接跑 Linux 容器（无 VM/Hypervisor），兼容 Docker CLI
- [HttpSMS](concepts/tool-httpsms.md) — 自托管短信网关，闲置 Android 手机变 HTTP 短信 API，云函数 / CI / AI agent 都能调

### 桌面 / 系统工具

- [OmniWM（macOS 水平滚动平铺 WM）](concepts/tool-omniwm-macos.md)
- [Forel（macOS 文件夹自动化）](concepts/tool-forel-macos.md)
- [BiliMusic（B 站音乐播放器）](concepts/tool-bili-music-electron.md)
- [LX Music Desktop](concepts/tool-lx-music-electron.md) — Electron 跨平台桌面音乐播放器，兼容 LX 音源生态
- [桌面 Markdown 浏览编辑器](concepts/tool-markdown-desktop-browser.md) — 文件树 + 渲染预览 + Mermaid + 大纲
- [Waylandar](concepts/tool-waylandar.md) — Wayland 桌面上的 Google Calendar 桌面挂件
- [Vaultty](concepts/tool-vaultty.md) — macOS 块式终端 + 钥匙串自动注入 .env
- [本地 AI 桌面工作台](concepts/tool-local-ai-workbench.md) — Electron + 模型/Agent/路由三件套，本地优先 AI 桌面应用
- [AQBot（AI 对话 / Agent / 网关桌面客户端）](concepts/tool-aqbot.md) — Tauri 2 多服务商对话 + Agent + API 网关三件套
- [linXiv（本地优先学术论文管理）](concepts/tool-linxiv.md) — Tauri 桌面，SQLite + Gemini 标注 + Obsidian 集成 + 论文网络图
- [Ember（原生 SwiftUI Hacker News 阅读器）](concepts/tool-ember-hackernews.md) — iOS/iPad/Mac 零依赖，评论原生展开 + 无障碍自动匹配
- [OpenMac](concepts/tool-openmac.md) — Swift macOS 本地 HTTP 服务，把 Vision / Translation 等系统能力暴露成 JSON API
- [Targie](concepts/tool-targie-similar-finder.md) — macOS 重复 / 视觉相似视频与图片扫描工具
- [Dfetch](concepts/tool-dfetch.md) — Go 写的轻量系统信息工具，neofetch 风格但更克制
- [DeskBox](concepts/tool-deskbox.md) — WinUI 3 桌面整理工具，托盘 / 全局快捷键管理文件收集与文件夹映射
- [Evano Studio](concepts/tool-evano-studio.md) — Electron + Python 本地 AI 桌面工作台
- [y-times-y / y](concepts/tool-y-times-y.md) — 可自我修改的桌面编程智能体
- [pi-desktop](concepts/tool-pi-desktop.md) — Pi Coding Agent 原生桌面外壳
- [autoshorts](concepts/tool-autoshorts.md) — 长视频转竖屏短视频
- [repotato](concepts/tool-repotato.md) — GitHub 日报 TUI + 本地 Claude 试用
- [lex-ghostty-shaders](concepts/tool-lex-ghostty-shaders.md) — Ghostty 终端水波纹 shader
- [shuangzi-xubei（双子续杯）](concepts/tool-shuangzi-xubei.md) — iPhone 桌面小组件，锁屏看 Claude Code / Codex 额度
- [MoChord（和弦创作工作台）](concepts/tool-mochord.md) — React + Tauri 2，和弦 / 把位 / AI 编曲
- [Free-TV/IPTV](concepts/tool-free-tv-iptv.md) — 全球免费电视频道 M3U 列表
- [Plaza](concepts/tool-plaza.md) — 跨发行版 TUI 包管理器，同时搜 Arch 官方源 + AUR
- [lazycron](concepts/tool-lazycron.md) — Go 写的 Linux cron TUI 管理器，vim 风格快捷键
- [tabiew](concepts/tool-tabiew.md) — Rust 写的 TUI 表格数据查看器，CSV / Parquet / JSON / Excel
- [Mineradio](concepts/tool-mineradio.md) — Electron 沉浸式 Windows 音乐播放器
- [Plex TUI](concepts/tool-plex-tui.md) — Python 写的终端 Plex 客户端，三栏布局 + Kitty/Ghostty 原生图片显示 + mpv 播放
- [Kanarenshu（假名练习 TUI）](concepts/tool-kanarenshu.md) — Go 写的终端日语假名练习工具，权重自适应算法多练薄弱字符
- [TidyFS（Linux 智能文件整理）](concepts/tool-tidyfs.md) — Go + Python 混编，按内容与文件名自动归类文档
- [TorLink（终端种子搜索下载）](concepts/tool-torlink.md) — Node.js 零配置 `npx torlnk`，聚合 FitGirl / YTS / 海盗湾 / 1337x / Nyaa
- [Refloow Photo Studio](concepts/tool-refloow-photo-studio.md) — Electron 桌面照片编辑器，完全本地运行 / 无水印
- [linux-antiquity](concepts/tool-linux-antiquity.md) — Hyprland 古典艺术风格主题包，Quickshell + 终端配色 + 图标 + 天气
- [MacOS-DPIManager](concepts/tool-macos-dpi-manager.md) — SwiftUI + IOKit 给外接显示器开 HiDPI
- [Vesta](concepts/tool-vesta-terminal.md) — macOS 原生终端，Swift/AppKit + GhosttyKit Metal 渲染；session 持久化（vestad 守护进程），为 AI 编码 agent 多会话并行设计
- [WaLinux](concepts/tool-walinux.md) — Linux 原生 WhatsApp 桌面客户端，Tauri 2 实现，比 Electron 更省资源
- [WeatherMaster](concepts/tool-weathermaster-android.md) — Android 本地天气 App，Kotlin 写仿 Pixel UI，聚合十几家气象数据源
- [ackem](concepts/tool-ackem.md) — 本地优先 Windows 桌面 AI 伙伴（Electron），记忆 / 情绪 / 关系感知全存本地
- [MacTools](concepts/tool-mac-tools.md) — 免费开源 macOS 菜单栏工具集（SwiftUI），Homebrew 一键装，30+ 小工具
- [CloseUp](concepts/tool-closeup.md) — macOS 原生小工具，给 Mission Control 缩略图直接加窗口操作按钮
- [MacMTP](concepts/tool-macmtp.md) — macOS 通过 USB MTP 协议原生传文件到 Android（SwiftUI + Go）
- [Dory](concepts/tool-dory.md) — macOS 上 Docker Desktop / OrbStack 的开源替代品，共享 Linux VM + 真 docker socket + 一键 K8s + ~6 MB 单二进制
- [Worf](concepts/tool-worf.md) — MIT 本地优先桌面应用，看板 / 笔记 / OKR / AI 聊天 / Sprint / 终端六合一
- [OpenNook](concepts/tool-opennook.md) — Swift 框架在 macOS 刘海区域跑自定义 SwiftUI 应用，展开 / 收起、磨砂背景、快捷键全内置
- [Hermex](concepts/tool-hermex.md) — SwiftUI 写的 iOS 应用，远程操控自托管 Hermes AI 代理（聊天 / 任务 / 技能 / 文件 / 用量）
- [SiphonDB](concepts/tool-siphondb.md) — Tauri v2 跨平台桌面数据库 GUI（PostgreSQL / MySQL / SQLite），内置 Rust 多线程 SSH 隧道
- [Squawk](concepts/tool-squawk.md) — macOS 智能通知代理，给 Claude Code 用：用户在场时静默、离开时弹窗、通知内可回复 / 批准

### 物联网 / 智能硬件

- [ESPHome Guition 语音助手旋钮屏](concepts/tool-esphome-guition-va.md)
- [Seahi-Serial](concepts/tool-seahi-serial.md) — 多串口调试工具
- [CasaOS](concepts/tool-casaos.md) — 个人云 OS，10 万+ Docker 镜像一键装

### 评测基准 / 论文索引

- [eot-bench（LiveKit 话轮检测基准）](concepts/tool-eot-bench.md)
- [Awesome World Action Models](concepts/tool-awesome-world-action-models.md)
- [awesome-evals（BenchFlow 带注释清单）](concepts/tool-awesome-evals.md)
- [EnterpriseClawBench](concepts/tool-enterpriseclaw-bench.md) — 真实企业工作会话的编码 Agent 基准

### 幻灯片 / 演示

- [MD→Slides](concepts/tool-markdown-slides.md)
- [Serenade（Nuxt 4 动静两栖博客）](concepts/tool-serenade-nuxt4.md) — Markdown 内容既可静态导出也能跑 Node SSR

## 自托管 / 邮件

- [Cloud Mail](concepts/tool-cloud-mail.md)

## 阅读 / 资源

- [10万本书 GitHub 仓库](concepts/tool-ebook-library-100k.md)
- [后端面试开放式问题清单](concepts/tool-backend-interview-questions.md) — 11 个方向的开源后端面试问题
- [ExamPrep-AI](concepts/tool-exam-prep-ai.md) — Streamlit 把 PDF 笔记转摘要/选择题/闪卡
- [codex-orange-book](concepts/tool-codex-orange-book.md) — 非官方 Codex 全链路指南
- [resume-jd-optimizer-cn](concepts/tool-resume-jd-optimizer-cn.md) — 基于 JD 解析差距 + 追问遗漏素材的中文定制简历
- [CS-Fundamentals](concepts/tool-cs-fundamentals.md) — 校招 CS 基础仓库，七大科目笔记 + 面试题 + HR 面经 + LeetCode 题集 + 公司列表
- [《线性代数不难》开源书](concepts/note-linear-algebra-made-easy.md) — GitHub 开源线代教材，几何图 + 可视化 + 动画 + 可运行 Jupyter Notebook
- [Top 10 系统设计资源清单](concepts/note-system-design-resources.md) — DDIA / SRE / Alex Xu / Jepsen 等十本经典与十种资源

## 金融 / 数据

- [a-stock-data](concepts/tool-a-stock-data.md)
- [global-stock-data](concepts/tool-global-stock-data.md) — 美港股全栈数据 Skill（期权链 / 财报三表 / 503 GAAP 指标）
- [ngrok / webernetes](concepts/tool-ngrok-webernetes.md)
- [Finnhub 美股 API](concepts/tool-finnhub-api.md) — 免费层 60 req/min 的美股行情/财报/新闻 REST API
- [chinese-buy-us-stock-guide](concepts/tool-chinese-buy-us-stock-guide.md) — 大陆投资者美股实操指南，开户 / 税务 / 合规 / 入金 / 出金
- [AI 托管个人资产的方向](concepts/tool-personal-asset-via-claude.md) — AI 全面接管个人财务的机会与风险
- [liangmai-sdk](concepts/tool-liangmai-sdk.md) — 良买金融数据 Python SDK，105 个 API 覆盖 A 股 / 港股 / 基金 / 龙虎榜
- [Cliare](concepts/tool-cliare.md) — Rust 写的 CLI 黑盒审计工具，给命令行界面打 Agent 就绪评分
- [pi-env](concepts/tool-pi-env.md) — Pi Coding Agent 的沙箱运行环境，隔离宿主 + 可复现环境 + 可选协作管理
- [pi-hive](concepts/tool-pi-hive.md) — Pi 的层次化多智能体团队协作工具，YAML 配置定义团队拓扑，规划/执行分离
- [Comando](concepts/tool-comando.md) — 本地优先多智能体协作代码编辑器（Electron + Rust），五种 ACP 运行时 + 逐块审查
- [VAF（Veyllo Agent Framework）](concepts/tool-vaf.md) — Python 自主智能体框架，桌面/服务端/终端三模式，本地 GGUF + OpenAI/Anthropic，pgvector + Redis 持久化
- [Codex-X](concepts/tool-codex-x.md) — Tauri 2 跨平台 Codex 桌面端管理器，提示词注入 + Provider 切换 + 配置可视化
- [token-diet](concepts/tool-token-diet.md) — Shell 编码代理令牌减肥技能，Claude Code/Codex/Cursor/Windsurf/Cline 通吃，平均省 ~31%
- [magic-compact](concepts/tool-magic-compact.md) — OpenCode 无损上下文压缩插件，助手轮次单独摘要 + 工具 I/O 缓存，read_omitted_content 回头查
- [Vibe-Trading](concepts/tool-vibe-trading.md) — 港大 HKUDS AI 交易研究平台，29 个 AI Agent 一句话跑量化研究流水线
- [stock-sdk](concepts/tool-stock-sdk.md) — 浏览器端股票数据库（零依赖），A 股 / 港股 / 美股 / 公募基金实时行情 + K 线，自带 CLI 和 MCP server
- [investing-for-beginners](concepts/tool-investing-for-beginners.md) — 中文投资入门公开指南，美股/期权/加密三大领域 100+ 文章 + 术语表

## 网络 / 代理

- [ClashOmega](concepts/tool-clash-omega.md) — Clash 代理规则管理 Chrome 扩展
- [HypoMux](concepts/tool-hypomux.md) — Windows 多网卡带宽聚合下载加速
- [shadowrocket-config](concepts/tool-shadowrocket-config.md) — 防 DNS 泄露配置（ACL4SSR）
- [sub-store-cloudflare](concepts/tool-sub-store-cloudflare.md) — Cloudflare Workers 部署的订阅聚合与规则配置工具，订阅源管理 / 节点处理 / 分流模板全云端

## AI 编码 IDE

- [Aura-IDE](concepts/tool-aura-ide.md) — Planner/Worker 双智能体本地编码工作台，diff 审批 + 自动验证

## 自托管 / 工具

- [3D 打印文件自托管资产管理](concepts/tool-3dprint-asset-manager.md) — STL/3MF/OBJ/STEP/G-code 多格式 + Moonraker/Klipper 工作流
- [Seeder（小团队自托管项目管理 + MCP）](concepts/tool-seeder.md) — 看板任务 + 客户请求队列 + 内置 MCP 服务器，Cloudflare Workers / Node VM 一键部署
- [SafeBucket（预签名 URL 直传直下）](concepts/tool-safebucket.md) — Go + React，文件不经服务器中转，组件可插拔
- [SimpleRelay（自托管 SMTP 中继）](concepts/tool-simplerelay.md) — FastAPI + Postfix + PostgreSQL，多租户 + IP 白名单 + SPF/DKIM/DMARC
- [EasySNI（SNI / XRay / 域名前置单文件面板）](concepts/tool-easysni.md) — Go 单二进制集成 SNI 隧道 + XRay/sing-box + 域名前置 + 扫描器
- [Incudal（Incus NAT VPS 销售面板）](concepts/tool-incudal.md) — Vue 3 + Fastify + Go Agent，LXC/KVM NAT VPS 自动交付 + 套餐余额 + 工单
- [MADO-queue](concepts/tool-mado-queue.md) — 北海道芽室町自研的行政窗口叫号系统
- [无状态自托管 TOTP 工具](concepts/tool-totp-stateless.md) — 无服务器无数据库的 2FA 生成器，密钥通过 URL 片段在浏览器本地计算
- [LawLink](concepts/tool-lawlink.md) — 中小律所开源自部署案件管理系统
- [Koryomi](concepts/tool-koryomi.md) — 单镜像自托管漫画/条漫阅读 PWA
- [GanCook / 干饭厨子](concepts/tool-gancook.md) — 家庭 NAS 点菜系统，Docker 一键部署
- [SimpleX Chat](concepts/tool-simplex-chat.md) — 首个无用户标识符的消息平台，双层加密 + 中继服务器架构
- [Fallegji](concepts/tool-fallegji.md) — Rust 终端 P2P 群聊应用，完全去中心化 + E2EE（X25519 + ChaCha20-Poly1305），无服务器无账号
- [Yamtrack](concepts/tool-yamtrack.md) — 给前 Trakt 用户准备的自托管媒体追踪平台，追影视 + 音乐 + 播客 + 收藏副本级详情
- [LinkBreeze](concepts/tool-linkbreeze.md) — 自托管 link-in-bio 平台，Next.js 16 + SQLite 一条 Docker 命令部署
- [shortlink](concepts/tool-flyfish-shortlink.md) — 自托管短链接 + 活码平台，发布前审核 + 品牌二维码 + 访问统计
- [HermitUI](concepts/tool-hermitui.md) — 单 HTML 文件的本地 AI 聊天界面，OpenAI 兼容 + 默认不存聊天记录
- [本地 LLM 硬件搭建实操指南](concepts/note-local-llm-hardware-guide.md) — jamesob/local-llm 两档预算配置 + PCIe 交换芯片多卡直连 + Docker 化 + 沙盒 VM

## 操作手册

- [在 Obsidian 里开始用 OKF（Playbook）](concepts/playbook-okf-obsidian-start.md)
- [VLESS + WebSocket + TLS 绕过电信 QoS](concepts/playbook-vless-bypass-telecom-qos.md)
- [SPA 内嵌 PDF 查看器（react-pdf + Hono 代理）](concepts/playbook-spa-pdf-viewer.md) — 跨前后端的 PDF 渲染 + 鉴权代理 + byte-range 透传 + 东财失效链兜底
- [应用外壳侧边栏（base-ui + motion 多层装配）](concepts/playbook-app-shell-sidebar.md) — shadcn primitive → AppShellSidebar 中间层 → 应用层数据的三层架构
- [双轴主题系统（next-themes + shadcn data-theme）](concepts/playbook-dual-axis-theming.md) — Mode × Preset 双维度自由组合 + 防 FOUC + 跨设备同步

## 本批新增（2026-07-08）

### 金融 / 数据
- [tickflow-stock-panel](concepts/tool-tickflow-stock-panel.md) — 自托管 A 股量化工作台：选股 / 回测 / 监控 / 复盘 / 18 内置策略 / AI 生成策略 / 连板梯队
- [farm-mall](concepts/tool-farm-mall.md) — Flask + MySQL 助农电商平台，本科毕业设计开源版

### 桌面 / 系统工具
- [Picot](concepts/tool-picot.md) — Pi 编码 agent 的本地桌面 GUI（Tauri 框架）
- [Nebula](concepts/tool-nebula-terminal.md) — Windows GPU 加速 / 会话持久的终端
- [tudo](concepts/tool-tudo.md) — 终端下的待办 + Markdown 笔记本二合一 TUI
- [Cyrene-Agent](concepts/tool-cyrene-agent.md) — Live2D AI 伴侣桌面应用，星穹铁道昔涟人设

### AI / Agent 生态
- [docker_images_sync](concepts/tool-docker-images-sync.md) — 借 GitHub Actions 免费算力同步海外 Docker 镜像到国内
- [trueline-mcp](concepts/tool-trueline-mcp.md) — 带哈希校验的 AI 编码精准改文件 MCP 插件
- [quickai](concepts/tool-quickai-claude-cost.md) — 本地 Claude Code transcript 剖析工具（token / 成本 / 时长）
- [Foundry](concepts/tool-foundry.md) — 开源 AI 数字公司平台，自动生成董事会→员工层级 agent 组织
- [fable-harness](concepts/tool-fable-harness.md) — Claude Code 纪律化流程行为协议（hooks / skill / 子代理）
- [LocalEyes](concepts/tool-localeyes.md) — 给本地纯文本 LLM 加 Ollama 视觉能力的工具
- [cpa-plugin-codexcomp](concepts/tool-cpa-plugin-codexcomp.md) — CLIProxyAPI 插件，自动修复 gpt-5.5 reasoning 截断
- [vibe-coding-rules](concepts/tool-vibe-coding-rules.md) — AI 编码 6-Skill 编程纪律流水线
- [pool](concepts/tool-pool-poolside.md) — Poolside 编码智能体，终端 / ACP 服务端 / ACP 客户端 / `pool exec` 四种运行方式

### 电商 / 自动化
- [Knockoff](concepts/tool-knockoff.md) — Chrome 扩展，自动过滤 Amazon 山寨品牌
- [creatorhub](concepts/tool-creatorhub.md) — Python 多平台（抖音/小红书/快手）内容监控采集搬运工具

### 后端 / 部署 / 自托管
- [gzh-design-skill](concepts/tool-gzh-design-skill.md) — Markdown → 微信公众号内联样式 HTML 转换器
- [BiliRoaming](concepts/tool-biliroaming.md) — 解除 B 站番剧区域限制的 Xposed 模块
- [Openprinter](concepts/tool-openprinter.md) — opentools.studio 开源打印机，结构极简 / 通用零件 / 可复制改造

### 阅读 / 资源
- [awesome-education](concepts/tool-awesome-education.md) — 教育优惠 / 学生权益 / 学术会员清单仓库

### 更新（Updated）
- [Free-TV/IPTV](concepts/tool-free-tv-iptv.md) — 补充媒体预览图与新一批推文剪藏链接
- [ShipSwift](concepts/tool-shipswift.md) — 补充 App Store 链接与新一批推文剪藏链接

## 本批新增（2026-07-09）

### AI / Agent 生态
- [TencentDB-Agent-Memory](concepts/tool-tencentdb-agent-memory.md) — 腾讯云开源的四层渐进式 Agent 记忆方案（短 / 中 / 长 / 永久）
- [Hermes Browser Extension](concepts/tool-hermes-browser-extension.md) — 给 Hermes Agent 做的浏览器侧边栏，自动抓网页上下文喂本地 / 远端运行时
- [retok](concepts/tool-retok.md) — 分析 Claude Code / Codex CLI 使用日志估算 token 成本并给出省 token 建议
- [claude-code-merge-queue](concepts/tool-claude-code-merge-queue.md) — 本地零成本合并队列，并行 worktree 按 FIFO 顺序串行落地 + 构建 + 测试
- [Mobius](concepts/tool-mobius-agent-os.md) — 自称首个自进化开源 Agent OS，项目 / 团队 / agent / 设备 / 算力同台且能自我改写
- [Open Connector](concepts/tool-open-connector.md) — 开源 Composio 替代品，1000+ SaaS / 9400+ Action，SDK / CLI / MCP / HTTP / OpenAPI 多协议
- [mattpocock wayfinder](concepts/tool-mattpocock-wayfinder.md) — DAG + 战争迷雾的大型项目规划 Skill，4 类节点票务
- [Hallmark](concepts/tool-hallmark-skill.md) — 开源 AI 编码设计 Skill，给 Claude Code / Cursor / Codex 一键加载「设计感」
- [J-lens for Qwen3.6](concepts/tool-jlens-qwen36.md) — Apple Silicon 本地跑 Qwen3.6-27B 4-bit（MLX），把层 × 位置 token 读可视化诊断
- [DataFoundry](concepts/tool-datafoundry-data-agent.md) — 企业级私有部署的数据 Agent 工作台，统一业务语义 + 只读边界 + 全程审计
- [Fable 5 案例：1 周把 email canvas 从 ReactFlow 迁到 WASM + Rust](concepts/note-fable5-email-canvas-case.md) — 笔记：性能从 100+ / 30fps 跳到 1000+ / 60fps

### 前端 / 设计资源
- [uikit-expt](concepts/tool-uikit-expt.md) — 基于 pmndrs/uikit 的 3D UI 实现实验
- [next-shadcn-admin-dashboard](concepts/tool-next-shadcn-admin-dashboard.md) — Next.js 16 + shadcn UI 的开源 admin dashboard 起点模板
- [pixel2motion](concepts/tool-pixel2motion.md) — 开源免费 Logo 动效生成工具
- [ai-website-cloner](concepts/tool-ai-website-cloner.md) — 给 AI 编码 Agent 用的网站复刻模板

### 基础与格式
- [auth.md](concepts/tool-auth-md.md) — 面向 LLM / agent 的服务鉴权说明书约定，与 x402 协同形成「鉴权 + 付费」闭环

### 后端 / 部署 / 自托管
- [Boring Computers](concepts/tool-boring-computers.md) — Firecracker microVM 给 AI agent 提供「一整台 Linux 电脑」
- [kodbox](concepts/tool-kodbox.md) — 浏览器即云端 OS 的开源 Web 文件管理器
- [ComPDFKit Self-Hosted](concepts/tool-compdf-self-hosted.md) — 企业可私有化部署的开源 PDF 编辑与格式转换平台

### 桌面 / 系统工具
- [cmdOS](concepts/tool-cmdos.md) — 键盘优先的浏览器 Chrome 命令终端扩展（Alt+S 唤出），本地存储
- [Live Photo Box](concepts/tool-live-photo-box.md) — Windows 桌面工具，查看 / 管理 / 修复 iPhone 实况照片跨设备配对问题

### 听写 / 语音输入
- [OmniVoice-Studio](concepts/tool-omnivoice-studio.md) — 3 秒样本开源语音克隆工具，本地运行 + 646 语言 + Claude/Cursor 直调

### 物联网 / 智能硬件
- [Pocket Lab Power Supply](concepts/tool-pocket-lab-power-supply.md) — 4S 锂电 + USB-C/PD 充电的口袋实验室电源
- [marine-acoustic-monitor](concepts/tool-marine-acoustic-monitor.md) — 低成本边缘计算海洋生态声学监测

### 编程语言 / 工具链
- [quic-go-ton](concepts/tool-quic-go-ton.md) — quic-go 的 TON 网络分支，纯 Go + RFC 7250 原始公钥 + Ed25519 ADNL 身份

### 金融 / 数据
- [iptv-org/iptv](concepts/tool-iptv-org.md) — 全球免费 IPTV 直播源大宝库，12 000+ 频道多维筛选 + EPG + API

### 更新（Updated）
- [wenyi（Claude 多语种长篇翻译 CLI）](concepts/tool-wenyi-translator.md) — 补充 EPUB / FB2 / TXT 多格式输入、断点续跑、术语库一致性

## 本批新增（2026-07-10）

### 桌面 / 系统工具
- [OpenDisplay](concepts/tool-opendisplay.md) — 把闲置 iPhone/iPad 变 Mac 副屏的自托管免费替代
- [Expenso](concepts/tool-expenso.md) — 离线优先 Android 记账 + Jetpack Compose + Material 3
- [davit](concepts/tool-davit.md) — SwiftUI 写的 macOS 原生 Apple container 管理界面
- [Smart Remarkable](concepts/tool-smart-remarkable.md) — reMarkable 电子墨水平板视觉-语言 agent，Rust 实现

### 终端 / 网络 / 系统管理
- [tork](concepts/tool-tork.md) — 终端 BT 客户端 + 一键拉取 Linux 发行版 ISO
- [nls](concepts/tool-nls.md) — Go 写的现代化 ls，Nushell 风格表格 + 管道兼容

### AI / Agent 生态
- [next-ai-draw-io](concepts/tool-next-ai-draw-io.md) — 自然语言 / 手绘草图 → draw.io 风格图表
- [Freely](concepts/tool-freely.md) — 本地运行实时会议提示助手，主打替代 150 美元/月 的 Cluely
- [PocketJS](concepts/tool-pocketjs.md) — 浏览器外跑 JSX UI 的运行时，Solid / Vue Vapor 经 QuickJS
- [NoteBrain CLI](concepts/tool-notebrain-cli.md) — Obsidian vault 离线索引到本地 ChromaDB，给 AI agent 提供语义搜索
- [语析 Yuxi](concepts/tool-yuxi.md) — RAG + Milvus 知识图谱 + LangGraph 多智能体编排的多租户平台
- [blockout](concepts/tool-blockout-previs.md) — 用灰盒场景 + 真实镜头参数做 AI 视频生成的 previs
- [openclaw-marketing-skills](concepts/tool-openclaw-marketing-skills.md) — 给 OpenClaw 智能体的 37 个营销技能集合 + 多广告平台实时数据
- [friskeval](concepts/tool-friskeval.md) — 发布前对 agent 技能目录做路由检查
- [AI Job Hunter](concepts/tool-ai-job-hunter.md) — 面向 AI 行业求职的 Claude Code 技能，30/60/90 天学习计划
- [Synapse CE](concepts/tool-synapse-ce.md) — SCA + 侦察 + 证据 + 报告收拢到一个治理控制平面

### 阅读 / 资源
- [AI User Roadmap](concepts/tool-ai-user-roadmap.md) — 面向普通 AI 使用者的入门到完成真实任务学习路线图

### 自托管 / 工具
- [Google《Agent Engineering》1 小时课程](concepts/note-google-agent-engineering-course.md) — Google 官方 1 小时 Agent Engineering 视频课速记

### 基础与格式 / 电商 / 自动化
- [Sleepwalker](concepts/tool-sleepwalker.md) — 扫描品牌在 AI 搜索中的可见度与被引用情况

## 本批新增（2026-07-11）

### 前端 / 设计资源
- [NumberFlow](concepts/tool-number-flow.md) — barvian/number-flow，丝滑数字滚动 React 组件
- [Liveline](concepts/tool-liveline.md) — benji/liveline，实时折线图 React 组件
- [Sonner（toast 组件）](concepts/tool-sonner-toast.md) — emilkowalski/sonner，API 极简 React toast，已被 shadcn 等绝大多数现代组件库采纳为默认 toast
- [Apple Design Skill](concepts/tool-apple-design-skill.md) — emilkowalski/skills 中的 /apple-design Skill，WWDC 提炼 17 条设计 + 动效原则

### AI / Agent 生态
- [Smart Task Assistant](concepts/tool-smart-task-assistant.md) — LangGraph + FastAPI 工作流，分类 → 计划 → 评审 → REST 输出
- [Flood Guard Agent](concepts/tool-flood-guard-agent.md) — 北京市山洪防御辅助决策智能体，Spring AI + ReAct + SSE 流式

### 桌面 / 系统工具
- [Garmin Tracker RS](concepts/tool-garmin-tracker-rs.md) — Tauri 2 + Rust + React 19，USB（MTP）直连 Garmin 手表取 .FIT 文件，全程无需云端
- [Orca Music Player](concepts/tool-orca-music-player.md) — Svelte 5 + Tauri 2 + Rust 本地音乐播放器，MP3/FLAC/M4A/WAV/OGG/OPUS/AIFF，rodio 引擎支持交叉淡入（与 stablyai/orca Coding IDE 同名不同项目）
- [Uninstally](concepts/tool-uninstally.md) — SwiftUI 写的 macOS 卸载工具，清残留 + Finder 右键卸载 + Homebrew 包管理

### 终端 / 网络 / 系统管理
- [Artix TUI Installer](concepts/tool-artix-tui-installer.md) — Rust + ratatui 终端安装器，乌克兰语 / 英语双语，专门给用 dinit 的 Artix Linux 用
- [Grom](concepts/tool-grom-prometheus.md) — Go 写的 Prometheus btop 风格终端仪表盘，支持读 Grafana 面板 JSON 在终端复现布局

### 后端 / 部署 / 自托管
- [Frp Manager](concepts/tool-frp-manager.md) — 本地桌面内网穿透管理系统（服务端控制面 + Wails/Vue 客户端）
- [Open WebUI Generate Documents](concepts/tool-openwebui-generate-documents.md) — Open WebUI 工具，用 python-docx 把模型输出的 Markdown / JSON 生成原生可编辑 .docx

### 电商 / 自动化
- [Article Format](concepts/tool-article-format.md) — 一句话指令把自媒体文案转微信公众号（内联 CSS）+ 今日头条（语义 HTML）排版

### 阅读 / 资源
- [Space Multi-Design PPT](concepts/tool-multi-design-ppt.md) — Agent Skills 协议幻灯片生成 Skill，按 62 种品牌设计语言出 HTML/PPTX/PDF

### 物联网 / 智能硬件
- [GitGrimoire](concepts/tool-gitgrimoire.md) — 输入 GitHub 用户名生成《黑色五叶草》风格 3D 魔法书档案 / 对决 / 排行榜

### 听写 / 语音输入
- [Claude-ZH-EN-Relay](concepts/tool-claude-zh-en-relay.md) — Chrome 扩展让用户用中文与 Claude 聊天（输入译英 / 回复译中），可省 token

### 金融 / 数据
- [Fintech Advisor](concepts/tool-fintech-advisor.md) — 开源净值与投资组合追踪（不是记账），多币种 + 自动汇率 + Yahoo Finance + AI 一键导入持仓 + AI 投顾对话

## 本批新增（2026-07-12）

### AI / Agent 生态
- [Orca 工单编排流程](concepts/playbook-orca-ticket-orchestration.md) — `/grill → /spec → /tickets → /orchestration` 一条 AI 编码会话流水线
- [fable-method](concepts/tool-fable-method.md) — Fable 5 解题方式（think/act/prove）提炼的通用 Skill + 对抗式 eval
- [jzsub](concepts/tool-jzsub-skill.md) — Codex Skill，自动下载视频 + 双语字幕 + 烧录 MP4
- [Lemma](concepts/tool-lemma-platform.md) — 人 + AI agent 共享工作空间平台
- [SpringNote](concepts/tool-springnote.md) — Flutter + Rust 桌面「懒人知识库」，AI 自动整理 + 回忆书
- [kunkun SkillHub](concepts/tool-kunkun-skillhub.md) — 本地盘点和搜索 Claude Code / Codex 技能
- [nsfc-benzi-audit](concepts/tool-nsfc-benzi-audit.md) — 国自然基金申请书结构化诊断 Agent Skill
- [PunamIDE](concepts/tool-punamide.md) — Tauri 2 + React 19 + Monaco 的原生 AI 桌面 IDE
- [annotai](concepts/tool-annotai.md) — Phoenix / LiveView 元素级 AI 编码注释工具

### 桌面 / 系统工具
- [TokenUsageInsights](concepts/tool-token-usage-insights.md) — AI CLI Token 戰情室 + Session 还原看板
- [Vortex](concepts/tool-vortex-vps.md) — 终端里的 VPS 管理工具，自动传监控程序
- [MarkdownReader](concepts/tool-markdown-reader-windows.md) — Windows 上的轻量 Markdown 编辑器 + PDF 导出
- [Vela](concepts/tool-vela-maps.md) — 去 Google 化的安卓地图 / 导航客户端

### 终端 / 网络 / 系统管理
- [Vortex](concepts/tool-vortex-vps.md) — 终端里的 VPS 管理工具，自动传监控程序
- [xan](concepts/tool-xan-csv.md) — Rust 写的「CSV 魔术师」命令行工具，GB 级 CSV + 社科向扩展
- [NaviTui](concepts/tool-navitui.md) — 终端里的 Subsonic / Navidrome 音乐播放器，TUI + mpv + MCP

### 阅读 / 资源
- [storage-book + KnotFS](concepts/tool-storage-book.md) — 从结绳记事到 LittleFS 源码剖析的存储技术书 + 教学级 LFS

### 编程语言 / 工具链 / 基础设施
- [Colibri](concepts/tool-colibri-inference.md) — 纯 C 零依赖 MoE 流式推理引擎，25GB 内存跑 744B
- [jspace-viz](concepts/tool-jspace-viz.md) — 开源 LLM 实时 Jacobian-lens「层 × 位置」热力图

## 本批新增（2026-07-13）

### 流程手册（Playbook）
- [多模态大模型驱动的 UI 自动化测试](concepts/playbook-multimodal-ui-test-automation.md) — 文本属性 → 控件 ID → 多模态融合 → 自主推理 四阶段演进，"描述即生成"端到端方法论

### AI / Agent 生态
- [exxperts](concepts/tool-exxperts.md) — 本地 AI 智能体运行时，"记忆房间" 跨会话记忆 + 写盘前必须用户批准
- [OpenAI4S](concepts/tool-openai4s.md) — 开源科研智能体，持久化内核跑真 Python/R，便宜模型复现 Claude Science 级自动化
- [readme-roast](concepts/tool-readme-roast.md) — Claude Code 技能，8 种人设毒舌吐槽 README + 诚实度评分 + 备选版本
- [ax](concepts/tool-ax-cli-scraper.md) — 给 AI 用的命令行抓取工具，本地 / 确定性 / 省 token
- [pi-computer-use](concepts/tool-pi-computer-use.md) — 给 pi harness 加 computer-use 能力，逆向自 codex，可挂到任意 harness

### 前端 / 设计资源
- [shadcn-fintech-template](concepts/tool-shadcn-fintech-template.md) — Next.js + shadcn/ui + Tailwind 金融仪表盘模板，11 个页面 + 实时行情 + 消费热力图

### 桌面 / 系统工具
- [CTRoadmap](concepts/tool-ctroadmap.md) — 本地优先基础设施图谱工具，磁贴 + 连线，数据存 atlas.json
- [mithka](concepts/tool-mithka.md) — Telegram 客户端，UI 致敬 macOS / iOS 风格
- [nvim-camel](concepts/tool-nvim-camel.md) — Neovim 插件，会走路的 ASCII 骆驼，纯装饰

### 物联网 / 智能硬件
- [mqttprobe](concepts/tool-mqttprobe.md) — 工业物联网 MQTT 诊断工具，原生解码 Sparkplug B + 模拟 EoN 节点

## 本批新增（2026-07-13，第二批：QingQ77 余量）

### AI / Agent 生态
- [marketing-studio](concepts/tool-marketing-studio.md) — Claude Code 营销工作室，`/marketing` 一条指令渲染品牌全套素材
- [agentic-mercy-10x](concepts/tool-agentic-mercy-10x.md) — Claude Code 发行版：单一路由器派单 + 写入钩子强制规范 / 测试 / 安全门禁
- [unsnooze](concepts/tool-unsnooze.md) — Claude Code / Codex / Grok / Qwen / Kimi / OpenCode / Antigravity 用量墙恢复工具
- [loop.js](concepts/tool-loop-js.md) — 目标 + 执行 + 验证三件事同一种 prompt，独立只读 Verify agent 判定达标

### 编程语言 / 工具链
- [pon](concepts/tool-pon-python.md) — Rust 写的 Python 3.14 原生编译器（JIT + AOT），目标 Python 版的 bun / v8
- [QwenAI-Webapp](concepts/tool-qwenai-webapp.md) — FastAPI + Vue 3 + DashScope 接入通义千问，流式 + 多模态

### 自托管 / 工具
- [shortlink](concepts/tool-flyfish-shortlink.md) — 自托管短链接 + 活码平台，发布前审核 + 品牌二维码 + 访问统计
- [HermitUI](concepts/tool-hermitui.md) — 单 HTML 文件的本地 AI 聊天界面，OpenAI 兼容 + 默认不存聊天记录
- [Magma](concepts/tool-magma-sveltekit.md) — SvelteKit 个人主页式看板，可拖可缩 + 多语言 + Docker 一键部署

## 本批新增（2026-07-14）

### 自托管 / 工具（本批新增）
- [Magma](concepts/tool-magma-sveltekit.md) — SvelteKit 个人主页式看板，可拖可缩 + 多语言 + Docker 一键部署

### 物联网 / 智能硬件（本批新增）
- [tapo-voltage-monitor](concepts/tool-tapo-voltage-monitor.md) — 给 Tapo P110 / P115 智能插座用的电压监测工具，本地网页仪表盘 + CSV 日志 + 越界告警

### 桌面 / 系统工具（本批新增）
- [auto-reply](concepts/tool-auto-reply-vlm.md) — 基于 SightFlow 的桌面端 VLM 自动回复，读聊天窗口截图 + 判情绪 + 攒本地经验
- [dj-usb-tkit](concepts/tool-dj-usb-tkit.md) — 本地 DJ 曲库管家，整理好直接写入 Pioneer DJ USB 盘
- [MacRazer](concepts/tool-macrazer.md) — macOS 菜单栏小程序，走 USB HID 控制 Razer 鼠标电量 / DPI / 灯效 / 回报率

### 终端 / 网络 / 系统管理（本批新增）
- [telegram-search](concepts/tool-telegram-search.md) — 终端里搜自己 Telegram 聊天记录 / 频道 / 文件的 CLI

### AI 编码 IDE（本批新增）
- [herdr-reviewr](concepts/tool-herdr-reviewr.md) — 给终端 AI agent herdr 配的代码审查侧栏，diff + 逐行批注 + 一键回灌

### 后端 / 部署 / 自托管（本批新增）
- [reame](concepts/tool-reame.md) — 廉价 CPU 上跑的 LLM 推理服务，用磁盘缓存让重复请求越用越便宜

### 金融 / 数据（本批新增）
- [agent-quantspace](concepts/tool-quantspace.md) — 把数据 / 因子 / 回测 / 报告收在固定 skill 边界内的量化投研框架
- [AutoPrism](concepts/tool-autoprism.md) — 汽车 / 投研全球事件可视化，AI 降噪 + 3D 地球 + 2D 战术地图

### 电商 / 自动化（本批新增）
- [xiaohongshu-assistant（薄荷工坊）](concepts/tool-xiaohongshu-assistant.md) — React + Vite 三列工作台，把小红书创作收纳成人设 + 热门 + 模型配置

### AI / Agent 生态（本批新增）
- [light-ocr](concepts/tool-light-ocr.md) — 离线 OCR 原生 / Node.js，单图 ≤ 100ms，约 30MB
- [logo-generator-skill](concepts/tool-logo-generator-skill.md) — 一次 6 种风格的 SVG logo 生成 Skill
- [agent-device](concepts/tool-agent-device-callstack.md) — 给 coding agent 操作 iOS / Android 真实 App 的 CLI（无障碍快照 + 语义 ref + .ad 复放）
- [brain0](concepts/tool-brain0.md) — 被动观测 git 与 agent 会话，把每次提交归因到 prompt 意图与读过的文件
- [fable-commander](concepts/tool-fable-commander.md) — Claude Code 三角色编排 Skill（强模型规划 + 弱模型执行 + 独立 agent 验收）
- [TIMA](concepts/tool-tiny-interjection-model-alpha.md) — 聊天回合决策小模型（等待 / 回复 / 插话 / 继续）
- [frugon](concepts/tool-frugon.md) — 本地 OpenAI 格式 JSONL 调用日志费用分析 + 换模型 / 路由建议

### 前端 / 设计资源（本批新增）
- [OriginKit](concepts/tool-originkit.md) — iOS App / SaaS 上线页模板段组件库
- [namethatui](concepts/tool-namethatui.md) — 「看得见但叫不出名字」的 UI 词典，众包学习 + 视觉反查

### 笔记（本批新增）
- [GitHub README 装修：SVG 组件 + Markdown 内容双层](concepts/note-github-readme-svg-slides.md) — oil-oil/oil-ppt 衍生的可复用 SVG 设计 README 套路

### 阅读 / 资源（本批新增）
- [ai-agent-guide](concepts/tool-ai-agent-guide.md) — 21 章中文 AI Agent 教程（6 大篇章 + 文章/八股/考试 + AI 助教）
- [4000-Essential-English-Words](concepts/tool-4000-essential-english-words.md) — 把经典词表抓取并打包成 Anki 牌组的 Python 脚本

## 本批新增（2026-07-15）

### Agent Skills 生态（本批新增）
- [WorkBuddyGuide](concepts/tool-workbuddy-guide.md) — AlephAITech 出的 WorkBuddy 开源蓝皮书教程，真实任务为线索串讲安装 / Skill / MCP / 多 agent
- [liurun-bookwriter-skills](concepts/tool-liurun-bookwriter-skills.md) — 学刘润 / 罗振宇中文商业写作风格的 Agent Skill 双件套
- [FTShare-skills](concepts/tool-ftshare-skills.md) — 把 FTShare 金融数据 / 投研流程包成 Claude Code / Codex 调用的 Skill

### AI / Agent 生态（本批新增）
- [FableCut](concepts/tool-fablecut.md) — 浏览器内视频编辑器，时间线为 JSON，Claude 等 Agent 经 MCP/REST 直接剪
- [Bonsai 27B](concepts/tool-bonsai-27b.md) — PrismML 27B 三值化模型，可在 iPhone 本地运行

### AI 编码 IDE（本批新增）
- [Clodex IDE](concepts/tool-clodex-ide.md) — 本地优先 / 零信任的 agentic IDE（Electron + TypeScript）

### 编程语言 / 工具链（本批新增）
- [retui](concepts/tool-retui.md) — Go 写的终端 UI 框架，React 风格（函数式组件 + hooks + flexbox 布局）
- [QuantoScript](concepts/tool-quantoscript.md) — C 写的小脚本语言，解释器 / 字节码 VM / 自动转 C 三档执行模型
- [arlan.me/vault](concepts/tool-arlan-vault.md) — 炫酷前端 / AI 效果合集，每个效果附 Markdown 提示词让 Agent 直拷还原

### 工具（Tools）（本批新增）
- [codemark](concepts/tool-codemark.md) — Rust 写的代码书签工具，基于 tree-sitter 抓代码语义结构定位书签
- [github-chinese](concepts/tool-github-chinese.md) — GitHub 界面中文化浏览器用户脚本，Tampermonkey / Violentmonkey 即装即用
- [journalit](concepts/tool-journalit.md) — IBKR / Tradovate / Bybit 等多平台成交记录汇总到 Obsidian 做本地复盘
- [mimic](concepts/tool-mimic.md) — 拦截任意应用进程，像调用 Python 库那样调用 CLI / GUI 程序

### 幻灯片 / 演示（本批新增）
- [presenter-mode](concepts/tool-presenter-mode.md) — 单 HTML 文件给任意幻灯片加演示者视图（备注 / 计时 / 黑屏），离线可用

### 终端 / 网络 / 系统管理（本批新增）
- [lazyrsync](concepts/tool-lazyrsync.md) — rsync 的 TUI 前端（ratatui + Rust），配置持久化 + dry-run + 危险开关二次确认

### 桌面 / 系统工具（本批新增）
- [navifsp](concepts/tool-navifsp.md) — Windows 小工具，借 WinFSP 把 Navidrome 音乐服务挂成磁盘
- [WinTrash](concepts/tool-wintrash.md) — 单 .ps1 扫 Windows 18 类残留（死 PATH / 幽灵服务 / 注册表 / 代理自签根证书）

### 自托管 / 工具（本批新增）
- [scroggo](concepts/tool-scroggo.md) — 自托管的 ListenBrainz 兼容 scrobble 服务，单二进制 + SQLite

### 后端 / 部署 / 自托管（本批新增）
- [bot-signal](concepts/tool-bot-signal.md) — TypeScript 全套机器人检测（浏览器标记 + 服务端 IP/TLS/时区 + 长期行为轨迹）

### 金融 / 数据（本批新增）
- [AI-Portfolio-Compass](concepts/tool-ai-portfolio-compass.md) — 本地投资组合工作台，多市场 / 多币种合并 + AI 诊断，AI 只诊断不交易

### 阅读 / 资源（本批新增）
- [UI Skills Top 10](concepts/note-ui-skills-top10.md) — UI-Skills 社区精选的 10 个 UI / 前端 Skill 清单

## 本批新增（2026-07-16）

### Agent Skills 生态（本批新增）
- [intercom-2x-skills](concepts/tool-intercom-2x-skills.md) — Intercom Fin 2x 团队开源的 Claude Code 技能合集(开发/安全/审查/测试)
- [codex-storyboard](concepts/tool-codex-storyboard.md) — 短视频/自媒体本地分镜台 Codex 插件,一句「打开分镜台」拉起 Web 工作台

### AI / Agent 生态（本批新增）
- [wigolo](concepts/tool-wigolo.md) — 免费 / 本地 / 私有 MCP 服务,让 AI Agent 搜索 / 抓取 / 研究网页
- [geoanalisis-mcp](concepts/tool-geoanalisis-mcp.md) — Claude Desktop 集成的空间数据 MCP 服务器,自然语言生成专业地图

### AI 编码 IDE（本批新增）
- [claude-code-recap](concepts/tool-claude-code-recap.md) — 一条命令跨目录聚合本机所有 Claude Code 会话,附续聊命令

### 桌面 / 系统工具（本批新增）
- [gemtype](concepts/tool-gemtype.md) — 免费开源 Grammarly 替代,浏览器扩展 + Word 插件,自配 Gemini API key
- [hermes-ui](concepts/tool-hermes-ui.md) — Hermes 桌面 UI 抽出来做成 Web 版,浏览器即开 + PWA 可装
- [wizarr](concepts/tool-wizarr.md) — Plex/Jellyfin/Emby 自托管邀请 + 引导系统,一条链接自动建账号

### 自托管 / 工具（本批新增）
- [joi-codex-pet](concepts/tool-joi-codex-pet.md) — ChatGPT Codex 像素桌宠资源包,基于 B 站 VTB 轴伊 Joi 形象
- [tonkatsu-box](concepts/tool-tonkatsu-box.md) — Flutter 跨端统一媒体收藏管理器,聚合十余数据源覆盖七类内容

### 金融 / 数据（本批新增）
- [repo-compete](concepts/tool-repo-compete.md) — 自动分析仓库定位,发现竞品,生成对比矩阵/雷达图/SWOT 等 HTML 报告
- [quantskills](concepts/tool-quantskills-nav.md) — QuantSkills 组织旗下量化 Skill/Agent 的导航仓库

### 物联网 / 智能硬件（本批新增）
- [gm-balancecar](concepts/tool-gm-balancecar.md) — 基于 STM32F4 的开源两轮平衡车,硬件 + 串级 PID 全套
- [noisy-speaker-anonymization](concepts/tool-noisy-speaker-anonymization.md) — 噪声环境下说话人匿名化的轻量 CASR 控制层,无需噪声标签自动调档位

### 写作 / 学术辅助（本批新增）
- [academic-humanizer](concepts/tool-academic-humanizer.md) — 修复 AI 辅助学术草稿的泛化、冗长与腔调,保留数据 / 引用 / 严谨性

### 阅读 / 资源（本批新增）
- [深入理解 AI Agent](concepts/note-ai-agent-book.md) — bojieli 把图灵《AI Agent 实战营》整理的开源电子书

## 本批新增（2026-07-17）

### AI / Agent 生态
- [domain-sdk（opencoredev）](concepts/tool-domain-sdk-opencore.md) — 域名「增、查、列、验、删」归一化为跨服务商 API,直接给出 DNS / 所有权 / 证书记录值
- [FreeBuddy](concepts/tool-freebuddy.md) — 桌面 GUI 并行承载多个本地编码 Agent,任务统一追踪
- [cynative](concepts/tool-cynative.md) — 跑在用户自己云、代码与运行时上的安全研究 Agent,跨 GitHub / AWS / K8s 只读沙箱化查询,给出可追源的结论
- [Microsoft Agent Framework (Go 版)](concepts/tool-agent-framework-go-microsoft.md) — 微软出的 Go 多智能体框架,多 Provider + 可插拔中间件 + DAG 图工作流
- [learn-agent (7-e1even)](concepts/note-learn-agent-zero-to-coding-agent.md) — 从零到完整 coding agent 的实战教程笔记,每机制附零依赖可运行的 Node.js 示例
- [brand-loom](concepts/tool-brand-loom.md) — 开放核心营销 Skill 库,钩子/文案/标签/SEO/FAQ/Schema/CTA 多 model 通用
- [ai-meter](concepts/tool-ai-meter.md) — macOS 菜单栏用量监控,接 ccusage 显示各编码 Agent 的剩余预算 / 周期 / 重置日

### AI 编码 IDE / 工作台
- [Codex Dream Skin](concepts/tool-codex-dream-skin.md) — 给 Codex 桌面端做外部换肤,通过本机 CDP 注入一张 16:9 壁纸
- [juggler](concepts/tool-juggler-ai.md) — 可视化工作台式 AI 编码 agent,工具调用全可见 + 分支线程回溯 + 上下文直接编辑
- [Pi Exa](concepts/tool-pi-exa.md) — Pi Agent 的 Exa 扩展包,基础搜索无 key 可用,深度搜索需 API key

### Skills / 内容 / 营销
- [SkillsPlusPlus](concepts/tool-skillsplusplus.md) — Tauri 2 桌面端 Skills 管理工具,聚合 skills.sh / LobeHub / SkillHub.cn 多源,一键安装到 10+ AI 工具
- [xiaohongshu-ai-workbench](concepts/tool-xiaohongshu-ai-workbench.md) — 配套《小红书运营手册》的开源 Codex Skills 集,把标题 / 主页 / 选题 / 评论 / 成交拆成可执行工作流

### 桌面 / 系统工具
- [inky-bird-frame](concepts/tool-inky-bird-frame.md) — 鸟类观测 → Codex 生成插画图版 → Pimoroni Inky 彩屏轮播
- [hashdraft](concepts/tool-hashdraft.md) — Windows 快速启动 / 纯本地的 Markdown 阅读编辑软件,分屏滚动同步
- [wlocks](concepts/tool-wlocks.md) — Go TUI 工具,轮询 /proc 展示进程 ↔ 文件描述符关系,模糊搜索 + 多维排序 + 主题切换

### 浏览器扩展 / 抓取
- [ditto.site](concepts/tool-ditto-site.md) — 把公开网址变可跑 TypeScript 应用,抓真实渲染后确定性地生成 Next.js / Vite 项目
- [doubao-international](concepts/tool-doubao-international.md) — Chrome/Edge 浏览器插件,劫持 JSON.parse + 网络请求取无水印原图 / 原视频,主攻豆包国际版

### 工具 / 资源
- [csakura](concepts/tool-csakura.md) — C99 + ncurses 终端樱花树动画,程序化生成会落樱的樱树

### App 生成 / 软件工程
- [QuantumByte](concepts/tool-quantumbyte.md) — 开源融合式 App 构建器,一句意图出应用,每回合后逐条核验业务需求驱动自动修复

## 配套文档

- [输出模板目录](./templates/_README.md)
- [变更记录](./log.md)

## 你（人类）的日常就是

1. 把资料丢进 [`inbox/`](./inbox/README.md)
2. 对 agent 说「**处理 inbox**」
3. agent 按 PRODUCER.md 产出到 `concepts/`、更新索引与 log、归档资料
4. 去 [`overview.md`](./overview.md) 看结果

## 本批新增（2026-07-20）

### AI / Agent 生态（本批新增）
- [Grok Build Plugin for Claude Code](concepts/tool-grok-build-plugin-cc.md) — xAI 官方 Claude Code 插件,斜杠命令直接调本机 grok CLI 干活,靠 PID + 日志跟踪运行状态
- [Zeraix](concepts/tool-zeraix.md) — 开源本地优先 AI 桌面工作区,跑私有模型 + agent + 文件,研究模型在个人硬件上的高效推理
- [PAXM](concepts/tool-paxm.md) — 厂商中立的编码 Agent 跨工具持久化记忆层,Codex / Claude Code / OpenCode / Pi / ZCode 共享记忆

### 企业 / 组织 / 数字员工（本批新增）
- [StaffDeck](concepts/tool-staff-deck.md) — OpenBMB 开源的企业数字员工平台,把工作经验 / 流程 / 决策标准沉淀为可复用可演进的数字员工

### AI 编码 IDE / 工作台（本批新增）
- [Nyx Local AI](concepts/tool-nyx-local-ai.md) — VS Code / Cursor 本地 AI 编码插件,接 Ollama / LM Studio,全程离线无 token 费
- [pi-discuss-mode](concepts/tool-pi-discuss-mode.md) — Pi Coding Agent 只读讨论模式扩展,禁写工具 + bash 受限,纯讨论 / 审 PR / 聊架构

### Skills / 内容 / 营销（本批新增）
- [oil-cover](concepts/tool-oil-cover.md) — Claude / Codex 用的小红书封面生成 Skill,Apple 风 + 真实屏幕证据,整图一张生成

### RAG / 数据工具（本批新增）
- [GoldPan](concepts/tool-gold-pan.md) — 隐私优先多模态数据提取 + 本地 RAG 工作台,异构源转 Markdown 入 100% 本地向量库

### 后端 / 部署 / 自托管（本批新增）
- [Openship](concepts/tool-openship.md) — 自托管部署平台 + 内置 CI/CD,桌面应用 / Web 仪表盘 / CLI 三形态
- [EdgeMirror](concepts/tool-edge-mirror.md) — Cloudflare Workers 单域名边缘镜像网关,9 大开发源(PyPI / PyTorch / HF / GitHub / Docker / npm / Go / Maven / crates)统一加速

### 桌面 / 系统工具（本批新增）
- [RoutineOps](concepts/tool-routine-ops.md) — 自托管 MDM / RMM 平台,常驻 gRPC / mTLS 通道跨公网管 Win / macOS / Linux 设备群
- [Rogallo](concepts/tool-rogallo.md) — Python 写的终端 Gemini 客户端,敏感内容自动掩码,自签证书按站点记忆

### 评估 / 基准（本批新增）
- [ReactBench](concepts/tool-react-bench.md) — 编码 Agent 用的 React 实战评测,专治「测试全绿但上线出问题」的 React 反模式
- [LHTB](concepts/tool-lhtb.md) — Agent 长任务基准,46 条终端跑几百步任务,隐藏验证器打分
- [Awesome Scientific LLM Benchmarks](concepts/tool-awesome-scientific-llm-benchmarks.md) — 精选科学 LLM 基准清单,数学 / 物理 / 化学 / 材料 / 生物 / 智能体科学全覆盖

### Codex 周边（本批新增）
- [quota-float](concepts/tool-quota-float.md) — Codex Desktop 额度悬浮小组件,直读登录态真实剩余 / 配额 / 重置时间

### 游戏（本批新增）
- [Steam 成就中文翻译安装工具](concepts/tool-steam-achievement-translation-installer.md) — Windows Steam 成就中文化一键工具,自动扫本机游戏 + 翻译库版本匹配 + 安全改写 + 备份恢复

## 本批新增（2026-07-21）

### 桌面 / 系统工具（本批新增）
- [Teleport](concepts/tool-teleport.md) — Windows 右键「发送到」批量移动文件 / 文件夹的桌面小工具
- [FocuSD Island](concepts/tool-focusd-island.md) — Windows 屏幕顶部透明悬浮岛工具面板,收纳待办 / 笔记 / 剪切板 / 媒体 / AI 编程状态
- [Torder 今序](concepts/tool-torder.md) — Tauri 2 + 本地 SQLite 的 Windows 待办,记录 / 整理 / 提醒全部本地完成
- [phone-record-manager](concepts/tool-phone-record-manager.md) — Python + PySide6 + SQLite 的 Windows 桌面工具,登记手机号都绑过哪些网站 / App / 账号
- [Grayslate](concepts/tool-grayslate.md) — 轻量桌面便签本,自动识别贴入内容、本地转换工具、自动保存 + 可搜索
- [Holo](concepts/tool-holo-macos-knock.md) — 实验性 macOS 原生工具,MacBook 周围桌面划成四块敲击区,麦克风本地识别敲击位置触发动作

### 终端 / 系统 / 网络（本批新增）
- [Network Doctor](concepts/tool-network-doctor.md) — TUI 网络诊断链,自动跑完 ping / dig / curl / traceroute,告诉你「断在哪、为什么、怎么修」
- [tuistore](concepts/tool-tuistore.md) — 终端里的应用市场,搜索 / 浏览几百款终端 + GUI 应用,一键安装,自动识别系统与包管理器
- [yoinks](concepts/tool-yoinks.md) — 终端里的视频下载器,无浏览器 / 无弹窗 / 无虚假下载按钮
- [cloudflare-ddns (favonia)](concepts/tool-cloudflare-ddns-favonia.md) — Cloudflare DDNS 守护进程,定期检测本机公网 IP 并自动更新 DNS 记录

### Android / 移动（本批新增）
- [Aether](concepts/tool-aether-android-agent.md) — Android 上的本地通用 AI Agent,类 ChatGPT 界面 + 内置 Alpine VM 跑 Shell,支持 Shizuku / Termux

### 自托管 / 资源目录（本批新增）
- [selfhost.directory](concepts/tool-selfhost-directory.md) — 可搜索的自托管开源应用目录,2,700+ 项目 + 安装指南 + 替代方案 + 实时版本跟踪

### 编程语言 / 工具链（本批新增）
- [ZSUI](concepts/tool-zsui.md) — Rust 轻量原生 UI 框架,组合 + trait 搭界面、强类型消息管状态,Win32 / AppKit / Linux 同源编译出原生窗口

### 前端 / 设计资源（本批新增）
- [react-textarea-code-editor](concepts/tool-react-textarea-code-editor.md) — 轻量 React 代码输入框组件,textarea 底层 + 语法高亮叠层,表单 / 嵌入场景特化

### 视频 / 影像（本批新增）
- [NTSCRT](concepts/tool-ntscrt.md) — macOS 原生 NTSC / VHS + RetroArch CRT 着色器,两阶段做「老电视在放」的复古质感

### AI / Agent 学习资料（本批新增）
- [dg-ai-notes](concepts/note-dg-ai-pi-agent-tutorial.md) — Pi-Agent 10 章源码级教程笔记,每章讲「概念 → 源码 → 设计取舍」三层,三种阅读方式

## 本批新增（2026-07-22）

### AI / Agent 生态 / 多代理协作（本批新增）
- [coding-control-tower](concepts/tool-coding-control-tower.md) — 同时跑多个 AI 编码 agent 的本地面板,NOW / NEEDS YOU / resume packet / 当日 token 全景,无需打标签
- [caw](concepts/tool-caw-multi-agent-terminal.md) — 浏览器里同时开多个 AI 编程智能体的终端,状态可视化
- [ccmux](concepts/tool-ccmux.md) — tmux 里跟踪 Claude Code / Codex / Cursor 多 agent 会话,一键跳转
- [agents-council](concepts/tool-agents-council.md) — Claude Code / Codex CLI 加「召集议会」Skill,多本地 CLI 并行回答
- [qiaomu-model-cli](concepts/tool-qiaomu-model-cli.md) — 把 Grok / Kimi / Claude Code 三家 CLI 串起来,batch / dual 两种模式

### Agent Skills / 内存 / 持久化（本批新增）
- [hermespace](concepts/tool-hermespace.md) — Hermes Agent 的持久层,跨会话记忆 / 信念 / 成长轨迹

### Skills / 内容 / 营销（本批新增）
- [niubiskill](concepts/tool-niubiskill.md) — AI Agent「盈利路径选择」Skill,离收钱近 + 七天可验证
- [workbuddy-xhs-skills](concepts/tool-workbuddy-xhs-skills.md) — 小红书 10 个 Agent Skill（6 内容 + 4 视觉）完整工作流
- [gc-minimal-zine-poster](concepts/tool-gc-minimal-zine-poster.md) — 独立杂志风海报生成 Skill,安静 / 克制 / 印刷质感

### 前端 / 设计资源（本批新增）
- [learnui](concepts/tool-learnui.md) — 中英双语 UI 视觉词典,精准术语名给 AI 用

### 视频 / 影像（本批新增）
- [vox-director](concepts/tool-vox-director.md) — 一句话全自动出片的 6 步流水线,拼贴海报 + 动效 + ffmpeg
- [video-shotcraft](concepts/tool-video-shotcraft.md) — Claude Code / Codex 用的「导演」Skill,106 镜头卡 + 162 动效样式 + 161 样片
- [Motionly](concepts/tool-motionly.md) — AI 驱动动效编辑器,AI 出 .motion 初稿 + 人手工精修时间轴

## 本批新增（2026-07-23）

### AI / Agent 生态 / 多代理协作（本批新增）
- [Harnss](concepts/tool-harnss.md) — 跨平台桌面软件,把 Claude Code / Codex / ACP 兼容的编程代理整合到同一个窗口
- [ThreadBeacon](concepts/tool-codex-threadbeacon.md) — Windows 原生小窗,实时显示 Codex 主任务状态 + 异常检测 + 自动续接
- [LLM Fingerprint Detector](concepts/tool-llm-fingerprint-detector.md) — 给 OpenAI 兼容 API 实际跑的 LLM 打行为指纹,识别模型替换 / 静态度量量化等代理欺骗
- [Inferock Bench](concepts/tool-inferock-bench.md) — 本地代理拦 LLM API 调用流量,独立记账「花了多少 / 失败几个 / 失败还被收费几个」

### 终端 / 系统 / 网络（本批新增）
- [CmdBox](concepts/tool-cmdbox.md) — 带别名 / 变量 / 标签的命令存储 + 快速执行工具,告别 shell 历史翻找
- [SpookiUI](concepts/tool-spookiui.md) — Ghostty 终端配置 TUI,改完自动写回 + 验证 + 触发重载
- [Haoleme](concepts/tool-haoleme.md) — `hao` 启动命令,手机 App 监控电脑 / 服务器命令运行状态

### 桌面 / 系统工具（本批新增）
- [study-desk](concepts/tool-study-desk.md) — Windows 桌面「一站式学习中心」,课表 + 番茄钟 + 备忘录 + 倒数日 + 资料库 + 健康提醒
- [Kudu](concepts/tool-kudu-cleaner.md) — 跨平台免费开源系统清理工具,Windows / macOS / Linux
- [RogueCleaner](concepts/tool-roguecleaner.md) — Windows 流氓软件残留清理,右键菜单 / 启动 / 服务 / 计划任务 / 浏览器插件 / 文件关联
- [OpenBrowser](concepts/tool-openbrowser.md) — 本地桌面指纹浏览器,隔离 Chromium 环境管多账号 + RPA

### 幻灯片 / 演示（本批新增）
- [Bento](concepts/tool-bento-slides.md) — 单 HTML 文件演示文稿,数据明文 JSON 存头部,Agent 可直接编辑
- [build-plan](concepts/tool-build-plan-html.md) — 把技术方案 / Build Plan 一键转可打开 HTML 页,带侧栏导航 + 内联 SVG + 多语言

### 前端 / 设计资源（本批新增）
- [thinking-orbs](concepts/tool-thinking-orbs.md) — AI / Agent 界面用 React 思考球加载动画,六种状态 + 两种尺寸 + 自动暗亮主题

### 视频 / 影像（本批新增）
- [Pireel](concepts/tool-pireel.md) — 浏览器内口播视频剪辑 + 字幕 + 主题,暴露 MCP 接口让 AI Agent 调用
