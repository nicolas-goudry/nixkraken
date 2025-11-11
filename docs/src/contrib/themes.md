[doc-contrib-gitflow]: ./contributing.md#get-familiar-with-our-git-workflow
[doc-opt-extrathemes]: ../reference/ui.md#uiextrathemes
[doc-theme-pkg]: ./pkgs/theme.md
[doc-theming]: ../guide/user/theming.md#use-a-nixkraken-theme
[flakes-outputs]: https://nixos-and-flakes.thiscute.world/other-usage-of-flakes/outputs
[gitkraken]: https://www.gitkraken.com/git-client
[hm]: https://nix-community.github.io/home-manager/index.xhtml
[jsonc]: https://jsonc.org
[loc-build]: #build
[loc-internals]: #internals
[loc-multiple-variants]: #multiple-variants
[loc-single-variant]: #single-variant
[nix-manual-drv]: https://nix.dev/manual/nix/stable/language/derivations.html
[nix-manual-functions]: https://nix.dev/manual/nix/stable/language/syntax#functions
[nix-manual-store]: https://nix.dev/manual/nix/stable/store
[nixpkgs-manual-fetchfromgh]: https://nixos.org/manual/nixpkgs/stable/#fetchfromgithub
[nixpkgs-manual-passthru]: https://nixos.org/manual/nixpkgs/stable/#chap-passthru
[nixpkgs-manual-src-hash]: https://nixos.org/manual/nixpkgs/stable/#sec-pkgs-fetchers-updating-source-hashes
[repo-themes-default]: https://github.com/nicolas-goudry/nixkraken/blob/main/themes/default.nix
[repo-themes-root]: https://github.com/nicolas-goudry/nixkraken/blob/main/themes

# Themes

Beyond the [Home Manager][hm] module, NixKraken provides complementary packages for [GitKraken][gitkraken] themes.

These reside under the [`themes` directory][repo-themes-root] and are exposed as [Flake outputs][flakes-outputs] inside the `packages.gitkraken-themes` output.

For end-user usage within NixKraken and the list of available themes, see the [theming guide][doc-theming].

## Build

The main entry point for building themes is [`themes/default.nix`][repo-themes-default]. It defines a [derivation][nix-manual-drv] that does two things:

- bundle all theme sets as part of the derivation build
- expose all theme sets as attributes of its [`passthru` attribute][nixpkgs-manual-passthru]

### All theme sets

```sh
# Build all theme sets using new Nix commands
$ nix build '.#gitkraken-themes'
```

```sh
# ...or classic Nix commands
$ nix-build ./themes
```

The `result` directory will bundle all theme sets and their respective theme files in subdirectories named after the theme set, as shown below:

```txt
result
├── catppuccin
│   ├── catppuccin-frappe.jsonc
│   ├── catppuccin-latte.jsonc
│   ├── catppuccin-macchiato.jsonc
│   ├── catppuccin-mocha.jsonc
│   └── VERSION
├── celestial-dark/
├── color-blind/
├── dracula/
├── matcha-dark-sea/
├── monochrome/
├── monokai/
├── night-owl/
├── nineteen-eighty-four/
├── nord/
├── oled-dream/
├── one-dark/
├── poimandres/
├── solarized/
├── the-matrix/
├── tokyo-night/
└── umbraco-dark/

18 directories, 41 files
```

::: info

This output is an example of the `result` directory built at the time of writing, actual content may change if themes are added/removed.

:::

### Specific theme set

```sh
# Build Catppuccin theme set using new Nix commands
$ nix build '.#gitkraken-themes.catppuccin'
```

```sh
# ...or classic Nix commands
$ nix-build ./themes -A catppuccin
```

```txt
result
├── catppuccin-frappe.jsonc
├── catppuccin-latte.jsonc
├── catppuccin-macchiato.jsonc
└── catppuccin-mocha.jsonc

1 directory, 4 files
```

## Directory Structure

Here is an overview of the [`themes` directory][repo-themes-root] structure:

```txt
themes
├── sets
│   ├── catppuccin
│   │   └── package.nix
│   ├── celestial-dark
│   │   ├── celestial-dark.jsonc
│   │   └── package.nix
│   ├── color-blind/
│   ├── dracula/
│   └── ...
└── default.nix
```

All theme sets live in `themes/sets` under directories named after the set. The set directory is the attribute used for theme selection in the entry point.

Each set must define a `package.nix` file holding the [derivation code][loc-internals], and may optionally include additional files needed for building the derivation.

## Internals

Each theme is a [Nix function][nix-manual-functions] that returns a [derivation][nix-manual-drv]. Theme derivations must:

1. Install [JSONC][jsonc] files to the derivation output (`$out`)
2. Expose variant filenames via [`passthru` attribute][nixpkgs-manual-passthru]

   - define a `passthru` attribute that maps the logical variant to the exact JSONC filename that GitKraken expects in `ui.theme`
   - for single-variant themes, set `passthru.default` to the filename

There are two common patterns, depending on whether the theme has a [single variant][loc-single-variant] or [multiple variants][loc-multiple-variants].

### Single Variant

For single variant themes, the derivation is straightforward:

<<< ../../../themes/sets/tokyo-night/package.nix

### Multiple Variants

Multi-variant themes typically accept an optional `withVariants` argument, validate it against supported variants, and output multiple JSONC files accordingly.

Example (Catppuccin):

<<< ../../../themes/sets/catppuccin/package.nix

## Maintenance

### Add New Themes

The simplest approach is to copy an existing theme with a similar variant pattern (single vs multiple) and adapt it.

::: warning

GitKraken theme filenames must be unique across installed themes. If two themes install the same filename, they will overwrite each other.

:::

Recommended checklist:

<i class="fa-regular fa-square-check"></i> Choose a base (single or multiple variants) theme as template\
<i class="fa-regular fa-square-check"></i> Update `name`, `version`, `src` and `meta`\
<i class="fa-regular fa-square-check"></i> Update `themePath` (single variant themes only)\
<i class="fa-regular fa-square-check"></i> Update `defaultVariants` list (multiple variants themes only)\
<i class="fa-regular fa-square-check"></i> Ensure the JSONC files are copied from the correct source location to `$out`\
<i class="fa-regular fa-square-check"></i> [Build the themes][loc-build] to validate your theme

### Updating Themes

When a theme releases a new version:

- bump the version attribute
- update the src fetcher hash (e.g., for [`fetchFromGitHub`][nixpkgs-manual-fetchfromgh])
  - easiest path: set `hash = ""` per the [manual][nixpkgs-manual-src-hash]
  - build once (expected to fail), copy the reported hash into the derivation
- verify file locations in the source repository
  - if paths changed, update the derivation's `installPhase` accordingly
- verify file names in the source repository
  - if names changed, update the derivation's accordingly (`themePath` or `defaultVariants`)
- rebuild and verify the passthru still matches the installed filenames
- [commit, push, open PR][doc-contrib-gitflow]
