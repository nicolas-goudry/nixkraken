# pyright: reportUndefinedVariable=false
import re

machine1.wait_for_x()

with subtest("GitKraken profile name is customized"):
    # GitKraken won't launch unless '--no-sandbox' is set when running as root
    # Disable splashscreen with '--show-splashscreen' ('-s') set to false
    machine1.succeed("gitkraken --no-sandbox -s false >&2 &")

    # Wait for GitKraken to fully start
    # This is required to avoid having X11 window tree mutate mid-query with 'wait_for_window'
    machine1.sleep(30)

    # Ensure GitKraken window exists
    machine1.wait_for_window("GitKraken Desktop")

    # Check if profile name is customized
    # NOTE: we have to loosely test this since OCR is not very precise with case detection
    ocr = machine1.get_screen_text()
    t.assertRegex(ocr, re.compile(r"NixKraken rocks", re.I))

    # Take a screenshot of GitKraken
    machine1.screenshot("snapshot")

# Exit GitKraken
machine1.succeed("pkill -f gitkraken")
