import path from "node:path"
import { fileURLToPath } from "node:url"
import accountsJson from "../accounts.json" with { type: "json" }

export interface Config {
  accounts: string[]
  newsAccounts: string[]
  maxPerRun: number
  authToken: string
  outDir: string // 绝对路径：<repoRoot>/content/inbox/twitter
  newsOutDir: string // 绝对路径：<repoRoot>/content/news/twitter
  inboxDoneDir: string // 绝对路径：<repoRoot>/content/inbox/_done
}

export function loadConfig(): Config {
  const raw = accountsJson as {
    accounts: string[]
    news_accounts?: string[]
    max_per_run?: number
  }
  const normalize = (a: string) => a.replace(/^@/, "")
  const accounts = (raw.accounts ?? []).map(normalize)
  const newsAccounts = (raw.news_accounts ?? []).map(normalize)
  const maxPerRun = Number(process.env.MAX_PER_RUN || raw.max_per_run || 20)
  const authToken = process.env.X_AUTH_TOKEN || ""

  // src/config.ts → 上两级 = 仓库根
  const here = path.dirname(fileURLToPath(import.meta.url))
  const repoRoot = path.resolve(here, "..", "..")
  const outDir = path.join(repoRoot, "content", "inbox", "twitter")
  const newsOutDir = path.join(repoRoot, "content", "news", "twitter")
  const inboxDoneDir = path.join(repoRoot, "content", "inbox", "_done")

  return { accounts, newsAccounts, maxPerRun, authToken, outDir, newsOutDir, inboxDoneDir }
}
