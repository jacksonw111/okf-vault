---
type: Index
title: 知识库仪表盘
description: 浏览 agent 产出的全部 OKF 概念。上半部分需要安装 Dataview 社区插件才能动态渲染；下半部分是无需插件的静态兜底，永远可用。
tags: [okf, dashboard]
timestamp: 2026-06-16T12:30:00Z
---

# 知识库仪表盘

## 按类型统计（需 Dataview 插件）

> 安装方法：Obsidian → Settings → Community plugins → 关闭安全模式 → Browse → 搜 "Dataview" → Install → Enable。
> 装好后下面这些  ```dataview ``` 代码块会自动变成实时列表。

**各类型数量**
```dataview
TABLE length(rows) AS 数量
FROM "concepts"
GROUP BY type
SORT type ASC
```

**全部概念（按更新时间倒序）**
```dataview
TABLE type, tags, timestamp AS 更新于
FROM "concepts"
WHERE type != "Index"
SORT timestamp DESC
```

**最近变更（来自 log.md 之外的笔记）**
```dataview
TABLE type, timestamp AS 更新于
FROM "concepts"
SORT timestamp DESC
LIMIT 10
```

---

## 静态兜底（无需任何插件，永远可用）

> 当 Dataview 没装时看这里。由 agent 在每次产出/更新概念时同步维护。

### Term（术语）
- [OKF 是什么](../concepts/term-okf.md)

### Tool（工具）
- [Obsidian](../concepts/tool-obsidian.md)

### Playbook（流程）
- [在 Obsidian 里开始用 OKF](../concepts/playbook-okf-obsidian-start.md)
- [OKF 生产者协议](../PRODUCER.md)

### Index（导航）
- [概念目录](../concepts/index.md)

## 相关概念
- [OKF 是什么](../concepts/term-okf.md)
- [生产者协议 PRODUCER](../PRODUCER.md)
