import type { UrlEntity, MediaInfo } from "./types.js";

/**
 * 把正文里的 t.co 短链还原成真实 URL，并剥离末尾的媒体 t.co。
 * 纯函数：不读时钟/网络。
 */
export function expandTco(
  text: string,
  urls: UrlEntity[],
  media: MediaInfo
): string {
  let out = text;

  // 1) 还原 url 实体里的短链
  for (const u of urls) {
    if (u.expandedUrl && u.url && u.url !== u.expandedUrl) {
      out = out.split(u.url).join(u.expandedUrl);
    }
  }

  // 2) 只剥离【尾部】媒体 t.co 占位（X 把它们追加在 fullText 末尾）；正文中间的保留
  const mediaTcos = [...media.images, ...media.videos].filter(
    (s): s is string => typeof s === "string" && s.startsWith("https://t.co/")
  );
  if (mediaTcos.length > 0) {
    const alt = mediaTcos.map(escapeReg).join("|");
    out = out.replace(new RegExp("(\\s*(?:" + alt + ")\\s*)+$"), "").trimEnd();
  }

  return out.trim();
}

function escapeReg(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}
