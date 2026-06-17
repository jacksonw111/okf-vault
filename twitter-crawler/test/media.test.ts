import { test } from "node:test";
import assert from "node:assert/strict";
import { extractMedia } from "../src/media.js";

test("extractMedia: 图片", () => {
  const m = extractMedia([
    { type: "photo", mediaUrlHttps: "https://pbs.twimg.com/a.jpg" },
  ]);
  assert.deepEqual(m, { images: ["https://pbs.twimg.com/a.jpg"], videos: [] });
});

test("extractMedia: 视频取最高码率 mp4", () => {
  const m = extractMedia([
    {
      type: "video",
      mediaUrlHttps: "https://pbs.twimg.com/thumb.jpg",
      videoInfo: {
        variants: [
          { contentType: "application/x-mpegURL", url: "https://v/hls.m3u8" },
          { contentType: "video/mp4", bitrate: 832000, url: "https://v/832.mp4" },
          { contentType: "video/mp4", bitrate: 2160000, url: "https://v/2160.mp4" },
        ],
      },
    },
  ]);
  assert.deepEqual(m, {
    images: [],
    videos: ["https://v/2160.mp4"],
  });
});

test("extractMedia: animated_gif 也算视频", () => {
  const m = extractMedia([
    {
      type: "animated_gif",
      mediaUrlHttps: "https://pbs.twimg.com/g.jpg",
      videoInfo: {
        variants: [{ contentType: "video/mp4", bitrate: 0, url: "https://g.mp4" }],
      },
    },
  ]);
  assert.deepEqual(m, { images: [], videos: ["https://g.mp4"] });
});

test("extractMedia: 空数组", () => {
  assert.deepEqual(extractMedia([]), { images: [], videos: [] });
});
