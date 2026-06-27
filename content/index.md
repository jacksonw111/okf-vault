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

### 编程语言 / 工具链

- [Node.js All-in-One](concepts/tool-node-all-in-one.md)
- [PHP 8.5 零依赖微型框架](concepts/tool-php85-micro-framework.md)
- [LaTeX→MathML 编译器](concepts/tool-latex-mathml-compiler.md) — 7.69KB 构建期编译器，比 KaTeX 快 3 倍
- [Haskell 反应式交互式笔记本](concepts/tool-haskell-reactive-notebook.md) — Markdown 嵌入 Haskell 代码块
- [Nefoin](concepts/tool-nefoin-nerdfont.md) — 一键安装 Nerd Font 的轻量 CLI
- [PP-OCRv6 Studio](concepts/tool-ppocrv6-studio.md) — 飞桨 PP-OCRv6 三档模型本地 OCR
- [Rust + QUIC 高性能 IM 后端](concepts/tool-rust-quic-im.md) — Actix-web + QUIC + P2P NAT 打洞
- [laravel-zero-console](concepts/tool-laravel-zero-console.md) — Laravel Zero CLI 通用 trait（表格 / 错误码 / 路径）

### 后端 / 部署 / 自托管

- [Single Server](concepts/tool-single-server.md) — 一台 Linux 服务器串 Cloudflare + Tailscale + Kamal 一键部署
- [OPG](concepts/tool-opg-backend.md) — 一人公司多 app 后端控制面（账号 / AI 网关 / 视频 / 支付）
- [NasberryPi](concepts/tool-nasberry-pi.md) — 树莓派轻量 NAS CLI，一条命令配 Samba
- [docker-android](concepts/tool-docker-android.md) — Docker 镜像封装 Android 模拟器
- [DataBuff](concepts/tool-databuff.md) — AI Native OpenTelemetry APM，链路追踪 + AI 智能分析
- [cfnew-deployer](concepts/tool-cfnew-deployer.md) — Cloudflare Pages 部署器面板，邮箱 + API Key 一键 Worker / Pages + KV
- [MediaCrawler](concepts/tool-mediacrawler.md) — 七平台自媒体数据采集（小红书 / 抖音 / 快手 / B 站等），Playwright + JS 表达式签名
- [Gorest](concepts/tool-gorest.md) — Codex 驱动的 2D 动画精灵表生成器与场景合成工作台

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

## 金融 / 数据

- [a-stock-data](concepts/tool-a-stock-data.md)
- [global-stock-data](concepts/tool-global-stock-data.md) — 美港股全栈数据 Skill（期权链 / 财报三表 / 503 GAAP 指标）
- [ngrok / webernetes](concepts/tool-ngrok-webernetes.md)
- [Finnhub 美股 API](concepts/tool-finnhub-api.md) — 免费层 60 req/min 的美股行情/财报/新闻 REST API
- [chinese-buy-us-stock-guide](concepts/tool-chinese-buy-us-stock-guide.md) — 大陆投资者美股实操指南，开户 / 税务 / 合规 / 入金 / 出金
- [AI 托管个人资产的方向](concepts/tool-personal-asset-via-claude.md) — AI 全面接管个人财务的机会与风险

## 网络 / 代理

- [ClashOmega](concepts/tool-clash-omega.md) — Clash 代理规则管理 Chrome 扩展
- [HypoMux](concepts/tool-hypomux.md) — Windows 多网卡带宽聚合下载加速
- [shadowrocket-config](concepts/tool-shadowrocket-config.md) — 防 DNS 泄露配置（ACL4SSR）

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

## 操作手册

- [在 Obsidian 里开始用 OKF（Playbook）](concepts/playbook-okf-obsidian-start.md)
- [VLESS + WebSocket + TLS 绕过电信 QoS](concepts/playbook-vless-bypass-telecom-qos.md)
- [SPA 内嵌 PDF 查看器（react-pdf + Hono 代理）](concepts/playbook-spa-pdf-viewer.md) — 跨前后端的 PDF 渲染 + 鉴权代理 + byte-range 透传 + 东财失效链兜底
- [应用外壳侧边栏（base-ui + motion 多层装配）](concepts/playbook-app-shell-sidebar.md) — shadcn primitive → AppShellSidebar 中间层 → 应用层数据的三层架构
- [双轴主题系统（next-themes + shadcn data-theme）](concepts/playbook-dual-axis-theming.md) — Mode × Preset 双维度自由组合 + 防 FOUC + 跨设备同步

## 配套文档

- [输出模板目录](./templates/_README.md)
- [变更记录](./log.md)

## 你（人类）的日常就是

1. 把资料丢进 [`inbox/`](./inbox/README.md)
2. 对 agent 说「**处理 inbox**」
3. agent 按 PRODUCER.md 产出到 `concepts/`、更新索引与 log、归档资料
4. 去 [`overview.md`](./overview.md) 看结果
