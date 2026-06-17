import { test } from "node:test";
import assert from "node:assert/strict";
import type { RawTweet } from "../src/types.js";

test("RawTweet 可以构造一个最小合法对象", () => {
  const rt: RawTweet = {
    id: "1",
    text: "hi",
    createdAt: "Mon Jan 01 12:00:00 +0000 2024",
    urls: [],
    media: { images: [], videos: [] },
    screenName: "wen",
    displayName: "Wen",
    threadParts: [],
    promoted: false,
  };
  assert.equal(rt.id, "1");
});
