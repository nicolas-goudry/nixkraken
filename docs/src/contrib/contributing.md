[cocogitto]: https://docs.cocogitto.io
[conventional-commits]: https://www.conventionalcommits.org/en/v1.0.0/#specification
[determinate-nix]: https://determinate.systems/nix
[direnv]: https://direnv.net
[doc-compat]: ../guide/notes/compatibility.md
[doc-docs]: ./docs.md
[doc-module]: ./modules.md
[doc-pkgs]: ./pkgs/intro.md
[doc-tests]: ./tests/intro.md
[doc-themes]: ./themes.md
[garnix]: https://garnix.io
[git-hooks]: https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
[github-coc]: https://github.com/nicolas-goudry/nixkraken/blob/main/CODE_OF_CONDUCT.md
[github-fork]: https://github.com/nicolas-goudry/nixkraken/fork
[github-issues]: https://github.com/nicolas-goudry/nixkraken/issues
[github-prs]: https://github.com/nicolas-goudry/nixkraken/pulls
[github-shell]: https://github.com/nicolas-goudry/nixkraken/blob/main/shell.nix
[github]: https://github.com/nicolas-goudry/nixkraken
[gitkraken]: https://www.gitkraken.com/git-client
[gnu-bash]: https://www.gnu.org/software/bash
[hm]: https://nix-community.github.io/home-manager/index.xhtml
[jq]: https://jqlang.org
[lix]: https://lix.systems
[lorri-github]: https://github.com/nix-community/lorri
[markdown]: https://www.markdownguide.org
[mdbook-alerts]: https://github.com/lambdalisue/rs-mdbook-alerts
[mdbook-linkcheck]: https://github.com/Michael-F-Bryan/mdbook-linkcheck
[mdbook-mermaid]: https://github.com/badboy/mdbook-mermaid
[mdbook]: https://rust-lang.github.io/mdBook
[mdn-css]: https://developer.mozilla.org/en-US/docs/Web/CSS
[mdn-html]: https://developer.mozilla.org/en-US/docs/Web/HTML
[mdn-js]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
[nix-github]: https://github.com/NixOS/nix
[nix-manual-language]: https://nix.dev/manual/nix/stable/language/index.html
[nixdev-shell]: https://nix.dev/tutorials/first-steps/declarative-shell#declarative-reproducible-envs
[nixos-manual]: https://nixos.org/manual/nixos/stable
[nixos-wiki-flakes]: https://wiki.nixos.org/wiki/Flakes
[nixpkgs-manual]: https://nixos.org/manual/nixpkgs/stable
[nodejs]: https://nodejs.org
[python]: https://python.org
[snix]: https://snix.dev
[tvix-github]: https://github.com/tvlfyi/tvix
[wikipedia-atomic-commits]: https://en.wikipedia.org/wiki/Atomic_commit#Revision_control
[wikipedia-json]: https://en.wikipedia.org/wiki/JSON

# How to Contribute

Contributions are welcome across [documentation][doc-docs], [module options][doc-module], [helper packages][doc-pkgs], [tests][doc-tests], [themes][doc-themes], compatibility work and every other aspects related to NixKraken.

Development occurs solely on the [official GitHub repository][github].

## Before Starting

### Do Not Waste Your Time

Please make sure to read the current documentation as a whole before considering to contribute, something you are planning to contribute to may already be available.

Also take a look at currently [open issues][github-issues] and [pull requests][github-prs] before starting to work on a feature or bug fix, as someone else may already be planning to or has already started working on something similar.

### Conform to the Code of Conduct

Read our [code of conduct][github-coc] and conform to it in all your interactions with others working on the project. However, do not stress yourself too much over this, everyone can make mistakes as long as they acknowledge and correct them.

### Be Polyglot?

NixKraken uses various languages, with the predominant one being the [Nix language][nix-manual-language].

Additionally, we use a fair bit of [Bash scripting][gnu-bash] for [helper packages][doc-pkgs], some [Python][python] for [automated tests][doc-tests] and some [HTML][mdn-html], [CSS][mdn-css] and [JavaScript][mdn-js] for the [documentation][doc-docs].

Contributors are expected to be familiar, to some varying extent, with the following languages and tools, depending on the topic involved:

|                                     | Modules | Tests | Pkgs | Themes | Caching | Docs |
| ----------------------------------- | :-----: | :---: | :--: | :----: | :-----: | :--: |
| [Nix language][nix-manual-language] |   ✅    |  ✅   |  ✅  |   ✅   |   ✅    |  ✅  |
| [NixOS][nixos-manual]               |   ✅    |  ✅   |  ┊   |   ┊    |    ┊    |  ┊   |
| [nixpkgs][nixpkgs-manual]           |   ✅    |  ✅   |  ✅  |   ✅   |   ✅    |  ✅  |
| [Home Manager][hm]                  |   ✅    |   ┊   |  ┊   |   ┊    |    ┊    |  ┊   |
| [Bash scripting][gnu-bash]          |   ✅    |   ┊   |  ✅  |   ┊    |    ┊    |  ┊   |
| [JSON][wikipedia-json]              |   ✅    |   ┊   |  ✅  |   ┊    |    ┊    |  ┊   |
| [jq][jq]                            |   ✅    |   ┊   |  ┊   |   ┊    |    ┊    |  ┊   |
| [GitKraken][gitkraken]              |   ✅    |  ✅   |  ✅  |   ┊    |    ┊    |  ┊   |
| [Python][python]                    |    ┊    |  ✅   |  ┊   |   ┊    |    ┊    |  ┊   |
| [Markdown][markdown]                |    ┊    |   ┊   |  ┊   |   ┊    |    ┊    |  ✅  |
| [mdBook][mdbook]                    |    ┊    |   ┊   |  ┊   |   ┊    |    ┊    |  ✅  |
| [HTML][mdn-html]                    |    ┊    |   ┊   |  ┊   |   ┊    |    ┊    |  ✅  |
| [CSS][mdn-css]                      |    ┊    |   ┊   |  ┊   |   ┊    |    ┊    |  ✅  |
| [JavaScript][mdn-js]                |    ┊    |   ┊   |  ┊   |   ┊    |    ┊    |  ✅  |
| [Garnix][garnix]                    |    ┊    |   ┊   |  ┊   |   ┊    |   ✅    |  ┊   |

