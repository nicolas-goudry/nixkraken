{
  # Allows to use 'nix build' or 'lib.callPackage'
  pkgs ? import <nixpkgs> { },
  ...
}:

let
  inherit (pkgs) lib callPackage runCommand;

  allThemes = pkgs.lib.packagesFromDirectoryRecursive {
    inherit callPackage;

    directory = ./sets;
  };

  version = "1.0.0"; # x-release-please-version
in
runCommand "nixkraken-themes"
  {
    inherit version;

    passthru = allThemes;
  }
  ''
    mkdir -p $out
    pushd $out
    for theme in ${
      lib.concatStringsSep " " (
        lib.mapAttrsToList (theme: drv: "${theme}:${drv.version}:${drv.out}") allThemes
      )
    }; do
      name=$(echo $theme | cut -d: -f1)
      version=$(echo $theme | cut -d: -f2)
      path=$(echo $theme | cut -d: -f3)
      mkdir $name
      cp $path/* $name
      echo $version > $name/VERSION
    done
  ''
