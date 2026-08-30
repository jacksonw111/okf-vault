---
type: "Tool"
title: "TestingFilesGenerator（QA 用测试文件批量生成器）"
description: "面向 QA / 工程师的测试文件生成器：PDF / PNG / ZIP / DOCX 等 22 种真实格式都能按需生成，大小精确到字节；同时生成一张清单说明每个文件该如何被处理——可直接喂给上传 / 解析 / 病毒扫描流程做测试。"
resource: "https://github.com/donislawdev/TestingFilesGenerator"
tags: [qa, testing, test-data, file-generator, validation]
timestamp: "2026-08-30T21:50:00Z"
---

# TestingFilesGenerator

## 它是什么
[donislawdev/TestingFilesGenerator](https://github.com/donislawdev/TestingFilesGenerator) 是给 **QA 工程师 / 后端开发者**的**测试文件批量生成器**——能按需生成 **22 种真实格式**（PDF、PNG、ZIP、DOCX、JPG、Excel、…）的测试样本，**大小精确到字节**；同时附带一张**说明每个文件该如何被处理**的清单。

它的核心价值是**「可预期的测试输入」**：

- 想测上传组件在「**1 KB、10 MB、500 MB**」分别会怎么反应？直接生成；
- 想测解析器在「**合法 PDF / 截断的 PDF / 假 PDF 头**」下的行为？直接生成；
- 想测病毒扫描在「**真实 ZIP / 套娃 ZIP / 加密 ZIP**」下的判断？直接生成；
- 配合清单文件，可作为**自动化 fixture** 直接被测试框架加载。

## 为什么用它 / 适合什么场景
- 写上传 / 解析 / 病毒扫描 / 邮件附件等**吃文件类型**的功能测试；
- 想要**「已知大小、已知格式、已知预期处理方式」**的可控测试样本；
- 在 CI 里**按需生成 fixture**，避免往仓库 commit 大二进制；
- 做 fuzz testing 的种子数据集。

## 关键能力

| 能力 | 说明 |
|------|------|
| 22 种格式 | PDF / PNG / ZIP / DOCX / JPG / Excel 等真实可解析格式 |
| 字节精确 | 输出大小可指定到字节，便于边界测试 |
| 处理清单 | 每个文件附带「该怎么被处理」的元数据 |
| 自动化友好 | 可作为 CI fixture 直接喂给测试 |
| 开源 | 自行扩展格式类型 |

## 媒体
- 视频：<https://video.twimg.com/amplify_video/2093860424261476352/vid/avc1/2248x1572/I7HbYoBrcwG1DCeS.mp4?tag=29>

## 相关概念
- [Mimik](tool-mimik.md) — 同属「**测试 / QA 工作流自动化**」生态

## 参考链接
- 项目链接：<https://github.com/donislawdev/TestingFilesGenerator>
