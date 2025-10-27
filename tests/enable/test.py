# pyright: reportUndefinedVariable=false
machine1.wait_for_x()

with subtest("GitKraken version matches"):
    # GitKraken won't launch unless '--no-sandbox' is set when running as root
    version = machine1.wait_until_succeeds(
        "gitkraken --no-sandbox --version | tr -d '\n'"
    )
    t.assertEqual(version, "@version@")

with subtest("GitKraken launches"):
    # GitKraken won't launch unless '--no-sandbox' is set when running as root
    # Disable splashscreen with '--show-splashscreen' ('-s') set to false
    machine1.succeed("gitkraken --no-sandbox -s false >&2 &")

    # Wait for GitKraken to fully start
    # This is required to avoid having X11 window tree mutate mid-query with 'wait_for_window'
    machine1.sleep(30)

    # Ensure GitKraken window exists
    machine1.wait_for_window("GitKraken Desktop")

    # Check if welcome screen is displayed
    ocr = machine1.get_screen_text()
    t.assertRegex(ocr, "GitKraken Desktop")

    # Take a screenshot of GitKraken
    machine1.screenshot("snapshot")

with subtest("Application config exists"):
    machine1.succeed("stat ~/.gitkraken/config")

with subtest("Default profile config exists"):
    machine1.succeed(
        "stat ~/.gitkraken/profiles/d6e5a8ca26e14325a4275fc33b17e16f/profile"
    )

# Exit GitKraken
machine1.succeed("pkill -f gitkraken")
