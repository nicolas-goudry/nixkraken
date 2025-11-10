{
  description = "GitKraken configuration and profiles, the Nix way";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-25.05";

    treefmt-nix = {
      url = "github:numtide/treefmt-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    {
      self,
      nixpkgs,
      treefmt-nix,
      ...
    }:
    let
      systems = [
        "x86_64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];
      eachSystem = f: nixpkgs.lib.genAttrs systems (system: f nixpkgs.legacyPackages.${system});
      treefmtEval = eachSystem (pkgs: treefmt-nix.lib.evalModule pkgs ./treefmt.nix);
    in
    {
      homeManagerModules.nixkraken = ./module.nix;

      # nix flake check
      checks = eachSystem (
        pkgs:
        let
          checks = {
            formatting = treefmtEval.${pkgs.stdenv.hostPlatform.system}.config.build.check self;
          };
        in
        checks
        // {
          all = pkgs.runCommand "all-checks" { buildInputs = builtins.attrValues checks; } "touch $out";
        }
      );

      # nix fmt
      formatter = eachSystem (pkgs: treefmtEval.${pkgs.stdenv.hostPlatform.system}.config.build.wrapper);

      # Packages
      packages = eachSystem (
        pkgs:
        let
          gitkraken = pkgs.callPackage ./gitkraken { };
        in
        {
          inherit gitkraken;

          docs = pkgs.callPackage ./docs { };
          gitkraken-themes = pkgs.callPackage ./themes { };
        }
        # This is used to cache GitKraken
        // gitkraken.passthru
        // (import ./pkgs pkgs)
      );

      # Development environment with packages used by the module available in PATH
      devShells = eachSystem (pkgs: {
        default = pkgs.callPackage ./shell.nix { };
      });

      legacyPackages = eachSystem (pkgs: {
        # Output tests as legacyPackages so that:
        # - they are runnable/buildable with 'nix run/build'
        # - they are not checked by 'nix flake check'
        # - they are not built by Garnix
        tests = import ./tests pkgs;
        # Output treefmt wrapped with config file
        treefmt = treefmt-nix.lib.mkWrapper pkgs ./treefmt.nix;
      });
    };
}
