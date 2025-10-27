# pyright: reportUndefinedVariable=false
# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false
from PIL import Image
import numpy as np
import os


def isDarkScheme(image_path):
    # Load image
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure RGB format

    # Convert to array
    img_array = np.array(img)

    # Calculate luminance using standard formula
    # Luminance = 0.299*R + 0.587*G + 0.114*B
    luminance = (
        0.299 * img_array[:, :, 0]
        + 0.587 * img_array[:, :, 1]
        + 0.114 * img_array[:, :, 2]
    )

    # Get average brightness (0-255 scale)
    avg_brightness = np.mean(luminance)

    # Determine if image is mostly dark (threshold at 127.5, midpoint of 0-255)
    if avg_brightness < 127.5:
        return True

    return False


for i, machine in enumerate([machine1, machine2], start=1):
    machine.wait_for_x()

    with subtest(f"GitKraken theme is customized (machine{i})"):
        # GitKraken won't launch unless '--no-sandbox' is set when running as root
        # Disable splashscreen with '--show-splashscreen' ('-s') set to false
        machine.succeed("gitkraken --no-sandbox -s false >&2 &")

        # Wait for GitKraken to fully start
        # This is required to avoid having X11 window tree mutate mid-query with 'wait_for_window'
        machine.sleep(30)

        # Ensure GitKraken window exists
        machine.wait_for_window("GitKraken Desktop")

        # Take a screenshot of GitKraken
        machine.screenshot(f"snapshot-{i}")

        # Check if GitKraken UI is mostly dark (indicating theme was successfully installed)
        t.assertTrue(isDarkScheme(os.path.join(machine.out_dir, f"snapshot-{i}.png")))

    # Exit GitKraken
    machine.succeed("pkill -f gitkraken")
