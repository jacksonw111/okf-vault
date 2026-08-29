---
type: Playbook
title: "simplify-codebase（编码代理的「先证明再删除」清理工作法）"
description: "给编码智能体一套「先证明再删除」的工作法：在现有代码库里找出真正多余的复杂度，确认删掉不会破坏现有行为、边界和兼容性之后再动手清理。"
resource: "https://github.com/tt-a1i/simplify-codebase"
tags: [playbook, coding-agent, refactor, simplification, deletion, prove-before-delete]
timestamp: "2026-08-29T21:30:00Z"
---

# simplify-codebase（编码代理的「先证明再删除」清理工作法）

## 适用场景

在大型现有代码库里，编码智能体经常被指示「**清理一下冗余代码**」——但删错了就是事故。该 Playbook 给出一种**带证据链**的删除流程，适合：

- 接手一个历史项目，发现大量疑似冗余 / 过时 / 未引用的代码；
- LLM 编码代理被要求「重构 / 简化」，但又不能乱删；
- 团队 review 时需要知道「每条删除的理由和证据」。

## 前置条件

- 仓库有完整的测试套件（单测 / 集成测 / e2e）；
- CI / 类型检查可运行，能 1 分钟内给出反馈；
- 编码代理具备：grep / 阅读 / 跨文件推理 / 生成补丁能力。

## 工作流（先证明再删除）

1. **盘点**：用 grep / 静态分析列出「疑似冗余」清单（未引用的导出 / 已弃用 API / 重复工具函数等）。
2. **追根**：对每条候选项，逆向追溯所有调用点、文档提及、配置引用、序列化键名、第三方合约。
3. **分类**：按删除风险打三档——
   - 🟢 安全：所有调用点已迁移、无外部合约引用；
   - 🟡 谨慎：调用点迁移完成，但还有动态反射 / 字符串拼接引用；
   - 🔴 高风险：公共 API / 序列化字段 / 配置文件键名（删了用户挂）。
4. **证明**：对 🟢 / 🟡 项，先**注释化 / 标记 deprecated**、跑测试、再**单条删除**——每步都有 diff + 测试结果留痕。
5. **观察**：上线 / 集成测试后看一段窗口期无回归，才在下一轮彻底删。
6. **审计**：每条删除都对应一条记录——「删了什么 / 为什么删 / 跑了哪些测试 / 影响的 commit」。

## 验证 / 自检

- [ ] 每条删除都对应一条「证明 + 调用点扫描」记录；
- [ ] 删除后 CI 全绿；
- [ ] 公共 API / 序列化字段只在充分 deprecation 周期后才删；
- [ ] 没有「为简化而简化」的纯审美删除。

## 相关概念

- [Codex Standard Devflow](./playbook-codex-standard-devflow.md) — 编码代理的标准化开发流程，simplify-codebase 是其「清理」子环节
- [Multimodal UI Test Automation](./playbook-multimodal-ui-test-automation.md) — UI 端到端验证，配合 simplify-codebase 给出删除的「前后行为不变」证据

## 参考链接

- 项目链接：<https://github.com/tt-a1i/simplify-codebase>
- 原始推文：<https://x.com/QingQ77/status/2093554233270554881>