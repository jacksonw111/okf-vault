---
type: Dataset
title: "Global Timezone Tracker"
description: "每周自动刷新的全球时区 JSON 数据集，收录 247 个国家 / 418 个时区，含 UTC 偏移 / 夏令时状态 / ISO 国家代码映射，前后端可直接复用。"
resource: "https://github.com/ramazancetinkaya/global-timezone-tracker"
tags: "[timezone, dataset, json, locale, i18n]"
timestamp: "2026-09-07T13:04:00Z"
---

# Global Timezone Tracker

## 它是什么
一份通过脚本每周自动刷新的全球时区数据仓库（Python 写，MIT 协议）。收录 247 个国家 / 418 个时区，每条记录标好当前 UTC 偏移、夏令时开没开，外加 ISO 国家代码映射。直接拉下来作为 JSON 用，省去自己维护时区表的麻烦。

## 数据形态（典型条目）
| 字段 | 说明 |
|------|------|
| country_code | ISO 3166-1 alpha-2 国家代码 |
| timezone | IANA 时区名（如 `Asia/Shanghai`） |
| utc_offset | 当前 UTC 偏移 |
| dst_active | 当前是否处于夏令时 |
| last_updated | 数据刷新时间 |

## 适用场景
- 跨国应用显示用户本地时间
- 日程 / 会议类 App 的时区转换
- 日志系统按本地时间归类
- 需要对接 IANA tz 数据库但不想自己解析的小工具

## 关键能力
| 能力 | 说明 |
|------|------|
| 自动刷新 | 脚本每周更新，无需手动维护 |
| 覆盖广 | 247 国家 / 418 时区 |
| ISO 国家代码 | 可直接对接 country code 字段 |
| MIT 协议 | 商用免费 |

## 参考
- 项目链接：<https://github.com/ramazancetinkaya/global-timezone-tracker>

## 相关概念
- [IANA tz database](https://www.iana.org/time-zones) — 全球时区的权威数据源