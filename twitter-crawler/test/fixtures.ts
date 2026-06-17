// 形状准确的合成夹具，镜像 twitter-openapi-typescript 的 TweetApiUtilsData（字段路径经源码核实）。
// 真实返回结构在 Task 13 用真实 token 抓一条做对照校验；如字段名漂移则在此修正。
import type { TweetApiUtilsData } from "twitter-openapi-typescript";

const user = (screenName: string, name = screenName) => ({
  restId: "1",
  isBlueVerified: false,
  core: { screenName, name },
  legacy: { screenName, name, description: "", followersCount: 1, friendsCount: 1 },
});

const legacy = (over: Record<string, unknown> = {}) => ({
  fullText: "short text",
  idStr: "100",
  createdAt: "Sat Jun 01 08:00:00 +0000 2024",
  lang: "en",
  conversationIdStr: "100",
  favoriteCount: 0,
  replyCount: 0,
  retweetCount: 0,
  entities: { urls: [] as any[], media: [] as any[] },
  extendedEntities: { media: [] as any[] },
  ...over,
});

const tweet = (over: Record<string, unknown> = {}) => ({
  restId: "100",
  legacy: legacy(over["legacy"] as Record<string, unknown>),
  ...over,
});

const base = (over: Record<string, unknown> = {}): TweetApiUtilsData =>
  ({
    raw: {} as any,
    tweet: tweet(),
    user: user("Wen_Zw"),
    replies: [],
    ...over,
  }) as unknown as TweetApiUtilsData;

/** 原创（短） */
export const fxOriginal = base();

/** 长推文（noteTweet 提供全文） */
export const fxNoteLong = base({
  tweet: tweet({
    legacy: legacy({
      fullText: "truncated… https://t.co/x",
      entities: { urls: [{ url: "https://t.co/x", expandedUrl: "https://real.example", displayUrl: "real", indices: [0, 0] }] as any[], media: [] as any[] },
    }),
    noteTweet: {
      noteTweetResults: { result: { text: "这是一条很长的推文全文，不会被截断，包含完整内容。 https://t.co/x" } },
    },
  }),
});

/** 线程：root + 1 条自回复 */
export const fxThread = base({
  tweet: tweet({
    restId: "100",
    legacy: legacy({ fullText: "thread start", conversationIdStr: "100", idStr: "100" }),
  }),
  replies: [
    {
      raw: {} as any,
      tweet: tweet({ restId: "101", legacy: legacy({ fullText: "thread cont", conversationIdStr: "100", idStr: "101", inReplyToStatusIdStr: "100" }) }),
      user: user("Wen_Zw"),
      replies: [],
    } as unknown as TweetApiUtilsData,
  ],
});

/** 引用 */
export const fxQuote = base({
  tweet: tweet({ legacy: legacy({ fullText: "my comment", isQuoteStatus: true, quotedStatusIdStr: "9" }) }),
  quoted: {
    raw: {} as any,
    tweet: tweet({ restId: "9", legacy: legacy({ fullText: "quoted full text" }) }),
    user: user("someoneelse"),
    replies: [],
  } as unknown as TweetApiUtilsData,
});

/** 转载 */
export const fxRetweet = base({
  tweet: tweet({ legacy: legacy({ fullText: "RT @someoneelse: body", retweeted: true }) }),
  retweeted: {
    raw: {} as any,
    tweet: tweet({ restId: "9", legacy: legacy({ fullText: "retweeted body" }) }),
    user: user("someoneelse"),
    replies: [],
  } as unknown as TweetApiUtilsData,
});

/** 广告（应被跳过） */
export const fxPromoted = base({ promotedMetadata: { advertiser: "x" } as any });
