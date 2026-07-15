---
type: "Tool"
title: "bot-signal（okasi/bot-signal）"
description: "TypeScript 全套机器人检测套件:浏览器端抓自动化标记(headless / webdriver),服务端验 IP / TLS / 时区,长期记录可识别真人 vs 脚本模拟轨迹。"
resource: "https://github.com/okasi/bot-signal"
tags: "[bot-detection, typescript, fingerprint, security, anti-fraud]"
timestamp: "2026-07-15T15:33:00Z"
---

# bot-signal

[bot-signal](https://github.com/okasi/bot-signal) 是 TypeScript 写的**全套机器人检测**——浏览器端抓自动化标记,服务端验 IP/TLS/时区,跑一段时间后还能看出是人在操作还是脚本模拟。

## 它解决了什么

通用 bot 拦截通常看单次请求指纹,容易被高质量代理绕。bot-signal 把**短时指纹**(headless / webdriver / TLS JA3 / 时区错配)+ **长期行为信号**(击键间隔 / 鼠标轨迹 / 操作密度)**两层结合**,难以伪造。

## 关键能力

| 能力 | 说明 |
|------|------|
| 浏览器标记 | 抓 headless / webdriver / canvas / audioContext 等已知指纹 |
| 服务端验证 | IP 黑名单 / TLS JA3 比对 / 时区一致性 |
| 行为时序 | 长期收集鼠标 / 键盘节律,识别脚本模拟 |
| TypeScript 全栈 | 端到端共用一套类型定义 |

## 参考链接

- [项目仓库](https://github.com/okasi/bot-signal)

## 相关概念

(无清晰相关概念,单飞)
