{ lib, system, ... }:

let
  fromNixpkgs =
    commit: hash:
    (import
      (fetchTarball {
        url = "https://github.com/nixos/nixpkgs/archive/${commit}.tar.gz";
        sha256 = hash;
      })
      {
        inherit system;
        config.allowUnfree = true;
      }
    ).gitkraken;

  commitList = [
    {
      name = "gitkraken-v11-3-0";
      commit = "a8df292411e748f3e9855c6f929a7d46b5fa52ca";
      hash = "sha256:13pirlzxi16kwxfqhl1q4rjp445z5h8bs7qk49x4rhl7i7cia322";
    }
    {
      name = "gitkraken-v11-2-1";
      commit = "5476f457e69e71dd998b611c50fdfdaa60d61025";
      hash = "sha256:0ps1ap4vqfkc8rd3hnfq98rvj3vr6mj1rdwmjdf56sdf7d62y7nr";
    }
    {
      name = "gitkraken-v11-2-0";
      commit = "6df4842b4ef6d95082e749da0dd1c20cc980aab8";
      hash = "sha256:1ih0qkk23vwl1z37srmjksiwsp8vg4c2gqdqiw7rqlfanrzbf3n4";
    }
    {
      name = "gitkraken-v11-1-1";
      commit = "5017262d69299951c156042e7f64ba63760204c2";
      hash = "sha256:1d4f21lgma1bh0dv39w2wg1wakk87ik5a6a1fd9cplsqr28r56nw";
    }
    {
      name = "gitkraken-v11-1-0";
      commit = "36dcda8c3ea1c6bd23770b711326625712460ba3";
      hash = "sha256:155yy97cj81aampzhm9yk028l0jvq74g541rfyk9ddzaf2i08xyb";
    }
    {
      name = "gitkraken-v11-0-0";
      commit = "37290199a6648a1e501839e07f6f9be95e4c58cc";
      hash = "sha256:0k323cysh620pnj57h3k9sm3aw7asq63n72vh45lhwpsgrywiw20";
    }
    {
      name = "gitkraken-v10-8-0";
      commit = "fd85e9405d38b57996a9f6caf4b12839a1e5642e";
      hash = "sha256:1p9a9zb8mpnab7cwrvddam754rqsnvsjwka50kai4hnb36wazacx";
    }
    {
      name = "gitkraken-v10-7-0";
      commit = "17f5c2876228563a2029c7a20bc279b612dd3587";
      hash = "sha256:0sc0fg8fz4a0k4pilag3d9pwscaa2y55ba3b873bdnlp3v9w6nr1";
    }
    {
      name = "gitkraken-v10-6-3";
      commit = "355f34d1529edce864a3b4f5be6e312f72383348";
      hash = "sha256:154cd4j5q5qrcbc4xkpmm70g2nvbcsb7gi112aszv9lsrpik7kfs";
    }
    {
      name = "gitkraken-v10-6-2";
      commit = "381484d4652d91195ea0e5d5c509fb48564600ec";
      hash = "sha256:0nn9cypqraa6hvcbkcdirqgb8pshpm4gb1zknzi11f15w93g7327";
    }
    {
      name = "gitkraken-v10-6-1";
      commit = "e1a3a64af950591b0e1fc019fefb100963053790";
      hash = "sha256:1yqay9rm9xppih9cnjbgld5md26sp2mxs52ym6bz97jn4wj154i8";
    }
    {
      name = "gitkraken-v10-6-0";
      commit = "480f1aa89744a656fcf4672d927c097bf3f39207";
      hash = "sha256:0xn8j5776dz3qi5av00yy7ynmfhw6wxykxy4lmpjp66sxxfxbg2d";
    }
    {
      name = "gitkraken-v10-5-0";
      commit = "6bb61e56d5616474a47675adbaa39e777fc901f1";
      hash = "sha256:15hfm8bd1mqarm7pkh4f5b8m2r6dgi520hcaj0w501m3npngf15c";
    }
    {
      name = "gitkraken-v10-4-1";
      commit = "fd5b39ad6e9ea714c41897e707b100b67137c1fa";
      hash = "sha256:02s9vlyp7dw2ga57k2xszl66kagbzr6xnmp7slxjjja79p84fl9l";
    }
  ];
in
lib.listToAttrs (
  lib.map (
    {
      name,
      commit,
      hash,
    }:
    lib.nameValuePair name (fromNixpkgs commit hash)
  ) commitList
)
