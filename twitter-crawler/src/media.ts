import type { MediaEntity, MediaInfo } from "./types.js";

/** 从 extendedEntities.media 抽图片 URL 和最佳码率视频 URL。 */
export function extractMedia(entities: MediaEntity[]): MediaInfo {
  const images: string[] = [];
  const videos: string[] = [];

  for (const e of entities ?? []) {
    if (e.type === "photo") {
      if (e.mediaUrlHttps) images.push(e.mediaUrlHttps);
    } else {
      // video | animated_gif
      const variants = e.videoInfo?.variants ?? [];
      const mp4s = variants.filter(
        (v): v is { contentType: string; bitrate: number; url: string } =>
          v.contentType === "video/mp4" && typeof v.bitrate === "number"
      );
      const best =
        mp4s.length > 0
          ? mp4s.sort((a, b) => b.bitrate - a.bitrate)[0]
          : variants.find((v) => v.contentType === "video/mp4");
      if (best?.url) videos.push(best.url);
    }
  }

  return { images, videos };
}
