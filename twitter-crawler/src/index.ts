import fs from "node:fs"
import path from "node:path"
import { loadConfig } from "./config.js"
import { buildClient } from "./auth.js"
import { fetchTweetsForAccount } from "./fetch.js"
import { classifyTweet } from "./classify.js"
import { renderMarkdown } from "./render.js"
import { tweetFilePath, alreadySavedTweetId } from "./io.js"

function todayUTC(): string {
  const d = new Date()
  const y = d.getUTCFullYear()
  const m = String(d.getUTCMonth() + 1).padStart(2, "0")
  const day = String(d.getUTCDate()).padStart(2, "0")
  return `${y}-${m}-${day}`
}

async function main() {
  const cfg = loadConfig()

  if (!cfg.authToken) {
    console.log("::warning::X_AUTH_TOKEN 未配置，跳过爬取（exit 0，不报红）。")
    process.exit(0)
  }

  if (cfg.accounts.length === 0 && cfg.newsAccounts.length === 0) {
    console.log("accounts.json 无账号，退出。")
    process.exit(0)
  }

  const client = await buildClient(cfg.authToken)
  const today = todayUTC()
  let totalWritten = 0

  async function crawlGroup(args: {
    accounts: string[]
    outDir: string
    tags: string[]
    archived: boolean
  }) {
    let groupWritten = 0
    for (const screenName of args.accounts) {
      const dir = path.join(args.outDir, screenName)
      fs.mkdirSync(dir, { recursive: true })

      const searchDirs = args.archived
        ? [dir, path.join(cfg.inboxDoneDir, "twitter", screenName), cfg.inboxDoneDir]
        : [dir]
      const isSaved = (id: string) => alreadySavedTweetId(searchDirs, id)

      let result
      try {
        result = await fetchTweetsForAccount({
          client,
          screenName,
          maxPerRun: cfg.maxPerRun,
          isSaved,
        })
      } catch (err: any) {
        // 不打印 err 里可能夹带的请求细节；只给状态（库堆栈若需排查可临时开启 err.stack）
        const msg = String(err?.message || err)
        if (/401|403|unauthor|ct0|invalid|expired/i.test(msg)) {
          console.error(`::error::@${screenName} 鉴权失败，X_AUTH_TOKEN 可能失效，请更换。`)
        } else if (/429|rate/i.test(msg)) {
          console.error(`::error::@${screenName} 被限流(429)，稍后再试。`)
        } else {
          console.error(`::error::@${screenName} 抓取失败：${msg}`)
        }
        continue
      }

      let written = 0
      for (const rt of result.tweets) {
        const type = classifyTweet(rt)
        const md = renderMarkdown(rt, type, today, { tags: args.tags })
        const fp = tweetFilePath(dir, rt)
        fs.writeFileSync(fp, md, "utf8")
        written++
      }
      groupWritten += written
      console.log(
        `@${screenName}: fetched ${result.tweets.length}, written ${written}` +
          (result.stoppedAtKnown ? " (stopped at known)" : ""),
      )
    }
    return groupWritten
  }

  totalWritten += await crawlGroup({
    accounts: cfg.accounts,
    outDir: cfg.outDir,
    tags: ["clippings", "twitter"],
    archived: true,
  })
  totalWritten += await crawlGroup({
    accounts: cfg.newsAccounts,
    outDir: cfg.newsOutDir,
    tags: ["news", "twitter"],
    archived: false,
  })

  console.log(`done. total written: ${totalWritten}`)
}

main().catch((err) => {
  console.error("::error::crawler crashed:", String(err?.message || err))
  process.exit(1)
})
