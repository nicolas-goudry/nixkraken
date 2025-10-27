import process from 'node:process'
import implicitFigures from 'markdown-it-implicit-figures'
import { defineConfig } from 'vitepress'
import { mermaidPlugin } from './plugins/vitepress-mermaid'

const BASE_PATH=process.env.CI ? '/nixkraken/' : '/'
const ROOT_URL=`https://github.com/nicolas-goudry${BASE_PATH}`


export default defineConfig({
  srcDir: 'src',
  title: 'NixKraken',
  base: BASE_PATH,

  lastUpdated: true,
  metaChunk: true,

  markdown: {
    gfmAlerts: false,
    config: (md) => {
      md.use(implicitFigures, {
        figcaption: true,
        copyAttrs: '^class$'
      })
      md.use(mermaidPlugin)
    }
  },

  themeConfig: {
    logo: { src: '/nixkraken-logo.svg', width: 24, height: 24 },

    socialLinks: [
      { icon: 'github', link: ROOT_URL },
    ],

    search: { provider: 'local' },

    outline: { level: [2, 4] },
  },

  head: [
    [
      'link',
      { rel: 'icon', type: 'image/svg+xml', href: '/nixkraken/favicon.svg' }
    ],
    [
      'link',
      { rel: 'icon', type: 'image/png', href: '/nixkraken/favicon.png' }
    ],
    ['meta', { name: 'theme-color', content: '#42abb0' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:site_name', content: 'NixKraken' }],
    [
      'meta',
      {
        property: 'og:image',
        content: `${ROOT_URL}nixkraken-logo.svg`,
      }
    ],
    ['meta', { property: 'og:url', content: ROOT_URL }],
  ],

  sitemap: {
    hostname: 'https://nicolas-goudry.github.io',
    transformItems: (items) => items.map((item) => {
      item.url = `${BASE_PATH}${item.url}`
      return item
    }),
  },
})
