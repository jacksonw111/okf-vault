---
type: Tool
title: "patent-disclosure-skill"
description: "AgentSkills 技能，从项目文档与代码自动生成中国专利技术交底书；扫文档 → 挖专利点 → 国知局查新 → 脱敏写交底书（含 Mermaid 系统框图 / 流程图）→ 输出 .md 与 .docx；支持迭代修订与历史另存。"
resource: "https://github.com/handsomestWei/patent-disclosure-skill"
tags: "[agent-skills, skill, patent, china, disclosure, claude-code]"
timestamp: "2026-07-03T02:36:00Z"
---

# patent-disclosure-skill

## 它是什么
**AgentSkills 技能**——从项目文档和代码自动生成符合国知局要求的中国专利**技术交底书**。

完整流程：扫项目文档 → 挖专利点 → 连国知局查新（优先用中国专利公布公告站）→ 脱敏成文（含 Mermaid 系统框图与流程图）→ 自动输出 `.md` 和 `.docx` 双格式。支持迭代修订——已有交底书可补材料或纠错，每次修改另存新文件，保留修订记录可追溯。

## 为什么用它 / 适合什么场景
- 研发团队有大量项目文档 / 代码，但没人愿意手动把技术方案写成交底书。
- 申请专利前需要先做查新检索（确认未被公开），又要避免文档外泄（脱敏）。
- 需要快速产出可视化系统框图 / 流程图（Mermaid）来辅助说明。
- 多团队共享同一份技术方案的不同版本（需要修订追溯）。

## 关键能力
| 能力 | 说明 |
|------|------|
| 输入 | 项目文档（README / 设计文档等）+ 代码 |
| 输出 | 中国专利技术交底书（`.md` + `.docx`） |
| 专利点挖掘 | 自动从文档和代码识别潜在发明点 |
| 查新检索 | 优先连中国专利公布公告站（国知局） |
| 脱敏 | 写交底书前自动做敏感信息脱敏 |
| 系统框图 | 内嵌 Mermaid 生成的系统框图 |
| 流程图 | 内嵌 Mermaid 生成的流程图 |
| 迭代 | 已生成的交底书可补材料 / 纠错，每次另存新文件 |
| 修订记录 | 保留历史修改轨迹可追溯 |
| 形态 | AgentSkills 技能（装到 Claude Code 等代理） |

## 相关概念
- [paper-lifecycle](tool-paper-lifecycle.md) — 论文写作 Codex skills 套件；patent-disclosure-skill 是专利交底书生成
- [paper2anything](tool-paper2anything.md) — 论文转 5 种宣传物料；patent-disclosure-skill 是技术文档转专利交底书

## 项目链接
- 项目主页：<https://github.com/handsomestWei/patent-disclosure-skill>

## 媒体
![](https://pbs.twimg.com/media/HMM_Q9AbMAAZHNv.png)