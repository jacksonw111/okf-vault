import fs from "node:fs"
import path from "node:path"
import type { RawTweet } from "./types.js"

/** X 时间串 "Sat Jun 01 08:00:00 +0000 2024" → "2024-06-01"；非法 → "unknown-date"。 */
export function formatDate(createdAt: string): string {
  const d = new Date(createdAt)
  if (isNaN(d.getTime())) return "unknown-date"
  const y = d.getUTCFullYear()
  const m = String(d.getUTCMonth() + 1).padStart(2, "0")
  const day = String(d.getUTCDate()).padStart(2, "0")
  return `${y}-${m}-${day}`
}

export function tweetFilePath(dir: string, rt: RawTweet): string {
  return `${dir}/${formatDate(rt.createdAt)}-${rt.id}.md`
}

export function alreadySaved(filePath: string): boolean {
  return fs.existsSync(filePath)
}

export function alreadySavedTweetId(searchDirs: string[], tweetId: string): boolean {
  const suffix = `-${tweetId}.md`

  for (const dir of searchDirs) {
    if (!fs.existsSync(dir)) continue
    const stack = [dir]
    while (stack.length > 0) {
      const cur = stack.pop()!
      for (const entry of fs.readdirSync(cur, { withFileTypes: true })) {
        const full = path.join(cur, entry.name)
        if (entry.isDirectory()) {
          stack.push(full)
        } else if (entry.isFile() && entry.name.endsWith(suffix)) {
          return true
        }
      }
    }
  }

  return false
}
