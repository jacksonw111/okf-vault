import test from "node:test"
import assert from "node:assert"
import renderToString from "preact-render-to-string"
import NotFound from "./404"

test("404 page redirects trailing slash article URLs to the extensionless page", () => {
  const Component = NotFound()
  const html = renderToString(
    <>{Component({ cfg: { baseUrl: "jacksonw111.github.io/okf-vault", locale: "en-US" } } as any)}</>,
  )

  assert.match(html, /location\.pathname\.endsWith\("\/"\)/)
  assert.match(html, /location\.replace\(next \+ location\.search \+ location\.hash\)/)
})