Although this list could look quite daunting, do not run away yet. You will most likely be doing great just knowing a small bit of any of these, and can only get better at them while working on NixKraken.

### Get Familiar with our Git Workflow

As noted in the [compatibility section][doc-compat], we use a variety of branches to conduct work on NixKraken:

- `main`: this is the development branch, where all new (potentially unstable) features live
- `stable`: this is a "dummy" branch which tracks the latest release branch commit
- release branches: these are branches named after the GitKraken version they are known to be compatible with

When contributing to NixKraken, you will either want to add something new or fix something broken. Your contribution could either target a specific release branch, or the development branch, or both.

In the case of a fix or feature targeting both development and release branch(es), we prefer to first integrate the changes into the development branch, and only then backport them to the release branch(es).

Please find below the lifecycle of a contribution to NixKraken:

1. [Fork the repository][github-fork]
2. Work on your feature/bugfix in whatever branch you wish
3. Commit your changes using [atomic commits][wikipedia-atomic-commits] and following [conventional commit style][conventional-commits]
4. Open a [pull request][github-prs] to either the `main` branch or a specific release branch
5. PR is merged
6. Backport to release branch(es) happens, if relevant
7. `stable` branch is updated, if relevant

::: info

We use [Cocogitto][cocogitto] to enforce conventional commits.

:::

## Repository Layout

Find below a root overview of the repository:

```txt
.
├── .github        # GitHub configuration (CI workflows, issue templates, …)
├── .hooks         # Auto Git hooks
├── docs           # Documentation website sources
├── gitkraken      # GitKraken derivations for caching
├── modules        # Module sources
├── pkgs           # Helper packages sources
├── tests          # Module tests
├── themes         # GitKraken themes
├── .envrc         # direnv configuration
├── .prettierrc    # Prettier custom configuration
├── flake.nix      # Root Flake definition
├── garnix.yaml    # Garnix CI configuration
├── module.nix     # Module entrypoint
├── shell.nix      # Nix development shell definition
└── treefmt.nix    # Code style formatters configuration
```

Admittedly this is a lot, but everything is covered in this documentation, so read along!

## Prerequisites

Since NixKraken is mostly written in [Nix][nix-manual-language], it is the only hard requirement. There is however a known constraint on Nix version ≥ 2.4, which is quite old anyway, so you should be good.

Additionally, NixKraken should be compatible with any Nix "flavor" ([upstream Nix][nix-github], [Determinate Nix][determinate-nix], [Lix][lix], [Tvix][tvix-github], [Snix][snix], …) since it only uses basic Nix capabilities.

Lastly, serving the documentation website locally for development purposes requires [mdBook][mdbook] to be available with the following plugins:

- [mdbook-alerts][mdbook-alerts]
- [mdbook-linkcheck][mdbook-linkcheck]
- [mdbook-mermaid][mdbook-mermaid]

Building the documentation website only requires Nix.

## Development Generalities

### Nix Development Shell

For a better developer experience, NixKraken provides a [Nix development shell][nixdev-shell] which source code can be viewed in the [`shell.nix` file][github-shell].

This development shell does several things:

- add [mdBook][mdbook] package and required plugins, for building documentation
- add [NodeJS][nodejs] package, for building options reference documentation
- add [helper packages][doc-pkgs], for testing and debugging
- add [Cocogitto][cocogitto], for:
  - enforcing conventional commits
  - installing [Git hooks][git-hooks]

Enabling the development shell can be done in various ways:

```bash
# Using new Nix commands
nix develop
```

```bash
# ...or classic Nix commands
nix-shell
```

```bash
# ...or direnv
direnv allow
```

#### About direnv

[direnv][direnv] is quite a handy tool which will automatically load the development shell (using classic Nix) when navigating to the project root directory or any of its subdirectories, as long as it is trusted using `direnv allow`.

::: tip

If working on [`shell.nix`][github-shell], do not forget to run `direnv reload` to _re-apply_ the development shell, or use tools like [lorri][lorri-github] to do this automatically for you.

:::

### To Flake or Not to Flake?

_…that is the question!_

The main distribution method for NixKraken is through [Flakes][nixos-wiki-flakes]. However, we do not want to alienate users who do not use them, nor do we want to force its use on everyone. Our goal is to satisfy everyone.

For this reason, all [Nix][nix-manual-language] code in the repository **must be compatible with both Flakes and non Flakes setups**. This means that building any of the tools provided by the project should work either with `nix build` and `nix-build`. This also means that all documentation bits should provide instructions for both worlds.
