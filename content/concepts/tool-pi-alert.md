---
type: Tool
title: "Pi.Alert"
description: "开源局域网设备监控与入侵检测面板：自动发现局域网设备、陌生设备告警、监控掉线/异常 DHCP/Web/SSL 证书变化；支持 Nmap、Wake-on-LAN、Telegram/ntfy/Home Assistant 通知。"
resource: "https://github.com/leiweibau/Pi.Alert"
tags: [network, iot, raspberry-pi, monitoring, security]
timestamp: "2026-09-08T00:00:00Z"
---

# Pi.Alert

## 它是什么
Pi.Alert（leiweibau 开源）是一套**局域网设备监控与入侵检测面板**：自动发现家里/办公室局域网里的设备，陌生设备接入时主动告警；并能持续监控设备掉线、异常 DHCP、Web 服务状态与 SSL 证书变化。适合树莓派、家庭服务器、NAS、自建网络等场景。

## 为什么用它 / 适合什么场景
- 家里设备多（NAS / 软路由 / IoT），想可视化"谁连进来了"。
- 担心陌生设备蹭网或被入侵。
- 想自己搭一个小型网络监控中心而不是用云服务。

## 关键能力
| 能力 | 说明 |
|------|------|
| 自动发现 | 主动枚举局域网内设备 |
| 入侵告警 | 新设备接入通知 |
| 状态监控 | 掉线 / 异常 DHCP / Web 服务 / SSL 证书 |
| 设备历史 | 长期记录设备在线状态 |
| Nmap 扫描 | 主动端口/服务扫描 |
| Wake-on-LAN | 远程唤醒 |
| 网络拓扑 | 自动绘制网络结构 |
| 通知渠道 | Telegram、ntfy 等 |
| 集成 | Home Assistant、API |
| 部署 | Linux / Docker |

## 参考
- 原始链接：<https://github.com/leiweibau/Pi.Alert>

## 媒体
- ![](https://pbs.twimg.com/media/HRkcw-ya8AAIi-0.jpg)

## 相关概念
- [Home Assistant](https://www.home-assistant.io/) — 智能家居中枢
- [Nmap](https://nmap.org/) — 端口/服务扫描底层
