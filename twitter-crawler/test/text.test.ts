import { test } from "node:test";
import assert from "node:assert/strict";
import { expandTco } from "../src/text.js";

test("expandTco: 把 t.co 短链还原成 expandedUrl", () => {
  const out = expandTco(
    "see https://t.co/abc1 now",
    [{ url: "https://t.co/abc1", expandedUrl: "https://example.com/page" }],
    []
  );
  assert.equal(out, "see https://example.com/page now");
});

test("expandTco: 没有 expandedUrl 时保留原短链", () => {
  const out = expandTco("x https://t.co/zz", [{ url: "https://t.co/zz" }], []);
  assert.equal(out, "x https://t.co/zz");
});

test("expandTco: 剥离尾部媒体占位 t.co", () => {
  const out = expandTco("hello https://t.co/media1", [], [
    "https://t.co/media1",
  ]);
  assert.equal(out, "hello");
});

test("expandTco: 媒体占位 t.co 全清除（含正文中间）", () => {
  // 媒体 t.co 是图片/视频占位符，真实媒体已单独渲染，正文里无论位置都清掉
  const out = expandTco(
    "see https://t.co/media1 in the middle",
    [],
    ["https://t.co/media1"]
  );
  assert.equal(out.includes("t.co/media1"), false);
  assert.match(out, /see.*middle/);
});

test("expandTco: 多个 url 都还原", () => {
  const out = expandTco(
    "a https://t.co/a b https://t.co/b",
    [
      { url: "https://t.co/a", expandedUrl: "https://a.com" },
      { url: "https://t.co/b", expandedUrl: "https://b.com" },
    ],
    []
  );
  assert.equal(out, "a https://a.com b https://b.com");
});

test("expandTco: 同时还原真链接 + 清媒体占位", () => {
  const out = expandTco(
    "项目 https://t.co/proj 配图 https://t.co/media1",
    [{ url: "https://t.co/proj", expandedUrl: "https://example.com/proj" }],
    ["https://t.co/media1"]
  );
  assert.equal(out, "项目 https://example.com/proj 配图");
});
