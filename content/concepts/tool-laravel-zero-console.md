---
type: Tool
title: "laravel-zero-console（Laravel Zero CLI 通用 trait 集合）"
description: "为 Laravel Zero（及普通 Laravel）命令行命令提供可复用 trait 的 PHP Composer 包：FormatsOutput 负责表格渲染 / 颜色 / 日期，HandlesApiErrors 统一 API 异常退出码，ResolvesPath 处理路径参数解析。"
resource: "https://github.com/jeffersongoncalves/laravel-zero-console"
tags: [php, laravel, laravel-zero, cli, composer, library]
timestamp: 2026-06-26T16:50:00Z
---

# laravel-zero-console

## 它是什么

laravel-zero-console 是一个 **PHP Composer 包**，给 [Laravel Zero](https://laravel-zero.com/)（以及普通 Laravel）写的 CLI 命令提供三个开箱即用的 trait，把每个 CLI 项目都要重写一遍的"杂活"封装好：

| Trait | 职责 |
|-------|------|
| `FormatsOutput` | 表格渲染、状态颜色化、日期格式化 |
| `HandlesApiErrors` | 把 API 异常统一转为标准退出码 |
| `ResolvesPath` | 路径参数与当前工作目录的解析（兼容相对/绝对/用户主目录） |

要求 PHP `^8.2`，Composer 一行安装即用，无额外配置。

## 为什么用它

- **避免重复造轮子**：每个 Laravel Zero 项目都要写一遍表格 / 错误码 / 路径解析
- **统一 CLI 行为**：API 错误退出码标准化，方便 CI 编排
- **保持代码短**：业务命令只关心业务逻辑，外围杂活交给 trait

## 关键能力

| 能力 | 说明 |
|------|------|
| 表格渲染 | 一行 trait 调用，告别手撸 `str_pad` |
| 状态颜色 | 成功 / 警告 / 失败 颜色统一 |
| 日期格式化 | 默认按本地化输出 |
| 错误码统一 | API 异常 → 标准退出码 |
| 路径解析 | 兼容相对 / 绝对 / `~` 展开 |

## 原始链接

- [项目仓库](https://github.com/jeffersongoncalves/laravel-zero-console)
- [原始推文剪藏](https://x.com/QingQ77/status/2070340270751687052)

## 相关概念

- [PHP 8.5 零依赖微型框架](./tool-php85-micro-framework.md) — 同样是 PHP 工具链生态，方向是"零依赖极简框架"
- [Node.js All-in-One](./tool-node-all-in-one.md) — 不同语言但相同"少写脚手架代码"诉求
- [Biome](./tool-biome.md) — 在 JS 生态里扮演"省掉 lint / 格式杂活"角色，与本包在 PHP CLI 里做的事异曲同工
