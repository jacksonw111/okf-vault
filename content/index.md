---
type: Index
title: "我的 OKF 知识库"
description: "基于 Open Knowledge Format v0.1 的个人知识库根入口。本目录即一个 OKF bundle——一个由 Markdown + YAML frontmatter 组成、可被人和 AI agent 共同消费的知识目录。"
tags: "[okf, root]"
timestamp: "2026-08-27T15:46:00Z"
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

- [Jakub 设计 Skills](concepts/note-jakub-design-skills.md) — `Note`
- [Agent Swarms](concepts/tool-agent-swarms.md)
- [Ai Gateway Tdn](concepts/tool-ai-gateway-tdn.md)
- [Auteur](concepts/tool-auteur.md)
- [Buckit](concepts/tool-buckit.md)
- [Callpilot](concepts/tool-callpilot.md)
- [Claude Account](concepts/tool-claude-account.md)
- [Crona](concepts/tool-crona.md)
- [Dashline](concepts/tool-dashline.md)
- [Doc Engine Cli](concepts/tool-doc-engine-cli.md)
- [Flashcard Quiz App](concepts/tool-flashcard-quiz-app.md)
- [Ghostties](concepts/tool-ghostties.md)
- [Ivy Obsidian Template](concepts/tool-ivy-obsidian-template.md)
- [Pigo](concepts/tool-pigo.md)
- [Prompt Self Tuning](concepts/tool-prompt-self-tuning.md)
- [Protocol Model](concepts/tool-protocol-model.md)
- [Qwen Audio Agent](concepts/tool-qwen-audio-agent.md)
- [Sitepins](concepts/tool-sitepins.md)
- [Toolknit Desktop](concepts/tool-toolknit-desktop.md)

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

## 本批新增（2026-07-24）

### AI / Agent 生态（本批新增）
- [CodexPetdexSkins](concepts/tool-codex-petdex-skins.md) — Codex 桌面端一站式换装工具,主题 / 皮肤 / 壁纸 / 宠物 / 搭配通过本机 CDP 注入,不改 ASAR/MSIX
- [codex-slides](concepts/tool-codex-slides.md) — 给 Codex 编程代理用的开源幻灯片工作室,跑在 Codex 内置浏览器里,45 套模板 + 73 套社区风格 + 24 种场景化工作流
- [coding-tools-mcp](concepts/tool-coding-tools-mcp.md) — Rust + Tauri 2 桌面 MCP 编程工作台,会话检查点写到 docs/history-session/,新对话调 history_session_bootstrap 自动续接
- [guidebridge](concepts/tool-guidebridge.md) — Python AI 代理操控 React 页面的桥,实时 DOM + 光标动作,不依赖截图与视觉模型

### 后端 / DevOps / 代码审查（本批新增）
- [yunxiao-mr-review-step](concepts/tool-yunxiao-mr-review-step.md) — 阿里云云效 Flow 流水线接入的 AI 自动评审 Codeup 合并请求步骤,模型输出转行级评论 + 飞书报告

### 数据库（本批新增）
- [libredb-studio](concepts/tool-libredb-studio.md) — 开源 AI 驱动 Web SQL IDE,PostgreSQL / MySQL / SQLite / MongoDB,浏览器打开即用

### 内容创作 / 写作辅助（本批新增）
- [no-ai-slop](concepts/tool-no-ai-slop.md) — 去 AI 套话味儿扫描器,识别 20+ 种 AI 常见句式（不是 A 而是 B / 冒号披露 / 虚词中心 / 同义词轮换等）
- [ticket-agent](concepts/tool-ticket-agent.md) — 黄牛票截图自动解析与比价,OCR + 加价倍数 + 价格波动,每个数字可点回原图

### 移动 / 嵌入式渲染（本批新增）
- [chronos](concepts/tool-chronos-kit.md) — App 内嵌 2D/3D 渲染与小游戏宿主方案,.cron 包 + 消息通道 RPC,已在 B 站弹幕与跨年晚会互动音游落地

### React Native / 移动 UI（本批新增）
- [expo-glass-tabs](concepts/tool-expo-glass-tabs.md) — Expo Router 毛玻璃底部标签栏组件,滚动缩小但不隐藏图标

### 桌面 / 系统工具（本批新增）
- [lan-file-transfer](concepts/tool-lan-file-transfer.md) — Windows 桌面文件共享工具,Tkinter + FastAPI + 三层权限 + 审计日志
- [pdfdown](concepts/tool-pdfdown.md) — 浏览器内本地 PDF → Markdown,全程不经过服务器

### 数据源 / MCP（本批新增）
- [douyin-mcp](concepts/tool-douyin-mcp.md) — 抖音创作者中心 MCP 数据桥,页面指标 + 视频文案结构化,AI 内容复盘友好

### 阅读 / 资源（本批新增）
- [yt-channels-DS-AI-ML-CS](concepts/tool-yt-channels-ds-ai-ml-cs.md) — 180+ 精选 YouTube 数据 / AI / CS 频道清单,按主题分类

### 时间线 / 世界构建（本批新增）
- [sreegjl/timelines](concepts/tool-sreegjl-timelines.md) — 免费开源本地优先时间线创建工具,面向世界构建与历史研究的交互式可视化

### 更新（Updated）
- [Network Doctor](concepts/tool-network-doctor.md) — 补充「依赖图顺序（网卡 → TCP 出口 → DNS → TCP → TLS → HTTP）+ 双模式（目标地址 / 仅本地）」最新特性

## 本批新增（2026-07-25）

- [Pigma](concepts/tool-pigma.md) — Rust + Ratatui 构建的终端音乐播放器，支持网易云与本地音乐，并提供歌词高亮和 YouTube 音源回退。
- [LogiTux](concepts/tool-logitux.md) — 面向 Linux 的原生 Logitech 外设配置工具，可管理 DPI、灯光、耳机均衡与摄像头参数。
- [Filester](concepts/tool-filester.md) — 面向 Android 的临时云存储工具，强调免账号、无广告与隐私优先。
- [Dapr Dev Dashboard](concepts/tool-dapr-dev-dashboard.md) — 面向 Dapr 本地开发的仪表盘，可实时查看运行状态并交互式生成组件与弹性策略。
- [CipherMoth](concepts/tool-ciphermoth.md) — 自托管密码管理器，采用 Argon2id 派生、Fernet 加密与 PostgreSQL 存储，并将解密密钥限制在浏览器会话内。
- [pgapp](concepts/tool-pgapp.md) — 用纯文本 .pgapp 文件描述应用，并由 PostgreSQL 自动建表和生成交互式 HTML 的应用构建工具。
- [LiveMarkDownEditor](concepts/tool-livemarkdown-editor.md) — 基于 .NET 10 WPF 的 Windows 所见即所得 Markdown 编辑器，底层文件始终保持纯 Markdown。
- [keepIT](concepts/tool-keepit-notes.md) — 支持多人共享、实时同步、搜索和提醒的自托管笔记系统，配套 Android 应用、桌面小部件与离线能力。
- [netmon](concepts/tool-netmon-ai-telegram.md) — 自托管网络监控工具，通过定时测速与 ARP 扫描采集状态，并生成分析后推送到 Telegram。
- [RoamRadar](concepts/tool-roamradar.md) — 部署在 Cloudflare Workers 上的个人旅行 PWA，可自动导入行程并集中提供目的地实用信息。
- [QueryForge](concepts/tool-queryforge.md) — 把自然语言转换为可审计 SQL 的数据查询工具，通过语义层与策略治理约束生成结果。
- [elements-release](concepts/tool-elements-release.md) — 基于 Unlayer Elements 的更新日志邮件模板，可从一个数据文件生成邮件、网页、纯文本和编辑器 JSON。
- [no-slop-zh](concepts/tool-no-slop-zh.md) — 用于 Claude Code 与 Codex 的中文文本清理 Skill，在锁定事实与术语的前提下削弱 AI 套话。
- [sshbox](concepts/tool-sshbox.md) — Go 单二进制 SSH 跳板工具，为每个会话启动受限 Alpine 容器并在断线后销毁。
- [InkOS](concepts/tool-inkos.md) — 面向电子墨水屏的内容系统，在服务端抓取并重排网页内容，设备端只接收页面帧与点击区域。
- [面向 Kotlin 开发者的 Rust 学习路径](concepts/note-rust-for-kotlin-devs.md) — 通过 Kotlin 与 Rust 对照示例学习所有权、错误处理、trait、生命周期、异步与并发。
- [PiTTy](concepts/tool-pitty.md) — 基于 TypeScript 与 OpenTUI 的 Pi 终端界面，强化对话滚动、折叠信息、子代理控制与任务管理。
- [Cloudflare Trace API](concepts/tool-cloudflare-trace-api.md) — Cloudflare 提供的免注册访客网络信息端点，可返回 IP、国家代码和接入数据中心代码。

## 本批新增（2026-07-26）

### AI / Agent 生态
- [Penguin Harness](concepts/tool-penguin-harness.md) — `Tool` — 开源 AI 代理构建框架,代理自动创建/优化其他代理,内置办公/开发/AI 应用/代理调优四大类技能
- [harness-remote](concepts/tool-harness-remote.md) — `Tool` — 手机端控制 OpenCode / Oh My Pi 等 AI 编程助手的远程遥控应用
- [opencode-fusion](concepts/tool-opencode-fusion.md) — `Tool` — OpenCode 多模型协作:主代理只规划/审查(权限层禁掉编辑工具),改代码强制路由给便宜副手
- [pi-extensible-workflows](concepts/tool-pi-extensible-workflows.md) — `Tool` — Pi 终端 AI 助手的确定性多代理工作流编排,支持并行派发/审批暂停/断点恢复

### 桌面 / 系统工具
- [Sonor](concepts/tool-sonor.md) — `Tool` — macOS 原生本地语音转文字,whisper.cpp + Apple Silicon Metal,数据不出设备
- [EnvNexus-AI](concepts/tool-envnexus-ai.md) — `Tool` — Rust + Tauri 2 的 Windows 桌面多语言 SDK 多版本管理 GUI
- [personal-os-setup](concepts/tool-personal-os-setup.md) — `Tool` — 一行命令在 Windows/Linux/macOS/WSL2/Google TV 搭一致开发环境
- [xiaoyun-translator](concepts/tool-xiaoyun-translator.md) — `Tool` — Windows 桌面划词翻译 + 公式 OCR + 本地 AI 文献阅读整合
- [OpenSurge for Mac](concepts/tool-opensurge-mac.md) — `Tool` — 把 Mac 变全屋透明代理网关,设备端零配置,按设备粒度选代理/直连

### 后端 / DevOps / 运维
- [Pagerlite](concepts/tool-pagerlite.md) — `Tool` — 轻量自托管的 Laravel 值班(on-call)与告警分派系统
- [SICK](concepts/tool-sick.md) — `Tool` — Linux 服务器运维脚本集,硬件检测 + 全球 23 节点 iperf3 + Geekbench 5/6/7
- [Storage UI](concepts/tool-storageui.md) — `Tool` — 自托管 S3/Cloudflare R2 文件浏览器,四种视图 + 搜索/筛选/排序
- [AgentAcct](concepts/tool-agentacct.md) — `Tool` — 读 Claude Code/Codex 本地会话日志展示 token 用量 + 费用 + 任务仪表盘

### 金融 / 量化
- [ETF Grid Design](concepts/tool-etf-grid-design.md) — `Tool` — Python Flask + React 的 ETF 网格交易参数生成器,基于 tushare/akshare 历史行情

### Generative UI / Chat 界面
- [ChatHTML](concepts/tool-chathtml.md) — `Tool` — 把 LLM 输出 HTML 流式渲染到沙箱 iframe,带选择编辑/重生成/截图修复/导出
- [Conversed](concepts/tool-conversed.md) — `Tool` — TypeScript 组件库(React+Angular),把 LLM 回复解析为 16 种可交互 UI 组件

### 跳过 / 复核（Skipped / No-op）
- QingQ77「事情正在起变化」+ 视频 — 短语 + 短视频,无可提取的工具/概念/项目信息,按「质量门槛」跳过
- QingQ77「哈哈哈」+ 视频 — 纯情绪反应类,无信息量,按「质量门槛」跳过
- QingQ77「好玩～」+ 视频 — 纯情绪反应类,无信息量,按「质量门槛」跳过

## 本批新增（2026-07-29）

### AI / Agent 生态 / 编排
- [Cloudflare Durable Objects Agent 运行时](concepts/tool-cloudflare-durable-objects-agent.md) — Durable Objects 跑 agent / 文件系统 + R2 存大文件 + Artifacts 管 git + pi 做 harness + Code Mode 写 JS
- [AxisAgentic](concepts/tool-axis-agentic.md) — 给 Agent 每次执行做不可篡改的运行记录,回放 / 评测 / 训练数据导出同一份
- [BanyanCode](concepts/tool-banyan-code.md) — 终端 AI 编程多代理编排,OpenCode + Effect + TypeScript
- [Factory (Agent Runtime)](concepts/tool-factory-agent.md) — 让编码 Agent 在仓库上自动持续工作
- [Metis (Coding Layer)](concepts/tool-metis-coding-layer.md) — 编程模型外层包装,改前查资料 + 改后验证
- [Spec-Superflow](concepts/tool-spec-superflow.md) — AI 编码规划 → 实现硬闸,先想清楚再动手
- [AnythingAtlas](concepts/tool-anything-atlas.md) — Agent 里的结构化学习地图生成器

### 持久化记忆 / 沙箱 / 授权
- [OptMem](concepts/tool-optmem.md) — 426 token prompt + 脚本极简跨会话记忆
- [Zestmem](concepts/tool-zestmem.md) — Go 写,多 Agent 跨会话分布式持久化记忆,MCP 两个工具 remember / recall
- [Dormice](concepts/tool-dormice.md) — 本地冷冻沙箱,空闲自动 freeze,50ms 恢复
- [CyVisGuard](concepts/tool-cyvisguard.md) — Agent 工具调用授权层,zero-trust 风格

### Claude / Codex 桌面增强
- [ClaudeDesktopPlusPlus](concepts/tool-claude-desktop-plus-plus.md) — Claude Desktop 功能增强套件,cc-switch + 第三方 API + 插件管理 + 汉化
- [WinUI4K](concepts/tool-winui4k.md) — Kotlin / Java 直接调 WinUI,不用改 C#

### 视频 / 长视频处理 / 视频笔记
- [Timecode-Agent](concepts/tool-timecode-agent.md) — 长视频带时间戳证据账本,转录优先
- [Bilibili Video Notes Skill](concepts/tool-bilibili-video-notes-skill.md) — B 站视频链接 → 带截图 DOCX 笔记

### 后端 / 部署 / 网络 / 搜索
- [RatholeEngine](concepts/tool-rathole-engine.md) — rathole + Nginx 多地点反向隧道编排
- [Xerj](concepts/tool-xerj.md) — Rust 从头实现的统一 AI 搜索引擎(全文 + 向量 + Agent 记忆),兼容 ES
- [raft-kv-engine-project](concepts/tool-raft-kv-engine.md) — Rust 实现的线性化复制 KV(LSM + 无 IO Raft + FoundationDB 风格模拟器)
- [CodeGo API](concepts/tool-codego-api.md) — Go 写,控制面 / 数据面分离,OpenAI 兼容多 provider

### 终端 / TUI
- [ArchWiki TUI](concepts/tool-archwiki-tui.md) — Go 写的终端 Arch Wiki 浏览器,TTY 修引导参数时直查

### 桌面应用 / 移动 / Wayland
- [Comail](concepts/tool-comail.md) — Tauri 2 键盘流桌面邮件客户端,Gmail/M365/IMAP + 本地 SQLite + 语义搜索
- [Habo](concepts/tool-habo.md) — Flutter 习惯追踪应用,端到端加密同步
- [Denial (Wayland Compositor)](concepts/tool-denial-wayland.md) — Flutter 做桌面图形层的 Wayland 合成器

### 写作 / 学习 / 学术 / 仿真
- [Scientific Illustrator](concepts/tool-scientific-illustrator-skill.md) — Codex 插件,把 AI 画的科研插图做成 PowerPoint / draw 可编辑对象
- [Inklish](concepts/tool-inklish.md) — 在真实写作场景(邮件 / Slack / GitHub Issues 等)中练习英语
- [Voxa](concepts/tool-voxa.md) — iPhone 语音远程指挥 AI 编程代理,任务完成自动回拨
- [FDA Endpoint Atlas](concepts/tool-fda-endpoint-atlas.md) — 161 适应症 / 15 治疗领域,跟踪 FDA 主要终点变化,Whitespace Explorer 综合打分
- [uavsim](concepts/tool-uavsim.md) — 本地四旋翼飞控仿真,LQR / PID / NDI 三种控制律

### 内容生产 / 长篇写作
- [OpenFic](concepts/tool-openfic.md) — Agent + RAG 驱动的长篇小说写作工具,百万字级上下文
- [Hammer (Story Editor)](concepts/tool-hammer-story-editor.md) — Kotlin 本地优先跨平台故事编辑器,数据纯文件
- [Self-Media Content Workflow](concepts/tool-self-media-content-workflow.md) — 自媒体全流程 9 Skill 套件,5 强制确认点防未授权发布

## 本批新增（2026-07-30）

### AI / Agent 生态
- [pi-tbox](concepts/tool-pi-tbox.md) — Pi 扩展工具开关面板，集中列出 / 分组开关 / 自定义工作流 / 跨会话持久
- [Nerve](concepts/tool-nerve-desktop-coding.md) — 本地优先桌面编码工具集，消息流 + 工具调用 + 审批 + 计划全暴露
- [openclaude-improved](concepts/tool-openclaude-improved.md) — TypeScript 写，OpenAI / Ollama / Gemini / Bedrock 等十几家 AI 后端可切换

### 终端 / TUI
- [hop](concepts/tool-hop-ssh-tui.md) — Go 写的终端 SSH 多服务器切换 TUI，内置 SSH + VT 模拟器
- [Ghostty Warp Shader](concepts/tool-ghostty-warp-shader.md) — Ghostty 终端星轨加速 GLSL shader，单文件即用

### 桌面 / 系统工具
- [PixShell](concepts/tool-pixshell.md) — 跨平台原生 SSH/SFTP 客户端（macOS Swift + Windows WPF，非 Electron）
- [Tinycast](concepts/tool-tinycast.md) — macOS 原生轻量启动器 + 剪贴板历史（3 MB / <100 MB 内存）
- [GodotHub](concepts/tool-godothub.md) — Godot 引擎的 Unity Hub 风格项目管理器
- [VS Code Fork / WSL 跨语言桌面 UI 思路](concepts/tool-vscode-fork.md) — VS Code 跨语言 / 跨平台桌面 UI 工程范式（Electron + WebView + LSP/DAP + WSL 桥接）

### 视频 / 多媒体
- [Rescript](concepts/tool-rescript-video-editor.md) — 浏览器视频编辑器，改字幕 = 剪视频，文件不出本机
- [Open AI Canvas / 影策](concepts/tool-open-ai-canvas.md) — AI 影视无限画布工作台，文字 / 图片 / 视频 / 音频 + 分镜 + 角色卡

### 本地 LLM / Agent
- [Local-Hermes-Portable](concepts/tool-local-hermes-portable.md) — llama.cpp + Hermes Agent 跨平台便携包，双击即跑

### 搜索 / 聚合 / 推送
- [NeoSearch](concepts/tool-neosearch.md) — C# 写的去广告去追踪 AI 搜索引擎，多视角分组
- [TrendRadar](concepts/tool-trendradar.md) — 多平台热榜聚合 + 关键词过滤 + 10+ 推送通道，30 秒 fork 部署
- [Streamflix](concepts/tool-streamflix.md) — Android TV / 手机流媒体聚合客户端
- [hark](concepts/tool-hark-webhook-push.md) — 任意 webhook 转带来源标识的 iPhone 推送通知

