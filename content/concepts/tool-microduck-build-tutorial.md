---
type: "Playbook"
title: "microduck 装机教程（从买件到跑起来）"
description: "microduck 桌面机器鸭的全流程装机指南：硬件 BOM 选购、舵机接线、固件烧录、上电测试、接入 AI agent 的全流程；面向硬件创客与机器人入门者。"
resource: "https://github.com/pollen-robotics/microduck"
tags: "[robotics, hardware, diy, build-guide, microduck, ai-agent]"
timestamp: "2026-09-12T22:00:00Z"
---

# microduck 装机教程

## 适用场景
- 想自己从零搭一台 [microduck](./tool-microduck.md) 桌面机器鸭。
- 教机器人入门课程、希望按一套成熟流程带学生跑通。
- 想把 microduck 当作 AI agent 的物理外壳，先让硬件层跑起来再说。

## 前置条件
- 基本的焊接 / 接线能力（舵机连接到主控板）。
- 一台能跑 Python 的电脑（用于烧录固件）。
- 愿意读英文文档与开源仓库 README。

## 步骤概览
1. **采购 BOM**：按 microduck 仓库 README 列出 BOM 采购舵机、主控板（如 ESP32 / Raspberry Pi Pico）、3D 打印件、外壳螺丝。
2. **3D 打印结构件**：下载 STL 文件，打印骨架 / 外壳 / 头部。
3. **组装机械部分**：装舵机到骨架、连杆、腿部。
4. **接线**：舵机信号线接到主控板 PWM 引脚；供电走独立 5V。
5. **烧录固件**：克隆仓库，按 README 用 `esptool.py` / `picotool` 烧入舵机控制固件。
6. **上电自检**：测试单舵机摆动、步态复位、头部转动。
7. **接入 AI agent（可选）**：把舵机控制 API 暴露给大模型，让 LLM 决定动作。

## 验证 / 自检
- [ ] 通电后舵机不抖、不发热。
- [ ] 行走 / 扭头基本动作流畅。
- [ ] 主控板串口能看到调试日志。
- [ ] （如接 AI）大模型能成功发出"前进 / 后退 / 转头"指令。

## 参考链接

- 项目仓库：<https://github.com/pollen-robotics/microduck>

## 相关概念

- [microduck](./tool-microduck.md) — 桌面机器鸭本体介绍
- [Autonomous OS](./tool-autonomous-os.md) — 可装在机器人上的开源操作系统
