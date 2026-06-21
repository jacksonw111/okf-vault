import { test } from "node:test"
import assert from "node:assert/strict"
import { formatDate, tweetFilePath, alreadySaved, alreadySavedTweetId } from "../src/io.js"
import type { RawTweet } from "../src/types.js"
import fs from "node:fs"
import os from "node:os"
import path from "node:path"

test("formatDate: 解析 X 时间串", () => {
  assert.equal(formatDate("Sat Jun 01 08:00:00 +0000 2024"), "2024-06-01")
})

test("formatDate: 非法串返回 unknown-date", () => {
  assert.equal(formatDate("garbage"), "unknown-date")
})

test("tweetFilePath: 格式 <date>-<id>.md", () => {
  const rt: RawTweet = {
    id: "123",
    text: "x",
    createdAt: "Sat Jun 01 08:00:00 +0000 2024",
    urls: [],
    media: { images: [], videos: [] },
    screenName: "Wen_Zw",
    displayName: "Wen",
    threadParts: [],
    promoted: false,
  }
  assert.equal(
    tweetFilePath("content/inbox/twitter/Wen_Zw", rt),
    "content/inbox/twitter/Wen_Zw/2024-06-01-123.md",
  )
})

test("alreadySaved: 文件存在返回 true", () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "tc-"))
  const f = path.join(dir, "x.md")
  fs.writeFileSync(f, "hi")
  assert.equal(alreadySaved(f), true)
  assert.equal(alreadySaved(path.join(dir, "nope.md")), false)
})

test("alreadySavedTweetId: 已归档推文也算已抓取", () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), "tc-"))
  const active = path.join(root, "content", "inbox", "twitter", "Wen_Zw")
  const done = path.join(root, "content", "inbox", "_done", "twitter", "Wen_Zw")
  fs.mkdirSync(active, { recursive: true })
  fs.mkdirSync(done, { recursive: true })
  fs.writeFileSync(path.join(done, "2026-06-16-2066866770447884610.md"), "hi")

  assert.equal(alreadySavedTweetId([active, done], "2066866770447884610"), true)
  assert.equal(alreadySavedTweetId([active, done], "999"), false)
})
