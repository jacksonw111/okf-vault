---
title: "Post by @vintcessun on X"
source: "https://x.com/vintcessun/status/2062755543811588448"
author:
  - "[[@vintcessun]]"
published: 2026-06-05
created: 2026-06-17
description: "AI agent 要跑沙箱隔离，但冷启动微VM太慢了。这个项目干脆把预热好的父 VM snapshot 当进程 fork：子 VM 共享内存直到写时才复制，100 个 KVM 隔离的沙箱 100ms 就能全出来。相当于把 fork 的开销套在 VM 身上，还保留了硬件隔离，思路挺"
tags:
  - "clippings"
---

AI agent 要跑沙箱隔离，但冷启动微VM太慢了。这个项目干脆把预热好的父 VM snapshot 当进程 fork：子 VM 共享内存直到写时才复制，100 个 KVM 隔离的沙箱 100ms 就能全出来。相当于把 fork 的开销套在 VM 身上，还保留了硬件隔离，思路挺离谱的。

[github.com GitHub - deeplethe/forkd: Fork() for AI agent microVMs. Spawn 100 children in ~100ms from a warm...](https://t.co/D9yIIHTLgJ)
