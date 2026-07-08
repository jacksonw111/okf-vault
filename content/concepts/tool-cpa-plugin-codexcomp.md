---
type: "Tool"
title: "cpa-plugin-codexcomp（CLIProxyAPI gpt-5.5 reasoning 截断修复插件）"
description: "CLIProxyAPI 的 C ABI 插件，Go 编写：拦截 gpt-5.5 流式 Responses API，检测并修复 reasoning token 在 518n−2 处的推理截断，通过 encrypted_content 重放自动续写，减少模型「降智」。"
resource: "https://github.com/uf-hy/cpa-plugin-codexcomp"
tags: "[gpt-5, cli-proxy-api, plugin, reasoning-token, streaming, bug-fix, go]"
timestamp: "2026-07-08T09:40:00Z"
---

# cpa-plugin-codexcomp

## 它是什么

[cpa-plugin-codexcomp](https://github.com/uf-hy/cpa-plugin-codexcomp) 是 **CLIProxyAPI 的 C ABI 插件**（用 Go 编写），专门解决 **gpt-5.5 流式 Responses API 在「518n−2」处的 reasoning 截断 bug**。

通过拦截 + 用 `encrypted_content` **重放续写**自动修复，减少模型「半途断推理」造成的「降智」现象。

## 解决的问题

| 痛点 | 解法 |
|------|------|
| gpt-5.5 流式推理在 518n−2 字符处被截断 | 拦截流 → 检测 → 用 encrypted_content 自动续写 |
| 用户看到「推理到一半就停」 | 插件自动把后续推理补上 |
| 模型像「突然降智」 | 实际上是 streaming 截断的视觉假象，插件修掉 |

## 关键能力

| 能力 | 说明 |
|------|------|
| C ABI 插件 | 与 CLIProxyAPI 的 C ABI 兼容 |
| Go 实现 | 高性能、易分发 |
| 流式拦截 | hook 在 streaming 响应上 |
| encrypted_content 重放 | 利用 gpt-5.5 加密回放机制续写 |
| 自动透明 | 上层无需任何改动 |

## 参考链接

- [项目仓库](https://github.com/uf-hy/cpa-plugin-codexcomp)

## 相关概念

- [Codex X](./tool-codex-x.md) — 同为 Codex / GPT-5 生态工具
- [Codex Orange Book](./tool-codex-orange-book.md) — 同为 Codex / GPT-5 系列参考资源