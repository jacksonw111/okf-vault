---
type: "Tool"
title: "fast-browser-use（本机浏览器自动化）"
description: "APUS AI Lab 把 Qwen3.5-9B / 35B-A3B 权重搬到本机，靠 MLX 或 PyTorch 驱动浏览器点击 / 填表。先扫一遍页面只收可见可点元素，模型在一个 token 的 logits 上挑动作——避免生成不存在的 CSS / XPath 选择器。"
resource: "https://github.com/APUS-AI-Lab/fast-browser-use"
tags: "[browser-use, local, llm, qwen, mlx, pytorch, automation, tool]"
timestamp: "2026-09-24T21:55:00Z"
---

# fast-browser-use（本机浏览器自动化）

## 它是什么

[fast-browser-use](https://github.com/APUS-AI-Lab/fast-browser-use) 是 APUS AI Lab 出品的本机浏览器自动化工具：把 Qwen3.5-9B / 35B-A3B 权重搬到本机，用 MLX 或 PyTorch 推理，把浏览器点击 / 填表这类操作完全交给本地模型，省掉云端 API 调用和账单。

## 关键设计

| 元素 | 说明 |
|------|------|
| 模型 | Qwen3.5-9B / 35B-A3B |
| 推理 | MLX 或 PyTorch（本机） |
| 页面扫描 | 只收当前可见、可点的元素，凑成候选动作清单 |
| 动作输出 | 模型在一个 token 的 logits 上挑定一个动作 |
| 选择器幻觉防护 | 不逐字解码，因此不会吐出页面里不存在的 CSS / XPath |

## 适用场景

- 想把浏览器自动化跑在本地以保护隐私 / 节省 API 费用
- 想用 Qwen3.5 系列模型做浏览器操作
- 想避免「模型生成不存在的选择器」导致的失败

## 注意点

- 本机推理需要合适的硬件（MLX 仅 Apple Silicon）
- 仅在「可见可点」的元素上做选择器，对隐藏元素支持有限

## 原始链接
- 项目主页：<https://github.com/APUS-AI-Lab/fast-browser-use>

## 相关概念
- [Browserbase Stagehand](./tool-browserbase-stagehand.md) — 云端浏览器自动化
- [Computer Use（计算机使用）](./term-computer-use.md) — 通用术语：让 AI 直接读屏 + 模拟键鼠