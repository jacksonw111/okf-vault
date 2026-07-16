---
type: "Tool"
title: "geoanalisis-mcp（alexrobl/geoanalisis-mcp）"
description: "与 Claude Desktop 集成的 MCP 服务器,让用户用自然语言指令读取、分析与制图矢量空间数据——生成专业地图无需打开桌面 GIS 软件。"
resource: "https://github.com/alexrobl/geoanalisis-mcp"
tags: "[mcp, gis, geo, spatial-analysis, vector-data, claude-desktop]"
timestamp: "2026-07-16T14:17:00Z"
---

# geoanalisis-mcp

[geoanalisis-mcp](https://github.com/alexrobl/geoanalisis-mcp) 是一个**与 Claude Desktop 集成的 MCP 服务器**,把矢量空间数据的读取、分析与制图暴露给 Claude,让用户用自然语言指令生成专业地图——无需打开 QGIS / ArcGIS 等桌面 GIS 软件。

## 它解决了什么

地理空间数据(Shapefile / GeoJSON / KML)做分析往往要开 GIS 软件手动加载图层、选字段、配可视化——流程碎片化。geoanalisis-mcp 让 Claude Desktop 直接读 `/path/to/data.geojson`、理解字段、按用户问句生成地图。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自然语言指令 | 通过 Claude 对话下达「画一张 X 省的某指标热力图」之类请求 |
| 矢量数据读取 | 直接加载 Shapefile / GeoJSON / KML 格式 |
| 空间分析 | 缓冲区、叠加分析、空间查询等基础 GIS 操作 |
| 制图输出 | 输出专业地图(分级色彩、热力、聚类等) |
| 零 GIS 软件 | 通过 Claude Desktop 即可,跳过 QGIS / ArcGIS 桌面客户端 |

## 媒体

![](https://pbs.twimg.com/media/HNRKFCobQAA7oCc.jpg)

## 参考链接

- [项目仓库](https://github.com/alexrobl/geoanalisis-mcp)

## 相关概念

(无清晰相关概念,单飞)
