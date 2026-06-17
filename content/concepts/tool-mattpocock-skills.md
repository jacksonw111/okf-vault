---
type: "Tool"
title: "mattpocock/skills"
description: "英国 TS 布道师 Matt Pocock 维护的 Claude Code skills 合集（.claude/commands/ 形态），定位「Real Engineers 准备的」；代表作 /grill-me、/zoom-out、/caveman、/hand-off、/teach 等，是学习 agent skills 写法的最佳入门。"
tags: "[ai, agent, skills, claude-code, prompt-engineering]"
timestamp: 2026-06-17T00:00:00Z
resource: "https://github.com/mattpocock/skills"
---

# mattpocock/skills

## 它是什么

[`mattpocock/skills`](https://github.com/mattpocock/skills) 是英国 TypeScript 布道师 **Matt Pocock** 维护的 [Claude Code](./tool-claude-code.md) skills 合集。每个 skill 一个 `.md` 文件，落在 `.claude/commands/` 下，被社区广泛认为是「Real Engineers 写的」参考实现——形式简单、几行 prompt 写完，但每条都对应一个开发中的真实经验 / 套路。

## 为什么值得关注

- **门槛低** —— 大部分 skill 只有几句话，新手也能读完理解。
- **场景真实** —— 都是 Matt 自己在日常开发中反复用的「老手套路」，不是炫技。
- **in-progress 也公开** —— 草稿阶段的 skill 也 push 上来，方便学习他的思考过程（如 `/teach`）。
- **是社区 [agent skills 概念](./term-agent-skills.md) 的事实标杆之一**。

## 代表 skill（vikingmute @x 推荐 2026-06）

| Skill | 作用 |
|-------|------|
| `/grill-me` | 让代理对自己刚做的方案做三轮反驳（假设 / 边界 / 失败） |
| `/zoom-out` | 把视角拉远：这件事的更大上下文是什么？现在做对吗？ |
| `/caveman` | 极简表达：把方案压到最少字、说人话 |
| `/hand-off` | 交接清单：把这个任务交给下一个人需要知道的一切 |
| `/teach` | 让代理「当老师」讲明白一个概念——学习用 |

> 社区建议：把仓库 rss 订阅、把 commit 当文章读——他加一个新 skill 就是一篇「我刚悟到的套路」。

## 使用方式

```bash
# 把 skills 拉到自己的项目
git clone https://github.com/mattpocock/skills .claude/skills-mattpocock
# 或者直接把 .claude/commands/ 里的 .md 复制到自己的 .claude/commands/
cp .claude/skills-mattpocock/commands/*.md .claude/commands/
```

启动 `claude`，输入 `/` 就能看到所有可用 skill。

## 相关概念

- [Agent Skills 是什么](./term-agent-skills.md)
- [Claude Code](./tool-claude-code.md)
- [shadcn/improve](./tool-shadcn-improve.md)
- [Hyperagent 设计网格 skill](./tool-hyperagent-design-skill.md)
- [Archify](./tool-archify.md)
- [JSON-Render / 生成式 UI](./tool-json-render.md)
- [OKF 是什么](./term-okf.md)
