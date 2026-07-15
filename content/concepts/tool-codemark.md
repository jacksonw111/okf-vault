---
type: "Tool"
title: "codemark（DanielCardonaRojas/codemark）"
description: "Rust 写的代码书签工具,基于 tree-sitter 解析代码语义结构定位书签,改名字 / 重排代码后书签照样能跟到原位置。"
resource: "https://github.com/DanielCardonaRojas/codemark"
tags: "[bookmark, code-navigation, rust, tree-sitter, semantic]"
timestamp: "2026-07-15T00:26:00Z"
---

# codemark

[codemark](https://github.com/DanielCardonaRojas/codemark) 是 Rust 写的**代码书签工具**,用 tree-sitter 抓代码的语义结构定位书签,而不是死记行号。

## 它解决了什么

普通书签/锚点工具靠行号定位:你改了函数名、调整了顺序,书签就漂了。codemark 把代码结构建模成 AST,书签指向的是「函数 / 类 / 块」这种语义节点,重命名或重排后仍能找回原位置。

## 关键能力

| 能力 | 说明 |
|------|------|
| 树语法定位 | 用 tree-sitter 解析语义,改个名书签还找得到 |
| 跨语言支持 | tree-sitter 内置几十种语言 parser |
| Rust 单二进制 | 一份 release 即可分发,无外部运行时 |

## 适合什么场景

- 大型代码库要长期保存「我读到这里」的位置。
- 写读书笔记 / 源码导读类内容,标注特定函数 / 块。
- 不想被 rebase、refactor 反复打断书签。

## 媒体

![](https://pbs.twimg.com/media/HNHGrLmbYAAuCCc.jpg)

## 参考链接

- [项目仓库](https://github.com/DanielCardonaRojas/codemark)

## 相关概念

- [Grove (tree-sitter 工具集)](./tool-grove-tree-sitter.md) — 同样基于 tree-sitter 的代码操作工具集,可作为底层基础设施互补
