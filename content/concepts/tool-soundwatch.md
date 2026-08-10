---
type: "Tool"
title: "SoundWatch"
description: "matthart1983 写的 Rust 终端音频诊断工具，跑在 macOS / Linux 上：十个标签页分别把设备、流、电平、频谱、延迟、xrun 列出，最后的 Insights 把数字翻译成「该看哪一页」的人话建议。NetWatch 系列的音频分支。"
resource: "https://github.com/matthart1983/soundwatch"
tags: [audio, diagnostics, terminal, rust, macos, linux]
timestamp: "2026-08-10T07:54:00Z"
---

# SoundWatch

## 它是什么

[SoundWatch](https://github.com/matthart1983/soundwatch) 是 NetWatch 系列的新成员（之前已有网络诊断方向的兄弟工具）：一款**用 Rust 写的终端音频诊断工具**，跨 macOS / Linux。它把音频栈的健康状况切成十个标签页——设备、流、电平、频谱、延迟、xrun 等各占一页。最后一个 **Insights** 标签页干一件特别的事：把前面几个标签页里的数字「翻译成人话」，直接告诉你「如果你看到 X，去第几页」。

## 为什么用它 / 适合什么场景

- 排查音频故障（声音卡顿 / 设备不可用 / 时不时爆音）：传统方式是挨个改设置碰运气，SoundWatch 把信号汇总在一处。
- 现场直播 / 录音棚前的快速自检：终端跑起来不挂额外 GUI。
- DevOps / 直播工程团队的远端排查脚本：终端里能跑，可批量化。

## 关键能力

| 能力 | 说明 |
|------|------|
| Rust 实现 | 单一二进制，跨 macOS / Linux |
| 十标签页 | 设备 / 流 / 电平 / 频谱 / 延迟 / xrun 等分页 |
| 实时数据 | 音频流参数持续刷新 |
| Insights 人话化 | 数字→「你该看哪一页」建议 |
| 终端可用 | 不挂 GUI，远程 / 自动化友好 |

## 媒体

![](https://pbs.twimg.com/media/HPQG7hUaMAAGYmS.jpg)

## 参考链接

- [项目仓库](https://github.com/matthart1983/soundwatch)
- [原始链接](https://x.com/QingQ77/status/2086722718620176461)
