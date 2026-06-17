import { TwitterOpenApi } from "twitter-openapi-typescript";

/**
 * 用 auth_token cookie 换 ct0（CSRF），建已鉴权客户端。
 * 镜像 x-kit 的 _xClient，但绝不打印 token/cookie。
 */
export async function buildClient(authToken: string) {
  if (!authToken) throw new Error("X_AUTH_TOKEN is empty");

  // 1) GET manifest.json 带 auth_token cookie，从 set-cookie 收 ct0 等会话 cookie
  const resp = await fetch("https://x.com/manifest.json", {
    headers: { cookie: `auth_token=${authToken}` },
  });

  const setCookies = resp.headers.getSetCookie?.() ?? [];
  const cookies: Record<string, string> = {};
  for (const sc of setCookies) {
    const pair = sc.split(";")[0];
    const idx = pair.indexOf("=");
    if (idx <= 0) continue;
    const name = pair.slice(0, idx).trim();
    const value = pair.slice(idx + 1).trim();
    if (name) cookies[name] = value;
  }
  cookies["auth_token"] = authToken;

  if (!cookies["ct0"]) {
    throw new Error(
      "Failed to harvest ct0 from x.com (token may be invalid/expired)"
    );
  }

  const api = new TwitterOpenApi();
  const client = await api.getClientFromCookies(cookies);
  return client;
}
