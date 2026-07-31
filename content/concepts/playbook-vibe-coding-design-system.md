---
type: "Playbook"
title: "Vibe Coding 设计系统八步法（david0520782123 / Wen_Zw 转推）"
description: "针对 Vibe Coding「陷在 UI 调试地狱」问题，从 VI（视觉识别）→ Design Token → 基础组件 → 状态 → 交互契约 → 动效 → 可撤销 → AI 约束，完整搭一套设计系统，把每次随机设计变成可复用规则，让 AI 真正按规范出 UI。"
resource: "https://x.com/Wen_Zw/status/2083224848139214900"
tags: "[design-system, vibe-coding, ai-coding, design-token, methodology, ui]"
timestamp: "2026-07-31T20:30:00Z"
---

# Vibe Coding 设计系统八步法

Vibe Coding 常常卡在 UI 上而不是代码上——按钮高度、圆角、Hover 颜色、选中态……每次让 AI 重新生成都会临时猜测，最终整个项目风格像东拼西凑。**这套八步法用一组可复用的设计规则替 AI 做决策**，把 UI 调试地狱变成「一次定义、长期复用」。

## 适用场景

- 用 AI 编码 agent（Cursor / Claude Code / Codex / Copilot…）一次性出整个项目的 UI 但风格散乱
- 团队或一人多 agent 协作时统一视觉与交互
- 想把「凭感觉改 UI」变成「按规范改 UI」

## 前置条件

- 已有或能写出一个最小可运行的项目骨架
- 愿意为视觉决策先投入 1–2 小时定义规则
- 选定一个底层组件库（Radix UI / shadcn/ui / Material UI / Ant Design 等）作为「原材料」

## 步骤

### 第一步：建立产品的视觉识别（VI）

不直接写组件，先回答最基础的问题：

- Logo 是什么？
- 核心主题色 / 陪衬色 / 中性色 / 状态色（success / warning / danger / info）
- 字体家族（衬线 / 无衬线 / 等宽）
- 是否同时支持亮暗主题

VI 决定产品整体感觉：开发者工具偏「高密度 + 克制 + 等宽」，内容阅读偏「留白 + 节奏 + 中性色」，消费级偏「鲜明 + 大圆角 + 显式动效」。**没有 VI，AI 就会在极简工具 / 圆润 SaaS / 炫酷渐变 / 默认组件库风格之间来回摇摆**。

### 第二步：用 Design Token 取代硬编码

不要在组件里写 `color: #2563eb`、`padding: 12px`，改用：

```
color: var(--color-primary);
padding: var(--space-md);
border-radius: var(--radius-md);
```

Token 至少包括：`color-primary / secondary / accent / background / surface / border / text-primary / text-secondary / success / warning / danger`、`space-xs / sm / md / lg / xl`、`radius-*`、`shadow-*`、`font-*`、`line-height-*`、`motion-*`。

直接好处：

1. 改主题只改一组 CSS 变量，不用全局替换十六进制色。
2. 亮 / 暗主题通过替换 Token 值实现，组件不动。
3. AI 生成代码时从已有 Token 选，而不是自由创造。
4. 代码审查可机械判定「硬编码颜色 / 随机圆角」= 不符合设计系统。

### 第三步：统一基础组件

最常见的问题不是没有组件，而是**同一种组件有十个版本**。把以下组件做成「唯一来源」：

- Button / Input / SearchBar / Select / Checkbox / Radio
- Tabs / Tree / Table / Dialog / Tooltip / Dropdown / Toast / Command Palette

业务代码组合这些基础组件，**禁止重写**。可以基于 shadcn/ui、Radix UI、MUI 等做封装层，但组件库是「原材料」，设计系统是「最终规范」——你仍需统一按钮高度、聚焦 / 错误状态、Tab 选中方式、Table 行密度、Tooltip 时机和内容、Dialog 宽度与遮罩。

### 第四步：定义组件状态（不止默认样式）

每个可交互元素至少有 8 种状态：

| 状态 | 用途 |
|------|------|
| default | 默认呈现 |
| hover | 鼠标悬停（不改变布局） |
| active | 按下（轻微位移或亮度变化） |
| focus | 键盘聚焦（统一 focus ring） |
| selected | 选中（强调色背景 + 强调色文字） |
| disabled | 禁用（降低对比度，禁止交互） |
| loading | 加载（避免重复提交） |
| error | 错误（明确提示） |

关键不是「选中后该改哪个属性」，而是**整个产品必须用一套规则**——资源树、菜单、列表、表格行、下拉选项都不能各自发明状态。

### 第五步：建立交互契约

设计系统管「长什么样」也管「如何响应」。