### 编辑器 / 写作
- [neocursor.nvim](concepts/tool-neocursor-nvim.md) — Neovim 插件读 Cursor 私有 API 拿 ghost text 补全
- [grammar-lol](concepts/tool-grammar-lol.md) — 桌面任意应用内 AI 语法校正（双 Right Shift 触发）

### 跳过 / 复核（Skipped / No-op）
- QingQ77「超梦？」+ 视频 (2082823150270927199) — 短语 + 短视频,无可提取的工具/概念/项目信息,按「质量门槛」跳过

### 更新（Updated）
- [Metis / Coding Layer](concepts/tool-metis-coding-layer.md) — 修正引用：tool-factory-agent / tool-spec-superflow 中断链改回指此（已有概念，未新建）
- [Factory](concepts/tool-factory-agent.md) — 同步修正 Metis 链接
- [Spec-Superflow](concepts/tool-spec-superflow.md) — 同步修正 Metis 链接

## 本批新增（2026-07-31）

### 方法论 / Playbook
- [Vibe Coding 设计系统八步法](concepts/playbook-vibe-coding-design-system.md) — 从 VI → Design Token → 组件 → 状态 → 交互 → 动效 → 撤销 → AI 约束搭设计系统

### AI / Agent 生态
- [AgentEnv](concepts/tool-agentenv-kvcache.md) — Firecracker microVM + overlaybd 分布式 agent 沙箱，启动 <50ms
- [Eve Directory](concepts/tool-eve-directory.md) — Eve agent 开放注册中心，shadcn CLI 安装 / GitHub 登录贡献
- [better-harness](concepts/tool-better-harness.md) — 五维审计 AI 编码工作流（目标 / 执行 / 验证 / 质量 / 沉淀），每项绑证据
- [ccsessions](concepts/tool-ccsessions.md) — Claude Code 终端会话的 TUI 管理器
- [sharedoc-mcp](concepts/tool-sharedoc-mcp.md) — agent 产出 Markdown 直接变可分享链接
- [livis-hermes-platform](concepts/tool-livis-hermes-platform.md) — Livis 眼镜 / 理想同学 到 Hermes Agent 的国内适配层
- [Graft](concepts/tool-graft.md) — 把代码依赖 / 模块边界预生成 Markdown 喂给 agent

### 阅读 / 笔记 / 写作
- [Tasogare](concepts/tool-tasogare.md) — 网页阅读器，真人 + AI 同书各画一色，配 MCP 服务
- [paperless-brain](concepts/tool-paperless-brain.md) — 给 Paperless-ngx 加 AI，对存档对话 / 提截止日期 / 写信
- [NodeGraph](concepts/tool-nodegraph.md) — VS Code 扩展，论文自动建知识图谱
- [fragment-garden](concepts/tool-fragment-garden.md) — 像素花园 + 散步重访，让碎片想法过几天自动浮现

### 渲染 / PDF / 多媒体
- [html2pdf (SanzarRehman)](concepts/tool-html2pdf-sanzar.md) — Rust 自建 HTML→PDF，不启 Chromium，内存大幅下降

### 终端 / TUI
- [herdr-browser](concepts/tool-herdr-browser.md) — 终端面板嵌真实 Chromium，通过 CDP 让 agent 驱动

### 桌面 / 系统工具
- [ZENCHE](concepts/tool-zenche.md) — 五端原生的 Nikon 相机控制 + 影像传输
- [知微 / Finance_Management](concepts/tool-zhiwei-finance.md) — 桌面财务记账（Qt/QML + Spring Boot）

### 数据 / 分析
- [Talivia](concepts/tool-talivia.md) — 网站分析 + Stripe / LemonSqueezy 收入数据并到一图

### 跳过 / 复核（Skipped / No-op）
- QingQ77「cool」+ 视频 (2083202443685573055) — 短语 + 视频，无可提取信息
- QingQ77「等等」+ 视频 (2082973668972638398) — 短语 + 视频，无可提取信息
- QingQ77「你们是什么时候开始注意到人类的」+ 视频 (2083047181746135237) — 短语 + 视频，无可提取信息

## 本批新增（2026-08-01）

### AI / Agent 生态
- [grafana-ai-sdk](concepts/tool-grafana-ai-sdk.md) — Go 后端多 provider LLM SDK（流式 / 工具调用 / 结构化输出），与 Vercel AI SDK 协议对齐
- [bbarit-agent-oss](concepts/tool-bbarit-agent-oss.md) — Rust 单文件二进制替代 Claude Code / Codex CLI，15+ provider / 1000+ 模型
- [claude-code-router](concepts/tool-claude-code-router.md) — 本地网关统一管理 Claude Code / Codex / Grok 凭据 / 路由 / 故障切换
- [agent-manager (tmux)](concepts/tool-agent-manager-tmux.md) — TUI 架在 tmux 上管 Claude Code / Codex / OpenCode / Grok Build 多 agent
- [memmy-agent](concepts/tool-memmy-agent.md) — 跨 AI 代理共享长期记忆中间层，一次记住到处用

### 评估 / 沙箱 / 反检测
- [ai-code-evaluation-suite](concepts/tool-ai-code-evaluation-suite.md) — Python 代码丢进一次性 Docker 隔离评分，可见 + 隐藏测试 + 分数分解
- [chrome-client (Cronet)](concepts/tool-chrome-client-cronet.md) — Python HTTP 客户端底层用 Chromium Cronet，拿真实 Chrome TLS 指纹过反爬

### 桌面 / 系统工具
- [session-manager (Tauri v2)](concepts/tool-session-manager-tauri.md) — Tauri v2 + React + Rust 桌面应用，三栏浏览 AI 编程助手历史会话与分支树
- [what-cant-i-press](concepts/tool-what-cant-i-press.md) — macOS 菜单栏 / Windows 托盘无障碍快捷键探查工具，聚合屏幕阅读器文档

### 自托管 / 智能家居 / 物联网
- [go2rtc](concepts/tool-go2rtc.md) — Go 单二进制摄像头流媒体服务器，RTSP/WebRTC/RTMP/HLS/HomeKit 互通，<0.5s 延时
- [sunshine-send](concepts/tool-sunshine-send.md) — Android TV 端 NanoHTTPD 局域网快传，启动即得二维码 + 上传页

### 数据 / 分析
- [the-daily-diff](concepts/tool-the-daily-diff.md) — 每天自动汇总 arXiv + HN，按天排好打分排序的技术早报
- [xy (Reflex)](concepts/tool-xy-reflex.md) — Rust 算 + WebGL2 画的 Python 图表库，1 万到 1 亿点都能秒出

### 容器 / 终端
- [docksurf](concepts/tool-docksurf.md) — 终端里用键盘操作 Docker 的 TUI，看容器 / 镜像 / 卷 / 网络 + 实时数据

### Android / 移动
- [OneStep4](concepts/tool-onestep4.md) — 已 Root Android 多窗口 / 侧边小窗，延续 Smartisan「One Step」逻辑

### 个人追踪 / 媒体
- [Kiroku](concepts/tool-kiroku.md) — 全栈个人动漫 / 漫画 / 小说追番追读工具，集中管理进度 / 评价 / 笔记

### 视觉 / 创作 / 营销
- [consulting-deck](concepts/tool-consulting-deck.md) — 咨询风格 PPT 工具包，论据可溯源 + 图表带分析 + PPTX 可继续编辑
- [open-image-prompts](concepts/tool-open-image-prompts.md) — 万级带参考图的 AI 图片 prompt 库，装 Skill 即可终端搜索

### 复核（Reused / No-op）
- Wen_Zw RT @BTCqzy1 gc-minimal-zine-poster (2083527924687515887) — 概念已建过，本次 RT 无新增信息，走「复核，无变更」分支

### 跳过 / 复核（Skipped / No-op）
- QingQ77「真正的大佬」+ 视频 (2083416873060958678) — 短语 + 短视频，纯情绪反应，按「质量门槛」跳过
- QingQ77「真玻璃种」+ 视频 (2083557362531749997) — 短语 + 短视频，纯情绪反应，按「质量门槛」跳过
- QingQ77「好柔软的身体」+ 视频 (2083463384805331013) — 短语 + 短视频，纯情绪反应，按「质量门槛」跳过

## 本批新增（2026-08-02 / 2026-08-03）

### AI / Agent 生态
- [Chartr](concepts/tool-chartr.md) — Go + Svelte 的 agent 多路复用器，规划 Markdown 自动渲染成星图
- [QM (Y Combinator)](concepts/tool-qm-yc.md) — YC 开源多人智能体框架，每员工隔离工作区 + Slack 协作
- [Pi-Livecraft](concepts/tool-pi-livecraft.md) — 给 Pi 终端 AI 助手套一个可被模型改的 React 网页界面
- [Hearth](concepts/tool-hearth-nl-game.md) — 自然语言描述想玩的游戏，AI 代理现场建好并跑起来
- [PicoLM](concepts/tool-picolm.md) — 2500 行 C11 写的极简 LLM 推理引擎，256MB 内存跑 TinyLlama 1.1B
- [Gendangzou Skill (跟党走)](concepts/tool-gendangzou-skill.md) — A 股板块政策/资金/ETF 数据封装成 Agent 可调用 Skill

### 桌面 / 系统工具
- [OpenDisk](concepts/tool-opendisk.md) — 开源 MIT 的 macOS 旭日图磁盘空间分析器
- [FolderSizeExplorer](concepts/tool-folder-size-explorer.md) — Windows x64 便携文件管理器，边浏览边递归统计文件夹大小
- [HalalDL](concepts/tool-halaldl.md) — Windows 本地优先 yt-dlp 桌面下载工具（Tauri v2 + React + TS）
- [LightMarkit](concepts/tool-lightmarkit.md) — Tauri v2 + React + TS 轻量桌面 Markdown 编辑器
- [FaceLogin](concepts/tool-facelogin.md) — 让不支持 Windows Hello 的电脑也能刷脸解锁

### 终端 / TUI / CLI
- [Blackguard](concepts/tool-blackguard.md) — Rust + ratatui 终端扑克牌 roguelike（Scoundrel 复刻）
- [Soap](concepts/tool-soap-paper-tui.md) — 纯终端文献管理工具，论文/PDF 自动补元数据 + 键盘浏览
- [fast-copy](concepts/tool-fast-copy.md) — Python 跨平台 CLI 复制工具，SSH 走 tar 管道比 scp/rsync 快 3-5 倍

### 浏览器 / 渲染引擎
- [Falco (Rust browser engine)](concepts/tool-falco-browser-engine.md) — 3.6 万行 Rust 从零实现，HTML/CSS/JS 渲染成 PNG 或交互窗口

### BaaS / 后端
- [CloudflareBase](concepts/tool-cloudflarebase.md) — Cloudflare 账户里自部署的开源 Firebase 替代方案

### Android / 移动
- [军师 (Junshi)](concepts/tool-junshi-android.md) — 本地优先的关系分析 Android App，事实 / 情绪 / 未知分三层

### AI Skill / 提示词
- [南鸢写真提示词 Skill](concepts/tool-nanyuan-prompt-skill.md) — 写真 / 人像摄影意图 → 中文生图 prompt，反推视觉关键词

### Updated（Reused）
- [Cloudflare Kumo](concepts/tool-kumo.md) — 增量更新：明确基于 Base UI 封装，约 45 组件 / 细粒度 tree-shaking

### 跳过 / 复核（Skipped / No-op）
- QingQ77「这种亏得最惨了」+ 视频 (2084238821185732877) — 短语 + 短视频，纯情绪反应，按「质量门槛」跳过
- QingQ77「喜欢这种婚宴，纯干饭。」+ 视频 (2084195988261200367) — 短语 + 短视频，纯情绪反应，按「质量门槛」跳过
- QingQ77「随着 AI 的发展，总有一天会来的。」+ 视频 (2084154544704172070) — 短语 + 短视频，纯情绪反应，按「质量门槛」跳过

## 本批新增（2026-08-04）

### 方法论 / Playbook
- [AGENTS.md 八规则（Vercel Next.js 团队）](concepts/playbook-agents-md-eight-rules.md) — 把 8 条规则放进 `AGENTS.md` 强制 AI 编码 agent 不写兼容层 / 不预防性抽象 / 不重复发明

### AI / Agent 生态
- [Pinvou Agent](concepts/tool-pinvou-agent.md) — 聊天 / 设计 / 写代码三合一桌面 AI 工作台，产出可继续使用的文件 / 产物
- [Sol Advisor](concepts/tool-sol-advisor.md) — Codex 原生 subagent 双角色（Sol 架构+验收 / Terra 实现）+ 全新上下文复审硬闸门
- [Codexloom](concepts/tool-codexloom.md) — 把 Codex 一条线程延续成跨任务累积知识的领域 Agent

### 本地知识库 / 原子笔记
- [My Wiki](concepts/tool-my-wiki.md) — 本地 AI Agent 把原始资料整理成可追溯、可复用的原子知识库

### AI 写作 / 去 AI 腔
- [humanizer-cli](concepts/tool-humanizer-cli.md) — Wikipedia《Signs of AI writing》33 种 AI 写作痕迹做成终端离线参考与草稿检查工具
- [Stop Slop](concepts/tool-stop-slop.md) — 教 LLM 去掉 AI 腔的技能包，5 维度评分凑不上 35 分重写

### 桌面 / 系统工具
- [TaskbarWidgets](concepts/tool-taskbar-widgets.md) — Win11 任务栏直接钉天气 / 系统监控 / 媒体控制小组件
- [GlassQuota](concepts/tool-glassquota.md) — macOS 实时显示 Codex / Gemini / Claude 三个 API 各自的剩余用量
- [cobalt-spark](concepts/tool-cobalt-spark.md) — 极简 Oh My Zsh 主题，闪电符号分隔上下文与命令

### 长篇写作 / 故事引擎
- [Novel Studio (Xiaoyangy/novel-studio)](concepts/tool-novel-studio.md) — Go 写的本地优先 AI 长篇小说引擎，卷—章—章纲冻结 + 弧封存 + 视角隔离

### 自托管 / 服务器 / 网络
- [KPanel (kejilion)](concepts/tool-kpanel.md) — 开源免费 Linux 服务器管理面板，脚本 / SSH / Compose 资源互通
- [TermPair](concepts/tool-termpair.md) — Rust 单二进制端到端加密远程终端共享，AES-128-GCM 盲中继

### 数据传输 / 离线通道
- [qr-data-transfer](concepts/tool-qr-data-transfer.md) — 文件 → 动态二维码，纯空气隔离传输

### 下载客户端
- [Orc-Torrent](concepts/tool-orc-torrent.md) — 跨 Win / macOS / Linux / Android 下载客户端，Rust 内核 + VPN 隐私

### 视频 / 监控 / NAS
- [TimeCut](concepts/tool-timecut.md) — NAS Docker 一体化监控循环录像 + AI 挑精华（人员 / 车辆 / 包裹）+ 日记化

### Python 项目任务
- [TermBoard](concepts/tool-termboard.md) — 常驻交互式 TUI 管理 Python 项目、虚拟环境与任务，自动识别 uv / poetry / pipenv / .venv

### GEO / AI 搜索优化
- [GeoLook](concepts/tool-geolook.md) — GEO「监控 → 诊断 → 开工单执行 → 自动复验」四步串成闭环，让 AI 引擎在回答时把品牌带出来

## 本批新增（2026-08-05）

### 长程代理 / Agent 框架
- [LongHorizon-Harness](concepts/tool-longhorizon-harness.md) — 高德 AMAP-ML 团队开源的「长程代理」脚手架：认知回路 + 经验记忆 + 工具/技能三件套

### 金融 / 市场情绪
- [CNN 恐慌贪婪指数拆解](concepts/note-fear-greed-index.md) — CNN 维护二十年的市场情绪指标，7 个等权重子指标汇总，反着看（均值回归）

### AI / Agent 生态
- [TideVec](concepts/tool-tidevec.md) — 带时间衰减的向量数据库，时间衰减直接算进 HNSW 检索打分
- [open·kritt](concepts/tool-open-kritt.md) — 多 AI 代理并行的安全扫描框架，结果合并为可验证可排序的漏洞发现
- [Tabminal](concepts/tool-tabminal.md) — 终端 + 文件编辑 + AI 智能体收进同一网页界面，服务端会话持久
- [mypaios](concepts/tool-mypaios.md) — Python/FastAPI 自托管本地优先 AI 工作台（MIT），十余项功能集于一身
- [Aimux](concepts/tool-aimux.md) — Rust crate 收敛上百家 AI 服务商 HTTP 接口为统一 API
- [codex-work-starter](concepts/tool-codex-work-starter.md) — 给非开发者的 Codex 稳妥路线：手动先跑通再沉淀可复用资产

### 桌面 / 系统工具
- [HomebrewApp](concepts/tool-homebrew-app.md) — macOS 原生 GUI 浏览 / 安装 / 维护 Homebrew formulae 与 casks
- [Birth](concepts/tool-birth.md) — macOS 启动项管理器：LaunchAgents / LaunchDaemons / 登录项一窗尽览
- [terminal-browser](concepts/tool-terminal-browser.md) — Electron 离屏渲染塞进 kitty graphics 终端，Agent 同标签页操作网页

### 终端 / 硬件
- [openmouse](concepts/tool-openmouse.md) — 跨品牌游戏鼠标设置统一到一份网页，插上即读 DPI / 回报率

### SEO / AI 搜索优化
- [Qiaomu SEO](concepts/tool-qiaomu-seo.md) — 装进 AI 智能体的 SEO 工作流：Google / Bing / AI Search 三块阵地，闭环

### 视频 / 内容生产
- [video-skills-toolkit](concepts/tool-video-skills-toolkit.md) — 把短视频生产沉淀成 6 个可复用 agent skills，字幕驱动流水线
- [Stickman Video Director](concepts/tool-stickman-video-director.md) — 文案 / 笔记 → 一分钟火柴人视频，分镜 + 6 段 Gemini 提示词

### UI / 文档组件
- [Brainless](concepts/tool-brainless.md) — Claude Code / Codex / Grok 终端界面做成 shadcn 组件，复制粘贴即用

### 教程 / 学习资源
- [Unpacking ChatGPT](concepts/tool-unpacking-chatgpt.md) — 中文 ChatGPT 科普系列《拆开 GPT》20 期 / 三阶段

### 跳过 / 复核（Skipped / No-op）
- QingQ77 6 条短语 + 短视频（武术九节鞭就业 / 聋的传人 / 非常想要 / AI特效火 / WTF / 基本告别摄影 / 演技炸裂）— 纯情绪反应或无关内容，按「质量门槛」跳过

## 本批新增（2026-08-06 / 2026-08-07）

### AI / Agent 生态
- [ChatGPT Video Editing Skills](concepts/tool-chatgpt-video-editing-skills.md) — 繁体中文 AI Agent 视频剪辑技能包：环境 Skill + 剪辑流水线 Skill
- [Vigla](concepts/tool-vigla.md) — 跨 Claude Code / Codex CLI / Antigravity 编程 agent 统一面板 + 授权边界 + 一键回退
- [Stella Pi Workbench](concepts/tool-stella-pi-workbench.md) — Pi 用户的桌面工作台 + 可审计本地 Agent 团队控制面
- [Frog (wevm)](concepts/tool-wevm-frog.md) — Agent 摩擦日志工具：`frog log` 入仓 → `frog publish` 提 issue → issue 关自动归档
- [Pi Bifrost](concepts/tool-pi-bifrost.md) — Pi 模型自动切换层，按任务复杂度 / 价格 / 速度 / 上下文长度路由
- [pi-working-activity](concepts/tool-pi-working-activity.md) — Pi 状态行扩展：监听工具事件 → 实时进度 + 彩蛋
- [RealReplicaBench](concepts/tool-replica-bench.md) — 阿里国际 Accio 团队的智能体业务流程度评测集：107 任务 / 4 类工具 / 干净容器 + LLM 裁判

