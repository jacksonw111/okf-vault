---
type: "Tool"
title: "tapo-voltage-monitor（KartoshaHv/tapo-voltage-monitor）"
description: "给 TP-Link Tapo P110 / P115 智能插座用的电压监测工具:本地网页仪表盘 + CSV 日志,识别越界与断电,可累计一周数据同供电公司交涉。"
resource: "https://github.com/KartoshaHv/tapo-voltage-monitor"
tags: "[tapo, smart-plug, voltage, monitoring, iot, csv, dashboard]"
timestamp: "2026-07-14T00:21:00Z"
---

# tapo-voltage-monitor

[tapo-voltage-monitor](https://github.com/KartoshaHv/tapo-voltage-monitor) 是给 **TP-Link Tapo P110 / P115** 智能插座用的**电压监测工具**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实时电压 | 墙插真实电压(官方 App 不显示) |
| 本地仪表盘 | Web UI 看趋势与异常 |
| CSV 日志 | 长期记录可导入 Excel / Pandas |
| 越界告警 | 偏离阈值即标记 |
| 断电识别 | 区分「电压波动」与「完全断电」 |
| 累计交涉 | 攒一周数据即可向供电公司反馈 |

## 适合什么场景

- 怀疑家庭 / 办公室**电压不稳**,但 Tapo App 看不到电压曲线。
- 给供电公司报修时,需要**数据证据**(「今天下午 2 点起电压降到 198V」)。
- 长期稳定运行 NAS / 服务器:**电压暂降是元件杀手**,需要历史曲线。
- 想做一个**24×7 电压事件审计**给家用 IoT 用。

## 与同类资源的差别

| 资源 | 特征 | tapo-voltage-monitor |
|------|------|----------------------|
| Tapo App(官方) | 不显示电压 | 本工具填补 |
| marine-acoustic-monitor | 海洋生态监测 | 不同域(海洋声学),同思路(本地仪表盘 + 日志) |
| Pocket Lab Power Supply | 输出电压的硬件 | 偏供电;本工具偏测量 |

## 参考链接

- [项目仓库](https://github.com/KartoshaHv/tapo-voltage-monitor)

## 相关概念

- [CasaOS](./tool-casaos.md) — 自托管 OS,可作本工具的部署底座
- [Garmin Tracker RS](./tool-garmin-tracker-rs.md) — 同样 USB 直连设备读原始数据的工具
