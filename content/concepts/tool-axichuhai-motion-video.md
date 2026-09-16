---
type: "Tool"
title: "axichuhai-motion-video-skills"
description: "专门做动效视频的开源 Skill 合集，一条命令装进 Claude Code 或 Codex 就能让 AI 直接生成丝滑动效视频；16 个 Skill 覆盖品牌宣传片、K 线蜡烛图动画、黑胶唱片播放器、procedural 鱼群动画、Claude 打字机动画、SVG logo 动效、Remotion 3D 滚动长廊等。"
resource: "https://github.com/axichuhai/animation-skills"
tags: "[motion, video, agent-skill, remotion, claude-code, codex]"
timestamp: "2026-09-16T16:19:00Z"
---

# axichuhai-motion-video-skills

## 它是什么

[axichuhai/animation-skills](https://github.com/axichuhai/animation-skills) 是**专门做动效视频的开源 Skill 合集**：一条命令装进 **Claude Code** 或 **Codex**，AI 就能直接生成丝滑动效视频。**16 个 Skill** 覆盖：

- 品牌宣传片
- K 线蜡烛图动画
- 黑胶唱片播放器
- Procedural 鱼群动画
- Claude 打字机动画
- SVG logo 动效
- Remotion 3D 滚动长廊
- ……

每个 Skill 对应一类具体视觉输出，**说一句话就能触发**。装完后告诉它想要什么效果，它自己去调对应 Skill 跑出来。

## 为什么用它 / 适合什么场景

- 想让 AI 编码 agent 直接出可发布的动效视频。
- 不想每次都从头写 Remotion / Three.js / Canvas 代码。
- 在 Claude Code / Codex 已有工程里复用同一套动效流水线。

## 关键能力

| 能力 | 说明 |
|------|------|
| 16 个 Skill | 按场景细分，按需加载 |
| 一行安装 | 装进 Claude Code / Codex 不改开发环境 |
| 自然语言触发 | 描述效果即可，不用写 spec |
| 多引擎混合 | Remotion / SVG / Procedural / 3D 滚动 |
| 可二次扩展 | Skill 结构标准化，可继续叠加新效果 |

## 媒体

- 视频：<https://video.twimg.com/amplify_video/2099841086063591424/vid/avc1/3824x2160/W8yECpRBbrQ9CZWC.mp4?tag=29>

## 相关概念

- [motion-skills（iart）](./tool-motion-skills.md) — 类似定位的动效 Skill 集合（50 个，按 14 分类）
- [video-skills-toolkit](./tool-video-skills-toolkit.md) — 偏「字幕驱动」流水线；axichuhai 这套偏「视觉表达」
- [lottiefiles-motion-design-skill](./tool-lottiefiles-motion-design-skill.md) — 动画导演思维 Skill；axichuhai 这套偏直接产出