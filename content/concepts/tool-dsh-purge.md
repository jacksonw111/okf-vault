---
type: Tool
title: "dsh-purge"
description: "去掉 DSH（DeepSeek Harness）渲染本地规则时附加的\"仅供参考、不得覆盖\"削弱文案与默认沙箱审批，把权限交还给 AGENTS.md。"
resource: "https://github.com/YuJunZhiXue/dsh-purge"
tags: [deepseek-harness, dsh, plugin, agents-md, prompt-rewriting]
timestamp: "2026-08-25T19:30:00Z"
---

# dsh-purge

## 它是什么

[YuJunZhiXue/dsh-purge](https://github.com/YuJunZhiXue/dsh-purge) 是给 [DeepSeek Harness（DSH）](./note-deepseek-harness-handbook.md) 的一个插件。DSH 在渲染本地用户自定义规则（AGENTS.md / 规则文件）时，会**先在用户原文之上垫一层「仅供参考、不得覆盖」之类的削弱文案**，再配**默认沙箱 + 弹窗审批**——结果是用户写的强制规则被「软化」，权限边界牢牢攥在 DSH 自己手里。

dsh-purge 做反向操作：把那一层削弱文案**直接换成强制指令**，默认权限放开到 `full-access`，让 AGENTS.md 真正说了算。

![](https://pbs.twimg.com/media/HQdH9gcbMAAuPTy.png)

## 为什么用它 / 适合什么场景

- **想让 AGENTS.md 真的生效**：现有 DSH 行为等于把规则当参考，purge 后规则就是规则。
- **减少弹窗审批**：默认放开 `full-access`，本地受信任环境下不再每步都要 confirm。
- **自己跑 DSH、明白风险的用户**：清楚「放开权限意味着什么」，不需要再被审批流程挡。
- **自动化 / CI 场景**：让 DSH 在无人值守脚本里不需要模拟点击弹窗。

## 关键能力

| 能力 | 说明 |
|------|------|
| 文案改写 | 把「仅供参考」类的削弱语句替换成强制指令 |
| 权限放开 | 默认 `full-access`（仍可手动调回） |
| 规则优先 | 让用户写的 AGENTS.md 真正高于内置安全层 |
| 适配 DSH | 作为插件直接接入现有 DSH 安装 |
| 可回滚 | 不动 DSH 源码，关闭插件即恢复默认行为 |

## 相关概念

- [DeepSeek Harness（DSH）生态手册](./note-deepseek-harness-handbook.md) — DSH 的规则加载与渲染机制
- [awesome-deepseek-harness](./tool-awesome-deepseek-harness.md) — 同生态的插件 / 工具索引

## 参考链接

- 项目链接: <https://github.com/YuJunZhiXue/dsh-purge>
- 原始链接: <https://x.com/QingQ77/status/2092172629423894562>