### Pi 桌面 / 终端增强
- [Dashi Taskboard](concepts/tool-dashi-taskboard.md) — 本地优先 Codex 任务看板，可嵌 Codex 侧栏
- [ComfyUI-Spectrum-MiniMax-H3](concepts/tool-comfyui-spectrum-minimax-h3.md) — ComfyUI MiniMax H3 加速采样节点：切比雪夫岭回归跳过 transformer 求值

### Flutter / 移动 / 跨端
- [hit](concepts/tool-hit-flutter.md) — Flutter 命中区扩展示例库，遵循 Apple HIG / Material ≥44pt
- [MaidKit](concepts/tool-maidkit.md) — Flutter 跨平台 SSH 服务器管理器，零服务端安装
- [YAFA](concepts/tool-yafa.md) — 面向 Clean Architecture 新手的 .NET SRS 闪卡应用

### 本地 LLM
- [Swiftlet](concepts/tool-swiftlet.md) — Apple 设备上流式运行 35B / 80B Qwen MoE，峰值内存 2.6GB / 4.3GB

### MCP 工具
- [gmail-mcp](concepts/tool-gmail-mcp.md) — 把 Gmail 接到 Claude 等 MCP 客户端，自托管 Cloudflare Worker

### 远程终端 / SSH
- [Remux](concepts/tool-remux-ios.md) — iOS 原生 tmux 远程管理：Ghostty 渲染 + 直连 SSH + iOS Keychain 存密钥

### 怀旧 / 玩具
- [zhuzhiliao（竹知了）](concepts/tool-zhuzhiliao.md) — 单文件零依赖 HTML 还原竹知了玩具，断网可玩

### 跳过 / 复核（Skipped / No-op）
- Wen_Zw RT @QingQ77「Qwen MoE 流式」Swiftlet (2085174723466666322) — 与同日主帖重复，原始来源已入 `tool-swiftlet.md`，按「概念已存在且资料无新增信息」跳过
- QingQ77 8 条短语 + 短视频 / 图片（好玩刺激 / DIY灭火器 / 仙王裹尸布 / 前30秒泪崩 / 男人的玩具 / 你儿子香晕 / 雷霆大嘴鱼 / 大飞碟）— 纯情绪反应或无关内容，按「质量门槛」跳过

## 本批新增（2026-08-07）

### AI / Agent 生态
- [RepoPilot](concepts/tool-repopilot.md) — 把软件项目从需求到验收交给模拟产品 / 架构 / 开发 / 测试等角色的 LangGraph Agent 协作体跑完
- [Codex Standard Devflow](concepts/playbook-codex-standard-devflow.md) — 把 Codex 跑大型项目拆成阶段管线 + G0–G5 五道门禁，装成 skill 复用
- [oh-my-cli](concepts/tool-oh-my-cli.md) — Node.js 22 + TS + ESM 写的小型代码智能体，OpenAI 兼容，自带工作区隔离
- [Liyuan（梨园）](concepts/tool-liyuan.md) — AI Agent 架构重构角色扮演：记忆账本 + 决策卡 + 自建面板 + 世界线存档
- [Human Writing Skill](concepts/playbook-human-writing.md) — 把「去掉 AI 味」做成 Agent skill，固化判断 / 节奏 / 口吻

### 本地 LLM / 推理
- [Ghostlink](concepts/tool-ghostlink.md) — Rust 写的分布式 LLM 推理平台，自动发现局域网异构设备，llama.cpp RPC 拼出集群
- [《深入理解 AI Agent》（chemark 版）](concepts/note-ai-agent-book-chemark.md) — 与 bojieli 同主题、同公式的另一份中文 AI Agent 开源电子书

### 桌面 / 系统工具
- [Ghostty Studio](concepts/tool-ghostty-studio.md) — macOS 上的 Ghostty 可视化配置工具（Tauri + TS），自动定位配置 + 视觉项上下文预览
- [Salience](concepts/tool-salience-macos.md) — macOS 桌面应用，跟踪 git 把 PR / 工单 / CI / 容器 / 部署连成图，按紧急度生成 situations 提醒

### 浏览器 / Web 工具
- [WebChat](concepts/tool-webchat.md) — 去中心化浏览器扩展，把任意网页变成公共聊天室，消息走 WebRTC 点对点加密
- [macOS Web](concepts/tool-macos-web.md) — 一个 HTML 文件在浏览器里复刻 macOS 桌面：窗口管理 + Dock + 菜单栏 + 30 个应用
- [Sparkfetch](concepts/tool-sparkfetch.md) — 把任意 URL 的杂乱 HTML 转成干净、带元数据的 Markdown / JSON / 纯文本
- [Deepclone Website](concepts/tool-deepclonewebsite.md) — 任务式全自动网站克隆：真实浏览器登录 + 离线重建 + AI 逆推四份 Markdown 文档

### 终端 / 开发者工具
- [Postcat](concepts/tool-postcat.md) — Rust + ratatui 写的终端 HTTP 调试 TUI，SSE / 分块响应实时绘制

### 邮件 / 自托管
- [Mailworker](concepts/tool-mailworker.md) — Cloudflare Workers 上的自托管邮件运行时：REST 发件 + CLI 收件 + 关键发送人批准
- [iCloud Create Workbench](concepts/tool-icloud-create-workbench.md) — 自建控制台批量管理 iCloud 隐藏邮箱，靠 Cookie 自动驱动

### 跳过 / 复核（Skipped / No-op）
- QingQ77「竹知了更新，好好好。」+ 视频 (2085555538461589755) — 短语 + 短视频，纯情绪反应，按「质量门槛」跳过
- QingQ77「3D加速设计业」+ 视频 (2085585057083978062) — 三字短语 + 短视频，无可提取信息，按「质量门槛」跳过
- QingQ77「发生肾么事了😅」+ 视频 (2085706803791446247) — 短语 + 短视频，纯情绪反应，按「质量门槛」跳过

## 本批新增（2026-08-08，断链修复 stub）

为修复 `inbox/_broken-links.md` 校验器列出的 22 条断链，新建 22 个 stub 概念。

### 工具（Tools）
- [HTTrack](concepts/tool-httrack.md) — 经典离线整站镜像工具
- [Firecrawl](concepts/tool-firecrawl.md) — 面向 AI / RAG 的网页抓取清洗 SaaS
- [llama.cpp](concepts/tool-llama-cpp.md) — 本地 LLM 推理引擎
- [Ghostty](concepts/tool-ghostty.md) — 高性能终端模拟器
- [SimpleLogin](concepts/tool-simplelogin.md) — 开源邮件别名服务
- [Win11 Web](concepts/tool-win11-web.md) — 单 HTML 文件复刻 Win11 桌面
- [Windows 98 in Browser](concepts/tool-win98-browser.md) — 浏览器内复刻 Win98 桌面
- [Resend](concepts/tool-resend.md) — 开发者事务邮件 API
- [Cloudflare Workers](concepts/tool-cloudflare-workers.md) — 边缘无服务器计算平台
- [Codex CLI](concepts/tool-codex-cli.md) — OpenAI 终端 AI 编码 Agent
- [HTTPie](concepts/tool-httpie.md) — curl 的现代友好替代
- [Bruno](concepts/tool-bruno.md) — 开源本地优先 API 客户端
- [LangGraph](concepts/tool-langgraph.md) — LangChain 的 Agent 编排框架
- [GitButler](concepts/tool-gitbutler.md) — 虚拟分支 Git 桌面客户端
- [Jina Reader](concepts/tool-jina-reader.md) — URL → Markdown 在线服务
- [Briar](concepts/tool-briar.md) — 去中心化加密消息应用

### 术语（Terms）
- [Apple Hide My Email](concepts/term-apple-hide-my-email.md) — iCloud+ 内置隐私邮箱别名
- [Story Engine](concepts/term-story-engine.md) — 决策卡 / 世界线驱动的叙事引擎总称
- [WebRTC](concepts/term-webrtc.md) — 浏览器原生 P2P 实时通信协议

### 笔记（Notes）
- [Single File Web Apps](concepts/note-single-file-web.md) — 无构建 / 无框架 / 单文件 Web 项目风格合集
- [Markdown Fetch Protocol](concepts/note-markdown-fetch-protocol.md) — 把 URL 抽成 Markdown 作为 AI 友好中间表示的思路

## 本批新增（2026-08-08）

### 前端 / 设计资源
- [Kage (MengTo)](concepts/tool-kage-mengto.md) — MengTo 开源「3D 滚动世界」landing page，< 1MB three.js

### AI / Agent 生态
- [trycompai/crm](concepts/tool-trycompai-crm.md) — AI Agent 驱动的 CRM，研究预算耗尽自停
- [OpenChatCut](concepts/tool-openchatcut.md) — 对话式 AI Agent + 多轨时间线同一本地视频工程

### 桌面 / 系统工具
- [Loopweek](concepts/tool-loopweek.md) — Android 极简周待办，一屏 7 天、零账号零追踪
- [大肥鱼宠物](concepts/tool-dafeiyu-pet.md) — DeepSeek 二创透明桌面宠物
- [clabar](concepts/tool-clabar.md) — macOS 菜单栏 Claude 用量 + 会话状态监控

### Skills / 内容 / 营销
- [小马杜蕾斯文案 Skill](concepts/tool-xiaoma-durex-copywriter.md) — Claude Code Skill，杜蕾斯文案方法可复用化
- [100x Learning](concepts/tool-100x-learning.md) — Agent Skills 协议的学习 / 内容 Skill

### 终端 / 系统管理
- [Tower (VPN Subscription)](concepts/tool-tower-vpn.md) — iPhone 机场订阅 / 节点本机转换
- [dotfiles-manager](concepts/tool-dotfiles-manager.md) — Rust dotfiles 同步工具
- [iGloo](concepts/tool-igloo-windows-linux.md) — Windows → Linux 现场迁移
- [zrk](concepts/tool-zrk.md) — Zig 重写 wrk2 的恒定吞吐量 HTTP 压测

### 自托管 / 工具
- [hbkit](concepts/tool-hbkit.md) — Python Synology Hyper Backup 还原工具
- [portfolio-os](concepts/tool-portfolio-os.md) — PHP + MySQL 合伙运营多站点工作台
- [LSPanel](concepts/tool-lspanel.md) — Tauri PHP 本地开发环境面板

### 物联网 / 智能硬件
- [ESP32 FluidBox](concepts/tool-esp32-fluidbox.md) — Waveshare ESP32-S3 3D 粒子流体

### 金融 / 数据
- [Valutio](concepts/tool-valutio.md) — 本地优先浏览器 PWA 个人理财

### 视频 / 影像
- [KeyboardWarrior](concepts/tool-keyboardwarrior.md) — Rust 节奏打字游戏，兼容 Clone Hero 谱面

### 阅读 / 资源
- [FDE 完整指南 (范冰)](concepts/note-fde-guidance-book.md) — 范冰公开免费电子书：硅谷 FDE 岗位研究 + 150 案例

## 本批新增（2026-08-09 断链修复）

### 工具（Tools — 补建断链 stub）
- [rclone](concepts/tool-rclone.md) — 「云存储版 rsync」，70+ 后端同步 / mount / crypt
- [Ollama](concepts/tool-ollama.md) — 基于 llama.cpp 的本地 LLM 一键启动器，OpenAI 兼容 HTTP
- [wrk2](concepts/tool-wrk2.md) — wrk 的恒定吞吐量分支，HdrHistogram 输出真实 P99
- [Locust](concepts/tool-locust.md) — Python 写用户行为的 HTTP 负载测试工具
- [k6](concepts/tool-k6.md) — Grafana Labs 现代化负载测试，JS 写场景

### 术语（Terms — 补建断链 stub）
- [three.js](concepts/term-three-js.md) — 浏览器端 3D / WebGL 事实标准底层
- [Synology Hyper Backup](concepts/term-synology-hyper-backup.md) — 群晖官方备份套件，`.hbk` 归档 + 块级去重 + 加密

### 笔记（Notes — 补建断链 stub）
- [Self-hosted 备份方案](concepts/note-self-hosted-backup.md) — 自托管备份选型参考：3-2-1 原则 / 工具矩阵 / 常见误区

### 修正（Fixed）
- `tool-kage-mengto.md` 中原本断链的 `./tool-solar-wander.md`（拼写与现有概念 `./tool-solar-wanderer.md` 不一致）已改为指向现有概念，避免重复建条

## 本批新增（2026-08-09）

### AI / Agent 生态
- [tokentab](concepts/tool-tokentab.md) — 本地 CLI 扫描 Claude Code / Codex / Cursor / Gemini CLI 会话日志，token 用量与花费按维度拆分
- [mycontext](concepts/tool-mycontext.md) — 把散落的 IM / 文档 / 日历 / 会议信息整理成 AI 直接可用的私有上下文

### 前端 / 设计资源
- [PrismSystem](concepts/tool-prism-system.md) — 「白标」设计系统，喂品牌输入自动生成全套对得上品牌调的 UI
- [react-native-jelly-tabs](concepts/tool-react-native-jelly-tabs.md) — 果冻质感 React Native 动画标签栏，可接 Expo Router / React Navigation

### 终端 / 系统 / 网络
- [sumlyzer](concepts/tool-sumlyzer.md) — npm workspace 测试增强，聚合 / fail-fast / 并发 / JUnit
- [caffyne-shell](concepts/tool-caffyne-shell.md) — Python + GTK + Fabric 写的 Wayland 桌面外壳

### 桌面 / 系统工具
- [macos-disk-cleanup](concepts/tool-macos-disk-cleanup.md) — macOS 只读磁盘扫描脚本，按危险分级列出可疑「系统资料」
- [appmop](concepts/tool-appmop.md) — macOS 终端应用 + Library 残留清理工具
- [DeskChan](concepts/tool-deskchan.md) — Windows 桌面「栅栏」工具（Fences 开源替身）
- [wfdash](concepts/tool-wfdash.md) — `/wayfinder` 任务地图的本地浏览器仪表盘

### 自托管 / 网络 / VPS
- [WARP-Manager](concepts/tool-warp-manager.md) — 纯 Bash VPS 工具，nftables TPROXY + sing-box 域名级 WARP 路由

### 编程语言 / 底层
- [asm-hall-of-shame](concepts/tool-asm-hall-of-shame.md) — xoreaxeaxeax（movfuscator 作者）的「汇编指令延迟耻辱柱」

### AI 语音 / 消息处理
- [SkipTheVoice](concepts/tool-skip-the-voice.md) — WhatsApp 语音消息转写工具，Web + CLI 双形态，自托管 Whisper

### 视觉 / 通知
- [cc-planet](concepts/tool-cc-planet.md) — 飞机横幅动画通知工具，CI/CD 与日常提醒「一眼可见」

### 成长 / 方向探索
- [becoming-lab](concepts/tool-becoming-lab.md) — 对话式 AI 工作流，把迷茫拆七种卡住状态，按三类证据形成方向假设

## 本批新增（2026-08-10）

### AI / Agent 生态
- [Lupin](concepts/tool-lupin.md) — Claude Code 整套壳借给别的模型用，MCP / Skills / CLAUDE.md / hooks 原样保留 + 会话评分
- [modeldock](concepts/tool-modeldock.md) — Codex 本地 Responses 桥，给 DeepSeek 补识图 / 语音 / 联网 / 记忆 + GPT 透传
- [codex-bridge](concepts/tool-codex-bridge.md) — 把 Codex CLI 里 ChatGPT 登录借给 Claude（gpt-image-2 出图 + GPT-5 子代理）
- [PixelVault Desktop](concepts/tool-pixelvault-desktop.md) — 复制图片自动换成托管 URL，给只收文本的云端编程 agent 看图

### 前端 / 设计 / 视觉
- [ComfyUI Cable Management](concepts/tool-comfyui-cable-management.md) — ComfyUI 节点连线的电路板式自动布线
- [Holosticker](concepts/tool-holosticker.md) — 浏览器内镭射 / 全息贴纸工作室，调箔面 + 透明 PNG 导出

### 桌面 / 系统工具
- [GitDesktop](concepts/tool-gitdesktop.md) — Tauri 2 + React 19 桌面 Git 客户端，走 gh CLI 不申请 OAuth + PR 全生命周期
- [DisplayHotKeys](concepts/tool-display-hotkeys.md) — Windows 热键切显示器分辨率 / 刷新率 / 缩放 / DPI / 方向
- [SoundWatch](concepts/tool-soundwatch.md) — Rust 终端音频诊断，十标签页 + Insights 人话建议
- [Emeraldian](concepts/tool-emeraldian.md) — Rust 写的 Obsidian 风格终端 UI，三栏 + 反向链接 + 力导向图

### 数据 / IDE / AI 创作
- [QuackWrangler](concepts/tool-quackwrangler.md) — DuckDB 内置进 VS Code 扩展，无 Python 环境跑 SQL 清洗 CSV/Parquet/JSON

### 物联网 / 智能硬件
- [Gemma Translator](concepts/tool-gemma-translator.md) — 树莓派完全离线实时语音翻译（Gemma 4 + LiteRT-LM），480x320 复古终端 UI + 3D 打印外壳

### iOS 开发 / 测试
- [location-spoofer](concepts/tool-location-spoofer.md) — iOS 定位调试代理，拦截 Apple 定位响应让 QA 不改 App 代码模拟任意坐标

### 更新（Updated）
- [Kage (MengTo)](concepts/tool-kage-mengto.md) — 补「生成式图像叠层」+「京都山寺夜间漫游」实例 + 单 HTML 无需构建

## 本批新增（2026-08-10 / 2026-08-11）

### AI / Agent 生态
- [LifeOS](concepts/tool-lifeos.md) — 给 Claude Code / Cursor 加外挂的 TELOS + 七段算法循环框架（Cortex 记忆 / Synapse 输入路由 / Pulse 守护 / 49 子技能）
- [OpenFox](concepts/tool-openfox.md) — 契约驱动的本地 Agent 框架，把验收标准当不可变契约，让 vLLM / Ollama 自己拆任务 + 跑流水线 + 反复验证
- [Pisper](concepts/tool-pisper.md) — Pi Coding Agent 的桌面 + 终端多会话并行客户端，工具 / 记忆 / MCP / 自动化统一收进本地应用
- [pi-peer](concepts/tool-pi-peer.md) — 同机多 pi 会话互相发现 + 互发纯文本消息（最多 32 KB），提供 list_peers / message_peer 两个工具
- [VibeSDK](concepts/tool-vibesdk.md) — 把"说句话生成应用"的 AI 编程平台整套开源，部署到自家 Cloudflare 账户即可跑

### 本地 LLM / 推理
- [DeepSeek SSD](concepts/tool-deepseek-ssd.md) — 让 284B 参数 DeepSeek-V4-Flash-0731 MoE 在 ~30 GB 内存的 M 系列 Mac 本地跑，路由激活的专家从 SSD 流式加载

