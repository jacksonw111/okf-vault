---
type: Tool
title: "Obsidian Fileclass"
description: "Obsidian 插件，把 frontmatter 属性定义为「类型 schema」——字段输入变下拉 / 日期选择器，类型不符自动标错，让手动 frontmatter 也能有类型校验。"
resource: "https://github.com/mdelobelle/fileclass"
tags: "[obsidian, plugin, frontmatter, schema, validation, open-source]"
timestamp: "2026-08-13T19:53:00Z"
---

# Obsidian Fileclass

## 它是什么
**Obsidian 插件**。Obsidian 的 frontmatter 通常全靠手敲——类型对不对、字段缺没缺没人管。Fileclass 把**属性定义成一份类型 schema**：

- 字段输入变成**下拉 / 日期选择器**等结构化控件
- 类型不符 / 字段缺失**自动标出来**
- 让「手写 frontmatter」也能享受**类型校验**

## 为什么用它 / 适合什么场景
- Obsidian Vault 体量大、frontmatter 字段多——靠记忆填会出错。
- 想把 frontmatter 当作「带类型的元数据」管理（而非自由文本）。
- 在 OKF 这类「frontmatter 是关键 metadata」的流程里——为属性加一层 schema 校验能直接复用本插件思路。
- 团队 / 多人对同一 Vault 协作——统一字段语义。

## 关键能力
| 能力 | 说明 |
|------|------|
| 形态 | Obsidian 插件 |
| 核心机制 | frontmatter schema 定义 |
| 输入控件 | 下拉 / 日期选择器等 |
| 校验 | 类型不符 / 字段缺失提示 |
| 适用 | 大型 Vault / 团队协作 |

## 相关概念
- [Obsidian](tool-obsidian.md) — 宿主；Fileclass 安装在该工具上
- [在 Obsidian 里开始用 OKF](playbook-okf-obsidian-start.md) — OKF 的 Obsidian 起步流程；OKF 也依赖 frontmatter，Fileclass 是给该流程加类型校验的天然搭档
- [OKF 是什么](term-okf.md) — OKF 规范把 `type` 列为唯一强制字段，但仍有许多推荐字段；Fileclass 能为这些字段做类型化

## 媒体
- 示意图：<https://pbs.twimg.com/media/HPftD3YboAAJbVy.jpg>

## 项目链接
- 项目主页：<https://github.com/mdelobelle/fileclass>