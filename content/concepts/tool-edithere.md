---
type: "Tool"
title: "EditHere（Inginnng 出品的 C++ 截图标注 → AI JSON 工具）"
description: "EditHere 是 C++ 桌面截图标注工具：全局快捷键呼出截图，圈区域、写意见，把识别出的组件拖到新位置、缩放尺寸，再把原图、批注、位置尺寸变化一起打包成 JSON 给 AI，让 AI 直接去改代码。"
resource: "https://github.com/Inginnng/EditHere"
tags: "[screenshot, annotation, c++, desktop, json, ai-coding, design-feedback]"
timestamp: "2026-10-02T14:22:00Z"
---

# EditHere（Inginnng 出品的 C++ 截图标注 → AI JSON 工具）

## 它是什么

[EditHere](https://github.com/Inginnng/EditHere) 是 Inginnng 出品的 **C++ 桌面截图标注工具**——把「截图 → 圈区域 → 写意见 → 拖组件调位置 → 打包 JSON → 给 AI 改代码」这一整套流程本地化，零云依赖。

## 三步工作流

1. **截图**——全局快捷键呼出截图界面
2. **标注 + 拖动**——圈区域写意见；可把识别出的 UI 组件拖到新位置、调整尺寸
3. **导出**——把「原图 + 批注 + 位置尺寸变化」一起打包成 JSON

## 为什么用它 / 适合什么场景

| 场景 | EditHere 的好处 |
|------|----------------|
| 给 AI 反馈界面问题 | 不止「截图 + 文字描述」，还把组件级位置变化一起给 |
| 设计师 ↔ 开发者 | 设计师改完直接 export 一份 JSON 给开发者 / AI |
| 远程协作 | 不必约会议讲「这个按钮往下移 8px」 |
| 数据敏感 | C++ 本地处理，不上传云端 |
| 批量反馈 | 一份 JSON 能挂多个修改点 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 全局快捷键 | 任意界面都能呼出截图 |
| 组件识别 | 截图后能识别 UI 组件边界 |
| 拖拽改位置 | 组件级位置 / 尺寸调整 |
| 多点批注 | 一张图里挂多个修改意见 |
| JSON 导出 | 直接喂给 AI 编码 agent |

## 输出 JSON 示例

```json
{
  "screenshot": "https://example.com/page.png",
  "annotations": [
    { "region": [120, 80, 200, 60], "text": "改成 primary 色" }
  ],
  "moves": [
    { "component": "submit-btn", "from": [320, 200], "to": [320, 240] }
  ]
}
```

## 参考链接

- 原始链接：<https://x.com/QingQ77/status/2106026416852664596>
- 项目链接：<https://github.com/Inginnng/EditHere>

## 相关概念

- [Mesurer](./tool-mesure.md) — 另一类截图标注工具，定位测距 / 录屏
- [Claude Code](./tool-claude-code.md) — 可作为 EditHere 输出的下游消费者
