---
type: "Tool"
title: "Magma（help-14/magma）"
description: "基于 SvelteKit 的个人主页式看板,提供可拖可缩的网格编辑区,内置多语言,i18n 就绪,Docker 一键部署,适合个人 dashboard / startpage。"
resource: "https://github.com/help-14/magma"
tags: "[dashboard, startpage, sveltekit, svelte, self-hosted, docker, i18n, personal-homepage]"
timestamp: "2026-07-14T12:22:00Z"
---

# Magma

[Magma](https://github.com/help-14/magma) 是一个 **SvelteKit** 写的**个人主页式看板**:**可拖可缩的网格编辑区**,配多语言(i18n 就绪),Docker 一键部署。

## 关键能力

| 能力 | 说明 |
|------|------|
| 网格编辑 | 拖动 / 缩放 widget,布局完全自定 |
| 组件化 widget | 各种 widget 可拼装(书签 / 待办 / RSS / 天气 …) |
| 多语言 | i18n 内置,可扩展 |
| 一键 Docker | 起一个容器即跑 |
| 个人主页 | 既可做 startpage,也能做内部 dashboard |

## 适合什么场景

- 想搭一个**自己用的 startpage**,告别浏览器首页一片白。
- 团队 / 家庭内部 dashboard(把常用链接、待办、生活 widget 集中)。
- 已有自托管栈(CasaOS / Umami / …)+ 想再加一块**个人主页**。

## 与同类资源的差别

| 资源 | 特征 | Magma |
|------|------|-------|
| Flame / Homer | 经典 startpage | Magma 是 SvelteKit 原生,组件更现代 |
| CTRoadmap | 基础设施图谱工具 | 偏网络/服务关系;Magma 偏个人内容聚合 |
| Glance | GitHub · Docker · SSH 桌面仪表盘 | 桌面原生;Magma Web,跨平台 |

## 参考链接

- [项目仓库](https://github.com/help-14/magma)

## 相关概念

- [CasaOS](./tool-casaos.md) — 自托管 OS,可作 Magma 的部署底座
- [CTRoadmap](./tool-ctroadmap.md) — 同为图谱 / 网格化展示工具,CTRoadmap 偏基础设施关系,Magma 偏个人主页
- [glance（GitHub · Docker · SSH 桌面仪表盘）](./tool-glance-dashboard.md) — 桌面版仪表盘,Magma 是 Web 版对应物
