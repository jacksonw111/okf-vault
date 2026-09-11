---
type: "Tool"
title: "swarmllm（浏览器标签页 P2P 分布式推理）"
description: "把大模型按层切开分给同一房间里各设备的浏览器标签页，免安装、经 WebRTC 直连做 P2P 推理，单台设备装不下的 27B 模型也能跑；GB10 上推测解码达 16 tok/s。"
resource: "https://github.com/Nehanth/swarmllm"
tags: "[llm, p2p, webrtc, browser, inference, distributed]"
timestamp: "2026-09-11T22:05:00Z"
---

# swarmllm

## 它是什么

[Nehanth/swarmllm](https://github.com/Nehanth/swarmllm) 是一个**浏览器端 P2P 分布式推理框架**：把大模型按层切开，分别跑在同一房间内多台设备的**浏览器标签页**里，标签页之间通过 **WebRTC** 直连传输中间结果，无需安装、无需服务器。

## 关键数字

| 指标 | 数值 |
|------|------|
| 设备组合 | GB10 |
| 推测解码吞吐 | **16 tok/s**（反超 llama.cpp 的 8.0） |
| 模型规模 | 27B（单设备装不下，靠多设备协作） |
| 拓扑 | 浏览器标签页 + WebRTC 直连 |

## 为什么用它 / 适合什么场景

- 想在本地跑**装不下的大模型**（27B / 70B / 更大）但只有几台家用机器。
- 想做**零部署** demo——只要浏览器打开就能用。
- 研究 P2P / WebRTC 在 LLM 推理中的可行性。

## 关键能力

| 能力 | 说明 |
|------|------|
| 模型分片 | 按层切到多设备 |
| WebRTC 直连 | 标签页之间 P2P 通信 |
| 免安装 | 浏览器打开即用 |
| 推测解码 | 显著快于普通逐 token 解码 |
| 局域网协同 | 同一房间多设备拼出单设备跑不了的模型 |

## 参考链接

- 项目仓库：<https://github.com/Nehanth/swarmllm>

## 媒体

- 视频：<https://video.twimg.com/amplify_video/2097866215259848704/vid/avc1/1562x1120/MNuyHwUQuH1vhS-F.mp4?tag=29>

## 相关概念

- [Browser-Use Pi](./tool-browser-use-pi.md) — 浏览器端的 Web Agent
- [lantunnel](./tool-lantunnel.md) — NAT 穿透型私有组网
- [note-local-llm-hardware-guide](./note-local-llm-hardware-guide.md) — 本地 LLM 硬件指南
</content>
</invoke>