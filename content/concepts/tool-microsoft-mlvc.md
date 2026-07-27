---
type: "Tool"
title: "Microsoft MLVC（机器学习视频编解码器）"
description: "微软开源的机器学习视频编解码器 MLVC：360p@30fps 下达到 H.264 同等画质时，H.264 需 ~1 Mbps，MLVC 只需 ~122 kbps（约为原码率 1/8）；结合移动端普及的 NPU 硬件，定位为「短视频时代带宽/存储省钱利器」。"
resource: "https://github.com/microsoft/mlvc"
tags: [video-codec, machine-learning, compression, microsoft, open-source, h264]
timestamp: "2026-07-27T20:30:00Z"
---

# Microsoft MLVC（机器学习视频编解码器）

## 它是什么

`microsoft/mlvc` 是微软**开源的机器学习视频编解码器**（ML Video Codec）。在 360p@30fps 下，达到与 H.264 相同的画质时，H.264 需要约 **1 Mbps** 码率，而 MLVC 只需约 **122 kbps**——约为原码率的 **1/8**。考虑当下绝大多数移动设备都已搭载 NPU，MLVC 的推理加速预期会非常快，定位是「**短视频公司节省带宽 / 存储费用**」。

## 为什么用它 / 适合什么场景

- 想把视频**带宽 / 存储成本压到 1/8**（同等画质下对比 H.264）；
- 目标平台多为**移动端 / 边缘端**，能借助 NPU 实时解码；
- 短视频点播、安防回放、视频会议存档等**码率敏感**业务；
- 愿意以**编码端复杂度**（依赖 ML 模型推理）换取**传输 / 存储侧大幅节省**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 超低码率 | 360p@30fps 等同 H.264 画质时仅 ~122 kbps（≈ 1/8 码率） |
| 开源实现 | 微软在 GitHub 开源模型与推理代码 |
| NPU 友好 | 适配移动 / 边缘 NPU 硬件加速解码 |
| 同画质替代 H.264 | 主打替代 H.264 的「短视频省钱位」 |
| 端侧部署路径 | 移动端 NPU 普及，普及周期预期短 |

## 媒体 / 原始链接

- 项目链接：<https://github.com/microsoft/mlvc>
- 项目介绍：<https://techcommunity.microsoft.com/blog/linuxandopensourceblog/announcing-the-open-source-release-of-ml-video-codec-mlvc/4539875>
