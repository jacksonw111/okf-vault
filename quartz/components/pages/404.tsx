import { i18n } from "../../i18n"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "../types"

const NotFound: QuartzComponent = ({ cfg }: QuartzComponentProps) => {
  // If baseUrl contains a pathname after the domain, use this as the home link
  const url = new URL(`https://${cfg.baseUrl ?? "example.com"}`)
  const baseDir = url.pathname
  const redirectScript = `
(() => {
  const { location } = window
  const basePath = ${JSON.stringify(baseDir)}
  const normalizedBase = basePath.endsWith("/") ? basePath : basePath + "/"
  if (location.pathname !== normalizedBase && location.pathname.endsWith("/")) {
    const next = location.pathname.slice(0, -1)
    location.replace(next + location.search + location.hash)
  }
})()
`

  return (
    <>
      <script dangerouslySetInnerHTML={{ __html: redirectScript }} />
      <article class="popover-hint">
        <h1>404</h1>
        <p>{i18n(cfg.locale).pages.error.notFound}</p>
        <a href={baseDir}>{i18n(cfg.locale).pages.error.home}</a>
      </article>
    </>
  )
}

export default (() => NotFound) satisfies QuartzComponentConstructor
