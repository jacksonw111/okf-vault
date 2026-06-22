import type { TweetApiUtilsData } from "twitter-openapi-typescript";
import type { RawTweet, MediaEntity, UrlEntity } from "./types.js";
import { expandTco } from "./text.js";
import { extractMedia } from "./media.js";

/** 库 TweetApiUtilsData → 本地 RawTweet。库字段名漂移只改这里。返回 null 表示无可用数据。 */
export function toRawTweet(t: TweetApiUtilsData | undefined | null): RawTweet | null {
  if (!t || !t.tweet) return null;
  const tw = t.tweet as any;
  const legacy = tw.legacy ?? {};
  const fullText: string = legacy.fullText ?? "";

  const noteResult: any = tw.noteTweet?.noteTweetResults?.result;
  const noteText: string | undefined = noteResult?.text;
  const baseText = noteText ?? fullText;

  // 链接实体：短推文在 legacy.entities.urls；长推文（note tweet）只在 noteTweet.entitySet.urls。
  // 两处合并，否则长推文里的 t.co 永远展不开。
  const urlEntities: UrlEntity[] = [
    ...((legacy.entities?.urls ?? []) as any[]),
    ...((noteResult?.entitySet?.urls ?? []) as any[]),
  ].map((u: any) => ({ url: u.url, expandedUrl: u.expandedUrl }));

  const mediaEntities: MediaEntity[] = (legacy.extendedEntities?.media ?? []) as MediaEntity[];
  const media = extractMedia(mediaEntities);

  // 媒体占位 t.co（entities.media[].url）：正文里清掉，真实媒体已单独渲染。
  const mediaTcoUrls: string[] = [
    ...((legacy.entities?.media ?? []) as any[]),
    ...((noteResult?.entitySet?.media ?? []) as any[]),
  ]
    .map((m: any) => m?.url)
    .filter((s: any): s is string => typeof s === "string");

  const screenName: string =
    (t.user as any)?.core?.screenName ?? (t.user as any)?.legacy?.screenName ?? "";
  const displayName: string =
    (t.user as any)?.legacy?.name ?? (t.user as any)?.core?.name ?? "";

  const threadParts = (t.replies ?? [])
    .map((r) => toRawTweet(r))
    .filter((x): x is RawTweet => x !== null)
    .sort((a, b) => (a.id < b.id ? -1 : a.id > b.id ? 1 : 0));

  return {
    id: tw.restId ?? legacy.idStr ?? "",
    text: expandTco(baseText, urlEntities, mediaTcoUrls),
    createdAt: legacy.createdAt ?? "",
    lang: legacy.lang,
    urls: urlEntities,
    media,
    screenName,
    displayName,
    quoted: t.quoted ? toRawTweet(t.quoted) ?? undefined : undefined,
    retweeted: t.retweeted ? toRawTweet(t.retweeted) ?? undefined : undefined,
    threadParts,
    promoted: !!t.promotedMetadata,
  };
}