**Hover 契约**：告诉用户元素可交互 + 不打断操作地补充信息；普通颜色反馈 100–150ms 完成；触屏设备不能依赖 Hover；只有图标含义不明确时才用 Tooltip；Tooltip 不承载必须被读的重要信息。

**按钮契约**：当前区域最重要操作用 Primary Button；一个区域不出现多个视觉权重相同的 Primary Button；危险操作用明确文案而非模糊的「确定」；提交中显示 loading 并防止重复提交；完成后必须有可感知反馈。

### 第六步：统一动画与反馈

为每个组件加不同动画 = 让产品显得「热闹但不专业」。最小动效 Token：

```
motion-fast: 100ms    // Hover、按钮反馈
motion-normal: 200ms  // 下拉、Tooltip
motion-slow: 300ms    // Dialog、页面级过渡
```

默认缓动：ease-out。列表重排 / 拖拽用专门的空间动画。移动端可配震动反馈；桌面端用 Toast / 状态栏 / 行内提示。

验收问题四件套：操作能否撤销？失败能否恢复？用户知不知道系统在做什么？完成后用户有没有收到反馈？

### 第七步：默认支持可撤销，不用确认框

「确定要删除吗？」「确定要关闭吗？」这类确认弹窗很快让人无意识点确定，**不如默认执行 + 结果反馈 + 短期撤销**：

- 删除文件 → 移到回收站 + Undo
- 关闭 Tab → 历史记录中可恢复
- 修改配置 → 撤销 / 重置按钮

### 第八步：把设计系统写进 AI 的工作约束

光有设计系统不够，**得让 AI 按它工作**。把以下规则做成项目级约束文件（如 `.cursor/rules` / `AGENTS.md`）：

```
本项目使用统一设计系统。
禁止在业务组件中硬编码颜色、间距、字号和圆角。
所有样式必须使用语义 Design Token。
所有按钮必须使用统一 Button 组件。
所有输入框必须使用统一 Input 组件。
Tab、Tree、Table、SearchBar 不允许重复实现。
所有交互组件必须包含 hover、focus、disabled、loading 状态。
默认支持亮色和暗色主题。
新增组件前，先检查现有组件库是否已经存在对应实现。
```

并在每次提交前自检：是否新增硬编码颜色？是否出现非标准间距？是否重复实现已有组件？是否遗漏暗色主题？是否遗漏键盘焦点状态？是否改了现有组件的交互规则？

## 验证 / 自检

- [ ] VI 文档（色板 / 字体 / Logo / 品牌方向）写完
- [ ] Design Token（颜色 / 间距 / 圆角 / 阴影 / 字号 / 动效）以 CSS 变量落地
- [ ] 基础组件库（Button / Input / Tabs / Tree / Table / Dialog 等）抽象完毕
- [ ] 组件状态（hover / focus / selected / disabled / loading / error）有统一规则
- [ ] Hover / Primary Button 等「交互契约」已写明
- [ ] 动效 Token（fast / normal / slow + 缓动函数）已定义
- [ ] 默认操作支持撤销而非确认弹窗
- [ ] AI 约束文件（`.cursor/rules` 或 `AGENTS.md`）已写好并在用
- [ ] 给出截图后，AI 能按规范实现新页面而不是临场猜测

## 一个最小可用的设计系统应包含

1. 品牌与视觉方向
2. 亮 / 暗主题
3. 颜色 / 字体 / 间距 / 圆角 / 阴影 Token
4. Button / Input / Tabs / Tree / Table 等基础组件
5. Hover / Focus / Selected / Disabled / Loading 等状态
6. Tooltip / Toast / Dialog 等反馈规则
7. 动画时长和缓动规则
8. **禁止硬编码和重复实现的工程约束**（给 AI 的 rule file）

形式不重要——可以是 Markdown 规范 + 一组 CSS Variables + 一个组件预览页面 + 一份 AI 编码约束。关键是**规则明确、可执行、被所有页面共用**。

## 相关概念

- [DESIGN.md 最佳实践（101babich 整理）](./note-design-md-best-practices.md) — 把设计系统信息沉淀进单个 DESIGN.md，喂给 AI 看
- [Vercel Design System](./tool-vercel-design-system.md) — 公开的 design.md 风格系统页面，是这套方法的公开样本
- [Penpot](./tool-penpot.md) — 开源自托管设计协作工具，能直接产 design token 喂给代码
- [vibe-coding-rules](./tool-vibe-coding-rules.md) — 给 AI 编码 agent 装的「编程纪律」六步流水线，与本条「设计纪律」互补
- [Claude Code](./tool-claude-code.md) — 终端原生 AI 编码 agent，通过 CLAUDE.md / AGENTS.md 吃这套约束
- [local-hermes-portable](./tool-local-hermes-portable.md) — 本地 LLM agent，规则同样适用
