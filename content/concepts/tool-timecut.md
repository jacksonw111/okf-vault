---
type: "Tool"
title: "TimeCut (foodpm)"
description: "把 NAS 上的监控摄像头自动循环录像，并用大模型从一天画面里挑出含人员、车辆、包裹的片段剪成精华、生成日记，省去手动翻看录像；整套流程塞进 NAS 的 Docker 里。"
resource: "https://github.com/foodpm/timecut"
tags: "[nas, surveillance, ai-clipping, docker, ffmpeg, fastapi, video, ai-vision]"
timestamp: "2026-08-04T20:30:00Z"
---

# TimeCut (foodpm)

## 它是什么

[TimeCut](https://github.com/foodpm/timecut) 把 NAS 上的监控摄像头**自动循环录像**，并用**大模型从一天画面里挑出含人员 / 车辆 / 包裹的片段**剪成精华、生成日记，**省去手动翻看录像**。

整套流程塞进 NAS 的 Docker 里：**go2rtc** 拉摄像头 RTSP 流，浏览器看实时画面（延迟不高）；录像、剪精华、记日记三件事由 **FFmpeg + Python/FastAPI** 在后台轮流干，**按天保留的旧录像到点自动清掉**。

## 为什么用它 / 适合什么场景

- **NAS 一体化**：不需要云服务，Docker 部署在自家 NAS。
- **AI 自动精华**：大模型自动识别有意义的画面（人员 / 车辆 / 包裹），不用人盯着。
- **日记化**：一天结束后自动生成视频日记。
- **存储友好**：按天滚动清理，长期跑不爆盘。

## 关键能力

| 能力 | 说明 |
|------|------|
| 摄像头自动循环录像 | 持续写盘，不漏录 |
| AI 挑精华 | 大模型识别人员 / 车辆 / 包裹片段 |
| 自动生成日记 | 一天一段视频日记 |
| RTSP 拉流 | 走 go2rtc 兼容大多数家用摄像头 |
| 浏览器实时看 | Web 端低延迟实时预览 |
| 自动清理 | 按天保留的旧录像到期自动删 |
| Docker 一体化 | 一套 Compose 拉起整套流程 |

## 技术栈

| 组件 | 角色 |
|------|------|
| go2rtc | 摄像头 RTSP / WebRTC 流 |
| FFmpeg | 录像 + 切片 |
| Python / FastAPI | 后台任务调度 + AI 触发 |
| 大模型（外部） | 画面内容识别 |

## 参考链接

- [项目仓库](https://github.com/foodpm/timecut)

## 相关概念

- [go2rtc](./tool-go2rtc.md) — Go 单二进制摄像头流媒体服务器，本项目用它拉流
- [Timecode Agent](./tool-timecode-agent.md) — 长视频带时间戳证据账本，转录优先 + 按需视觉验证
- [KPanel](./tool-kpanel.md) — Linux 服务器面板，TimeCut 部署在 NAS 上时可一起管