### 桌面 / 系统工具
- [MangoDisk](concepts/tool-mangodisk.md) — macOS / Windows 磁盘清理 + 空间分析，按类扫描后用户确认再删
- [E.V. Assistant](concepts/tool-ev-assistant.md) — Python + Electron 写的 Windows 语音助手（faster-whisper + Ollama + ElevenLabs/浏览器 TTS），造型取自《蜘蛛侠》新片 E.V.
- [InkBoard](concepts/tool-inkboard.md) — 墨水屏平板专用 HOME 桌面，纯黑白 / 零动画 / 大触控 / 手动翻页
- [WorkBuddy-Dream-Skin](concepts/tool-workbuddy-dream-skin.md) — 本机回环 CDP 注入 CSS 与主题变量给 WorkBuddy 桌面换肤，不碰源文件
- [LaunchCorner](concepts/tool-launchcorner.md) — 免费开源 SwiftUI 工具，把屏幕四角变成应用启动开关

### 终端 / 系统 / 网络
- [openstack-zsh-plugin](concepts/tool-openstack-zsh-plugin.md) — Oh My Zsh 插件，把 OpenStack CLI 日常做成 fzf 交互选择（切云 / venv / 模糊搜 VM 再 SSH）

### 配置 / 系统管理
- [Eljangus NixOS](concepts/tool-eljangus-nixos.md) — NixOS + Nix-Darwin 统一配置仓库，一台机器按需切 Niri / Plasma 6 / GNOME 三套桌面

### 文档 / Office 自动化
- [OfficeCLI](concepts/tool-officecli.md) — Word / Excel / PowerPoint 的读 / 写 / 编辑压成一行命令，跨 Linux / macOS / Windows

### 金融 / 行情聚合
- [MarketingDashboard](concepts/tool-marketingdashboard.md) — 把指数 / 商品 / 美债 / 板块 / 资金流塞进同一浏览器页面，后端 Node 代理聚合公开接口，零数据库

### 浏览器扩展 / 隐私
- [BlackBar](concepts/tool-blackbar.md) — Chrome 截图扩展，截图前先扫整页 DOM，把凭证 / 卡号 / 邮箱 / 地址遮成黑条

### 编程语言 / 底层
- [binja-diff](concepts/tool-binja-diff.md) — Binary Ninja 插件，QBinDiff 引擎做两二进制并排对比，CFG / 汇编 / LLIL / MLIL / HLIL 五层差异展示

### 跳过 / 复核（Skipped / No-op）
- Wen_Zw RT @QingQ77 marketingdashboard (2087095424025022795) — 同源主帖 2087089888046789080 已入 `tool-marketingdashboard`，按「复核，无变更」处理
- QingQ77「艺术已成」+ 视频 (2087191809822724520) — 情绪短语 + 短视频，按「质量门槛」跳过
- QingQ77「好设计，借不走的304不锈钢梯子👍」+ 视频 (2087120929893822855) — 情绪短语 + 短视频，按「质量门槛」跳过
- QingQ77「纸模 M1911，真是有能人啊。」+ 视频 (2087005536256725484) — 情绪短语 + 短视频，按「质量门槛」跳过
- QingQ77「我可以玩一天」+ 视频 (2087172200269013328) — 情绪短语 + 短视频，按「质量门槛」跳过

## 本批新增（2026-08-11 / 2026-08-12）

### AI / Agent 生态 / Skills / MCP 工具
- [Qwen-MM-Plugins](concepts/tool-qwen-mm-plugins.md) — 通义千问多模态插件仓库，skill + MCP server 形式给 Claude Code / Codex 加图像/音频/视频能力
- [Voxel Icon](concepts/tool-voxel-icon.md) — Codex Skill 形态的体素图标生成器，低密度等距 + 4 帧物理循环

### 数据库 / 数据工具
- [LakeDB](concepts/tool-lakedb.md) — 本地优先桌面数据库客户端（MySQL/MariaDB/SQLite），AI 出 SQL 永远先审后跑

### 前端 / 设计 / 视觉
- [expo-content-transition](concepts/tool-expo-content-transition.md) — Expo / React Native 数字平滑过渡库，字符级滚动 / 缩放 / 模糊 / 错峰
- [quickdraw](concepts/tool-quickdraw.md) — MIT 许可无限画布白板 SDK，tldraw 的开源替代，可嵌 React / React Native / 纯 JS

### 桌面 / 系统工具
- [NIGHTRUN](concepts/tool-nightrun.md) — Rust UEFI bare-metal LLM 运行时，x86_64 从 USB / 树莓派 5 从 SD 卡启动，开机即聊天
- [SSHBool](concepts/tool-sshbool.md) — Tauri v2 + Rust 桌面工作区，SSH / SFTP / 远程编辑 / 服务器监控 / 数据库查询合一
- [Ukishima](concepts/tool-ukishima.md) — Hyprland 动态岛式控制中心，启动器 / 日历 / 媒体 / 混音 / WiFi 等面板合一
- [Cyclop](concepts/tool-cyclop.md) — MacBook 刘海悬停展开的工具面板，原生 SwiftUI、零系统权限

### 远程 / 文件系统
- [CloudFolder](concepts/tool-cloudfolder.md) — Rust 写 Windows 工具，rclone SFTP + WinFsp 把远端 GPU 目录挂载成本地路径

### 密码 / 隐私
- [Zero Password Manager](concepts/tool-zero-password-manager.md) — 用户自托管 + 客户端加密，服务器在密码学层面对保险库完全不可见
- [blueferry](concepts/tool-blueferry.md) — Linux 桌面蓝牙直连 iPhone 收发 iMessage / 短信，无需 Mac / iCloud / 云服务

### 写作 / 内容生产
- [dashiai-ppt-skill](concepts/tool-dashiai-ppt-skill.md) — 网页版 PPT 编辑器 Skill，每页可改后导出可编辑 PPTX，1020 版式 + SWOT/波特五力/PEST
- [GetbijiEx](concepts/tool-getbijiex.md) — 把 Get笔记订阅博主笔记一键导出 Markdown + Agent skill

### 知识管理 / 个人工具
- [chat-later](concepts/tool-chat-later.md) — 聊天时间线回顾工具，自动捞一年没人回看的约定/反馈/没下文，每条钉回原始消息 ID

### Web 模板 / 站点搭建
- [Mkdirs](concepts/tool-mkdirs.md) — Next.js 目录网站模板，TS + Tailwind，AI 提交 / 支付 / 认证开箱即用

### 监控 / 仪表盘
- [pico-pu-api-control](concepts/tool-pico-pu-api-control.md) — 系统托盘 API 余额仪表盘，多 AI 服务商余额 / 剩余比例本地轮询

### 跳过 / 复核（Skipped / No-op）
- Wen_Zw RT @scottymatt 「this is sick」(2087283131640611060) — 纯审美欣赏 + 链接，按「质量门槛」跳过
- Wen_Zw RT @nixfutures 「traders.. this website is beautiful」(2087284775874945454) — 纯审美欣赏 + 链接，按「质量门槛」跳过
- QingQ77「真佩服玉雕师变废为宝的本事」+ 视频 (2087532353736651209) — 情绪短语 + 短视频，按「质量门槛」跳过
- QingQ77「哈哈哈」+ 视频 (2087553103927394552) — 纯笑声，按「质量门槛」跳过
- QingQ77「太勇了」+ 视频 (2087400216408559961) — 情绪短语 + 短视频，按「质量门槛」跳过
- QingQ77「翻过来的时候，小脑萎缩了一下。」+ 视频 (2087365445473206565) — 情绪反应 + 昆虫雕塑展示，按「质量门槛」跳过

## 本批新增（2026-08-13）

### AI / LLM 工具
- [gpt56_api_detector](concepts/tool-gpt56-api-detector.md) — 本机两层检测识别「中转 API 实际跑的模型」并输出七种结论报告
- [claudish-to-english](concepts/tool-claudish-to-english.md) — Claude Code 插件用本地 ollama 把消息实时重写成通俗英语，仅改屏幕、会话与推理过程保持原样
- [attention-span](concepts/tool-attention-span.md) — Claude Code 插件提供三种「输出样式」，仅改说话方式不改动编码行为
- [repowise](concepts/tool-repowise.md) — 给 AI 编码代理预建代码库持久索引，省去每次 grep / 重读 / 重熟悉
- [relmio](concepts/tool-relmio.md) — OpenAI 兼容 API 边车复用 ChatGPT / Codex 登录态，自托管 n8n 用占位 key 调模型免另购 Platform 额度

### 嵌入式 / 存储
- [lkv](concepts/tool-lkv.md) — 嵌入式 KV 用哈希表换读性能与零拷贝查找，比 LMDB / RocksDB 更轻

### 硬件 / 物联网
- [Apollo (ESP32 语音助手)](concepts/tool-apollo-esp32-voice.md) — ESP32 桌面装置 + Cloudflare Workers 云端语音助手
- [xyprt_android](concepts/tool-xyprt-android.md) — Android 蓝牙连学科网错题小印 X1 热敏机打印文字 / 图片 / PDF

### 前端 / Web
- [next16-calendar](concepts/tool-next16-calendar.md) — Next.js 16 参考实现：日历 + 预约应用把缓存 / 预取 / 即时导航新特性串成能跑能测的样例

### Obsidian 生态
- [Obsidian Fileclass](concepts/tool-obsidian-fileclass.md) — Obsidian 插件把 frontmatter 属性定义成类型 schema，字段输入变下拉 / 日期选择器并自动校验

### macOS / 系统工具
- [Sift (macOS)](concepts/tool-sift-macos.md) — macOS 本地应用集中存储分析 / 清理 / 卸载 / 网络排查六类操作

### Home Assistant
- [mw-ha-humidifier-card](concepts/tool-mw-ha-humidifier-card.md) — Home Assistant Lovelace 卡片把加湿器与功率计智能插座合并到一张卡片

### 阅读 / 内容
- [kagi-news](concepts/tool-kagi-news.md) — 把 Kagi News 新闻流渲染成可离线阅读的「当日报纸」，支持整页滚动与杂志双页翻页

### 影视后期
- [conform-desktop](concepts/tool-conform-desktop.md) — 音频对轨工具按参考视频时间轴自动识别剪辑 / 插入 / 删减 / PAL 变速 / 3:2 电视电影痕迹，输出 FLAC + 质量报告

### 网盘 / 自动化
- [Ydisks 批量转存助手](concepts/tool-ydisks-drive-assistant.md) — 夸克 / 百度 / 迅雷网盘分享链接批量转存 + 批量生成小红书抖音短链

### CI / CD
- [cloudflare/ci](concepts/tool-cloudflare-ci.md) — Cloudflare 官方开源 CI 引擎，流水线跑在自家 Workflows + Sandbox 上免运维 runner 集群

### 跳过 / 复核（Skipped / No-op）
- Wen_Zw RT @midudev gooey liquid UI effect (2087646198610243950) — 单特效库，无概念 / 项目 / 方法增量，按「质量门槛」跳过
- Wen_Zw RT @cnemalek kinetics 144 motion effects (2087818255952162889) — 已有 [`tool-kinetics`](concepts/tool-kinetics.md) 覆盖，重复跳过
- QingQ77「变身赛罗」+ 视频 (2087821783982612919) — 角色扮演短视频，按「质量门槛」跳过
- QingQ77「这些神对话😅」+ 梗图 (2087744764083118272) — 纯情绪反应 + 梗图，按「质量门槛」跳过
- QingQ77 pyroclear ASCII 火焰清屏 (2087850650852032717) — Rust 玩具级清屏动画，按「质量门槛」跳过

## 本批新增（2026-08-14）

### AI / Agent 生态
- [codex-host](concepts/tool-codex-host.md) — 把 Codex Desktop 当宿主界面，CDP 注入 Agent 选择器，CLI Shim 接 app-server，支持 Pi / Claude Code 等多 Agent 后端
- [InsightForge](concepts/tool-insightforge.md) — 本地多 Agent 协作 AI 视频成片引擎，Idea/Script/Novel → 叙事 / 角色 / 分镜 / 镜头 / 关键帧 / 视频片段
- [dscode](concepts/tool-dscode.md) — 以 DeepSeek 为默认模型、本地优先的多模型编码智能体运行时，可按仓库任务切 DeepSeek / Codex / OpenAI / Anthropic
- [HeyAgent](concepts/tool-heyagent.md) — 本地桌面 Agent：动鼠标键盘 / 开应用 / 控浏览器 / 建 Google 文档，Telegram 远程指令

### AI 视频 / 游戏测试
- [wai-play](concepts/tool-wai-play.md) — 让 AI 在真实浏览器里自动试玩网页游戏，输出可复现的问题证据与修复建议

### 前端 / 设计 / 视觉
- [UI SFX](concepts/tool-uisfx.md) — 936 个免费开源 UI 音效，12 个语义包，开箱即用
- [smoothui](concepts/tool-smoothui-react.md) — educlopez 开源的 React 动画组件合集，复制粘贴即用，免配 Framer Motion
- [GPUI Component](concepts/tool-gpui-component.md) — Longbridge 开源 Rust UI 组件库，WASM 浏览器可跑，DataTable Demo 100 万行流畅
- [everycube](concepts/tool-everycube.md) — 把魔方 4.3×10¹⁸ 种可达排列做成可滚动索引，滚动到任意一格即时 3D 渲染
- [china-antique-maplibre](concepts/tool-china-antique-maplibre.md) — 中国历史地图 MapLibre 渲染栈，复古羊皮纸风格 / 卫星底图 / 地形阴影 / 水域叠加

### 终端 / 编辑器
- [luna.nvim](concepts/tool-luna-nvim.md) — Neovim 暗色配色主题，纯黑灰阶底 + 4 种冷暖强调色，夜间不刺眼

### 桌面 / 系统工具
- [orbit-desktop](concepts/tool-orbit-desktop.md) — 本地优先 macOS 工作区，习惯 / 想法 / 任务 / 画布 / 人脉跟进收进一处，SwiftUI 原生复刻 React Flow
- [flyingmouse-format](concepts/tool-flyingmouse-format.md) — 离线文件格式转换，FFmpeg / LibreOffice / Poppler / Tesseract 内置，覆盖图片 / 文档 / 表格 / PPT / PDF / 音视频 / WPS

### 写作 / 知识库
- [distill-novels](concepts/tool-distill-novels.md) — 把多本小说拆成可复用的写作知识库（世界观 / 人物 / 情节 / 文风），AI 写作助手 Skill 形式

### 网络 / VPS / 运维
- [tcpfit](concepts/tool-tcpfit.md) — Linux VPS TCP 调优脚本，自动测速找丢包点，避开「买了 500M 跑不满」的尴尬
- [checkfleet](concepts/tool-checkfleet.md) — 单静态 Go 二进制的领域知识运维检查（TLS / NATS / PG 复制槽），目标机无 agent 无守护
- [orbien](concepts/tool-orbien.md) — Rust + Tokio 内网穿透工具，单二进制 ~5MB，TCP / QUIC / KCP / WebSocket 多协议

### 3D 打印 / 工程
- [gfty](concepts/tool-gfty.md) — 用 CLI 定义并批量生成 Gridfinity 收纳盒 / 底板 / 标签 / 边框，对接 Onshape API 导出 STEP

### Web 分析 / 隐私
- [openanalytics](concepts/tool-openanalytics.md) — 隐私优先 Web 分析，无 Cookie / 无跨站画像，支持自托管 + 收入归因 + MCP

### 邮件 / 协作
- [hqbase](concepts/tool-hqbase.md) — 部署在 Cloudflare 账户里的共享邮箱工作台，OAuth 保护的远程 MCP 服务器

### 跳过 / 复核（Skipped / No-op）
- Wen_Zw RT @abderizik @dwhitedesign wiredjs showcase (2088071111661768832) — 一句话「This may help」+ 一个链接，无概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「不用电池？」+ 视频 (2088103188876714100) — 一句短语 + 短视频，纯情绪反应，按「质量门槛」跳过
- QingQ77「中国小孩防近视，这叫拉远镜。」+ 视频 (2088045198068854860) — 一句短语 + 短视频，无可提取的工具 / 概念 / 项目信息，按「质量门槛」跳过
- QingQ77「3D 渲染 2D😍」+ 视频 (2088126791777227119) — 一句短语 + 短视频，纯情绪反应，按「质量门槛」跳过
- QingQ77 空标题 + 视频 (2088265189372408034) — 无文字内容，仅短视频，按「质量门槛」跳过
- QingQ77 空标题 + 视频 (2088238501674520772) — 无文字内容，仅短视频，按「质量门槛」跳过
- QingQ77「一生如牛不得闲，闲时已与山共眠。」+ 视频 (2088279682173251714) — 抒情诗句 + 短视频，纯情绪 / 无信息量，按「质量门槛」跳过

## 本批新增（2026-08-15）

### AI / Agent 生态 / 多代理编排
- [pi-omo-slim](concepts/tool-pi-omo-slim.md) — 给 Pi 编码助手配的 OMO-slim 风格多代理编排（Orchestrator + 6 个专精代理），不 fork 上游
- [pi-fabric](concepts/tool-pi-fabric.md) — Pi 扩展，把多工具调用合成 TypeScript 程序由 `fabric_exec` 执行，运行前过类型检查
- [axern](concepts/tool-axern.md) — AI agent 代码执行沙箱：不可信代码进 `runsc`、可信服务放 `runc`，统一资源 / 生命周期接口

### Pi / Codex 生态扩展
- [ASu-skills](concepts/tool-asu-skills.md) — Codex 中文求职工作流插件：4 个斜杠命令（`/contributor` / `/asu` / `/resume` / `/offer`）
- [dsh-diff-viewer](concepts/tool-dsh-diff-viewer.md) — DSH 的纯插件，把 write / edit 的 diff 渲染换成 PiUI 风格，靠 `ui-tool keyed` 接管
- [GrokBuild](concepts/tool-grokbuild-openai-gateway.md) — Grok Build CLI 接入任意 OpenAI 兼容网关的配置模板 + 交互式安装脚本

### 知识 / 写作 / 创作
- [DeepWrite](concepts/tool-deepwrite.md) — 本地 AI 写作工作台：模型 / 提示词 / 技能 / 素材 / 文稿组织在同一桌面，AI 真改磁盘文稿
- [pi-agent-core 中文架构书](concepts/note-pi-agent-core-book.md) — 源码出发解读 pi-agent-core 架构，每处论断带文件:行号引文

### macOS / Windows 桌面工具
- [local-ops](concepts/tool-local-ops.md) — macOS 本地服务 / 项目命令 / 一次性任务指挥台，2 秒轮询端口与服务
- [Celldock for Mac](concepts/tool-celldock-for-mac.md) — QDC507 蜂窝模块客户端：短信 / 通话 / 录音 / SOCKS5 代理共享
- [Shrinkit](concepts/tool-shrinkit.md) — macOS 屏幕录制 ffmpeg 压缩 + 加速，丢进文件夹或右键出 `.mp4`
- [DeskBuddy](concepts/tool-deskbuddy.md) — Mac 菜单栏控制 IKEA IDÅSEN 等蓝牙升降桌，预设高度 + 坐站提醒
- [bow-git-vault](concepts/tool-bow-git-vault.md) — Windows Git Electron GUI：克隆 / 状态 / 暂存 / 提交 / 拉取 / 推送 / 分支一键
- [EasyAlias](concepts/tool-easyalias.md) — 终端别名 GUI 管理，自动生成 shell alias / function / `.cmd` / PowerShell

### 自托管 / 隐私优先
- [iCloud Prime](concepts/tool-icloud-prime.md) — 本地「隐藏我的邮箱」控制台：Web + API + Windows 便携版 + 多 iCloud 账号
- [Machinexis](concepts/tool-machinexis.md) — 设备 → 传感器 → 规则 → 告警 → 工单多租户平台
- [PocketWatch](concepts/tool-pocketwatch.md) — 自由职业者自托管时间记录：JSON 存储 + PDF 直出 + 零网络请求

