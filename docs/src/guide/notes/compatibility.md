[doc-contrib]: ../../contrib/contributing.md
[doc-install-nonflake]: ../getting-started/classic-install.md
[gh-issues]: https://github.com/nicolas-goudry/nixkraken/issues
[gh-nixpkgs-gitkraken]: https://github.com/NixOS/nixpkgs/blob/nixos-25.05/pkgs/by-name/gi/gitkraken/package.nix
[gh-prs]: https://github.com/nicolas-goudry/nixkraken/pulls
[gitkraken]: https://www.gitkraken.com/git-client
[nixos-wiki-flakes]: https://wiki.nixos.org/wiki/Flakes
[semver]: https://semver.org

# Compatibility

Since [GitKraken][gitkraken] is a **proprietary** and **unfree** software (to some extent), various aspects of this module's development rely on interacting with minified JavaScript code, and internal application behaviors, that may change between releases.

As a result, **compatibility cannot be guaranteed**, and the module is likely to break with each new GitKraken update.

When the module is confirmed to work with a new GitKraken version, a tagged release will be created, following [semantic versioning][semver], and the compatibility matrix below will be updated. Same goes for newly added module options.

| GitKraken |  NixKraken  |
| :-------: | :---------: |
|  11.1.0   |     1.x     |
|  11.1.1   |     1.x     |
|  11.2.0   |     1.x     |
|  11.2.1   |     1.x     |
|  11.3.0   |     1.x     |
|  11.4.0   |     1.x     |
|  11.5.0   |     1.x     |
|  11.5.1   | Coming soon |

::: details About support ranges

We use [SemVer][semver] ranges notation to denote compatibility between NixKraken and GitKraken:

| Range    | Interval           | Human                                               |
| -------- | ------------------ | --------------------------------------------------- |
| `1.x`    | 1.0.0 <= x < 2.0.0 | All minor and patches of major version 1            |
| `1.2.x`  | 1.2.0 <= x < 1.3.0 | All patches of minor version 1.2                    |
| `^1.2.3` | 1.2.3 <= x < 2.0.0 | All further minors and patches of minor version 1.2 |
| `~1.2.3` | 1.2.3 <= x < 1.3.0 | All further patches of patch version 1.2.3          |

:::

Additionally, users should be aware that **NixKraken will only actively support GitKraken versions present in current stable and unstable branches of nixpkgs**.

For example, at the time of writing (Oct. 2025), [nixpkgs 25.05 has GitKraken 11.1.0][gh-nixpkgs-gitkraken], meaning that earlier versions will not be supported.

::: info

This does not mean earlier versions of GitKraken would not work with current NixKraken releases, but no support will be provided in such case.

:::

## Stability

Development occurs on the `main` branch, which should be **considered unstable** and incompatible with any version of GitKraken.

**Users seeking stability should use release tags** rather than the `main` branch.

To use a specific release, modify `flake.nix`'s inputs like this:

```nix
# Use a specific version
{
  inputs.nixkraken.url = "github:nicolas-goudry/nixkraken/@CURRENT_VERSION@";
}
```

::: tip

The examples above use [Nix Flakes][nixos-wiki-flakes], please refer to the [non-Flake installation guide][doc-install-nonflake] to learn how to use a specific version of NixKraken.

:::

**Breakages may occur** from time to time, potentially resulting in **missing features**, **incomplete configuration**, or **general incompatibility** between the module and the installed version of GitKraken.

## Velocity

Although we strive to test NixKraken with new GitKraken versions and address issues as quickly as possible, updates are provided on a best-effort basis and there is no strict update schedule. Users should be prepared for occasional delays in compatibility following new GitKraken releases.

Users are also encouraged to **[report any issues][gh-issues]** encountered or to **contribute fixes**!

[Pull requests][gh-prs] are always welcome 🙂

::: info

Users willing to contribute should refer to the [contributors documentation][doc-contrib].

:::
