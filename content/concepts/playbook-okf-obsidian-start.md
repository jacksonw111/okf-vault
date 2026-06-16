---
type: Playbook
title: 在 Obsidian 里开始用 OKF
description: 一步一步把一个 Obsidian vault 改造成合规的 OKF v0.1 bundle，并准备好让人和 AI agent 都能消费。
tags: [okf, obsidian, howto]
timestamp: 2026-06-16T12:00:00Z
---

# 在 Obsidian 里开始用 OKF（分步 Playbook）

## 第 0 步：理解心智模型

- **vault = OKF bundle**（一个文件夹）
- **一条笔记 = 一个概念**（一件事、一个表、一个指标、一个术语、一份 runbook……）
- **笔记路径 = 概念身份证**（稳定、唯一、别乱挪）
- **frontmatter 的 `type` = 唯一必填字段**

## 第 1 步：决定你的概念类型词表

OKF 不强制类型名，你自己定。建议先用一小套，例如：

`Term`（术语）/ `Tool`（工具）/ `Playbook`（流程）/ `Note`（笔记）/ `Index`（目录页）
数据团队可用：`Dataset` / `Table` / `Metric` / `API` / `Runbook`。

> 先小后大。类型可以随时加，别一开始就过度设计。

## 第 2 步：建立目录骨架

```
<vault>/
├── index.md            ← bundle 根入口（渐进式披露）
├── concepts/           ← 所有概念文件
│   ├── index.md
│   ├── term-okf.md
│   ├── tool-obsidian.md
│   └── ...
└── log.md              ← 变更时间线（可选）
```

> 路径即身份。建议用稳定的、英文/连字符的文件名（如 `tool-obsidian.md`），避免中文/空格在跨工具时出问题。

## 第 3 步：给每条笔记加 frontmatter

每条笔记顶部至少写：

```yaml
---
type: Tool            # 必填
title: Obsidian       # 可选，但强烈建议
description: ...      # 可选，一句话摘要（agent 最依赖这个）
tags: [okf, tool]     # 可选
timestamp: 2026-06-16T12:00:00Z  # 可选
---
```

正文随便写：章节、表格、代码块、Mermaid 都行。

## 第 4 步：用链接把概念连成图

在正文里引用别的概念时，**用链接而不是纯文字**：

```markdown
参见 [Obsidian](./tool-obsidian.md) 和 [OKF 是什么](./term-okf.md)。
```

打开 Obsidian 的 **Graph View**，链接越多，图谱越密——这正是 OKF「目录即图」的体现。

## 第 5 步（可选但推荐）：进阶 Obsidian 增强

- **Dataview**：用 frontmatter 做查询，自动生成「所有 Playbook 列表」
- **Templater**：为每个类型建模板，新建笔记即带好 frontmatter
- **Git 插件**：把 vault push 到 git 仓库 → 实现 OKF「和代码同仓、可被 agent 拉取」

## 第 6 步：让 AI agent 消费你的 bundle（OKF 的真正价值）

- vault 就是个普通文件夹，agent 直接读 Markdown + frontmatter 即可
- 给 agent 一个入口：让它先读 `index.md` 做渐进式披露，再按链接下钻
- 你也可以把整个 bundle 压成 zip / 放进 git，交给任意 agent 框架——无需 SDK、无需翻译

## 第 7 步：维护

- `log.md` 记录重要变更（谁、何时、改了什么）
- 旧的、废弃的概念文件**别删路径**，可以加 `status: deprecated` 之类字段，保持身份稳定

## 自检清单

- [ ] 每个笔记都有 `type` 字段？
- [ ] 文件名稳定、有意义？
- [ ] 关键概念之间有链接？
- [ ] 有根 `index.md`？
- [ ] 放进 git 了？

## 相关概念

- [OKF 是什么](./term-okf.md)
- [Obsidian](./tool-obsidian.md)
