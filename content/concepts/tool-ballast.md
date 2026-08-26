---
type: "Tool"
title: "ballast（Claude Code 上下文关键词规则注入器）"
description: "svy04 把 Claude Code 里「上个月纠正过的事下个月再纠正一次」的痛点做成工具：把规则 / 结论搬进文件，消息命中关键词时由 hook 自动把规则原文塞回上下文。"
tags: "[claude-code, hook, rules, memory, key-word, agent]"
timestamp: "2026-08-26T16:30:00Z"
resource: "https://github.com/svy04/ballast"
---

# ballast（Claude Code 上下文关键词规则注入器）

## 它是什么

[`ballast`](https://github.com/svy04/ballast) 是 svy04 给 Claude Code 写的「规则 / 结论回流」机制：

> 在 Claude Code 里上个月纠正过的事，这个月往往得再纠正一遍，规矩和结论全躺在对话记录里。

ballast 把规则 / 结论**搬进独立文件**，**消息一命中关键词**就由 **hook 自动把规则原文塞回上下文**——无需人工反复复述。

## 为什么用它 / 适合什么场景

- 想让「我们项目里 XX 应该这样处理」的结论**跟时间无关地**回灌到 Agent 上下文
- 想在长项目里保留历史决策，避免新人 / 新会话每次都得重新解释
- 不想每次都把这些规则塞进 CLAUDE.md 造成主规则文件臃肿

## 关键能力

| 能力 | 说明 |
|------|------|
| 关键词触发 | 自动检测消息里的关键词 |
| Hook 注入 | 命中即把规则原文塞回上下文 |
| 规则文件化 | 结论写文件，不靠人脑复述 |
| 长期保值 | 历史结论跨月跨会话有效 |
| Claude Code 集成 | 直接挂到 harness |

## 参考链接

- [项目链接](https://github.com/svy04/ballast)
