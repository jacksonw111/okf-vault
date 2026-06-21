import { test } from "node:test"
import assert from "node:assert/strict"
import accountsJson from "../accounts.json" with { type: "json" }

test("config: normal and news accounts are declared separately", () => {
  const raw = accountsJson as { accounts: string[]; news_accounts?: string[] }

  assert.ok(raw.accounts.includes("Wen_Zw"))
  assert.ok(raw.accounts.includes("QingQ77"))
  assert.deepEqual(raw.news_accounts, ["fxtrader", "livermoerR"])
})
