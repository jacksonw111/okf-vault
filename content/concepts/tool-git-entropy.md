---
type: "Tool"
title: "git-entropy（Git 仓库压缩后真实信息量度量）"
description: "FelixKramer 写的 git 脚本：把项目多年提交记录压成 tar.gz / zip 测实际字节数，还附带一个对照组（不含运行时常量 / 随机数据那种），告诉你真实「信息」到底有多少。"
tags: "[git, metrics, entropy, repository, diagnostic, script]"
timestamp: "2026-08-26T16:30:00Z"
resource: "https://github.com/FelixKramer/git-entropy"
---

# git-entropy（Git 仓库压缩后真实信息量度量）

## 它是什么

[`git-entropy`](https://github.com/FelixKramer/git-entropy) 是 FelixKramer 写的小脚本——把 git 仓库**导出压缩后**测**实际字节数**（相当于对该仓库**信息量**的近似度量），还**带对照组**（去掉运行时常量 / 随机 seed 数据）：

> 「想知道你项目几年的提交记录压成一团到底有多少字节的真实信息？」

## 为什么用它 / 适合什么场景

- 想知道自己的项目「真实信息量」——多年的提交流到底沉淀了多少有效字节
- 排查「为什么我的包那么大」——揪出被 run-time 常量 / 随机数据撑大的部分
- 给仓库做减肥前后对比

## 关键能力

| 能力 | 说明 |
|------|------|
| 压缩度量 | tar.gz / zip 后字节数 |
| 对照组 | 剥离运行时常量 / 随机数据后的「真信息」 |
| 简单脚本 | 上手极简 |
| 仓库诊断 | 找「信息密度低」的子目录 |

## 媒体

![](https://pbs.twimg.com/media/HQibGKLbEAAJkAK.png)

## 参考链接

- [项目链接](https://github.com/FelixKramer/git-entropy)
