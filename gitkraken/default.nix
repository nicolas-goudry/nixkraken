{
  pkgs ? import <nixpkgs> { },
  version ? null,
  ...
}:

let
  inherit (pkgs) lib;

  versions = import ./versions.nix;

  fromNixpkgs =
    commit: hash:
    (import
      (fetchTarball {
        url = "https://github.com/nixos/nixpkgs/archive/${commit}.tar.gz";
        sha256 = hash;
      })
      {
        system = pkgs.stdenv.hostPlatform.system;

        config.allowUnfreePredicate =
          pkg:
          builtins.elem (lib.getName pkg) [
            "gitkraken"
          ];
      }
    ).gitkraken;
in

if version != null then
  if lib.hasAttr version versions then
    let
      inherit (versions.${version}) commit hash;
    in
    fromNixpkgs commit hash
  else
    throw "Invalid version provided: ${version}. Valid versions: ${lib.concatStringsSep ", " (lib.attrNames versions)}."
else
  let
    latest =
      lib.findSingle (version: version ? latest) (throw "No latest version defined")
        (throw "Multiple latest versions defined")
        (lib.attrValues versions);
  in
  (fromNixpkgs latest.commit latest.hash).overrideAttrs {
    passthru = lib.mapAttrs' (
      version:
      { commit, hash, ... }:
      let
        dashVersion = lib.replaceStrings [ "." ] [ "-" ] version;
      in
      lib.nameValuePair "gitkraken-v${dashVersion}" (fromNixpkgs commit hash)
    ) versions;
  }