### 内容创作 / 排版
- [md-wechat](concepts/tool-md-wechat.md) — 公众号 Markdown 排版工具：左侧编辑 / 右侧预览 / 一键复制富文本

### 本地 LLM
- [Qwen3.8-27B Unsloth GGUF](concepts/tool-qwen3-8-27b-unsloth.md) — Unsloth 动态 GGUF 量化，17GB 内存即可本地跑 27B；同尺寸段最强

### 终端 / 编辑器
- [cendre](concepts/tool-cendre-nvim.md) — Neovim 木柴光谱配色主题，5 色相来自燃烧木柴实测光谱，终端配色自动同步

### 跳过 / 复核（Skipped / No-op）
- QingQ77「她会不会吃一嘴沙啊」(2088477366809133304) — 情绪反应短句 + 视频，无概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「重新定义梳子🤣」(2088496657507754331) — 表情包反应，无概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「好玩」(2088560163901079894) — 情绪短句 + 视频，无概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「cool 1300 颗霓虹粒子组成的时间」(2088626310264533444) — 视觉短句 + 视频，无概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「iOS 装修风格😅」(2088428530480939057) — 表情反应短句 + 视频，无概念 / 工具 / 项目信息，按「质量门槛」跳过

## 本批新增（2026-08-16）

### AI / Agent 生态 / 编码助手
- [fob (Secure Enclave SSH)](concepts/tool-fob-ssh-secure-enclave.md) — Mac 物理钥匙扣：SSH 私钥锁 Secure Enclave + Touch ID 现场授权 + 主机指纹绑定
- [opencode-senses](concepts/tool-opencode-senses.md) — 给纯文本 OpenCode 编码 agent 加本地视觉层（OCR / 目标定位 / 颜色），零 API key
- [HERO-Anti-OverDefense](concepts/tool-hero-anti-overdefense.md) — 治 AI 编码助手过度防御的规则块
- [rakazo (akazo)](concepts/tool-rakazo.md) — Cursor + Grok 4.6 构建的开源 Grok Bot 替代品，一库覆盖 Web / Electron / 移动

### DeepSeek Harness (DSH) 生态扩展
- [deepseek-harness-desktop (steven-kid)](concepts/tool-deepseek-harness-desktop.md) — DSH 官方 Web 界面打包成跨平台桌面应用
- [DeepSeek-Harness-Desktop (sleep2agi)](concepts/tool-deepseek-harness-desktop-shell.md) — dsh 命令行运行时套 macOS / Windows 桌面外壳
- [dsh-desktop (bruc3van)](concepts/tool-dsh-desktop.md) — DSH 官方 Web UI 原样装进原生桌面窗口
- [dsh-vision-toolkit](concepts/tool-dsh-vision-toolkit.md) — 让纯文本 DeepSeek 模型在 DSH 里做视觉任务
- [dsh-visualize](concepts/tool-dsh-visualize.md) — DSH 插件：把模型输出就地渲染成交互式可视化卡片
- [dsh-auto-continue](concepts/tool-dsh-auto-continue.md) — DSH 会话被网络错误打断时自动续写
- [dsh-agent-teams](concepts/tool-dsh-agent-teams.md) — DSH 多代理插件：单个会话升格「队长」+ 持久子代理
- [dshfind](concepts/tool-dshfind.md) — DSH 学习与分享社区站点（原理课程 / 插件市场 / 最佳实践）
- [dsh-deep-whale](concepts/tool-dsh-deep-whale.md) — DSH Web GUI 鲸鱼娘主题皮肤
- [deepseek-whale-girl-icon](concepts/tool-deepseek-whale-girl-icon.md) — DSH 桌面端鲸鱼娘主题应用图标
- [deepseek-harness-orange-book](concepts/note-deepseek-harness-orange-book.md) — DSH 开源 24 小时写出来的电子书

### macOS / 桌面工具
- [OceanPet](concepts/tool-oceanpet.md) — 角色化 AI 桌宠，常驻 macOS 桌面，会散步、看鼠标、用角色性格陪聊

### 前端 / UI 设计资源
- [drawably](concepts/tool-drawably.md) — 手绘风 UI 控件库，每次挂载自动重画笔触，4 KB 零依赖
- [amicro](concepts/tool-amicro.md) — 免费开源 React UI 库（图表 / Loader / 组件）
- [shadcndashboard](concepts/tool-shadcndashboard.md) — shadcn/ui + Base UI + Next.js + Tailwind v4 开箱即用的 admin dashboard kit

### 音频 / 媒体
- [procedural-sounds](concepts/tool-procedural-sounds.md) — 程序化音效生成工具

### 平台参考 / 目录
- [github-profile-achievements](concepts/tool-github-profile-achievements.md) — GitHub 官方未发布的成就徽章全清单参考目录

### 跳过 / 复核（Skipped / No-op）
- QingQ77「所以这恐怖片主角非常弱小...」(2088794262112698766) — 影视评论 + 短视频，按「质量门槛」跳过
- QingQ77「豆包以为你中邪了...」(2088827840771043337) — 情绪反应 + 短视频，按「质量门槛」跳过
- QingQ77「无敌预制画，2026年还学美术吗。」(2089001274796904784) — 情绪反应 + 短视频，按「质量门槛」跳过
- Wen_Zw「微软是真的屎...」(2088870214440239327) — 纯情绪发泄，按「质量门槛」跳过

## 本批新增（2026-08-17）

### AI / Agent 生态 / 编码助手
- [codex-trajectory](concepts/tool-codex-trajectory.md) — 把本地 Codex 任务日志解析成结构化事件账本 + 交互时间线，只读、隐私友好
- [ompweb](concepts/tool-ompweb.md) — 给 oh-my-pi 编码代理配的本地 Web 控制台
- [agent-vision-toolkit](concepts/tool-agent-vision-toolkit.md) — 给纯文本 coding agent 配眼睛：CLI + skill + 本地透明代理
- [Argo](concepts/tool-argo-search.md) — 给 AI Agent 用的多语言搜索工具，输出「证据候选 + 可信度评分」
- [OPC-Nexus](concepts/tool-opc-nexus.md) — 单人公司 / 独立开发者用的本地优先桌面 AI Agent 管理器

### AI 编码 IDE / 工作台
- [Calyx](concepts/tool-calyx.md) — 原生 macOS 终端应用，并行监督多个编码 AI agent

### 前端 / 设计资源
- [md2hd](concepts/tool-md2hd.md) — Markdown 笔记文件夹 → 浏览器交互式超图（frontmatter 变节点、wikilink 变连线）
- [pdfcn](concepts/tool-pdfcn.md) — shadcn 团队出的开源 React PDF 组件库
- [2D-to-3D Voxelizer](concepts/tool-2d-to-3d-voxelizer.md) — 把 2D 像素画升维成 3D 体素艺术并导出 .obj
- [iconcreator](concepts/tool-iconcreator.md) — 免费在线动画 / 3D 图标设计器

### 桌面 / 系统工具
- [Aurora Audio Studio](concepts/tool-aurora-audio-studio.md) — Windows 本地音频 AI 一体化工作台（七种功能合一 GUI）

### 金融 / 数据
- [GraphShield-Fraud](concepts/tool-graphshield-fraud.md) — 时序图欺诈检测项目，严格时间切分下比较非图基线与因果 Temporal GraphSAGE

### 后端 / 部署
- [Sevalla](concepts/tool-sevalla.md) — 应用部署托管平台，免去管理基础设施的负担

### 阅读 / 资源
- [scan-to-practice](concepts/tool-scan-to-practice.md) — 扫描版 PDF / 练习册 / 题库照片 → 可答题交互产品的端到端操作手册

### 跳过 / 复核（Skipped / No-op）
- Wen_Zw「noice 69」(2089089056424808720) — 情绪化感叹词 + 截图，按「质量门槛」跳过
- QingQ77「未来 AI 时代，让自己独处的能力」(2089365775832486277) /「真人版影子传说」(2089212854864097726) /「微观世界里的食草动物」(2089305661100437516) — 短语 + 短视频，纯情绪反应，按「质量门槛」跳过
- QingQ77 yueyuan-bazi 八字命理 (2089207089138675973) — 命理 / 玄学应用与本知识库主线不符，按「说不清理由就别链」原则跳过
- QingQ77 cyber-crowd 浏览器生成艺术 (2089376706469769347) — 纯艺术项目无可复用知识，按「说不清理由就别链」原则跳过
- QingQ77 whale-girl DSH 桌宠 (2089237791062609996) / k4 Hyprland 状态栏 (2089268494063857993) — 定位过窄与已有同类项目重叠，按「不为了凑数而链接」原则跳过

## 本批新增（2026-08-18）

### AI / Agent 生态 / 编码助手
- [comet (zeronsh)](concepts/tool-comet-zeronsh.md) — 把 Claude Code / Codex / Cursor 等编码 agent 收拢到本机控制：会话存本机、免账号、按需多设备同步
- [nopus (Vistyy)](concepts/tool-nopus.md) — 编码助手回复的抽象度检测器：按词频 / 名词堆叠 / 短语密度打分，超阈值自动重写
- [ScanSci Pi](concepts/tool-scansci-pi.md) — 科研引用核对工作流：每一步钉原文，证据不足即声明，不编造出处

### DeepSeek Harness (DSH) 生态扩展
- [dsh-desktop (dataelement)](concepts/tool-dsh-desktop-dataelement.md) — Electron 封装 DSH：启动时自动拉 Harness 子进程 + 随机端口 + 持久化配置
- [dsh-tianshu-tui (huiliyi37)](concepts/tool-dsh-tianshu-tui.md) — DSH 的交互式 TUI：自研 ANSI 渲染 + TDD / 证据门 / 视觉图像模块工作流
- [dsh-market](concepts/tool-dsh-market.md) — DSH 内置插件市场：800+ 社区插件、分类筛选 + 星数 / 新旧排序、双语说明
- [dsh-peer-link (czm15053)](concepts/tool-dsh-peer-link.md) — Unix socket 把 DSH ↔ Claude Code 等本机 agent 串成可互发消息的协作网络
- [deepseek-harness-studio (fufankeji)](concepts/tool-deepseek-harness-studio-fufankeji.md) — DSH 零代码桌面端：一键安装 / 启停 / 管插件，内置图像理解给纯文本模型补眼睛

### 桌面 / 系统工具
- [btop-quattro-plugin](concepts/tool-btop-quattro-plugin.md) — Omarchy 顶栏的 btop 摘要：悬停看 CPU/内存/GPU/温度，单击聚焦 btop 主窗口
- [tuios (Gaurav-Gosain)](concepts/tool-tuios.md) — Go 写轻量终端复用器：vim 式模态、9 工作区 + BSP 平铺 + 命令面板
- [Texpile](concepts/tool-texpile.md) — 完全离线 / 免注册的桌面级 LaTeX / Typst / Markdown 编辑器，可视化 + 源代码双模式
- [CivitaiFreeTool](concepts/tool-civitai-free-tool.md) — Windows 桌面 AI 模型批量下载工具：批量拉取、断点续传、SHA256、写元数据
- [忆辰 · 阴历生日提醒](concepts/tool-lunar-birthday-reminder.md) — 以阴历生日为基准的提醒 App：提前 1~7 天 + 到点反复通知均可独立设置

### 数据库 / 数据工具
- [pgbot (pgrundev)](concepts/tool-pgbot.md) — Postgres 只读健康诊断 CLI：读统计视图 → 健康评分 + 历次变化对比，DBA / AI agent 直接消费

### 金融 / 数据
- [easy-stock (jundizhou)](concepts/tool-easy-stock.md) — 面向 A 股的 AI 原生投研桌面工作台：盘中 / 盘后 / 长期三段沉淀 + Agent 自动收大 V 文章提炼观点

### 后端 / 实时数据流
- [PulseNews-Live (jinit-00)](concepts/tool-pulsenews-live.md) — 实时新闻 AI 流式平台：多源 RSS → Kafka → 向量索引 → AI 问答 / 流式分析

### 前端 / 设计资源
- [aicss.dev](concepts/tool-aicss.md) — 面向设计工程师的 AI 界面纯 CSS 资源站
- [bloub](concepts/tool-bloub-mascot.md) — Grok Bot 风格吉祥物生成器：浏览器内画 / 上色 → 导出 SVG 动画

### 项目管理 / 模板
- [circle (ln-dev7)](concepts/tool-circle-ln-dev7.md) — 开源项目管理模板，Next.js + Tailwind，项目视图开箱即用

### 跳过 / 复核（Skipped / No-op）
- Wen_Zw「好神奇」(2089558732380512670) — 短语 + 视频，纯情绪反应，按「质量门槛」跳过
- QingQ77「腿有了自己的想法」(2089660859417248171) /「演技炸裂，演员可以失业了，当年嘎你蛋的人，也是我安排的」(2089672630031015972) /「这个机器人是不是飞起来了」(2089745061982654660) /「点外卖的顾客：我说我的订单怎么老是超时」(2089583650455314788) /「cool」(2089694752384176444) — 短语 + 视频，纯情绪反应，按「质量门槛」跳过
- QingQ77 opencode-senses (2089613013565264288) — 仓库 URL 与既有概念 tool-opencode-senses 完全一致，描述亦无新增信息，按「概念已存在且资料无新增信息」原则**不动文件，仅 log**

## 本批新增（2026-08-19）

### AI / Agent 生态 / Skills
- [animate-expo](concepts/tool-animate-expo-skill.md) — `Tool` — Emil Kowalski 与 Expo 团队合作的 Skill，把动效知识移植到 React Native / Expo 原生应用
- [HarnessRouter](concepts/tool-harness-router.md) — `Tool` — 自托管、兼容 OpenAI Responses API 的统一网关，把 Codex / Claude Code / Hermes 等多个 agent harness 收进同一界面与一套 API

### DeepSeek Harness (DSH) 生态扩展
- [dsh-usage-stats](concepts/tool-dsh-usage-stats.md) — `Tool` — dsh 网页端补的多供应商账户余额 + Token 用量监测侧边栏
- [DSH-SessionGraph](concepts/tool-dsh-sessiongraph.md) — `Tool` — 把长 dsh 调试会话压缩成可编辑、可复制的结构化导图与大纲
- [dsh-auto-mode](concepts/tool-dsh-auto-mode.md) — `Tool` — 权限分级：常规操作走 sandbox，越界高风险才交模型分类审查
- [deepseek-harness-handbook](concepts/note-deepseek-harness-handbook.md) — `Note` — dsh 中文零基础手册，17 章 + 实测附录覆盖安装到写插件

### 终端 / 命令行 / TUI
- [SimulTeX](concepts/tool-simultex.md) — `Tool` — 把 Codex / Claude Code 的终端会话镜像到本地 localhost 浏览器
- [pkgtui](concepts/tool-pkgtui.md) — `Tool` — htop 风格 TUI 同时管理 apt 与 snap
- [asciicut](concepts/tool-asciicut.md) — `Tool` — 面向 asciinema .cast 的可视化剪辑

### 桌面 / 系统工具
- [fluent-sensors](concepts/tool-fluent-sensors.md) — `Tool` — Windows 11 上长得像系统原生的硬件监控面板
- [CodePulse](concepts/tool-codepulse.md) — `Tool` — macOS 菜单栏原生编码计时器
- [svg_animate](concepts/tool-svg-animate.md) — `Tool` — Flutter 用 flutter_svg 渲染器跑 SVG SMIL / CSS 动画

### 跨平台 / 自托管 / 离线
- [FileApex](concepts/tool-fileapex.md) — `Tool` — 同局域网 Android / macOS / Windows 设备互传文件
- [Resonant](concepts/tool-resonant.md) — `Tool` — Windows 本地离线 AI 音乐工作室

### 前端 / 设计 / 头像资源
- [Blobatar](concepts/tool-blobatar.md) — `Tool` — 输入用户信息生成固定对应、会动的几何 SVG 小生物

### 本体 / 知识图谱 / AI 写作
- [ontopilot](concepts/tool-ontopilot.md) — `Tool` — 本地优先 / 自托管的本体工程工作台
- [sloptrim](concepts/tool-sloptrim.md) — `Tool` — 本地检测 AI 写作套路，71 模式 / 62 检测器

### AI 模型训练 / 桌面端
- [LabLLM](concepts/tool-labllm.md) — `Tool` — macOS 桌面应用小模型训练工作台
- [grokx](concepts/tool-grokx.md) — `Tool` — 把 Grok Build 引擎绑进桌面窗口

### 旅行规划
- [ai_travel_agent](concepts/tool-ai-travel-agent.md) — `Tool` — 对话式 AI 旅行规划代理 + 强制人工确认后再下单

### 跳过 / 复核（Skipped / No-op）
- Wen_Zw RT vikingmute Departure Mono 字体 (2089976344570696135) — 字体审美欣赏，无概念增量，按「质量门槛」跳过
- Wen_Zw RT vikingmute Memmy (2090050558992462298) — 仓库与既有概念 tool-memmy-agent 完全一致，描述无新增信息，按「概念已存在且资料无新增信息」原则不动文件，仅 log
- Wen_Zw RT QingQ77 SimulTeX (2089924885506334957) — 与同日 QingQ77 主帖 2089916515466235998 同一项目，已新建独立概念 tool-simultex，本条仅 RT 不重复
- QingQ77「我不听我不听」(2089972971951866112) — 短语 + 视频，纯情绪反应，按「质量门槛」跳过
- QingQ77「有点意思🎛️」(2090059034619736519) — 一词感叹 + emoji + 视频，无信息量，按「质量门槛」跳过
- QingQ77「I, Robot !」(2089904635796746587) — 一词感叹 + 视频，纯情绪反应，按「质量门槛」跳过
- QingQ77「打丧尸小战锤」(2090029180494971242) — 游戏短句 + 视频，按「质量门槛」跳过

## 本批新增（2026-08-20）

### DeepSeek Harness (DSH) 生态扩展
- [dsh-crew](concepts/tool-dsh-crew.md) — `Tool` — 把 DSH agent 当子代理接到 Claude Code 与 Codex，进度同步显示在宿主面板
- [dsh-context](concepts/tool-dsh-context.md) — `Tool` — DSH 上下文窗口可视化插件，把 token 用量与压缩过程拆开
- [dsh-rs](concepts/tool-deepseek-harness-rs.md) — `Tool` — Rust 重写的 DSH 命令行 `dsh`，终端里搜代码 / 读文件 / 打补丁 / 跑命令
- [dsh-im](concepts/tool-dsh-im.md) — `Tool` — 把 9 个 IM 平台（飞书 / 微信 / 钉钉 / 企微 / QQ / Slack / Telegram / Discord / WhatsApp）机器人统一接入 DSH
- [dsh-client-ui-skin-claude](concepts/tool-dsh-client-ui-skin-claude.md) — `Tool` — 给 DSH Web UI 套 Claude 风格皮肤的换皮插件
- [Minke](concepts/tool-minke.md) — `Tool` — 把 DSH 装进本地优先的桌面工作台，对话 / 文件 / 终端 / 网页工具同窗

### 任务管理 / Agent 工作台
- [Muqi Task](concepts/tool-muqi-task.md) — `Tool` — 以 Task 为主线、会话挂任务底下的 AI 协作组织方式

### 桌面 / 视觉 / 系统
- [barehands](concepts/tool-barehands.md) — `Tool` — 把网络摄像头变成手势界面，玻璃浮卡 + 裸手操控，可接给 AI 当手和眼睛
- [Humla](concepts/tool-humla.md) — `Tool` — Mac 本地跑的会议记录 / 转写 / 分人 / 总结工具，录音与笔记不出本机
- [omarchy-pod](concepts/tool-omarchy-pod.md) — `Tool` — 把 AirPods 的电量 / ANC / 入耳检测等细粒度状态挂到 Omarchy 状态栏
- [omawhoop](concepts/tool-omawhoop.md) — `Tool` — 把 WHOOP 健康数据（strain / recovery / 睡眠）挂到 Omarchy 桌面状态栏

