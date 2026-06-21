---
type: Tool
title: "ngrok / webernetes"
description: "ngrok 团队的 Kubernetes 集成项目：把 K8s 服务通过 ngrok 隧道暴露到公网，自带 demo 与 YouTube 录屏讲解。"
resource: "https://github.com/ngrok/webernetes"
tags: [ngrok, kubernetes, networking, k8s, ingress]
timestamp: 2026-06-19T00:00:00Z
---

# ngrok / webernetes

ngrok 团队开源的「Kubernetes + ngrok」集成项目，名字 webernetes = web + Kubernetes。目标是把 K8s 集群里的服务通过 ngrok 隧道安全地暴露到公网，省掉自建 Ingress / 反代 / 证书续签。

## 关键链接

| 资源 | 链接 |
|------|------|
| 仓库 | <https://github.com/ngrok/webernetes> |
| 在线 Demo | <https://webernetes-demo.ngrok.app> |
| 录屏 1 | <https://www.youtube.com/watch?v=xckIMSFaB3s> |
| 录屏 2 | <https://www.youtube.com/watch?v=wRSyz0_bhPI> |

## 适合什么场景

- 开发 / 演示 K8s 服务，需要临时公网入口（避免自建 ngrok Operator / Ingress-nginx）
- 本地集群（kind / k3d / minikube）想被外部访问
- 不想管 TLS 证书与端口转发

## 与 ngrok 的关系

属于 ngrok 官方维护的 K8s 方向生态——延续 ngrok 「把复杂网络暴露简化成单条隧道」的核心思路，把这一能力下沉到 K8s Operator 层。

## 参考链接

- [原始链接 1](https://x.com/samwhoo/status/2067652753288057102)
- [原始链接 2](https://x.com/Wen_Zw/status/2067774781836108067)

## 相关概念

- [Cloud Mail](./tool-cloud-mail.md) — 同为「自托管 + 简化部署」类工具，思路相近
- [Lucky](./tool-lucky.md) — NAS 上的 DDNS + ACME + 反代瑞士军刀，K8s 之外的另一种「自建公网入口」路径
- [3X-UI](./tool-3x-ui.md) — 另一种自建公网入口的方案（Xray 面板，偏代理）
