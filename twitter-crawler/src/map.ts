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

  const noteText: string | undefined = tw.noteTweet?.noteTweetResults?.result?.text;
  const baseText = noteText ?? fullText;

  const urlEntities: UrlEntity[] = (legacy.entities?.urls ?? []).map((u: any) => ({
    url: u.url,
    expandedUrl: u.expandedUrl,
  }));

  const mediaEntities: MediaEntity[] = (legacy.extendedEntities?.media ?? []) as MediaEntity[];
  const media = extractMedia(mediaEntities);

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
    text: expandTco(baseText, urlEntities, media),
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
