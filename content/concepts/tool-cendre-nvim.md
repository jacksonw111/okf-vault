---
type: "Tool"
title: "cendre（Neovim 木柴光谱配色）"
description: "只做深色的 Neovim 配色主题，五个色相全部从燃烧木柴的实测光谱推算出来；编辑器外的终端同款配色由同一份调色板自动生成。"
tags: "[neovim, color-theme, dark-theme, palette, terminal]"
timestamp: "2026-08-15T10:21:00Z"
resource: "https://github.com/Aejkatappaja/cendre"
---

# cendre（Neovim 木柴光谱配色）

## 它是什么

`Aejkatappaja/cendre` 是一款只做深色的 Neovim 配色主题，名字 *cendre* 是法语「灰烬」。

**核心特点**：五个色相（红、橙、黄、蓝、品红）的取色**全部从燃烧木柴的实测光谱推算**——不是凭感觉挑色，而是从物理测光谱里抽出的「真实木柴色」。同一份调色板**自动生成 Neovim 外的终端配色**（iTerm2 / Kitty / Alacritty / WezTerm 等），编辑器与终端视觉一致。

> ![](https://pbs.twimg.com/media/HPphfekbQAAgik8.png)

## 为什么用它 / 适合什么场景

- **审美独特**：木柴光谱 → 灰烬色调，比常规深色主题更柔和、不刺眼。
- **色彩科学严谨**：色相有物理依据，不是凭空调色。
- **编辑器 + 终端同步**：一份调色板，nvim 与 terminal 视觉一致。
- **极简**：只做深色，不为「亮色 / 暗色切换」做妥协。

## 关键能力

| 能力 | 说明 |
|------|------|
| 五个色相 | 红 / 橙 / 黄 / 蓝 / 品红，全部来自木柴光谱 |
| 自动生成终端配色 | iTerm2 / Kitty / Alacritty / WezTerm 等 |
| 仅深色 | 不为亮色妥协，专注夜间使用 |
| Tree-sitter 支持 | 完整语法高亮 |
| LSP 诊断色 | 错误 / 警告 / 信息色与主题一致 |
| 配色脚本 | 同款调色板工具可单独抽出复用 |

## 与相关主题的差异

| 主题 | 取色依据 | 同步终端 |
|------|----------|----------|
| tokyo-night | 城市夜景美学 | 需手写配置 |
| gruvbox | 复古怀旧 | 需手写配置 |
| [luna.nvim](tool-luna-nvim.md) | 纯黑灰阶 + 冷暖强调色 | 内置 |
| **cendre** | **燃烧木柴实测光谱** | **自动生成** |

## 适用人群

- 喜欢深色主题、且审美疲劳于「常规暗色配色」的开发者。
- 想让编辑器与终端配色完全一致的人。
- 对「色相有物理依据」这件事有要求的人。

## 参考链接

- [项目链接](https://github.com/Aejkatappaja/cendre)

## 相关概念

- [luna.nvim](tool-luna-nvim.md) — Neovim 暗色配色主题，纯黑灰阶底 + 4 种冷暖强调色