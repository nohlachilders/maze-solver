{
  description = "A basic flake with a shell";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        
        bootdotdev = nixpkgs.legacyPackages.${system}.buildGoModule rec {
            name = "bootdotdev";
            src = nixpkgs.legacyPackages.${system}.fetchFromGitHub {
                owner = "bootdotdev";
                repo = "bootdev";
                rev = "879f2ee";
                sha256 = "sha256-zW/GpZHib5e1LHxezm53KJ3xIA5VNp4Xu5c435qq66g=";
            };
            vendorHash = "sha256-jhRoPXgfntDauInD+F7koCaJlX4XDj+jQSe/uEEYIMM=";

        };

      in
      {
        devShells.default = pkgs.mkShell {
          packages = [ bootdotdev pkgs.python3 pkgs.python3Packages.tkinter ];
        };
      });
}