### 自托管 / 云基础设施
- [Spinifex](concepts/tool-spinifex.md) — `Tool` — AGPL-3.0 开源的 AWS API 兼容私有云（EC2 / EBS / S3 / VPC / IAM），让现有 AWS 代码零改动部署到自有硬件
- [synap.md](concepts/tool-synap-md.md) — `Tool` — 自托管、Obsidian 风格的 Markdown 笔记应用，纯 .md 文件 + 自建同步服务器

### AI Agent / 网络抓取
- [DonSeTch](concepts/tool-donsetch.md) — `Tool` — Rust 单二进制 Web 抓取 / 搜索 / 爬站，通过 MCP 给 AI 代理 web_fetch / web_search / web_crawl

### Pi 扩展 / AI 写作辅助
- [SLYE / speak-like-you-eat](concepts/tool-slye-speak-like-you-eat.md) — `Tool` — Pi 扩展，在模型回答后自动追加大白话重写，把 AI 套话翻译成人话

### AI 视频 / 设计资源
- [Magiviz](concepts/tool-magiviz.md) — `Tool` — MIT 全栈开源的 AI 视频创作平台，写剧本 → 定角色 → 画分镜 → 生成视频 → 成片全流程
- [iris](concepts/tool-iris-site-builder.md) — `Tool` — 代码优先的轻量级网站构建工具，整合 Astro 简洁性与组件化开发体验

### Playbooks（设计原则）
- [Logo First, IP Second](concepts/playbook-logo-first-ip-skill.md) — `Playbook` — 把可爱 IP 压成精致 Logo 的六原则（极简构成 / 圆润线条 / 克制色彩 / 人格化构图）

### 跳过 / 复核（Skipped / No-op）
- Wen_Zw「RT bridgertower iris」(2090307655051157814) — 仅 GitHub URL + 一张截图；与本批 QingQ77 同期 iris 概念信息互补，概念已建，本条仅 archive，不重复
- Wen_Zw「RT noahelhadedy Free invoice templates」(2090397715821953472) — 模板资源链接，无新概念 / 工具 / 项目增量，按「质量门槛」跳过
- Wen_Zw「RT madebyhex motion-gpu.dev」(2090172778540584965) — 一句感叹 + 空链接，无概念增量，按「质量门槛」跳过
- Wen_Zw「RT davidhdev canvasui ASCII sweep」(2090284541688848567) — 单组件链接 + 营销文，无独立概念，按「质量门槛」跳过
- Wen_Zw「RT arknow91 liquid-taffy update」(2090367297810784617) — 项目更新视频，无可复用经验，按「质量门槛」跳过
- Wen_Zw「RT lassejlv build-gpui-apps」(2090173023362191384) — 「thank me later」+ 空链接，无信息量，按「质量门槛」跳过
- Wen_Zw「RT QingQ77 dsh-crew」(2090329482435695101) — 与同日 QingQ77 主帖 2090321431347298649 同一项目，已新建独立概念 tool-dsh-crew，本条仅 RT 不重复
- Wen_Zw「RT QingQ77 DSH-SessionGraph」(2090336158828122196) — 与既有概念 tool-dsh-sessiongraph 完全一致，描述无新增信息，按「概念已存在且资料无新增信息」原则不动文件，仅 log
- QingQ77「氢能两轮动力」(2090265003639361880) — 讽刺段子 + 视频，无知识 / 概念 / 工具 / 项目增量，按「质量门槛」跳过
- QingQ77「金牙出现」(2090433393276375408) — 「哈哈哈」情绪反应 + 视频，无信息量，按「质量门槛」跳过
- QingQ77「Hacker News Flutter app」(2090226304817717695) — 一个原生客户端，描述无新增概念 / 可复用经验，按「质量门槛」跳过
- QingQ77「pkgtui」(2090309100345143430) — 与既有概念 tool-pkgtui 完全一致，描述无新增信息，按「概念已存在且资料无新增信息」原则不动文件，仅 log

## 本批新增（2026-08-21）

### AI / Agent 生态
- [OpenBot](concepts/tool-openbot.md) — `Tool` — CopilotKit 出品的 Bot 运行时，一 Bot 一电脑 + 策略网关 + 审计记录
- [autoprompt-skill](concepts/tool-autoprompt-skill.md) — `Tool` — 给编码 agent 加「拆目标 + 并行 + 独立质检」纪律，Terminal-Bench 失败次数减半
- [Sprix SAGE Router](concepts/tool-sprix-sage-router.md) — `Tool` — A2A 网络里「继续独干 / 叫帮手 / 整体换人」三路效用函数决策路由
- [plannotator / guides](concepts/tool-plannotator-guides.md) — `Tool` — 把 diff 拆成有章节的阅读顺序，产出浏览器即开单文件 HTML 评审页

### DeepSeek Harness (DSH) 生态扩展
- [cordis-mini](concepts/tool-cordis-mini.md) — `Tool` — 把 deepseek-harness 五个核心机制各写一份约 600 行 Python 迷你版
- [Boujoy Harness](concepts/tool-boujoy-harness.md) — `Tool` — 给 dsh 套一层产品工作台外壳：任务 / 知识库 / 对话分得开
- [dsh-plugin-dir-tree](concepts/tool-dsh-plugin-dir-tree.md) — `Tool` — 在 DSH 对话框以浮窗展示工作区目录树，拖拽即填路径

### 终端 / IDE / 编辑器
- [terminal-code / tode](concepts/tool-terminal-code-tode.md) — `Tool` — 把 code-server 与 terminal-browser 串起来，让 VS Code 直接跑在终端里
- [Flare](concepts/tool-flare-ide.md) — `Tool` — 以代码依赖图谱为核心的 IDE，文件节点 + 导入连线，三视图实时同步

### 阅读 / 资源
- [What is an Agent Harness (earendil)](concepts/note-earendil-agent-harness.md) — `Note` — earendil.com 上 pidotdev 写的科普长文，把 agent harness 概念一次性拆给入门读者

### Agent Skills 生态
- [jakubkrehel Skills](concepts/tool-jakubkrehel-skills.md) — `Tool` — 含 `/explain-interface`：用 DevTools 风格手段拆解任意网页交互与视觉技术

### 多媒体 / 视频 / AI 创作
- [VedioHub / DoVideoAI](concepts/tool-vediohub-dovideoai.md) — `Tool` — 把小时级长视频拆成带时间戳片段交给 Agent，结论挂可回放证据链

### 运动 / 自托管 / 健康
- [Dreeve](concepts/tool-dreeve.md) — `Tool` — 自托管开源 Strava 数据面板，FIT/TCX/GPX 导入 + Strava 同步 + 装备追踪 + Rewind 年度回顾

### 电商 / 自托管
- [SimpleCard](concepts/tool-simplecard.md) — `Tool` — Spring Boot 3.4 + Next.js 16 自托管数字商品发卡平台
- [Crocs Visualizer](concepts/tool-crocs-visualizer.md) — `Tool` — 浏览器内给洞洞鞋换色 + 拖 Jibbitz 挂件，实时预览定制效果

### 桌面 / 系统工具
- [desktop-fly](concepts/tool-desktop-fly.md) — `Tool` — 用 FlyWire 真实果蝇脑图谱跑脉冲仿真，macOS 桌面上一只由真实神经元驱动的 3D 果蝇

### 金融 / TUI
- [Helius Finance Tracker](concepts/tool-helius-finance-tracker.md) — `Tool` — Rust TUI + SQLite 本地优先记账，账目 / 预算 / 循环账单 / 对账 / 现金流预测

### Playbooks（设计原则）
- [Logo First, IP Second](concepts/playbook-logo-first-ip-skill.md) — `Playbook` — 补充「四件硬性约束」+ Agent 平台兼容列表（Codex / Coze / Doubao / YouMind / Manus / Gemini Apps / Replit Agent）

### 跳过 / 复核（Skipped / No-op）
- Wen_Zw「RT rabi_guha openui.com/benchmarks」(2090613983481110905) — 仅一句 URL，无项目描述 / 截图 / 关键功能信息，按「质量门槛」跳过
- QingQ77「知道了」+ 图片 (2090625247326372116) — 仅两字 + 一张图，无可提取的概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「笑岔气了」+ 视频 (2090598759109435543) — 情绪反应 + 短视频，无可提取的概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「这就尴尬了」+ 视频 (2090657967578521981) — 情绪反应 + 短视频，无可提取的概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「红色警戒2巨炮」+ 视频 (2090630968344530974) — 游戏怀旧 + 短视频，无知识增量，按「质量门槛」跳过

## 本批新增（2026-08-23）

### AI / Agent 生态（本批新增）
- [OpenViking（火山引擎上下文数据库）](concepts/tool-openviking.md) — `Tool` — volcengine/OpenViking，把 Agent 的记忆 / 文档 / 技能挂到 `viking://` 虚拟文件系统
- [KITE / memoket-kite](concepts/tool-kite-memoket.md) — `Tool` — memoket 的非向量 AI 记忆方案：结构化事实 + 可读查询计划
- [SkillCorpus](concepts/tool-skillcorpus.md) — `Tool` — EverMind-AI 把公开 SKILL.md 收拢 + 安全审核 + 按任务检索的可信技能库
- [hunter-community](concepts/tool-hunter-community.md) — `Tool` — 个人投资者的自部署金融 AI Agent 平台：行情 / 分析 / 预测 / 投研方法论
- [agent-office](concepts/tool-agent-office.md) — `Tool` — baturyilmaz/agent-office，给一群 AI 编码代理一套 Slack 式协作环境
- [dsh-desktop (SnowCrescenter-tech)](concepts/tool-dsh-desktop-snowcrescenter.md) — `Tool` — 把 DeepSeek Harness Web UI 装进 Windows 桌面，双击即用
- [herdr-nvim](concepts/tool-herdr-nvim.md) — `Tool` — ChmaraX 把 Neovim 嵌入 herdr 工作区，编辑器 / AI 改动 / 批注贯通

### 后端 / 开发工具 / MCP（本批新增）
- [proxypin-mcp-workbench](concepts/tool-proxypin-mcp-workbench.md) — `Tool` — sinyu1012 把抓包变可积累工作流 + 本地 AI 直接分析流量
- [floci-oci](concepts/tool-floci-oci.md) — `Tool` — Oracle Cloud Infrastructure 本地模拟器，Docker 单容器替真租户测试

### 桌面 / 终端 / 物联网（本批新增）
- [OcPlayer · 橘猫播放器](concepts/tool-ocplayer.md) — `Tool` — 1824239290/OcPlayer，SwiftUI + Rust 内核的 Jellyfin 苹果端原生客户端
- [kitty-sessionizer](concepts/tool-kitty-sessionizer.md) — `Tool` — BearDad 给 kitty 终端补的 tmux-sessionizer 式项目管理
- [mimimodel](concepts/tool-mimimodel.md) — `Tool` — memovai/mimimodel，45M 参数的 ESP32-S3 端侧工具调用小模型

### 自托管 / 隐私 / 网络（本批新增）
- [ssh-clipboard](concepts/tool-ssh-clipboard.md) — `Tool` — standardagents 点对点 SSH 同步系统剪贴板，文本 / 图片 / 文件原生格式
- [lightspeed](concepts/tool-lightspeed.md) — `Tool` — khydrogenous 去中心化阅后即焚社交应用，设备端加密 + P2P + 看一次即全删
- [psipool](concepts/tool-psipool.md) — `Tool` — xHossein/psipool 终端多地区 Psiphon 代理池管理

### 金融 / 数据（本批新增）
- [post-investment-platform](concepts/tool-post-investment-platform.md) — `Tool` — Oliveluo666 的 VC/PE 投后管理开源平台：项目台账 / 财务 / 合规待办 / 报告

### 更新（Updated）
- [ThreeUI（MengTo/threeui）](concepts/tool-threeui.md) — 补充「社区版整套开源」最新公告：50 个 Three.js / React 交互组件可直接看源码 + `npm` 安装

### 跳过 / 复核（Skipped / No-op）
- Wen_Zw RT @srbh_here「Floating menu」+ 视频 (2091349639408877784) — 仅 UI 动效展示 + great-ui.com 链接，无可定位的工具 / 项目仓库，按「质量门槛」跳过
- QingQ77「第3道选手 这里不让睡觉」+ 视频 (2091328952401092965) — 仅短语 + 短视频，无可提取的概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「我准备了两套说辞」+ 视频 (2091448627780792456) — 仅短语 + 短视频，无可提取的概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「原来彩虹是圆的」+ 视频 (2091472462261456954) — 仅短语 + 短视频，无可提取的概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「我看到了什么😍」+ 视频 (2091461855298679006) — 仅情绪反应 + 短视频，按「质量门槛」跳过
- QingQ77「起猛了，超人给祖国人介绍女超人。」+ 视频 (2091434483472101487) — 仅梗图式短语 + 视频，按「质量门槛」跳过
- QingQ77「第一次见 3D 转 2D」+ 视频 (2091386099096867236) — 仅感受表达 + 视频，按「质量门槛」跳过
- QingQ77「全球10大指数十年前各买 10 万会发生什么」+ 视频 (2091351836309799100) — 好奇心向短视频，无可定位的项目 / 工具，按「质量门槛」跳过

## 本批新增（2026-08-24）

### AI / Agent 生态（本批新增）
- [CCSwitch-operations](concepts/tool-ccswitch-operations.md) — `Tool` — RuriLothlorien 把 CC Switch 多处分散配置维护收拢为带校验命令
- [teamEvolver](concepts/tool-teamevolver.md) — `Tool` — leoriczhang 把团队真实 Agent 使用记录沉淀为可版本管理的共享 Skill / Memory
- [chat-on-steroids](concepts/tool-chat-on-steroids.md) — `Tool` — totec448-spec 给网页 ChatGPT 加本地 MCP 操控 Windows 桌面
- [Perenna](concepts/tool-perenna.md) — `Tool` — scarletkc 把跨 AI 编程客户端的长期记忆放进用户自控的 Git 仓库
- [EvoTrace](concepts/tool-evotrace.md) — `Tool` — jinzijian 把 Claude Code / Codex 历史会话编译成可后训练的数据集

### DeepSeek Harness (DSH) 生态扩展（本批新增）
- [DSH Image Gen](concepts/tool-dsh-image-gen.md) — `Tool` — shanliuling 给 DSH 加对话内直接生成图片能力

### 桌面 / 系统工具（本批新增）
- [Omarchy Zonda Zoom Theme](concepts/tool-omarchy-zonda-zoom-theme.md) — `Tool` — DHH 出品的帕加尼 Zonda 碳黑风 Omarchy 主题
- [Home KTV (ktv-home)](concepts/tool-ktv-home.md) — `Tool` — zhayinggang 自托管家庭局域网 KTV：扫码点歌 + Android TV 播放
- [Cobalt (BandarLabs Kobo 平台)](concepts/tool-cobalt-kobo.md) — `Tool` — BandarLabs 用 Rust 写的 Kobo 应用平台 + 浏览器模拟器

### 数据 / 文档自动化（本批新增）
- [Open-Sheet](concepts/tool-open-sheet.md) — `Tool` — lianghsun 让 Agent 写电子表格时按名字引用，框架统一解析为 A1 + 活公式 .xlsx
- [vault-graph](concepts/tool-vault-graph.md) — `Tool` — luke321 把整个 Obsidian 库画成可交互圆形图谱，可导出离线单文件 HTML

### macOS 客户端（本批新增）
- [Kumone（macOS 网易云原生客户端）](concepts/tool-kumone.md) — `Tool` — missuo 用 SwiftUI 写的网易云原生客户端，免网页套壳

### 自托管 / README 工具（本批新增）
- [minimal-github-stats](concepts/tool-minimal-github-stats.md) — `Tool` — antonisloukis 用 GitHub Actions + Python 标准库生成 GitHub 统计 SVG
- [gitglance](concepts/tool-gitglance.md) — `Tool` — rafaeloliveiraz 自部署 GitHub 统计 SVG 卡片生成器

### 学习 / 面试（本批新增）
- [DevOps Interview Guide](concepts/tool-devops-interview-guide.md) — `Tool` — iam-veeramalla 整理的 DevOps 面试问答指南

### 复核（No-op）
- Wen_Zw RT @tom_doerr HttpSMS (2091773744440381482) — 既有概念 [`tool-httpsms`](concepts/tool-httpsms.md) 已完整覆盖，无新增信息

### 跳过 / 复核（Skipped / No-op）
- QingQ77「道高一尺，魔高一丈，饭卡手机。」+ 视频 (2091798795445301299) — 仅为产品硬件形态描述，无可定位的开源项目 / 工具，按「质量门槛」跳过
- QingQ77「没有 AI 提示，居然是真实存在的🤯」+ 视频 (2091769941557203174) — 情绪反应短语 + 短视频，无可提取的概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「这个『我不听』真的太形象了🤣」+ 视频 (2091732567443878045) — 情绪反应短语 + 短视频，无可提取的概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「有谁不喜欢这种电竞房呢」+ 视频 (2091902050263265344) — 情绪反应短语 + 短视频，无可提取的概念 / 工具 / 项目信息，按「质量门槛」跳过

## 本批新增（2026-08-26）

### AI / Agent 生态（本批新增）
- [Solweaver](concepts/tool-solweaver.md) — `Tool` — jay7793 给 Codex 多 Agent 协作压 Sol 一头做单一问责，按合算 / 风险派 Terra/Luna
- [ballast](concepts/tool-ballast.md) — `Tool` — svy04 给 Claude Code 加关键词触发 hook，把历史规则原文自动塞回上下文
- [Encephalon](concepts/tool-encephalon.md) — `Tool` — isaachinman 把 Claude Code 项目级结论写进仓库 JSON，Agent 跨会话可查
- [Apodex 1.1 + FrontierAgent](concepts/tool-apodex-frontieragent.md) — `Tool` — ApodexAI 科研场景多 Agent：核查事实 → 子 Agent 并行 → 交叉验证 → 终审；附 35B 本地模型
- [qiling-soulmate](concepts/tool-qiling-soulmate.md) — `Tool` — Soulmate-Halo 本地优先桌面，把多 Agent CLI 收进同一工作台统一调度，强弱模型分工 + 器灵压缩

### DeepSeek Harness (DSH) 生态扩展（本批新增）
- [awesome-dsh-plugin](concepts/tool-awesome-dsh-plugin.md) — `Tool` — bruc3van 维护的 DSH 插件质量审核清单：每日自动抓 + 人工逐一审 + 踢除留档

### 前端 / 设计 / 工具型（本批新增）
- [Paperlab](concepts/tool-paperlab.md) — `Tool` — NourMtir 的网页真纸张画布：折叠、抓角掀起，文字随网格形变（three.js + gsap）
- [workout-guide](concepts/tool-workout-guide.md) — `Tool` — bryllim 把 302 个健身动作各画 3 帧（共 906 张 512×512 SVG）+ 框架无关 npm 包
- [PrelineUI Animated Icons](concepts/tool-preline-animated-icons.md) — `Tool` — 65 个单 SVG 内置 CSS 关键帧的动画图标，零 JS 零运行时，颜色跟父级文字
- [shuohao-skills](concepts/tool-shuohao-skills.md) — `Tool` — eternityspring 把说话风格 / 角色腔调做成 Code Agent 可加载 Skills
- [SpatialBoard](concepts/tool-spatialboard.md) — `Tool` — hishamk 的 React 白板底层（平移 / 缩放 / 撤销 / 吸附对齐），开发者注册节点即用
- [CozyClay](concepts/tool-cozyclay.md) — `Tool` — NomaDamas 出的 `npx cozyclay` 一键起手的浏览器 3D 动画工作室，Prompt Block 接力

