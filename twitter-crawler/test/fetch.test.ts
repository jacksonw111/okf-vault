import { test } from "node:test";
import assert from "node:assert/strict";
import { fetchTweetsForAccount } from "../src/fetch.js";
import type { RawTweet } from "../src/types.js";

// Minimal fake client: returns predetermined pages with cursor support
function fakeClient(pages: any[][]) {
  let i = 0;
  return {
    async getUserByScreenName({ screenName }: { screenName: string }) {
      return { data: { user: { restId: "u1" } } };
    },
    async getUserTweets({ cursor }: { cursor?: string }) {
      const page = pages[Math.min(i, pages.length - 1)];
      i++;
      return { data: { data: page, cursor: { bottom: undefined } } };
    },
  };
}

const mk = (id: string): RawTweet => ({
  id,
  text: "t " + id,
  createdAt: "Sat Jun 01 08:00:00 +0000 2024",
  urls: [],
  media: { images: [], videos: [] },
  screenName: "wen",
  displayName: "Wen",
  threadParts: [],
  promoted: false,
});

test("fetch: stops when encountering known tweet", async () => {
  const client = {
    getUserApi: () => ({
      async getUserByScreenName() {
        return { data: { user: { restId: "u1" } } };
      },
    }),
    getTweetApi: () => ({
      async getUserTweets() {
        return {
          data: {
            data: [
              { tweet: { restId: "200", legacy: { fullText: "a", createdAt: "Sat Jun 01 08:00:00 +0000 2024" } }, user: { core: { screenName: "wen" }, legacy: {} }, replies: [] },
              { tweet: { restId: "100", legacy: { fullText: "b", createdAt: "Sat Jun 01 08:00:00 +0000 2024" } }, user: { core: { screenName: "wen" }, legacy: {} }, replies: [] },
            ],
            cursor: { bottom: { value: "next-cursor" } },
          },
        };
      },
    }),
  };
  const { tweets, stoppedAtKnown } = await fetchTweetsForAccount({
    // @ts-ignore only methods we consume
    client,
    screenName: "wen",
    maxPerRun: 50,
    isSaved: (id) => id === "100",
  });
  assert.equal(stoppedAtKnown, true);
  // 100 is known so skipped; only 200 produced
  assert.equal(tweets.length, 1);
  assert.equal(tweets[0].id, "200");
});

test("fetch: maxPerRun limits results", async () => {
  const client = {
    getUserApi: () => ({
      async getUserByScreenName() {
        return { data: { user: { restId: "u1" } } };
      },
    }),
    getTweetApi: () => ({
      async getUserTweets() {
        return {
          data: {
            data: [
              { tweet: { restId: "5", legacy: { fullText: "x", createdAt: "Sat Jun 01 08:00:00 +0000 2024" } }, user: { core: { screenName: "wen" }, legacy: {} }, replies: [] },
              { tweet: { restId: "4", legacy: { fullText: "x", createdAt: "Sat Jun 01 08:00:00 +0000 2024" } }, user: { core: { screenName: "wen" }, legacy: {} }, replies: [] },
              { tweet: { restId: "3", legacy: { fullText: "x", createdAt: "Sat Jun 01 08:00:00 +0000 2024" } }, user: { core: { screenName: "wen" }, legacy: {} }, replies: [] },
            ],
            cursor: { bottom: { value: "more" } },
          },
        };
      },
    }),
  };
  const { tweets } = await fetchTweetsForAccount({
    // @ts-ignore
    client,
    screenName: "wen",
    maxPerRun: 2,
    isSaved: () => false,
  });
  assert.equal(tweets.length, 2);
});
