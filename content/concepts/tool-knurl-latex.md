---
type: Tool
title: "knurl（LaTeX 宏包自动解析与一键安装）"
description: "读你的 LaTeX 项目，把每个 \\usepackage 映射到正确的 TeX Live 包名，缺什么一键装好——解决 CTAN 包名与 TeX Live 包名不对齐的痛点。"
resource: "https://github.com/gilsonolegario/knurl"
tags: [latex, tex-live, ctan, package-manager, automation]
timestamp: "2026-08-29T21:30:00Z"
---

# knurl（LaTeX 宏包自动解析与一键安装）

## 它是什么

[gilsonolegario/knurl](https://github.com/gilsonolegario/knurl) 是一个 LaTeX 工程的**宏包依赖解析器**：扫描项目里所有 `\usepackage{...}` / `\RequirePackage{...}`，把每个名字映射到 **TeX Live 包**（注意：CTAN 包名 ≠ TeX Live 包名，是常见坑），并自动装齐缺失的包。

痛点：LaTeX 编译失败大部分是「找不到宏包」，但报错里给的名字常常是**CTAN 名**（如 `algorithm2e`），你要装的是 **TeX Live 名**（如 `texlive-science` 里的子包，或 `tlmgr install algorithm2e`）。靠记忆 / 文档查不现实，knurl 直接替你做映射 + 安装。

## 为什么用它 / 适合什么场景

- 经常要在多台机器 / CI 上复现 LaTeX 编译环境；
- 跨项目共享 .tex 源码，新机器上每次都要查包；
- 学生 / 教学场景：让 LaTeX 新手不必陷在宏包管理里；
- CI 跑 LaTeX 编译，不想手写 Dockerfile 装 TeX Live 包。

## 关键能力

| 能力 | 说明 |
|------|------|
| 依赖解析 | 扫描 `\usepackage` / `\RequirePackage` 全部调用 |
| 名映射 | CTAN 包名 ↔ TeX Live 包名自动对齐 |
| 一键安装 | 缺什么 `tlmgr install` 什么 |
| 工程级 | 不只是一个文件，整目录 / 子目录递归扫 |
| 节省时间 | 把「查包名 + 装包 + 重编译」缩到一条命令 |

## 相关概念

- [FFmpegFreeUI](./tool-ffmpeg-free-ui.md) — Windows 端的 FFmpeg 图形外壳，knurl 是 LaTeX 端的「依赖一键装」配套

## 参考链接

- 项目链接：<https://github.com/gilsonolegario/knurl>
- 原始推文：<https://x.com/QingQ77/status/2093615638002426174>
- 媒体：<https://pbs.twimg.com/media/HQ0WF_4aAAAKr1r.jpg>