### 游戏 / 2D 资源生产（本批新增）
- [zpack](concepts/tool-zpack.md) — `Tool` — masonschafercodes 的流式资源打包工具，打成单 `.zpak`，运行时按名直查，字节一致
- [sprite-maker](concepts/tool-sprite-maker.md) — `Tool` — JohnKinyanjui 的 Tauri 桌面 + Codex CLI：聊天出静态精灵 + 「Animate this」逐帧 24–48 帧身份不丢形

### 桌面 / 浏览器扩展（本批新增）
- [ocr-it](concepts/tool-ocr-it.md) — `Tool` — thiagotigaz 的 Chrome 扩展，离线 OCR 翻页书/幻灯片/PDF：⌥⇧R 框选 → ⌥⇧S 截图 → ⌥⇧A 自动翻页
- [herdr-file-annotator](concepts/tool-herdr-file-annotator.md) — `Tool` — JonasBaeumer 给 herdr 工作区加可视代码评审面板，fix/verify/question/nit 标签 + 行号锚点回灌 Agent
- [doop](concepts/tool-doop.md) — `Tool` — kgoedecke 出品的 AGPL-3.0 协作画布，对标 Paper.design：Canvas+Frame + iframe 真渲染 + WebSocket 同步

### 网络 / DevOps / 自托管（本批新增）
- [ZSvirt](concepts/tool-zsvirt.md) — `Tool` — Kid-G0629 把 ZStack ZSphere 虚拟化引擎开源，给家庭实验室到机房一个自托管替代
- [api-balance-checker-extension](concepts/tool-api-balance-checker-extension.md) — `Tool` — zhuifengshaonian6 给 Chrome/Edge 写的多 AI 中转站余额聚合，Key 只存本地会话

### 工程实践 / Note（本批新增）
- [Anthropic Claude Code Startups 指南要点](concepts/note-claude-code-startups-guide.md) — `Note` — 把 Claude Code 深度集成进 SDLC 的 5 条原则：全员参与 / 重复活自动化 / 信任必验证 / 重建为前提 / 原型→内部用→产品化

### 趣味 / 数据度量（本批新增）
- [git-entropy](concepts/tool-git-entropy.md) — `Tool` — FelixKramer 把 git 仓库压成 tar.gz/zip 测真实信息量字节数 + 不含运行时数据的对照
- [Pindo](concepts/tool-pindo.md) — `Tool` — LunarXuan 把图片转拼豆图纸（网格+色号+用量统计），浏览器本地跑，旧图纸自动补色号

### 跳过 / 复核（Skipped / No-op）
- Wen_Zw RT @sitenley @boardui live here (2092422910317404427) — 仅一句「live here boardui.com」无项目描述，按「质量门槛」跳过
- Wen_Zw RT @kookaking ThreeUI 高质量开源 (2092447805126402447) — 与既有概念 [`tool-threeui`](concepts/tool-threeui.md) 一致，无新增信息
- Wen_Zw RT @Manixh02 MetalForge progress bar (2092456653425885620) — 与既有概念 [`tool-metalforge-orbs`](concepts/tool-metalforge-orbs.md) 同一项目，无新增信息
- Wen_Zw RT @studiowondercat「Best UI design resources Part 2」(2092479298053833062) — 仅四个已知资源链接，按「质量门槛」跳过
- Wen_Zw RT @csaba_kissi 设计资源链接列表 (2092517745724367354) — kinetics / iconcreator 已有同概念，剩三个无可定位项目信息，按「质量门槛」跳过
- Wen_Zw RT @grug_speak handdrawn.software (2092542170578497712) — 仅一句 + 一 URL，无项目描述，按「质量门槛」跳过
- Wen_Zw RT @Zh_Crypto517「打破信息差，5 个网站」(2092584798967755024) — 国内下载站列表，无开源项目信息，按「质量门槛」跳过
- Wen_Zw RT @QingQ77 SpatialBoard (2092516472568643801) — 与 QingQ77 主帖（已建 [`tool-spatialboard`](concepts/tool-spatialboard.md)）同项目，本条仅 RT
- QingQ77「这不比谈朋友更香吗」+ 视频 (2092443065969680877) — 纯情绪反应 + 短视频，按「质量门槛」跳过
- QingQ77「🤯保鲜膜无壳孵化乌龟」+ 视频 (2092528009798635713) — 自然科学短视频，按「质量门槛」跳过
- QingQ77「这才是化腐朽为神奇」+ 视频 (2092564992499614192) — 短语 + 短视频，按「质量门槛」跳过
- QingQ77「理想中的House」+ 视频 (2092597242645618714) — 房屋 / 家居短视频，按「质量门槛」跳过
- QingQ77「以前我听到这首歌会想起很多人和事...」+ 视频 (2092613509645561986) — 抒情短语 + 短视频，按「质量门槛」跳过

## 本批新增（2026-08-27）

### AI / Agent 生态（本批新增）
- [FyAgent](concepts/tool-fyagent.md) — `Tool` — fy-agent 把 Claude Code / Codex / Gemini CLI 等多 AI 编码代理的 Key / MCP / 提示词收进一个本地桌面应用，改一处同步到所有工具
- [ThinkRail](concepts/tool-thinkrail.md) — `Tool` — JetBrains 给自家 Pi 编码 Agent 出的桌面客户端，引擎嵌入应用进程跑
- [pi-agent-desktop](concepts/tool-pi-agent-desktop.md) — `Tool` — Chasen-Liao 社区版 Pi Agent 独立窗口客户端
- [Strado](concepts/tool-strado.md) — `Tool` — strado-io 多 AI 编码代理并行协作平台：独立 worktree + 内置浏览器 / IDE
- [Capstan](concepts/tool-capstan.md) — `Tool` — theStrangeAdventurer C + 嵌入式 Lua 实现的轻量终端编码 Agent
- [remotifyd](concepts/tool-remotifyd.md) — `Tool` — langgenius（Dify 团队）专为 AI Agent 设计的远程设备管理守护进程
- [wildchopper/financial-dashboard](concepts/tool-wildchopper-financial-dashboard.md) — `Tool` — React + Express 财务报表看板参考实现，外部数据必须先过结构 + 语义双重校验才进 UI
- [angkorgit](concepts/tool-angkorgit.md) — `Tool` — cheat2001 跨平台开源 Git 客户端，二进制仅 ~12 MB

### Agent Skills 生态（本批新增）
- [Gradio Agent Workflow Guide](concepts/tool-gradio-agent-workflow-guide.md) — `Tool` — Hugging Face 主张 agent-friendly ≈ human-friendly
- [fireworks-open-eli5](concepts/tool-fireworks-open-eli5.md) — `Tool` — yizhiyanhua-ai 把复杂系统讲成带证据、可交互的离线 HTML 视觉故事
- [taste-skill / redesign-existing-projects](concepts/tool-taste-skill-redesign.md) — `Tool` — Scan → Diagnose → Fix 三步 Agent Skill

### 跨端 / 前端 / 设计（本批新增）
- [StyleX Blocks](concepts/tool-stylexblocks.md) — `Tool` — eelcodotdev 基于 Stylex + Ark UI / Base UI 的组件积木站
- [wsrv.nl](concepts/tool-wsrv.md) — `Tool` — 开源图像 CDN / 图像代理，可 Docker 自托管
- [Highball](concepts/tool-highball.md) — `Tool` — gauthierpiarrette Apple Silicon Mac 一键运行 Windows 游戏 + 开放兼容性数据库
- [GLTFVisu](concepts/tool-gltfvisu.md) — `Tool` — MaxMFonseca 把 glTF + 自定义着色器调试装进同一个网页
- [uni-baidu-map-harmony](concepts/tool-uni-baidu-map-harmony.md) — `Tool` — carlChina88 把百度地图 HarmonyOS NEXT 原生 SDK 补进 uni-app

### 个人 / 财务 / 健康（本批新增）
- [life-ipo（衡 · 人生 IPO）](concepts/tool-life-ipo.md) — `Tool` — gtlhuyidan-sketch 统一个人数据操作系统

### 流程手册（Playbooks）
- [Fact-Anchored Discovery Learning](concepts/playbook-fact-anchored-discovery-learning.md) — `Playbook` — amosblomqvist 把「先锁事实、再发现推导」教学法编码成 Pi 配置

### 更新（Updated）
- [sim-use](concepts/tool-sim-use.md) — `Tool` — 更新 v0.14.0：新增物理 iPhone / iPad 真机实验性支持 + 既有的 iOS 模拟器 / Android 改进

### 跳过 / 复核（Skipped / No-op）
- Wen_Zw RT @davidhdev CRTWarp reactbits.dev 组件 (2092819930962096233) — 单组件展示，按「质量门槛」跳过
- Wen_Zw RT @csaba_kissi 设计资源链接列表 (2092938911580557480) — 多为已知资源或目录站，按「质量门槛」跳过
- Wen_Zw RT @shao__meng ui-skills.com (2092964573439771061) — 与既有概念 [`note-ui-skills-top10`](concepts/note-ui-skills-top10.md) 同一项目，无新增信息
- Wen_Zw RT @bestdesignsonx Binder tabs (2092979032510115846) — 单 UI 设计展示，按「质量门槛」跳过
- Wen_Zw RT @remvze mnmm.xyz 极简网站列表 (2093000225829134396) — 4 个极简网站链接列表，按「质量门槛」跳过
- Wen_Zw RT @ShadcnAdmn shadcnuidashboard.com 仪表盘模板 (2093001664240443441) — 仅 demo URL 与营销截图，按「质量门槛」跳过
- Wen_Zw RT @QingQ77 fireworks-open-eli5 (2093002329482309989) — 与 QingQ77 主帖（已建 [`tool-fireworks-open-eli5`](concepts/tool-fireworks-open-eli5.md)）同项目，本条仅 RT
- QingQ77「我看的是正经《奥德赛》吗？」+ 视频 (2092780783077593128) — 短语 + 短视频，按「质量门槛」跳过
- QingQ77「canvas-retro-engine 在 Obsidian Canvas 内玩 NES/PS1」(2092790198761316370) — 娱乐性怀旧模拟器，按「质量门槛」跳过
- QingQ77「机器人：一生只能用一次的大招」+ 视频 (2092838456926023887) — 情绪反应 + 短视频，按「质量门槛」跳过
- QingQ77「FrontierAgent 终端多 Agent 框架」(2092846066974834889) — 与既有概念 [`tool-apodex-frontieragent`](concepts/tool-apodex-frontieragent.md) 同一项目，无新增信息

## 本批新增（2026-08-29）

### AI / Agent 生态（本批新增）
- [Lody](concepts/tool-lody.md) — `Tool` — LodyAI 通过 ACP 把任意机器上的 Claude Code / Codex / Kimi / OpenCode 接入团队共享工作空间，桌面 / 手机 / 网页 / CLI 同源访问
- [Open Agent View](concepts/tool-open-agent-view.md) — `Tool` — xhluca 把 Claude Code / Codex / Cursor / Pi 等 15+ 本地编码 Agent 收进同一个 TUI 仪表盘
- [unbox-ai](concepts/tool-unbox-ai.md) — `Tool` — tester-army 把 LLM trace 中每轮重复的 system prompt 与工具定义摊开画图，定位 token 浪费源头
- [Pentest Harness](concepts/tool-pentest-harness.md) — `Tool` — S1N6H 给授权渗透 / 漏洞悬赏 / CTF 的自托管 AI Agent Harness，BYO 模型 API、会话全留本地

### DeepSeek Harness (DSH) 生态扩展（本批新增）
- [dsh-harmonyos-pc](concepts/tool-dsh-harmonyos-pc.md) — `Tool` — Entity-Him 把 DSH 核心运行时搬上 HarmonyOS PC，免装 Linux 虚拟机

### 前端 / 设计 / 工具型（本批新增）
- [Keyline Icons](concepts/tool-keyline-icons.md) — `Tool` — iszafar92 为 shadcn 生态定制的开源 Keyline 图标集，585 个 + React / MCP / CLI + Figma 社区文件 + Figma 插件，MIT 免署名

### 数据 / 文档 / 跨端（本批新增）
- [go-llama](concepts/tool-go-llama.md) — `Tool` — goccy 把 llama.cpp 推理完整搬进纯 Go（零 cgo、零共享库），单静态二进制跨平台跑 GGUF 模型
- [Bookshelf](concepts/tool-bookshelf.md) — `Tool` — murerkinn 的无数据库自托管电子书发布：Cloudflare R2 / 本地目录 + OPDS 协议
- [kiri](concepts/tool-kiri.md) — `Tool` — yuxino 把截图 / 标注 / OCR / 录屏四件套并进一个本地桌面工作区
- [mamf](concepts/tool-mamf.md) — `Tool` — macOS 上极简、自管的截图 + OCR + 标注本地工具

### 网络 / DevOps / 系统诊断（本批新增）
- [whoiz](concepts/tool-whoiz.md) — `Tool` — jkup 给一个域名自动画出每个路径和子域背后各是哪家 CDN / 托管商在顶
- [Tasks–To Do Sync](concepts/tool-tasks-todo-sync.md) — `Tool` — simonchai-tw 跑在自家 Google Apps Script 的 Google Tasks ↔ Microsoft To Do 双向同步桥

### 桌面 / macOS / Omarchy（本批新增）
- [omacosy](concepts/tool-omacosy.md) — `Tool` — paulsp94 给 macOS 26 写的 omarchy 风格平铺桌面，五个自编译 Swift 小二进制
- [Realmheart](concepts/tool-realmheart.md) — `Tool` — kzahed610 用 C++ + GTK 4 把平铺桌面 shell 整套塞进一个仓库，外观按 TBATE 动画风格做
- [omarchy-time-machine](concepts/tool-omarchy-time-machine.md) — `Tool` — jankeesvw 给 Omarchy 顶栏写的备份插件，按计划拷主目录，超时或失败才亮红

### 个人 / 创作 / 桌面玩具（本批新增）
- [QzoneArchive](concepts/tool-qzone-archive.md) — `Tool` — Gaoshu705 把 QQ 空间旧动态 / 照片 / 视频 / 点赞评论全部抓回本地 SQLite
- [oimimo 画师排单助手](concepts/tool-oimimo-scheduler.md) — `Tool` — mimo9708 给独立插画师从接单到归档一条龙收进本地工具
- [StockPet](concepts/tool-stockpet.md) — `Tool` — YellowPancake 把 A 股 / 港股 / 美股分时行情养在桌面角落，触阈值用小牛小熊动画提醒

### 自托管 / 跨端互传 / 隐私（本批新增）
- [OneSend（扫传）](concepts/tool-onesend.md) — `Tool` — makerjackie 用屏幕光学码 + 摄像头在无网络环境下两台设备间传文件

### AI 创作 / 多模型 Web 工作室（本批新增）
- [Open Higgsfield](concepts/tool-open-higgsfield.md) — `Tool` — wide-trace 把 12 图像 + 28 视频模型收进同一免费开源 Web 工作室

### AI / Agent 框架 / 多模型生态（本批新增 2026-08-29 二轮）
- [deepseek-harness（核心框架）](concepts/tool-deepseek-harness-core.md) — `Tool` — deepseek-ai 官方开源的可插拔智能体框架，模型 / 工具 / 存储 / agent loop 都可配置替换
- [opengrok](concepts/tool-opengrok-bot.md) — `Tool` — OnlyTerp 给 Grok Bot 内每个 agent 换上任意 LLM，按各家 API 真实协议对接
- [pi-clinepass](concepts/tool-pi-clinepass.md) — `Tool` — fifidayone 给 pi 编码代理加 ClinePass 接入，美元限额 + 实时成本 + 套餐上报
- [opencode-usage](concepts/tool-opencode-usage.md) — `Tool` — xhang1108 的 Chrome 扩展，把 opencode 用量同步本地 + 仪表盘，补齐免费模型统计
- [docker-auth-boundary](concepts/tool-docker-auth-boundary.md) — `Tool` — decionis 给 Docker 内 AI 代理加确定性执行授权边界

### 桌面 / 多媒体 / 文档处理（本批新增 2026-08-29 二轮）
- [Flow 提词器](concepts/tool-flow-teleprompter.md) — `Tool` — LumoRez07 的 Windows 置顶悬浮窗提词器
- [FFmpegFreeUI](concepts/tool-ffmpeg-free-ui.md) — `Tool` — Lake1059 给 Windows 进阶用户做的免费 FFmpeg 图形外壳
- [knurl](concepts/tool-knurl-latex.md) — `Tool` — gilsonolegario 读 LaTeX 项目把 \usepackage 映射到 TeX Live 包名，一键装好
- [GPUI Component Motion](concepts/tool-gpui-component-motion.md) — `Tool` — LongBridge 给 GPUI Component 加的动画 / 过渡系统

### 终端 / 网络 / 安全研究（本批新增 2026-08-29 二轮）
- [tailcat](concepts/tool-tailcat.md) — `Tool` — Tailscale 的 netcat 替代，跑在数据平面上无账号 / 无 root
- [darwin-vm](concepts/tool-darwin-vm.md) — `Tool` — jprx 在 QEMU 上跑 iOS / macOS 27（含 SPTM），iPhone 12–17 + M1–M5
- [ipatool](concepts/tool-ipatool.md) — `Tool` — majd 的命令行工具，从 App Store 下 IPA / 发起 SAP 签名

### 嵌入模型 / 多模态（本批新增 2026-08-29 二轮）
- [WeMM-Embedding](concepts/tool-wemm-embedding.md) — `Tool` — 腾讯微信团队的通用多模态嵌入模型，支持 Matryoshka 维度截断

### 推理 / 集群 / GPU（本批新增 2026-08-29 二轮）
- [Qwen3.8-Flash-Next-Dual-DGX-Sparks](concepts/tool-qwen-dual-dgx-spark.md) — `Tool` — MiaAI-Lab 用两台 DGX Spark 张量并行跑 176B NVFP4 量化 MoE

### Playbooks（本批新增 2026-08-29 二轮）
- [simplify-codebase](concepts/playbook-simplify-codebase.md) — `Playbook` — 编码代理的「先证明再删除」清理工作法

