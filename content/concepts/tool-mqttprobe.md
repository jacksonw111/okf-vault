---
type: Tool
title: "mqttprobe"
description: "面向工业物联网（IIoT）的 MQTT 诊断工具：可连任意 broker、实时浏览主题树、查看 payload、把 JSON 指标画成图表，原生解码 Sparkplug B，可模拟 EoN 边缘节点；全程开源、不依赖云端。"
tags: "[mqtt, iiot, sparkplug, diagnostics, observability, tool]"
timestamp: "2026-07-13T00:00:00Z"
resource: "https://github.com/bluegrassiot/mqttprobe"
---

# mqttprobe

面向**工业物联网（IIoT）**的 **MQTT 诊断工具**——可连任意 broker、实时浏览主题树、查看 payload、把 JSON 指标画成图表，**原生解码 Sparkplug B**，可**模拟 EoN 边缘节点**；全程开源、不依赖云端。

## 它是什么

- 一款 MQTT 客户端 + 诊断/分析 UI（不是又一个通用 MQTT 客户端）；
- 面向**工业物联网场景**（工厂、SCADA、边缘设备），重点支持 **Sparkplug B** 工业协议；
- 完全本地运行，**不把数据发到云端**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 任意 broker 接入 | 兼容标准 MQTT broker（Mosquitto、EMQX、HiveMQ、AWS IoT Core 等） |
| 主题树浏览 | 实时浏览 broker 上的主题结构 |
| Payload 查看 | 一键展开消息 payload |
| 指标绘图 | 识别 JSON 数值字段自动绘制时序图 |
| Sparkplug B 解码 | 原生理解 Sparkplug B（工业 IIoT 主流协议）payload 语义 |
| EoN 模拟 | 充当 Edge of Network 节点，可发布/订阅测试流量 |
| 全开源 / 本地 | 无云端依赖，无追踪，无遥测 |

## 为什么用它 / 适合什么场景

- 工厂 / 车间 / 实验室**排障 MQTT 通信**：看不到主题、猜 payload、看不了曲线——它是这一类问题的桌面工具；
- 部署 Sparkplug B 系统的工程师：用它**对比 payload、确认节点上线、监控指标**；
- 想**离线、干净**地用 MQTT 工具（不想到处装 HiveMQ WebUI、不想给 AWS 账户授权）；
- 在 CI / 集成测试中**模拟一个 EoN 节点**给被测系统灌数据。

## 关键协议与角色

- **MQTT**：轻量发布/订阅消息协议，IIoT 现场主流；
- **Sparkplug B**：在 MQTT 之上定义的工业数据语义层（topic 命名空间、payload 格式、状态生命周期）；
- **EoN（Edge of Network）**：连接现场设备到 broker 的边缘节点；本工具可**模拟 EoN 角色**做测试。

## 预览

![](https://pbs.twimg.com/media/HM_oOMpawAAek6o.jpg)

## 相关概念

- [Quic-go TON](tool-quic-go-ton.md) — 同样面向"协议/网络"诊断的轻量工具思路
- [ESPHome Guition VA](tool-esphome-guition-va.md) — 另一类"嵌入式 / IoT 端"的本地化工具
