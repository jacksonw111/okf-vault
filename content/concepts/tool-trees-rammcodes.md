---
type: "Tool"
title: "Trees（IDE 风格文件树组件）"
description: "一个打磨精致的开源「文件树」组件库——支持搜索、拖放、多选、Git 状态指示器、键盘导航；定位 IDE 风格的文件浏览器，可直接塞进代码编辑器、开发者工具、文件管理器。"
tags: "[frontend, ui-component, file-tree, open-source, ide, react]"
timestamp: "2026-06-17T00:00:00Z"
resource: "https://github.com/rammcodes/trees"
---

# Trees（IDE 风格文件树组件）

## 它是什么

[`Trees`](https://github.com/rammcodes/trees) 是「**IDE 风格文件浏览器**」组件库——给前端项目提供**开箱即用**的文件树 UI：

- 搜索（实时过滤）；
- 拖放（节点重排 / 移动）；
- 多选 + 复选框；
- Git 状态指示器（modified / untracked / added…）；
- 键盘导航；
- 自定义节点渲染。

## 为什么值得收藏

- **「文件树」看似简单，做精很难**——搜索 + 拖放 + 多选 + 性能（大目录）每一个坑都要填。Trees 把这些都填好了。
- **不是 demo，是生产组件**——作者风格是「打磨精致」+ 「直接可用」。
- **跨框架可用**——HTML / JavaScript 原生版本，按 README 提示引入即可（同时支持 React / Vue 包装，按项目使用方式取舍）。

## 适用场景

| 场景 | 用 Trees 干嘛 |
|------|--------------|
| 在线代码编辑器 | 文件浏览面板 |
| 开发者工具 / DevTool | 配置文件 / 日志 / 资源浏览 |
| 文件管理器 | SaaS 文件系统的左侧目录 |
| AI Agent UI | 让 agent 看到/操作的文件结构可视化 |
| 知识库前端 | 像 Obsidian 的文件树，但嵌进 web |

## 关键能力

| 能力 | 说明 |
|------|------|
| 实时搜索 | 输入即时过滤 |
| 拖放 | 节点重排 / 跨节点移动 |
| 多选 + 复选 | 批量操作 |
| Git 状态 | modified / untracked / added / deleted / renamed 颜色标记 |
| 键盘导航 | 方向键 / Enter / Space / 多选 shift |
| 自定义节点 | 可传入渲染函数覆盖默认图标 / 文本 |
| 虚拟滚动 | 大目录（>10k 节点）保持流畅 |

## 与本知识库其他概念的关系

- [Cabinet](tool-cabinet.md) — Cabinet 是 Obsidian + AI 代理；Trees 是 web 端文件树组件，两者都涉及「文件作为一等公民」的 UI，但层级不同（Cabinet 是应用，Trees 是组件）。

## 相关概念

- [Cabinet](tool-cabinet.md) — 同为「文件作为一等公民」UI，Cabinet 是应用层、Trees 是组件层
