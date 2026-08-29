---
type: Tool
title: "darwin-vm（QEMU 上跑最新版 iOS / macOS 的虚拟化研究环境）"
description: "jprx/darwin-vm：在 QEMU 上启动最新版 iOS 与 macOS 27（含 SPTM），支持从 iPhone 12 到 17、每代 M1–M5 Mac；可调试 / 修改 kernel / SPTM / TXM / launchd / dyld / 用户程序，秒进 root shell，无需越狱。"
resource: "https://github.com/jprx/darwin-vm"
tags: [qemu, darwin, ios, macos, sptm, security-research, virtualization]
timestamp: "2026-08-29T21:30:00Z"
---

# darwin-vm（QEMU 上跑最新版 iOS / macOS 的虚拟化研究环境）

## 它是什么

[jprx/darwin-vm](https://github.com/jprx/darwin-vm) 是把**最新 iOS 与 macOS 27** 引导到 **QEMU 虚拟机**里的开源工程，支持包括 **SPTM**（Secure Page Table Monitor）在内的现代 Apple 安全特性：

- **覆盖机型广**：iPhone 12–17 全代、每代 M1–M5 Mac；
- **完整可调试**：kernel、SPTM、TXM、launchd、dyld、用户程序均可修改、可 GDB 调试；
- **秒进 root shell**：直接启动到 root shell，几秒即可用；
- **无需越狱 / 无需内核补丁**：以可执行 root 的用户态程序视角运行；
- **支持特性多**：SPTM、TXM、MTE/MIE、genter/gexit、GXF/SPRR/GL0–2、AMCC、AIC v1–3、Apple timer、众多 sysregs；
- **跨主机**：QEMU 能跑的平台都能跑，**不必 ARM CPU**；
- **自动化**：几分钟内 setup 完。

## 为什么用它 / 适合什么场景

- **Apple 安全研究**：在不受真机限制的环境里研究 SPTM / TXM / 新指令集；
- **越狱研究 / 内核安全**：需要可调试的 root 环境，但不想碰真机 / 不想买开发证书；
- **工具链测试**：要在多代 Apple 平台上验证 Frida / Hopper / 自家 patch；
- **CTF / 教学**：让学员在普通 x86 笔记本上跑 Apple 内核实验；
- **学术研究**：内核安全、内存隔离、syscall 实验。

## 关键能力

| 能力 | 说明 |
|------|------|
| 全机型覆盖 | iPhone 12–17、M1–M5 Mac |
| SPTM 支持 | 含 Secure Page Table Monitor |
| 可调试 | kernel / SPTM / TXM / launchd / dyld / 用户程序 |
| 秒进 root | 几秒到 root shell |
| 无需越狱 | 不依赖真机越狱 / 内核补丁 |
| 无需 ARM CPU | 跑在任意 QEMU 平台 |
| 自动化 setup | 几分钟内可启动 |

## 相关概念

- [Protocol Model](./tool-protocol-model.md) — 与协议适配层无直接关系；darwin-vm 是 Apple 平台安全研究的工具
- [docker-android](./tool-docker-android.md) — 容器化 Android，与 darwin-vm 同属「跨主机虚拟化研究」思路

## 参考链接

- 项目链接：<https://github.com/jprx/darwin-vm>
- 原始推文：<https://x.com/Wen_Zw/status/2093554562590523462>