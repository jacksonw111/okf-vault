# twitter-crawler

每小时抓取指定 X 账号推文（原创/长文/线程/引用/转载，不含回复），渲染成 Markdown 落到 `content/inbox/twitter/<账号>/`，交 OKF agent 每天整理。

## 配置 auth token

1. 浏览器登录 x.com。
2. DevTools → Application → Cookies → `https://x.com` → 复制 `auth_token` 的值。
3. 仓库 Settings → Secrets and variables → Actions → New repository secret：
   - Name: `X_AUTH_TOKEN`
   - Value: 上一步的值
4. （建议）仓库设为 private。

> `ct0`（CSRF）由爬虫运行时自动获取，无需配置。token 可能数周失效，401 时更换即可。建议用 burner 账号。

## 加账号

编辑 `twitter-crawler/accounts.json`：

```json
{ "accounts": ["Wen_Zw", "anotherAccount"], "max_per_run": 20 }
```

## 本地手动跑

```bash
cd twitter-crawler
npm ci
X_AUTH_TOKEN=xxx tsx src/index.ts
```

## 回填历史

Actions 页面 → X/Twitter Crawl → Run workflow → `max_per_run` 填大数（如 200）。

## 产出

- 路径：`content/inbox/twitter/<账号>/<YYYY-MM-DD>-<tweetId>.md`
- 去重：文件名含 tweetId，已存在即跳过。
- 不触发 agent：用 GITHUB_TOKEN 推送；okf.yml 每天定时 run 才整理。
