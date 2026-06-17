import { test } from "node:test";
import assert from "node:assert/strict";
import { expandTco } from "../src/text.js";

test("expandTco: 把 t.co 短链还原成 expandedUrl", () => {
  const out = expandTco(
    "see https://t.co/abc1 now",
    [{ url: "https://t.co/abc1", expandedUrl: "https://example.com/page" }],
    { images: [], videos: [] }
  );
  assert.equal(out, "see https://example.com/page now");
});

test("expandTco: 没有 expandedUrl 时保留原短链", () => {
  const out = expandTco("x https://t.co/zz", [{ url: "https://t.co/zz" }], {
    images: [],
    videos: [],
  });
  assert.equal(out, "x https://t.co/zz");
});

test("expandTco: 剥离尾部媒体 t.co（图片）", () => {
  const out = expandTco(
    "hello https://t.co/media1",
    [],
    { images: ["https://t.co/media1"], videos: [] }
  );
  assert.equal(out, "hello");
});

test("expandTco: 嵌入正文中间的媒体 t.co 保留（只剥尾部）", () => {
  const out = expandTco(
    "see https://t.co/media1 in the middle",
    [],
    { images: ["https://t.co/media1"], videos: [] }
  );
  assert.equal(out, "see https://t.co/media1 in the middle");
});

test("expandTco: 多个 url 都还原", () => {
  const out = expandTco(
    "a https://t.co/a b https://t.co/b",
    [
      { url: "https://t.co/a", expandedUrl: "https://a.com" },
      { url: "https://t.co/b", expandedUrl: "https://b.com" },
    ],
    { images: [], videos: [] }
  );
  assert.equal(out, "a https://a.com b https://b.com");
});
