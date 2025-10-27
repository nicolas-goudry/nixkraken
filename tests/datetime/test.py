# pyright: reportUndefinedVariable=false
machine1.wait_for_x()

# Initialize test repository
machine1.succeed("mkdir -p ~/test-repo")
machine1.succeed("touch ~/test-repo/test")
machine1.succeed("git -C ~/test-repo init")
machine1.succeed("git -C ~/test-repo add test")
machine1.succeed("git -C ~/test-repo commit -m 'test commit'")

# Update configuration to open test repository
machine1.succeed(
    "jq --slurpfile merge ~/repoTab.json '. * $merge[0]' ~/.gitkraken/profiles/d6e5a8ca26e14325a4275fc33b17e16f/profile > ~/profile.tmp"
)
machine1.succeed(
    "mv ~/profile.tmp ~/.gitkraken/profiles/d6e5a8ca26e14325a4275fc33b17e16f/profile"
)

with subtest("Custom time is displayed"):
    # GitKraken won't launch unless '--no-sandbox' is set when running as root
    # Disable splashscreen with '--show-splashscreen' ('-s') set to false
    machine1.succeed("gitkraken --no-sandbox -s false >&2 &")

    # Wait for GitKraken to fully start
    # This is required to avoid having X11 window tree mutate mid-query with 'wait_for_window'
    machine1.sleep(30)

    # Ensure GitKraken window exists
    machine1.wait_for_window("GitKraken Desktop")

    # Hide commit details panel (wait for UI to be updated before doing OCR)
    machine1.send_key("ctrl-k")
    machine1.sleep(5)

    # Check that:
    # - test repository is opened
    # - custom time is displayed
    # - commit message is not displayed
    ocr = machine1.get_screen_text()
    t.assertRegex(ocr, "test-repo")
    t.assertRegex(ocr, "custom time")
    t.assertNotRegex(ocr, "test commit")

    # Take a screenshot of GitKraken
    machine1.screenshot("snapshot")

# Exit GitKraken
machine1.succeed("pkill -f gitkraken")
