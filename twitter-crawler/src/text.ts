import type { UrlEntity } from "./types.js";

/**
 * 把正文里的 t.co 短链还原成真实 URL，并剥离媒体占位 t.co。
 * 纯函数：不读时钟/网络。
 *
 * @param text 推文正文（长推文优先用 noteTweet 全文）
 * @param urls url 实体（t.co → expandedUrl）；应同时来自 legacy.entities.urls 和
 *             noteTweet.entitySet.urls（长推文的链接实体只在 entitySet 里）
 * @param mediaTcoUrls 媒体占位 t.co 列表（来自 entities.media[].url）；这些 t.co 只是
 *                     图片/视频的占位符，真实媒体已单独渲染，故从正文里全部清除
 */
export function expandTco(
  text: string,
  urls: UrlEntity[],
  mediaTcoUrls: string[] = []
): string {
  let out = text;

  // 1) 还原 url 实体里的短链（t.co → expandedUrl）
  for (const u of urls) {
    if (u.expandedUrl && u.url && u.url !== u.expandedUrl) {
      out = out.split(u.url).join(u.expandedUrl);
    }
  }

  // 2) 清除媒体占位 t.co（图片/视频已单独渲染，正文里的占位短链无信息量）
  for (const m of mediaTcoUrls) {
    if (!m) continue;
    out = out.replace(new RegExp("\\s*" + escapeReg(m), "g"), "");
  }

  // 收拾残留空行
  return out.replace(/\n{3,}/g, "\n\n").trim();
}

function escapeReg(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}
