// 本地最小类型层：只描述我们消费的字段，与 twitter-openapi-typescript 的重类型解耦。
// 库的 TweetApiUtilsData → toRawTweet(map.ts) → RawTweet。库字段名变了只改 map.ts。

export type TweetType = "original" | "thread" | "quote" | "retweet" | "article";

export interface UrlEntity {
  url: string;          // t.co 短链
  expandedUrl?: string; // 真实地址
}

export interface MediaVariant {
  bitrate?: number;
  contentType: string;
  url: string;
}

export interface MediaEntity {
  type: "photo" | "video" | "animated_gif";
  mediaUrlHttps: string;
  videoInfo?: { variants: MediaVariant[] };
}

export interface MediaInfo {
  images: string[];
  videos: string[];
}

export interface RawTweet {
  id: string;                  // restId
  text: string;                // 全文（noteTweet 优先），t.co 已还原，媒体 t.co 已剥离
  createdAt: string;           // 原始串，如 "Mon Jan 01 12:00:00 +0000 2024"
  lang?: string;
  urls: UrlEntity[];
  media: MediaInfo;
  screenName: string;          // 不带 @
  displayName: string;
  quoted?: RawTweet;           // 引用推文
  retweeted?: RawTweet;        // 被转载推文
  threadParts: RawTweet[];     // 线程续条（root 之外），id 升序
  promoted: boolean;           // 广告
}
