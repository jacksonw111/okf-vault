import { test } from "node:test"
import assert from "node:assert/strict"
import { renderMarkdown } from "../src/render.js"
import type { RawTweet } from "../src/types.js"

function base(over: Partial<RawTweet> = {}): RawTweet {
  return {
    id: "100",
    text: "hello world",
    createdAt: "Sat Jun 01 08:00:00 +0000 2024",
    urls: [],
    media: { images: [], videos: [] },
    screenName: "Wen_Zw",
    displayName: "Wen",
    threadParts: [],
    promoted: false,
    ...over,
  }
}

test("render: original 基本结构 + frontmatter", () => {
  const md = renderMarkdown(base(), "original", "2024-06-17")
  assert.match(md, /title: "hello world"/)
  assert.match(md, /source: "https:\/\/x\.com\/Wen_Zw\/status\/100"/)
  assert.match(md, /tweet_type: "original"/)
  assert.match(md, /tweet_id: "100"/)
  assert.match(md, /published: 2024-06-01/)
  assert.match(md, /published_at: "2024-06-01T08:00:00\.000Z"/)
  assert.match(md, /created: "2024-06-17"/)
  assert.match(md, /\[\[@Wen_Zw\]\]/)
  assert.match(md, /\- "clippings"/)
  assert.match(md, /\- "twitter"/)
})

test("render: 媒体附在正文", () => {
  const md = renderMarkdown(
    base({ media: { images: ["https://pbs/a.jpg"], videos: ["https://v/x.mp4"] } }),
    "original",
    "2024-06-17",
  )
  assert.match(md, /!\[\]\(https:\/\/pbs\/a\.jpg\)/)
  assert.match(md, /视频：[\s\S]*https:\/\/v\/x\.mp4/)
})

test("render: thread 拼接续条", () => {
  const rt = base({
    text: "part1",
    threadParts: [base({ id: "101", text: "part2" })],
  })
  const md = renderMarkdown(rt, "thread", "2024-06-17")
  assert.match(md, /part1/)
  assert.match(md, /2\/2/)
  assert.match(md, /part2/)
})

test("render: quote 含被引用全文", () => {
  const rt = base({
    text: "my comment",
    quoted: base({ id: "9", text: "the quoted full text", screenName: "other" }),
  })
  const md = renderMarkdown(rt, "quote", "2024-06-17")
  assert.match(md, /my comment/)
  assert.doesNotMatch(md, /引用 @other：/)
  assert.match(md, /> 引用内容/)
  assert.match(md, /the quoted full text/)
})

test("render: retweet 含被转载全文", () => {
  const rt = base({
    retweeted: base({ id: "9", text: "original body", screenName: "other" }),
  })
  const md = renderMarkdown(rt, "retweet", "2024-06-17")
  assert.doesNotMatch(md, /转载 @other：/)
  assert.match(md, /> 转发内容/)
  assert.match(md, /original body/)
})

test("render: title/description 双引号转义", () => {
  const md = renderMarkdown(base({ text: 'she said "hi": http://x.com' }), "original", "2024-06-17")
  // 不应出现裸冒号破坏 YAML（双引号包裹内已转义）
  assert.match(md, /title: "she said \\"hi\\".*/)
})
