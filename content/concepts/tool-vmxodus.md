---
type: Tool
title: "vmxodus（VMware → Proxmox VE 零拷贝迁移脚本）"
description: "Bash 脚本：把 VMware ESXi 上的虚拟机搬到 Proxmox VE 时**避免复制磁盘数据**，靠 Storage vMotion 把虚拟磁盘挪到两边都能挂载的 NFS 共享，再在 PVE 节点上原地转换为 PVE 镜像格式，最大限度缩短停机时间。"
resource: "https://github.com/luka0x73/vmxodus"
tags: [vmware, proxmox, migration, bash, storage-vmotion, virtualization]
timestamp: 2026-09-30T11:21:00Z
---

# vmxodus

## 它是什么

**vmxodus** 是 [luka0x73](https://github.com/luka0x73) 维护的 Bash 脚本，用来把 VMware ESXi 上的虚拟机搬到 Proxmox VE。它特别关注一个具体目标：**避免复制磁盘数据**——也就是说不把磁盘镜像从一头拷到另一头，而是直接在共享存储上"改格式"。

迁移流程：

1. **Storage vMotion**：先把虚拟磁盘搬到 ESXi 与 PVE 都能挂载的 NFS 共享上。
2. **prepare**：在 PVE 节点读取 `.vmx` 配置并创建一台空的 PVE 虚拟机（壳）。
3. **cutover**：把虚拟机关机后，把 `-flat.vmdk` 直接 `mv` 成 PVE 的镜像布局（qcow2 / raw）。

由于磁盘始终在同一份存储上"原地变身"，**停机窗口几乎只剩 cutover 步骤的几秒钟**。

## 为什么用它 / 适合什么场景

- 计划把 VMware ESXi 迁到 Proxmox VE，又**不想让磁盘复制拖上几小时 / 几天**。
- 已有或愿意搭建一个 ESXi 与 PVE 都能挂的 NFS 共享。
- 希望迁移脚本用简单 Bash 实现，便于审计每一步。

## 关键能力

| 能力 | 说明 |
|------|------|
| 语言 | Bash |
| 迁移源 | VMware ESXi |
| 迁移目标 | Proxmox VE |
| 磁盘处理 | **原地转换，不复制数据** |
| 前置条件 | ESXi / PVE 都可挂载同一 NFS 共享 |
| 停机时间 | 仅 cutover 一步所需 |
| 形态 | CLI 脚本 |

## 参考链接

- 仓库：<https://github.com/luka0x73/vmxodus>

## 相关概念

- [Proxmox VE 代理](./tool-streamdeck-proxmox-agent.md) — 同为 Proxmox 生态工具；这里是迁移链路上的对应环节