---
type: "Tool"
title: "zpack（流式资源打包 / .zpak 归档）"
description: "masonschafercodes 出的游戏 / 应用资源打包工具：把整个资源目录打成单个 .zpak 文件，运行时按名直接查归档；打包流式处理不占大量内存，解出来与原目录字节完全一致。"
tags: "[gamedev, resource, packing, archive, cli, runtime]"
timestamp: "2026-08-26T16:30:00Z"
resource: "https://github.com/masonschafercodes/zpack"
---

# zpack（流式资源打包 / .zpak 归档）

## 它是什么

[`zpack`](https://github.com/masonschafercodes/zpack) 是 masonschafercodes 写的资源归档工具，专为**游戏 / 应用读取散装资源**的场景：

- 把整个资源目录打成**单文件 `.zpak`**——不必在运行时维护一堆散文件路径
- **打包流式处理**——不会因目录大就一次性吃满内存
- **运行时按名查归档**——查表即可拿到原始字节
- **解出来字节完全一致**——和原目录拆分比对无差
- 配套运行时，把「原本走 FileSystem 的 IO」换成「读归档」基本无侵入

## 为什么用它 / 适合什么场景

- 游戏 / 桌面应用配置 / 美术资源 散装加载麻烦，文件还容易**漏 / 被改**
- 想要**单可执行 + 单资源文件**的干净发布产物
- 资源量大（GB 级），不想打包时把内存涨爆
- 需要确保部署版本资源与原始素材**字节一致**（避免 hash 不匹配）

## 关键能力

| 能力 | 说明 |
|------|------|
| 流式打包 | 不一次性载入全目录到内存 |
| 字节一致 | 解出来与原目录相同 |
| 运行时直查 | 避免散文件路径管理 |
| 单文件产物 | `.zpak` 一文件即发布包 |
| 轻依赖 | 上手门槛低 |

## 参考链接

- [项目链接](https://github.com/masonschafercodes/zpack)
