---
type: Index
title: "知识库仪表盘"
description: "知识库导航中枢。下方链接全部指向 Quartz 自动生成的聚合页（目录索引 / 标签索引），内容随知识库增长自动更新——无需 Dataview。"
tags: "[okf, dashboard]"
timestamp: 2026-06-17T00:00:00Z
---

# 知识库仪表盘

> 本站由 **Quartz** 生成，它不是 Obsidian，**不支持 Dataview 插件**。
> 这里改用 Quartz 原生的「目录索引」和「标签索引」——它们由站点根据实际文件**自动生成**，效果等同于 Dataview 的聚合查询，而且永远是最新。

## 📂 浏览全部概念

→ [**concepts 目录索引**](concepts/)：自动列出所有概念文件，按最后修改时间排序。

## 🏷️ 按标签浏览

→ [**全部标签**](tags/)

常用标签（点击进入对应的自动聚合页）：

- [okf](tags/okf) · [term](tags/term) · [tool](tags/tool) · [playbook](tags/playbook)
- [producer](tags/producer) · [agent](tags/agent) · [protocol](tags/protocol) · [markdown](tags/markdown)

## 🧭 主要入口

- [知识库首页]()
- [生产者协议 PRODUCER](PRODUCER)
- [变更记录 log](log)
- [投喂资料 inbox](inbox/README)

## ✅ 自检 / 当前规模

- 概念文件数：见 [concepts 目录索引](concepts/)
- 全部标签：见 [标签索引](tags/)
- 最近变更：见 [log](log)

---

## 💡 在本地 Obsidian 想要 Dataview 动态表？

本地 Obsidian 已装 Dataview 插件。新建一篇笔记，粘贴下面的代码即可得到动态表格（**仅 Obsidian 本地有效，Quartz 不渲染**）：

~~~md
```dataview
TABLE type, tags, timestamp AS 更新于
FROM "concepts"
WHERE type != "Index"
SORT timestamp DESC
```
~~~
