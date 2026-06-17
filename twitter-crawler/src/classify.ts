import type { RawTweet, TweetType } from "./types.js";

/**
 * 判定推文类型。注意：getUserTweets 已排除回复，故这里不处理 reply。
 * 优先级：retweet > quote > thread > original。
 * （article 类型 V1 不主动产出，保留在枚举里供未来。）
 */
export function classifyTweet(rt: RawTweet): TweetType {
  if (rt.retweeted) return "retweet";
  if (rt.quoted) return "quote";
  if (rt.threadParts.length > 0) return "thread";
  return "original";
}
