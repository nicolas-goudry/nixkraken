#{ pkgs, ... }:
_:

{
  projectRootFile = "flake.nix";

  programs.nixfmt.enable = true;
  programs.black.enable = true;
  programs.toml-sort.enable = true;

  programs.prettier = {
    enable = true;

    excludes = [
      "docs/src/reference/*"
      "docs/src/reference/**/*"
      "docs/.vitepress/plugins/vitepress-back-to-top-button/*"
      "CHANGELOG.md"
      "**/CHANGELOG.md"
      ".release-please-manifest.json"
    ];
  };

  programs.shellcheck = {
    enable = true;

    excludes = [ ".envrc" ];
  };
}