### 跳过 / 复核（Skipped / No-op）
- Wen_Zw RT @shao__meng Anti-Slop 品味 Skills (2093169094686318701) — 与既有概念 [`tool-taste-skill-redesign`](concepts/tool-taste-skill-redesign.md) 同一项目，无新增信息
- Wen_Zw RT @flaviocopes StyleX 深度文章 (2093231697122955600) — 外部博客链接，无可独立收录的具体项目 / 文档，按「质量门槛」跳过
- Wen_Zw RT @DrCapsoul toon-shaded world (2093188644760867180) — three.js + ref.design demo 视频，无项目仓库 / 文档，按「质量门槛」跳过
- Wen_Zw RT @dwhitedesign drawably.dev 手绘字体 (2093225945130037516) — 与既有概念 [`tool-drawably`](concepts/tool-drawably.md) 同一项目，无新增信息
- Wen_Zw RT @immersivetran A Soft Murmur (2093277361416606081) — 单一白噪音网站推荐，无开源项目 / 工具增量，按「质量门槛」跳过
- Wen_Zw RT @liutauras_liu swiped.design 设计策展 (2093109104969646161) — 单一 SaaS 站点链接，按「质量门槛」跳过
- Wen_Zw RT @taishik_ stylexcn.vercel.app (2093240062469443653) — 单一 UI 演示站，按「质量门槛」跳过
- Wen_Zw RT @emilwidlund soundscape 颗粒合成器 (2093139150757331349) — 单一音乐工具 demo，按「质量门槛」跳过
- Wen_Zw RT @Pixel_Salvaje Pixzels (2093109355302539555) — itch.io 个人项目无 GitHub / 文档，按「质量门槛」跳过
- Wen_Zw RT @Mike_Andreuzza Lexington Themes (2093174856418492827) — 付费商业主题（$99），按「质量门槛」跳过
- Wen_Zw RT @QingQ77 Lody (2093225990353006959) — 与 QingQ77 主帖（已建 [`tool-lody`](concepts/tool-lody.md)）同项目，本条仅 RT
- QingQ77「AI 做的，感觉她有意识了。」+ 视频 (2093121792072355878) — 短语 + 短视频，按「质量门槛」跳过
- QingQ77「我以为玩的是卡车模拟器，其实是实操。」+ 视频 (2093358252277026932) — 短语 + 短视频，按「质量门槛」跳过
- QingQ77「豆包：对不起我刚才搞错了...下辈子注意听」+ 视频 (2093158893493113116) — 豆包梗 + 短视频，按「质量门槛」跳过
- QingQ77「这是我一个被吓到的 AI 视频」+ 视频 (2093184643667534082) — 短语 + 短视频，按「质量门槛」跳过
- QingQ77「摄影界到底有多少天才」+ 视频 (2093176394310361189) — 短语 + 短视频，按「质量门槛」跳过
- Wen_Zw RT @kail_designs 动效图标站合集 (2093587754542391547) — 5 个图标站 URL 罗列，按「质量门槛」跳过
- Wen_Zw RT @cameronmoll mjbarton 新作品集 (2093478317790048398) — 单一作品集站点推荐，按「质量门槛」跳过
- Wen_Zw RT @tranmautritam pixlo.me (2093649665623490717) — 单 SaaS 站点无 GitHub，按「质量门槛」跳过
- Wen_Zw RT @AdhamDannaway inspora.design (2093733055890669680) — 单一设计策展站点推荐，按「质量门槛」跳过
- Wen_Zw RT @QingQ77 DGX Spark (2093580926848794756) — 与 QingQ77 主帖（已建 [`tool-qwen-dual-dgx-spark`](concepts/tool-qwen-dual-dgx-spark.md)）同项目，本条仅 RT
- QingQ77「完美的末日之家」+ 视频 (2093719741793984823) — 短语 + 短视频，按「质量门槛」跳过
- QingQ77「有意思」+ 视频 (2093638287022018907) — 短语 + 短视频，按「质量门槛」跳过
- QingQ77「起猛了，居然请到了黄眉大王！」+ 视频 (2093667613641695290) — 短语 + 短视频，按「质量门槛」跳过
- QingQ77「石头、剪刀、布大逃杀」+ 图 + 视频 (2093696617782329767) — 短语 + 短视频，按「质量门槛」跳过
- QingQ77「一切都在意料之中😅」+ 视频 (2093636966294458382) — 短语 + 短视频，按「质量门槛」跳过
- QingQ77「Cybercab 纯无人驾驶时代即将到来」+ 视频 (2093706913137799578) — 短语 + 短视频，按「质量门槛」跳过
- QingQ77 my-girlfriend-jingtian-latex (2093667982840824075) — 个人小说 LaTeX 排版示例，按「质量门槛」跳过
- QingQ77 Rust 终端倒计时 + 视频 (2093643320404873257) — 描述提到但无 GitHub 链接，按「质量门槛」跳过

## 本批新增（2026-08-30）

### AI / Agent 生态（本批新增）
- [CXX（微信远程接管）](concepts/tool-cxx-wechat.md) — `Tool` — focuxdot 用微信当遥控器接管电脑上跑的 Codex / Claude Code：看会话进度、审批命令、发新指令

### 前端 / 设计 / 组件库（本批新增）
- [Moduix](concepts/tool-moduix.md) — `Tool` — 构建在 Ark UI 之上的框架无关组件库：同一 API 自动适配 React / Vue / Solid / Svelte，样式默认 Tailwind 但可整体替换
- [Polkadot](concepts/tool-polkadot.md) — `Tool` — 零依赖 SVG 占位图生成器：URL 参数化尺寸 / 图案 / 配色 / 文字，可直接 `<img>` 引用、可 CDN 缓存
- [ln-dev7/logos](concepts/tool-logos-ln-dev7.md) — `Tool` — ln-dev7 的开源 logo 合集：15000+ 应用与公司矢量 logo，可直接复制 SVG / PNG 用于落地页 / Dashboard 集成列表

### SEO / 搜索可见性（本批新增）
- [geo-seo-claude](concepts/tool-geo-seo-claude.md) — `Tool` — zubair-trabzada 的 GEO / AI 搜索审计工具：并行自动化代理审计 ChatGPT / Claude / Perplexity / Google AI Overviews 的引用分数、schema、品牌权威度

### 终端 / 编辑器（本批新增）
- [Shoin / 書院](concepts/tool-shoin.md) — `Tool` — nol00p 用 Rust 写的极简终端 Markdown 编辑器：界面只有一列文字，菜单 / 文件树 / 状态行都没有，面板按需按键唤起
- [essh](concepts/tool-essh.md) — `Tool` — matthart1983 用纯 Rust 写的终端 SSH 客户端：多会话 + 实时主机指标 + 群组差异对比，替代 ssh + htop + cluster-ssh 组合

### 桌面 / macOS / 硬件（本批新增）
- [macscope](concepts/tool-macscope.md) — `Tool` — rsm23 给 Apple Silicon Mac 做的桌面工具箱：系统监控 + 进程管理 + macOS 控制 + 小工具集成到单个原生应用
- [microduck](concepts/tool-microduck.md) — `Tool` — Pollen Robotics 开源机器鸭：双舵机驱动 + 全开源 BOM / 3D / 固件，可作 AI 代理物理外壳 / STEM 教学

### 文档 / 测试 / 工作流（本批新增）
- [Mimik](concepts/tool-mimik.md) — `Tool` — westpoint-io 的本地优先浏览器操作录制扩展：录一遍自动产出带截图 / 标注的图文指南，无账号 / 不上云 / 不追踪
- [TestingFilesGenerator](concepts/tool-testing-files-generator.md) — `Tool` — donislawdev 给 QA 的测试文件生成器：22 种真实格式按字节大小生成，附「该如何处理」清单可作 CI fixture

### 写作 / De-AI（本批新增）
- [Sepia](concepts/tool-sepia-deai.md) — `Tool` — Nanako0129 的跨平台 De-AI 写作技能：从叙事架构层（节拍 / 视角 / 节奏 / 主观偏差）消除 AI 痕迹，不是改词改句表面

### 系统诊断 / 磁盘健康（本批新增）
- [lindiskinfo](concepts/tool-lindiskinfo.md) — `Tool` — pacmanics 受 CrystalDiskInfo 启发的 Linux 磁盘健康监控工具：图形化呈现 S.M.A.R.T. 与 NVMe 健康状态，给 Linux 用户一个等了多年的等价物

### 复核无新增（Re-check no-op）
- QingQ77 tailcat (2093854209729048582) — 与既有概念 [`tool-tailcat`](concepts/tool-tailcat.md) 同一项目（Tailscale 数据平面 netcat 替代），无新增信息
- QingQ77 darwin-vm (2094066357969264642) — 与既有概念 [`tool-darwin-vm`](concepts/tool-darwin-vm.md) 同一项目（QEMU 上跑 iOS / macOS 27 含 SPTM），无新增信息

### 跳过（Skipped / 质量门槛）
- Wen_Zw RT @AdhamDannaway Claude Code 101 for Designers (2094091069810167809) — 仅外部博客链接解释 Claude Code 行话，与既有 [`tool-claude-code`](concepts/tool-claude-code.md) 无新工程增量，按「质量门槛」跳过
- Wen_Zw RT @sheerluck_io GPUI 教程博客 (2093938978470977779) — 外部教程博客链接，与既有 [`tool-gpui-component`](concepts/tool-gpui-component.md) 无新增工程增量，按「质量门槛」跳过
- Wen_Zw RT @iamncdai chanhdai.com/blocks 缩略图更新 (2093986258020372812) — 仅个人作品集缩略图更新公告，无可独立收录的工程 / 工具 / 方法，按「质量门槛」跳过
- QingQ77「居然还有乌龟视角」+ 视频 (2093905760128487839) — 短语 + 短视频，无概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「大疆 avata360 新玩法」+ 视频 (2093929203993633274) — 短语 + 视频，无可独立收录的概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「回来了，都回来了。」+ 图 + 视频 (2093914449287749866) — 短语 + 图 + 视频，无概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「可以在末日生活一辈子」+ 视频 (2094035948275388609) — 短语 + 短视频，无概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「孙哥头上是什么🤣」+ 视频 (2093860754411884688) — 短语 + 短视频，无概念 / 工具 / 项目信息，按「质量门槛」跳过

## 本批新增（2026-08-31）

### AI / Agent 生态（本批新增）
- [Nanocoder](concepts/tool-nanocoder.md) — `Tool` — Nano Collective 社区集体维护的终端编码 Agent（npm / Homebrew / Nix Flakes 三种安装）
- [Headcount](concepts/tool-headcount.md) — `Tool` — 把 Claude Code 技能组织成 16 个部门 / 146 项技能的公司化框架，按需加载
- [codex-with-chatgpt](concepts/tool-codex-with-chatgpt.md) — `Tool` — 让网页版 ChatGPT 订阅额度当 Codex 规划 / 审查大脑，Codex 只负责执行
- [Vercel Labs `run`](concepts/tool-vercel-labs-run.md) — `Tool` — worker 线程隔离的 QuickJS 沙箱，让来宾代码只能调用宿主注入函数

### 桌面 / 系统工具（本批新增）
- [CleeCode](concepts/tool-cleecode.md) — `Tool` — Rust 写的终端 IDE，编辑器 + 文件树 + shell 终端共处一窗，200+ 语言高亮 + LSP
- [Beichen Pi / 北辰 Pi](concepts/tool-beichen-pi.md) — `Tool` — Windows 极简 Agent 桌面平台，面向本地部署模型，实时显示剩余 context / Token 消耗

### 终端 / 网络 / 系统管理（本批新增）
- [Swrm](concepts/tool-swrm.md) — `Tool` — Go 写的终端 BitTorrent 客户端（Bubble Tea），所有流量锁死 VPN 接口防 IP 泄漏
- [Tether](concepts/tool-tether-zackb.md) — `Tool` — C++ 写的 iPhone ↔ Linux 桥接套件（守护进程 + CLI + GTK + iOS App + 浏览器扩展）

### 前端 / 设计 / 移动（本批新增）
- [PanelUI](concepts/tool-panelui.md) — `Tool` — Expo / React Native UI 组件库 + Flow 节点编辑器（pan / zoom / 可拖拽节点 / 动画边线）
- [Simslim](concepts/tool-simslim.md) — `Tool` — iOS 模拟器瘦身工具，缓解低内存 Mac 跑 Xcode 模拟器的痛点

### 前端 / 设计资源（本批新增）
- [Cizgile](concepts/tool-cizgile.md) — `Tool` — 零依赖 URL slug 引擎（RFC 3986/3987 + 7 种文字转写 + IRI/URI）
- [Frontier Models Evidence Board](concepts/tool-frontier-evidence-board.md) — `Tool` — 用证据板风格可视化解释前沿模型与架构的交互式站点
- [Design Engineer Tools](concepts/tool-design-engineer-tools.md) — `Tool` — James Warner 维护的面向 Web 设计工程师的工具精选目录

### 复核无新增（Re-check no-op）
- QingQ77 S1N6H/pentest-harness (2094235220517978604) — 与既有概念 [`tool-pentest-harness`](concepts/tool-pentest-harness.md) 同一项目（授权渗透测试自托管 AI harness，基于 DeepSeek Harness 重新品牌），无新增信息

### 跳过（Skipped / 质量门槛）
- Wen_Zw RT @vinitj888 Annnimate.com (2094285395534237754) — 转发「创意 UI 组件」单句推荐，无项目仓库 / 安装说明 / 工程细节，按「质量门槛」跳过
- Wen_Zw RT @SwamiMalode RareUI sidebar (2094434470288031786) — 转发「Just shipped a new sidebar interaction」单句更新公告 + 演示视频，无独立项目增量，按「质量门槛」跳过
- Wen_Zw RT @wong2__ umami.is (2094434637628199414) — 单句「umami.is 好用」推荐，无项目仓库 / 安装说明 / 工程细节，按「质量门槛」跳过
- Wen_Zw RT @withden_ paceui.com/changelog (2094296774777385332) — 转发个人 UI 库 changelog 公告 + 链接，无项目仓库 / 独立增量，按「质量门槛」跳过
- Wen_Zw RT @Heylaosan www-marijanapav (2094433967525306727) — 转发「项目源码公开了👇」单 GitHub 链接，无项目描述 / 用途 / 上下文，按「质量门槛」跳过
- QingQ77「cool 高斯泼溅重建杭州灵隐寺」+ 视频 (2094285682357473286) — 单句 + 短视频，无具体工具 / 项目信息可提取，按「质量门槛」跳过
- QingQ77「可爱」+ 视频 (2094207635725996516) — 单短语 + 短视频，无工具 / 概念内容，按「质量门槛」跳过
- QingQ77「或许它也能把多玛姆劝退」+ 视频 (2094426402431107476) — 流行文化梗 + 视频，无具体工具 / 项目信息，按「质量门槛」跳过
- QingQ77「阴得没边了」+ 视频 (2094447287795867834) — 短语 + 短视频，无工具 / 概念 / 项目信息，按「质量门槛」跳过

## 本批新增（2026-09-01）

### AI / Agent 生态（本批新增）
- [hermes-agent-demo](concepts/tool-hermes-agent-demo.md) — `Tool` — Spring Boot 4 + Spring AI 2.0 多模型 Agent 运行时示例：把子代理 / Skills / 沙箱 / MCP / 人工审批统一进 SSE 事件流
- [pi-agenticoding](concepts/tool-pi-agenticoding.md) — `Tool` — 给 Pi 编码智能体加一层可组合工作流层：编排规则写进 prompt / Skills，让关键评审可以照着重复
- [PromptForge](concepts/tool-promptforge.md) — `Tool` — 本地优先的 LLM 提示词打分与改写工具（ModernBERT 7 维评分 + Qwen2.5 + LoRA 重写，PyPI 包名 `tuneprompt`）

### 写作 / 内容生成（本批新增）
- [NEO](concepts/tool-neo-hughhowey.md) — `Tool` — 休·豪伊（羊毛战记作者）开发的本地小说写作工具：可视化书架 + 默认成书排版（章节编号 / 首字下沉 / 智能标点）

### 视频 / 多媒体（本批新增）
- [MoneyPrinterTurbo](concepts/tool-moneyprinterturbo.md) — `Tool` — 一站式 AI 短视频生成器：输入主题 → 自动写脚本 / 找素材 / 配音 / 加字幕 → 出片

### 终端 / 编辑器（本批新增）
- [Runyte](concepts/tool-runyte.md) — `Tool` — Rust 写的终端开发工作区：Helix 风模态编辑 + 文件树 + 终端 + Git 共用同一批面板 / 命令 / 主题
- [TJA](concepts/tool-tja-de-verbs.md) — `Tool` — Go 写的终端老虎机式德语动词学习工具（前缀 × 词干双转轮互相过滤）

### 代码质量 / Git 工具（本批新增）
- [sanityme](concepts/tool-sanityme.md) — `Tool` — 一条命令装上 Git hooks，每次 commit 自动检查格式与拼写，让仓库历史从第一天起保持规范

### 桌面 / 跨平台（本批新增）
- [Todofy](concepts/tool-todofy.md) — `Tool` — Tauri + Preact + Rust 跨平台桌面待办（智能列表 / 标签 / 循环任务 / 番茄钟 / 托盘常驻）
- [JeffBox](concepts/tool-jeffbox.md) — `Tool` — .NET 9 + WPF 单文件 Windows 工具箱（约 450KB、零依赖，含待办 + Markdown + 启动器）
- [Kenote](concepts/tool-kenote.md) — `Tool` — Raycast Notes 平替：Tauri + React 跨平台 Markdown，所见即所得（输入即渲染）

### 运维 / 自托管（本批新增）
- [Ops Admin](concepts/tool-ops-admin.md) — `Tool` — Go + Vue 3 一体化运维管理平台（监控 + 资产 + 命令 + 告警）
- [securo](concepts/tool-securo.md) — `Tool` — 开源自托管隐私优先的个人理财管理器

### 前端 / 设计资源（本批新增）
- [Dotmatrix](concepts/tool-dotmatrix.md) — `Tool` — 点阵 / 字符微动画站点（前端微动效灵感参考）
- [text-effects.colorion](concepts/tool-text-effects-colorion.md) — `Tool` — 81 款免费文字效果集合站点（CSS / WebGL 实现）
- [tourcn](concepts/tool-tourcn.md) — `Tool` — 通过 shadcn 注册表安装的 Tour 引导组件，代码落在自家仓库、样式与项目天然一致
- [Icon Sites Collection](concepts/note-icon-sites-collection.md) — `Note` — 9 个图标资源站清单（itshover / iconly / nucleo / iconsax / isocons / hugeicons / morphicons / lucide-animated / movingicons）

### AI 硬件 / 嵌入式（本批新增）
- [FreeInk + Dayring](concepts/tool-freeink-dayring.md) — `Tool` — 嵌入式 UI 的本地闭环 AI 工作流：浏览器调视觉、AI 迭代 C++ 代码直到对齐

### 复核无新增（Re-check no-op）
- QingQ77 引用 microduck (2094674563011621162) — 与既有概念 [`tool-microduck`](concepts/tool-microduck.md) 同一项目（开源机器鸭），无新增信息
- QingQ77 PromptForge 重复 (2094783596758196689) — 与本批新增 [`tool-promptforge`](concepts/tool-promptforge.md) 同一项目（同链接同描述），无新增信息

### 跳过（Skipped / 质量门槛）
- Wen_Zw RT @MapleLeafCap bidclub.ai (2094720956875039073) — 电视剧观看推荐，无项目 / 工具信息，按「质量门槛」跳过
- Wen_Zw RT @insporadesign inspora.design (2094666556135596340) — 单一设计策展站点推荐 + Hero section 视频，与既有跳过条目同模式，无独立项目增量，按「质量门槛」跳过
- QingQ77「燕云十六声双生木偶」+ 视频 (2094815796975284319) — 游戏画面 + 短语，无工具 / 概念 / 项目信息，按「质量门槛」跳过
- QingQ77「除了 Apple vision 其他都是神」+ 视频 (2094799025598005345) — 情绪评价 + 短视频，无工具 / 概念 / 项目信息，按「质量门槛」跳过
- QingQ77 仅图片推文 (2094570857788330483) — 空标题 + 仅图片，无可提取的概念 / 工具 / 项目信息，按「质量门槛」跳过
- QingQ77「这才是真正的端游」+ 视频 (2094763142907916352) — 短语 + 短视频，无工具 / 概念 / 项目信息，按「质量门槛」跳过
- QingQ77「这对吗？」+ 视频 (2094623122230296682) — 短语 + 短视频，无工具 / 概念 / 项目信息，按「质量门槛」跳过
- QingQ77「什么黑科技」+ 视频 (2094778878929821724) — 短语 + 短视频，无工具 / 概念 / 项目信息，按「质量门槛」跳过
- Wen_Zw RT @QingQ77 todofy (2094778739959955867) — RT 与 QingQ77 原创（已建 [`tool-todofy`](concepts/tool-todofy.md)）同项目，本条仅 RT 留痕
