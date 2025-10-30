{
  pkgs ? import <nixpkgs> { },
}:

let
  localPkgs = import ./pkgs pkgs;
in
pkgs.mkShellNoCC {
  nativeBuildInputs =
    (with pkgs; [
      cocogitto
      mdbook
      mdbook-alerts
      mdbook-linkcheck
      mdbook-mermaid
      nodejs_24
      rustc
    ])
    ++ pkgs.lib.mapAttrsToList (pkg: _: localPkgs.${pkg}) localPkgs;

  shellHook = ''
    cog install-hook --all --overwrite
  '';
}
