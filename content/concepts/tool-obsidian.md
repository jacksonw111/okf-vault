---
type: Tool
title: "Obsidian"
description: "基于本地 Markdown 文件的个人知识库工具。一个 vault = 一个文件夹里的 Markdown 文件，原生支持 YAML frontmatter（Properties）和双向链接，自动构建知识图谱——因此它既是 OKF 的天然编辑器，也是 OKF 的天然消费者。"
resource: "https://obsidian.md"
tags: "[okf, tool, pkm, markdown]"
timestamp: 2026-06-16T12:00:00Z
---

# Obsidian

## 为什么 Obsidian 天生适合 OKF

| OKF 要求 | Obsidian 现状 |
|----------|---------------|
| 一个概念 = 一个 Markdown 文件 | ✅ vault 就是文件夹，一个笔记一个 `.md` |
| YAML frontmatter | ✅ 原生 Properties，自动渲染成表单 |
| 文件之间链接 → 图谱 | ✅ `[[wikilink]]` 与 Markdown 链接都能进图谱视图 |
| 目录 + index.md | ✅ 文件夹 + 任意 `index.md` |
| 可放进 git | ✅ 纯文本，天然版本管理 |

换句话说：**你的 Obsidian vault 只要补上 OKF 的几条小约定，就变成一个合规的 OKF bundle。**

## 让 OKF 更好用的 Obsidian 配置

1. **Settings → Files & Links**
   - 关闭「New link format」用相对路径，或保持默认；确保链接可移植
   - 开启「Detect all file extensions」便于 `.md` 链接解析
2. **Properties（frontmatter）**：直接在笔记顶部写 `---` YAML 块，Obsidian 会渲染成属性面板
3. **图谱视图（Graph View）**：链接越多越好看，正好印证 OKF「目录即图」的理念
4. **推荐插件**（可选）
   - `Dataview` —— 用 frontmatter 字段做查询（如「列出所有 type=Playbook 的笔记」）
   - `Templater` —— 给每类概念做带 frontmatter 的模板
   - `Git` —— 把 vault 纳入版本控制，实现 OKF「与代码同仓」的理念

## 链接写法的选择

OKF 规范示例用的是**标准 Markdown 链接** `[X](./x.md)`（最可移植、GitHub/agent 友好）。Obsidian 原生 `[[wikilink]]` 更适合纯 Obsidian 内部。建议：**对外要可移植的 bundle 用 Markdown 链接；纯本地用 wikilink 也行**。两者 Obsidian 都能识别进图谱。

## 相关概念

- [OKF 是什么](./term-okf.md)
- [在 Obsidian 里开始用 OKF](./playbook-okf-obsidian-start.md)
