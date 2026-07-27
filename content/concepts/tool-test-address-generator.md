---
type: "Tool"
title: "Test Address Generator（daimon3332/address）"
description: "自托管的测试地址生成器：基于 OpenStreetMap 等开源地理数据，为 27 个国家和地区生成带真实坐标的测试地址与档案；适合做需要伪造地址、地图选址、物流模拟、隐私数据的开发与测试场景。"
resource: "https://github.com/daimon3332/address"
tags: [test-data, address-generator, openstreetmap, self-hosted, fake-data]
timestamp: "2026-07-27T20:30:00Z"
---

# Test Address Generator（daimon3332/address）

## 它是什么

`daimon3332/address` 是一个**自托管地址生成器**：用开源地图数据（OpenStreetMap 等）给 **27 个国家和地区**生成带**真实坐标**的测试地址和档案。用于需要假地址、地图选址、物流模拟、隐私测试数据等场景，避免使用真实用户地址触犯合规风险。

## 为什么用它 / 适合什么场景

- 想做**地图标注 / 路线规划 / 地理围栏** Demo，但不想用真实地址；
- 需要**多国地址 + 经纬度**配套生成（默认 27 个国家）；
- 测试**电商下单 / 物流配送 / 外卖 / 隐私保护**产品时填充数据；
- 希望**完全自托管**、不依赖第三方假数据 API。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多国覆盖 | 默认支持 27 个国家和地区 |
| 真实坐标 | 基于 OpenStreetMap 等开源地图数据，地址带真实经纬度 |
| 自托管 | 本地服务，避免调用第三方接口 |
| 一键生成 | 测试用地址 + 配套档案（街、区、城市、邮编、坐标） |
| 离线数据源 | 使用开源地理数据集 |

## 媒体 / 原始链接

![](https://pbs.twimg.com/media/HOH7YmIbcAAwnhj.jpg)

- 项目链接：<https://github.com/daimon3332/address>
