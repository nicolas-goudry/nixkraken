import { promises as fs } from 'node:fs'
import { defineAdditionalConfig, type DefaultTheme } from 'vitepress'

export default defineAdditionalConfig({
  description: 'GitKraken configuration and profiles, the Nix way.',

  themeConfig: {
    nav: nav(),

    sidebar: {
      '/guide/': { base: '/guide/', items: sidebarGuide() },
      '/contrib/': { base: '/contrib/', items: sidebarContrib() },
      '/reference/': { base: '/reference/', items: await sidebarReference() },
    },

    editLink: {
      pattern: 'https://github.com/nicolas-goudry/nixkraken/edit/main/docs/src/:path',
      text: 'Edit this page on GitHub',
    },

    footer: {
      message: 'Released under the MIT License',
      copyright:
        'Copyright © 2025 Nicolas Goudry<br/><sub><sup>GitKraken is the property of <a target="_blank" href="https://www.axosoft.com">Axosoft</a>, this project is not affiliated with them in any way</sup></sub>',
    },
  },
})

function nav(): DefaultTheme.NavItem[] {
  return [
    {
      text: 'Guide',
      link: '/guide/getting-started/quick-start',
      activeMatch: '/guide/',
    },
    {
      text: 'Reference',
      link: '/reference/nixkraken',
      activeMatch: '/reference/',
    },
    {
      text: 'Contribute',
      link: '/contrib/contributing',
      activeMatch: '/contrib/',
    },
    { text: 'Version: @CURRENT_VERSION@', link: '#' },
  ]
}

function sidebarGuide(): DefaultTheme.SidebarItem[] {
  return [
    {
      text: 'Getting Started',
      base: '/guide/getting-started/',
      items: [
        { text: 'Quick Start', link: 'quick-start' },
        {
          text: 'Installation',
          collapsed: false,
          items: [
            { text: 'Flakes', link: 'flakes-install' },
            { text: 'Non-Flakes', link: 'classic-install' },
            { text: 'Additional Packages', link: 'packages' },
          ],
        },
        { text: 'Examples', link: 'config-examples' },
      ],
    },
    {
      text: 'Important Notes',
      base: '/guide/notes/',
      items: [
        { text: 'Known Caveats', link: 'caveats' },
        { text: 'Compatibility', link: 'compatibility' },
      ],
    },
    {
      text: 'User Guides',
      base: '/guide/user/',
      items: [
        { text: 'Binary Cache', link: 'caching' },
        { text: 'Authentication', link: 'auth' },
        { text: 'Profiles', link: 'profiles' },
        { text: 'Theming', link: 'theming' },
      ],
    },
    { text: 'Options Reference', base: '/reference/', link: 'nixkraken' },
  ]
}

function sidebarContrib(): DefaultTheme.SidebarItem[] {
  return [
    {
      text: 'Contributing',
      items: [
        { text: 'How To', link: 'contributing' },
        { text: 'Modules', link: 'modules' },
        { text: 'Themes', link: 'themes' },
        {
          text: 'GitKraken',
          base: '/contrib/gitkraken/',
          collapsed: true,
          items: [
            { text: 'Redistribution', link: 'redistribution' },
            {
              text: 'Utilities',
              base: '/contrib/gitkraken/utils/',
              collapsed: true,
              items: [
                { text: 'App Extractor', link: 'app-extractor' },
                { text: 'Deep JSON Differ', link: 'deep-json-differ' },
                { text: 'Config Discovery', link: 'config-discovery' },
              ],
            },
          ],
        },
        {
          text: 'Helper Packages',
          base: '/contrib/pkgs/',
          collapsed: true,
          items: [
            { text: 'Introduction', link: 'intro' },
            { text: 'gk-configure', link: 'configure' },
            { text: 'gk-encrypt and gk-decrypt', link: 'encrypt-decrypt' },
            { text: 'gk-login', link: 'login' },
            { text: 'gk-theme', link: 'theme' },
          ],
        },
        {
          text: 'Tests',
          base: '/contrib/tests/',
          collapsed: true,
          items: [
            { text: 'Introduction', link: 'intro' },
            { text: 'Running Tests', link: 'running' },
            { text: 'Writing Tests', link: 'writing' },
          ],
        },
        { text: 'Documentation', link: 'docs' },
      ],
    },
  ]
}

function sidebarReference(): DefaultTheme.SidebarItem[] {
  return [
    {
      text: 'Options Reference',
      items: [
        { text: 'Module', link: 'nixkraken' },
        {
          text: 'Groups',
          collapsed: false,
          items: [
            { text: 'datetime', link: 'datetime' },
            { text: 'git', link: 'git' },
            { text: 'gpg', link: 'gpg' },
            { text: 'graph', link: 'graph' },
            { text: 'notifications', link: 'notifications' },
            {
              text: 'profiles',
              link: 'profiles',
              collapsed: true,
              items: [
                { text: 'git', link: 'profiles/git' },
                { text: 'gpg', link: 'profiles/gpg' },
                { text: 'graph', link: 'profiles/graph' },
                { text: 'ssh', link: 'profiles/ssh' },
                { text: 'tools', link: 'profiles/tools' },
                { text: 'ui', link: 'profiles/ui' },
                { text: 'user', link: 'profiles/user' },
              ],
            },
            { text: 'ssh', link: 'ssh' },
            { text: 'tools', link: 'tools' },
            { text: 'ui', link: 'ui' },
            { text: 'user', link: 'user' },
          ],
        },
      ],
    },
  ]
}
