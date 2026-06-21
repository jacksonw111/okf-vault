import type { RawTweet, MediaInfo } from "./types.js"
import { formatDate } from "./io.js"

/** YAML 双引号安全包裹：转义反斜杠/双引号，换行→空格。 */
export function yamlQuote(s: string): string {
  const safe = (s ?? "").replace(/\\/g, "\\\\").replace(/"/g, '\\"').replace(/\r?\n/g, " ").trim()
  return `"${safe}"`
}

function titleFor(rt: RawTweet): string {
  const t = rt.text ?? ""
  const head = t.split(/\r?\n/)[0] ?? ""
  if (head.length <= 80) return head
  return [...head].slice(0, 77).join("") + "…"
}

function descriptionFor(rt: RawTweet): string {
  return [...(rt.text ?? "")].slice(0, 280).join("")
}

function isoDateTime(createdAt: string): string {
  const d = new Date(createdAt)
  if (isNaN(d.getTime())) return ""
  return d.toISOString()
}

function mediaBlock(media: MediaInfo): string {
  const lines: string[] = []
  for (const img of media.images) lines.push(`![](${img})`)
  if (media.videos.length > 0) {
    lines.push("")
    lines.push("视频：")
    for (const v of media.videos) lines.push(`- <${v}>`)
  }
  return lines.join("\n")
}

function bodyFor(rt: RawTweet, type: string): string {
  const parts: string[] = []

  if (type === "retweet" && rt.retweeted) {
    const r = rt.retweeted
    parts.push("> 转发内容")
    parts.push("")
    parts.push(quoteBlock(r.text))
    parts.push("")
    parts.push(`> 原帖：<https://x.com/${r.screenName}/status/${r.id}>`)
    if (hasMedia(r.media)) {
      parts.push("")
      parts.push(mediaBlock(r.media))
    }
    return parts.join("\n")
  }

  // 自身正文
  parts.push(rt.text)

  if (type === "thread" && rt.threadParts.length > 0) {
    const total = rt.threadParts.length + 1
    let i = 2
    for (const p of rt.threadParts) {
      parts.push("")
      parts.push(`--- ${i}/${total} ---`)
      parts.push("")
      parts.push(p.text)
      if (hasMedia(p.media)) {
        parts.push("")
        parts.push(mediaBlock(p.media))
      }
      i++
    }
  }

  if (type === "quote" && rt.quoted) {
    const q = rt.quoted
    parts.push("")
    parts.push("> 引用内容")
    parts.push("")
    parts.push(quoteBlock(q.text))
    parts.push("")
    parts.push(`> 原帖：<https://x.com/${q.screenName}/status/${q.id}>`)
    if (hasMedia(q.media)) {
      parts.push("")
      parts.push(mediaBlock(q.media))
    }
  }

  if (hasMedia(rt.media)) {
    parts.push("")
    parts.push(mediaBlock(rt.media))
  }

  return parts.join("\n")
}

function quoteBlock(text: string): string {
  return (text ?? "")
    .split(/\r?\n/)
    .map((l) => `> ${l}`)
    .join("\n")
}

function hasMedia(m: MediaInfo): boolean {
  return m.images.length > 0 || m.videos.length > 0
}

export function renderMarkdown(
  rt: RawTweet,
  type: string,
  createdDate: string,
  options: { tags?: string[] } = {},
): string {
  const tags = options.tags ?? ["clippings", "twitter"]
  const fm = [
    "---",
    `title: ${yamlQuote(titleFor(rt))}`,
    `source: ${yamlQuote(`https://x.com/${rt.screenName}/status/${rt.id}`)}`,
    "author:",
    `  - "[[@${rt.screenName}]]"`,
    `tweet_type: ${yamlQuote(type)}`,
    `tweet_id: ${yamlQuote(rt.id)}`,
    `published: ${formatDate(rt.createdAt)}`,
    `published_at: ${yamlQuote(isoDateTime(rt.createdAt))}`,
    `created: ${yamlQuote(createdDate)}`,
    `description: ${yamlQuote(descriptionFor(rt))}`,
    "tags:",
    ...tags.map((tag) => `  - ${yamlQuote(tag)}`),
    "---",
  ].join("\n")

  const body = bodyFor(rt, type)

  const tail = ["", "## 来源", `<https://x.com/${rt.screenName}/status/${rt.id}>`, ""].join("\n")

  return `${fm}\n\n${body}\n${tail}`
}
