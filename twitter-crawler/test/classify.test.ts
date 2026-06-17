import { test } from "node:test";
import assert from "node:assert/strict";
import { classifyTweet } from "../src/classify.js";
import type { RawTweet } from "../src/types.js";

function base(over: Partial<RawTweet> = {}): RawTweet {
  return {
    id: "1",
    text: "x",
    createdAt: "Mon Jan 01 12:00:00 +0000 2024",
    urls: [],
    media: { images: [], videos: [] },
    screenName: "wen",
    displayName: "Wen",
    threadParts: [],
    promoted: false,
    ...over,
  };
}

test("classify: retweet 优先", () => {
  assert.equal(
    classifyTweet(base({ retweeted: base({ id: "9" }) })),
    "retweet"
  );
});

test("classify: quote", () => {
  assert.equal(classifyTweet(base({ quoted: base({ id: "9" }) })), "quote");
});

test("classify: thread（有续条）", () => {
  assert.equal(
    classifyTweet(base({ threadParts: [base({ id: "2" })] })),
    "thread"
  );
});

test("classify: original", () => {
  assert.equal(classifyTweet(base()), "original");
});
