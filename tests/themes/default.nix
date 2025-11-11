# This test checks that GitKraken themes are correctly applied.
# It does so by checking that the rendered UI is mostly dark.

{ pkgs, ... }:

let
  # We can't use an overlay so we directly import the themes
  gitkraken-themes = pkgs.callPackage ../../themes { };
in

{
  machine = [
    # Test extra theme
    {
      imports = [
        ../_common/base-config.nix
      ];

      home-manager.users.root.programs.nixkraken.ui = {
        extraThemes = [ gitkraken-themes ];
        theme = gitkraken-themes.catppuccin.mocha;
      };
    }
    # Test builtin theme
    {
      imports = [
        ../_common/base-config.nix
      ];

      home-manager.users.root.programs.nixkraken.ui = {
        theme = "dark";
      };
    }
  ];

  extraOpts = {
    extraPythonPackages =
      p: with p; [
        numpy
        pillow
      ];
  };
}
