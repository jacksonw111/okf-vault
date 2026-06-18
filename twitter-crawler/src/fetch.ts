import type { RawTweet } from "./types.js";
import { toRawTweet } from "./map.js";

// Minimal client interface (subset of twitter-openapi-typescript client)
export interface MinClient {
  getUserApi(): {
    getUserByScreenName(p: { screenName: string }): Promise<{
      data: { user?: { restId?: string } | undefined };
    }>;
  };
  getTweetApi(): {
    getUserTweets(p: {
      userId: string;
      count?: number;
      cursor?: string;
    }): Promise<{
      data: {
        data: any[];
        cursor?: { bottom?: { value?: string } };
      };
    }>;
  };
}

export interface FetchResult {
  tweets: RawTweet[];
  stoppedAtKnown: boolean;
}

/**
 * Fetch tweets for an account, paginating until: hitting a known tweet, reaching maxPerRun, or no more pages.
 */
export async function fetchTweetsForAccount(args: {
  client: MinClient;
  screenName: string;
  maxPerRun: number;
  isSaved: (tweetId: string) => boolean;
}): Promise<FetchResult> {
  const { client, screenName, maxPerRun, isSaved } = args;

  let userResp;
  try {
    userResp = await client.getUserApi().getUserByScreenName({ screenName });
  } catch (err: any) {
    throw new Error(`getUserByScreenName(@${screenName}) failed: ${err?.message || err}`);
  }
  const userId = userResp.data.user?.restId;
  if (!userId) throw new Error(`account @${screenName} not found (no restId)`);

  const out: RawTweet[] = [];
  let cursor: string | undefined;
  let stoppedAtKnown = false;

  for (;;) {
    let resp;
    try {
      resp = await client.getTweetApi().getUserTweets({ userId, count: 40, cursor });
    } catch (err: any) {
      throw new Error(`getUserTweets(@${screenName}) failed: ${err?.message || err}`);
    }
    for (const item of resp.data.data ?? []) {
      if (item?.promotedMetadata) continue; // skip ads
      let rt;
      try {
        rt = toRawTweet(item);
      } catch (err: any) {
        // 单条推文解析失败不拖垮整个账号：跳过并记日志
        console.error(
          `::warning::@${screenName} skip malformed tweet item: ${err?.message || err}`
        );
        continue;
      }
      if (!rt) continue;

      if (isSaved(rt.id)) {
        stoppedAtKnown = true;
        return { tweets: out, stoppedAtKnown };
      }

      out.push(rt);
      if (out.length >= maxPerRun) {
        return { tweets: out, stoppedAtKnown };
      }
    }

    cursor = resp.data.cursor?.bottom?.value;
    if (!cursor) break;
  }

  return { tweets: out, stoppedAtKnown };
}
