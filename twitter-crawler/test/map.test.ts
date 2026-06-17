import { test } from "node:test";
import assert from "node:assert/strict";
import { toRawTweet } from "../src/map.js";
import {
  fxOriginal,
  fxNoteLong,
  fxThread,
  fxQuote,
  fxRetweet,
  fxPromoted,
} from "./fixtures.js";

test("toRawTweet: 原创", () => {
  const rt = toRawTweet(fxOriginal)!;
  assert.equal(rt.id, "100");
  assert.equal(rt.screenName, "Wen_Zw");
  assert.equal(rt.promoted, false);
  assert.equal(rt.threadParts.length, 0);
});

test("toRawTweet: 长推文取 noteTweet 全文 + t.co 还原", () => {
  const rt = toRawTweet(fxNoteLong)!;
  assert.equal(rt.text, "这是一条很长的推文全文，不会被截断，包含完整内容。 https://real.example");
});

test("toRawTweet: 线程续条进 threadParts 且升序", () => {
  const rt = toRawTweet(fxThread)!;
  assert.equal(rt.threadParts.length, 1);
  assert.equal(rt.threadParts[0].id, "101");
});

test("toRawTweet: quote 映射", () => {
  const rt = toRawTweet(fxQuote)!;
  assert.ok(rt.quoted);
  assert.equal(rt.quoted!.text, "quoted full text");
  assert.equal(rt.quoted!.screenName, "someoneelse");
});

test("toRawTweet: retweet 映射", () => {
  const rt = toRawTweet(fxRetweet)!;
  assert.ok(rt.retweeted);
  assert.equal(rt.retweeted!.text, "retweeted body");
});

test("toRawTweet: promoted 标记", () => {
  assert.equal(toRawTweet(fxPromoted)!.promoted, true);
});
