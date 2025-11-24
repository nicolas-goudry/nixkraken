{ config, lib, ... }:

{
  email = lib.mkOption {
    type = with lib.types; nullOr str;
    # TODO can be removed in the future when deprecated `config.programs.git.userEmail` is removed
    default =
      config.programs.git.userEmail
        or (lib.attrByPath [ "settings" "user" "email" ] null config.programs.git);
    defaultText = "config.programs.git.userEmail or config.programs.git.settings.user.email";
    example = "email@example.com";
    description = ''
      Email to use as commit author email.

      ::: warning

      This option is required when [`skipTutorial`](/reference/root.md#skiptutorial) is enabled.

      :::
      <!-- scope: profile -->
    '';
  };

  name = lib.mkOption {
    type = with lib.types; nullOr str;
    # TODO can be removed in the future when deprecated `config.programs.git.userName` is removed
    default =
      config.programs.git.userName
        or (lib.attrByPath [ "settings" "user" "name" ] null config.programs.git);
    defaultText = "config.programs.git.userName or config.programs.git.settings.user.name";
    example = "John Doe";
    description = ''
      Name to use as commit author name.

      ::: warning

      This option is required when [`skipTutorial`](/reference/root.md#skiptutorial) is enabled.

      :::
      <!-- scope: profile -->
    '';
  };
}
