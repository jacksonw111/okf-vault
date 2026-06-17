---
source: manual-test
purpose: 验证 push 进 inbox 是否自动触发 pipeline
---

# Push 触发测试

这是一份测试资料，用来验证：往 content/inbox/ push 新文件后，OKF Pipeline 是否被自动触发。

内容：Anthropic 的 Claude Code 是一个终端原生的 AI 编码 agent，支持 --permission-mode auto（自动批准工具调用）、-p（非交互 print 模式）、--output-format 等参数。它通过 ANTHROPIC_BASE_URL / ANTHROPIC_AUTH_TOKEN / ANTHROPIC_MODEL 环境变量接入第三方 Anthropic 协议端点。
