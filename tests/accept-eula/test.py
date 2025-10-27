# pyright: reportUndefinedVariable=false
import json

machine1.wait_for_x()

# GitKraken won't launch unless '--no-sandbox' is set when running as root
# Disable splashscreen with '--show-splashscreen' ('-s') set to false
machine1.succeed("gitkraken --no-sandbox -s false >&2 &")

# Wait for GitKraken to fully start
# This is required to avoid having X11 window tree mutate mid-query with 'wait_for_window'
machine1.sleep(30)

# Ensure GitKraken window exists
machine1.wait_for_window("GitKraken Desktop")

# Get screen text content
ocr = machine1.get_screen_text()

with subtest("EULA popup is not displayed"):
    # Check EULA popup is not displayed on screen
    t.assertNotRegex(ocr, "agree to our EULA")

with subtest("Tutorial is skipped"):
    # Check new tab is opened
    ocr = machine1.get_screen_text()
    t.assertRegex(ocr, "New Tab")
    t.assertRegex(ocr, "Release Notes")

with subtest("Configuration is reporting accepted EULA"):
    # Parse config as JSON
    config = machine1.succeed("cat ~/.gitkraken/config")
    data = json.loads(config)

    # Check EULA status is agreed and verified
    t.assertEqual(data["registration"]["EULA"]["status"], "agree_verified")

# Take a screenshot of GitKraken
machine1.screenshot("snapshot")

# Exit GitKraken
machine1.succeed("pkill -f gitkraken")
