---
type: "Tool"
title: "ASu-skills（Codex 中文求职工作流插件）"
description: "装进 Codex 的中文求职工作流插件，把「贡献刷绿点 / 经历改写 / 简历排版 / 投递漏斗」拆成 4 个可单独调用的入口，每步都直接产出可编辑的 HTML 与 CSV。"
tags: "[codex, job-search, resume, open-source, skill-pack]"
timestamp: "2026-08-15T00:10:00Z"
resource: "https://github.com/Hisn00w/ASu-skills"
---

# ASu-skills（Codex 中文求职工作流插件）

## 它是什么

`ASu-skills` 是一组给 Codex（ChatGPT 桌面端 / CLI 编码代理）使用的斜杠命令式中文求职工作流，安装后在 Codex 里直接 `/contributor`、`/asu`、`/resume`、`/offer` 调用。整套插件不依赖云端服务，全程在本地生成可编辑的 HTML 与 CSV 文件，思路是把「刷绿点 → 经历改写 → 简历排版 → 投递进度」串成一条流水线，每步单独可跑。

## 四个斜杠命令

| 命令 | 作用 | 产物 |
|------|------|------|
| `/contributor` | 自动在 GitHub 找自己能合并的小 PR 并刷绿点 | PR 列表 + 自动 commit |
| `/asu` | 把底层经历改写成贴合目标岗位的招聘语言 | 结构化「岗位语言」版简历 |
| `/resume` | 18 个中文模板 + A4 单/双页排版 + 浏览器内编辑文字/照片/字体/颜色 + 按截图复刻布局 + 导出 PDF | HTML 简历 + PDF |
| `/offer` | 汇总招聘邮件 / 截图做投递漏斗 | `application-tracker.html`（支持搜索、筛选、CSV/JSON 备份） |

## 为什么用它 / 适合什么场景

- **求职流程完全可重复**：每一步都跑在本地、不依赖 SaaS，把「面试前的所有材料准备」拆成可调用的脚本。
- **`/resume` 把排版做成可编辑 HTML**：截图别人的简历布局也能复刻，无需装 Word / LaTeX。
- **`/offer` 自带漏斗视图**：把分散在邮箱 / 微信 / 截图里的招聘进度聚合到一张表，方便看转化率。
- **适合中文环境**：默认模板、内置字体都按中文简历习惯设计。

## 关键能力

| 能力 | 说明 |
|------|------|
| `/contributor` 刷绿点 | 主动找自己能合并的小 PR，覆盖多个 GitHub 账号 |
| `/asu` 经历改写 | 把口语化经历翻译成招聘语言，匹配 JD 关键词 |
| `/resume` 编辑器 | 浏览器内 WYSIWYG，文字 / 照片 / 字体 / 颜色都可调 |
| `/resume` 截图复刻 | 上传一张截图，反推生成同款版式 |
| `/resume` PDF 导出 | 浏览器内 → PDF，中文排版不丢字 |
| `/offer` 进度漏斗 | 按公司 / 岗位 / 状态 / 下一步聚合，CSV/JSON 双格式备份 |
| 18 套模板 | 单页 / 双页 / 不同风格，适合不同岗位类型 |

## 工作流示意

```
/contributor  →  GitHub 绿点（简历亮点素材）
        ↓
/asu          →  把绿点经历翻译成招聘语言
        ↓
/resume       →  18 模板 + 截图复刻 → HTML / PDF
        ↓
/offer        →  投出去后聚合邮件 / 截图 → 漏斗视图
```

## 适用人群

- 中文环境求职 / 转岗 / 找实习的开发者。
- 想把「求职过程工程化、自动化」的人。
- 不想依赖付费简历 SaaS、要完全本地可编辑的人。

## 参考链接

- [项目链接](https://github.com/Hisn00w/ASu-skills)

## 相关概念

- [CodexPro](tool-codexpro.md) — ChatGPT Web ↔ 本地仓库 MCP 桥
- [Codex Control Plane MCP](tool-codex-control-plane-mcp.md) — Codex Desktop 的持久化任务队列 MCP
- [Codex-X](tool-codex-x.md) — Tauri 2 跨平台 Codex 桌面端管理器