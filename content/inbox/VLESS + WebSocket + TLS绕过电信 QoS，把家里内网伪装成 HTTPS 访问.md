---
title: "VLESS + WebSocket + TLS绕过电信 QoS，把家里内网伪装成 HTTPS 访问"
source: "https://x.com/xiaojingshe/status/2064554366783381583"
author:
  - "[[@xiaojingshe]]"
published: 2026-06-10
created: 2026-06-17
description: "前情提要：本来我用Tailscale组网很方便，后来发现 UDP 被限速到 5M 了，前面折腾了两轮，基本确认武汉电信对某些组网流量有 QoS。实测结果：1. Tailscale 直连走 UDP，上传被限到 3-5Mbps 左右2. 有公网 IP 群晖自建 DERP 虽然走 TC..."
tags:
  - "clippings"
---
![图像](https://pbs.twimg.com/media/HKbE_EYa4AAYycj?format=jpg&name=large)

前情提要：

本来我用Tailscale组网很方便，后来发现 UDP 被限速到 5M 了，前面折腾了两轮，基本确认武汉电信对某些组网流量有 QoS。

实测结果：

1\. Tailscale 直连走 UDP，上传被限到 3-5Mbps 左右

2\. 有公网 IP 群晖自建 DERP 虽然走 TCP/TLS，但特征明显，刚开始 30Mbps，几秒后掉回 3Mbps

3\. 普通 HTTPS 上传没被限制，B 站上传、DDNS + TCP 端口转发都能跑满 40Mbps

所以思路变成：

既然普通 HTTPS 不限速，那就把“异地访问家里内网”伪装成一个正常 HTTPS 网站访问。

![图像](https://pbs.twimg.com/media/HKbCG0Ua0AEIOBY?format=jpg&name=large)

最终拓扑：

```text
异地设备
->  Clash/小火箭 客户端分流
-> Lucky HTTPS 反向代理
-> 群晖 3x-ui / Xray搭建 VLESS + WebSocket
-> 家里内网服务
```

最终效果：

![图像](https://pbs.twimg.com/media/HKbCb1ybsAAnnKE?format=jpg&name=large)

**本方案不光 UDP 流量被限速能绕过，正常使用也很好，平时代理软件开启，就能无缝回家，很舒服，不需要单独开别的 VPN 软件**

**如果你也准备使用这个方案前置条件：**

1\. 家里有 动态公网 IP

2\. 有一个域名

3\. 24 小时设备，比如群晖/飞牛/软路由等

4\. 掌握Docker / 反向代理 / 域名证书 / clash/小火箭客户端配置

**这不是保姆级教程，适合有一定网络经验、会折腾的人。**

**第一步：Docker部署 3x-ui**

群晖 Container Manager 新建项目，Compose 示例：

```yaml
services:
  3x-ui:
    image: ghcr.io/mhsanaei/3x-ui:latest
    container_name: 3x-ui
    restart: unless-stopped
    network_mode: host
    volumes:
      - /volume1/docker/3xui/db:/etc/x-ui
```

启动后访问3x-ui面板：http://群晖IP:2053

![图像](https://pbs.twimg.com/media/HKbDOYia0AAG8Kh?format=jpg&name=large)

默认用户和密码：admin

安全起见：进去后立刻修改 用户名、密码、面板路径

**不改也行，重点：不要把 3x-ui 面板端口暴露到公网。**

**第二步：3x-ui 新建入站**

在 3x-ui 新建一个入站：

![图像](https://pbs.twimg.com/media/HKbDdMSbAAAcUoR?format=jpg&name=large)

\- 协议：VLESS

\- 监听：127.0.0.1

\- 端口：10080 （不冲突随意）

\- 传输：WebSocket

\- Path：/home （任意名称）

\- 安全：无

这里 TLS 交给 Lucky 做。

也就是：

Xray 只在本机提供一个 WebSocket 后端，Lucky 负责公网 HTTPS 入口

**检查 Xray 路由规则**

![图像](https://pbs.twimg.com/media/HKbDnxhb0AAsKKa?format=jpg&name=large)

设置里删除第二个规则：geoip:private → direct，否则客户端把家里内网 IP 送进来了，服务端又给你拦了。

**第三步：Lucky 配置 HTTPS 反向代理**

这里Lucky先搞定 DDNS + 推荐 ACME 方式证书自动续签

Lucky 新增 Web 服务规则：

\- 服务类型：反向代理

\- 前端地址：[home.example.com](https://home.example.com/):22443

\- 后端地址：http://127.0.0.1:10080

![图像](https://pbs.twimg.com/media/HKbDxica4AAPW8k?format=jpg&name=large)

如果 Lucky 和 3x-ui 不在同一台设备，后端填：\`http://群晖IP:10080\`

**第四步：路由器端口转发**

路由器上做DDNS也可以的，主路由器（拨号需要获取公网 IP）做端口转发：

![图像](https://pbs.twimg.com/media/HKbD6tJa0AAjM43?format=png&name=large)

外部 TCP 22443 -> 群晖/Lucky:22443

默认 443、8443 是封的，这里的端口用一个高一点数字随意

**第五步：客户端节点配置**

自建的节点导入你的clash/小火箭等客户端，这里使用小火箭为例：

![图像](https://pbs.twimg.com/media/HKbEFWjboAAF1HI?format=jpg&name=large)

关键信息就四个：地址、端口、UUID、传输方式（里面的路径要填写）， TLS 默认开启，备注随意。

**设置分流规则**

比如家里网段是：\`192.168.31.0/24\`

规则放最前面：

```text
- IP-CIDR,192.168.31.0/24,🏠 回家,no-resolve
```

每个人使用的客户端不同，怎么分流自己设置，上面只是个演示！

**删除局域网绕过**

这里还有一个坑：很多客户端默认会有：绕过局域网、跳过私有地址

![图像](https://pbs.twimg.com/media/HKbEVbIbYAAksGr?format=jpg&name=large)

clash verge 比如： 192.168.0.0/16 直接不走代理。要把这个绕过规则删掉，否则访问家里内网 IP 时，流量根本不会进入节点。

**验收成功**

先看节点是否能连通（有没有延时），有才正常：

![图像](https://pbs.twimg.com/media/HKbEevEaIAE5DrT?format=jpg&name=large)

然后访问家里内网服务，比如路由器管理页面：192.168.31.1

![图像](https://pbs.twimg.com/media/HKbEkBcaEAEgYg-?format=jpg&name=large)

如果访问时 Lucky / 3x-ui 有流量，说明链路进来了。

如果没有流量，优先查：

\- 节点信息导入是否正确

\- 客户端规则

\- 局域网绕过

\- 策略组是否选中回家节点

**SSH 访问家里设备**

![图像](https://pbs.twimg.com/media/HKbEv_kbgAAsBSG?format=jpg&name=large)

SSH 流量默认不会被系统代理，开启 TUN 模式 即可强制走代理，才能连回家里的设备。

**最终结果**

我这里跑 Homebox / LibreSpeed：

![图像](https://pbs.twimg.com/media/HKbE2eWawAAk6bN?format=jpg&name=large)

跑满两边电信宽带的 40Mbps 上行，之前 Tailscale 被 QoS 后只有2-5Mbps，远程桌面macmini都很卡，现在非常流畅了～

**另外把 NAS 换成 VPS，发现没？这就是自建 VPS 节点教程呀，这波不亏～**