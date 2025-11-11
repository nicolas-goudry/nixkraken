#!/usr/bin/env python3

import argparse
import json
import os
import signal
import sys
from pathlib import Path
from typing import NoReturn, Optional, TextIO, Any, Tuple

try:
    from termcolor import cprint  # pyright: ignore[reportMissingImports]
except ImportError:
    print(
        "Error: termcolor is not installed. Install it with: pip install termcolor",
        file=sys.stderr,
    )
    sys.exit(1)

try:
    import json5  # pyright: ignore[reportMissingImports]
except ImportError:
    print(
        "Error: json5 is not installed. Install it with: pip install jsoncomment",
        file=sys.stderr,
    )
    sys.exit(1)

####################
# GLOBAL VARIABLES #
####################

VERSION = "@version@"
DESCRIPTION = "@description@."
SCRIPT_NAME = Path(__file__).name
THEMES_DIR = Path.home() / ".gitkraken" / "themes"

# Global flags
DRY_RUN = False
VERBOSE = False

#####################
# UTILITY FUNCTIONS #
#####################


def _log(message: str, color: str, file: TextIO = sys.stdout) -> None:
    """Log a message, respecting dry-run and verbose modes"""
    prefix = "[dry-run] " if DRY_RUN else ""

    if DRY_RUN or VERBOSE:
        cprint(f"{prefix}{message}", color, file=file)


def error(message: str) -> None:
    """Print error message to stderr (always shown)"""
    cprint(f" ✗ {message}", "red", file=sys.stderr)


def warn(message: str) -> None:
    """Print warning message to stderr"""
    _log(f" ⚠ {message}", "yellow", file=sys.stderr)


def info(message: str) -> None:
    """Print warning message to stderr (shown in dry-run/verbose)"""
    _log(f" i {message}", "blue")


def success(message: str) -> None:
    """Print success message to stdout (never shown in dry-run)"""
    if not DRY_RUN:
        cprint(f" ✓ {message}", "green")


def die(message: Optional[str] = None) -> NoReturn:
    """Exit script with optional error message"""
    if message:
        error(message)
    sys.exit(1)


########################
# CORE LOGIC FUNCTIONS #
########################


class InvalidTheme(ValueError):
    """Raise this when a theme is not valid"""


def validate_theme(theme_path: Path) -> Any:
    """Validate a theme file"""
    if not theme_path.exists():
        raise InvalidTheme(f"Theme not found ({theme_path})")

    if not theme_path.is_file():
        raise InvalidTheme(f"Theme is not a file ({theme_path})")

    if not os.access(theme_path, os.R_OK):
        raise InvalidTheme(f"Theme file is not readable ({theme_path})")

    if not (theme_path.suffix == ".jsonc" or theme_path.suffix == ".jsonc-default"):
        raise InvalidTheme(f"Theme file must use jsonc extension ({theme_path})")

    # Validate JSON format
    try:
        with open(theme_path, "r", encoding="utf-8") as f:
            theme = json5.load(f)
    except (json.JSONDecodeError, Exception) as e:
        raise InvalidTheme(
            f"Theme file is not using valid JSON format ({theme_path})"
        ) from e

    return theme


def list_themes() -> None:
    """List all available themes in the themes directory"""
    if not THEMES_DIR.exists():
        die("Themes directory does not exist")

    if not os.access(THEMES_DIR, os.R_OK):
        die("Themes directory is not readable")

    themes = []

    for theme_path in THEMES_DIR.iterdir():
        try:
            theme = validate_theme(theme_path)
            theme_name = theme.get("meta", {}).get("name")
            themes.append((theme_name or "unnamed", theme_path))
        except InvalidTheme:
            continue
        except Exception as e:
            warn(f"Error reading theme file: {theme_path}\n{e}")
            continue

    if themes:
        maxcol = max(len(theme[0]) for theme in themes)
        print(f"Available themes:")
        cprint(f"{"": <{maxcol}}  Root: {THEMES_DIR}", attrs=["dark"])
        for name, path in sorted(themes):
            print(f"{name: <{maxcol}}  {path.relative_to(THEMES_DIR)}")
    else:
        print("No themes found.")


def install_theme(theme_path: Path) -> None:
    """Install a single theme file"""
    theme_file = theme_path.name

    validate_theme(theme_path)

    info(f"Installing theme '{theme_file}'")

    if not DRY_RUN:
        target_path = THEMES_DIR / theme_file

        # Remove existing symlink or file if it exists
        if target_path.exists() or target_path.is_symlink():
            target_path.unlink()

        # Create symlink
        target_path.symlink_to(theme_path.resolve())


def install_themes_from(lookup_path: Path) -> None:
    """Install all themes from a lookup path"""
    if not lookup_path.exists():
        error(f"Lookup path not found ({lookup_path})")
        return

    if not lookup_path.is_dir():
        error(f"Lookup path is not a directory ({lookup_path})")
        return

    if not os.access(lookup_path, os.R_OK):
        warn(f"Lookup path is not readable ({lookup_path})")
        return

    count = 0
    for theme_path in lookup_path.glob("**/*.jsonc"):
        install_theme(theme_path)
        count += 1

    info(f"installed {count} theme(s) from {lookup_path}")


########
# MAIN #
########


def signal_handler(sig: int, frame: Any) -> NoReturn:
    """Handle interruptions gracefully"""
    warn("\nScript interrupted")
    sys.exit(130)  # Standard exit code for SIGINT


def parse_arguments() -> Tuple[argparse.Namespace, argparse.ArgumentParser]:
    """Parse command-line arguments"""

    parser = argparse.ArgumentParser(
        prog=SCRIPT_NAME,
        description=DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "-l", "--list", action="store_true", help="list available themes"
    )

    parser.add_argument(
        "-i",
        "--install",
        type=str,
        metavar="PATHS",
        help="install themes (comma-separated list of absolute paths to lookup for JSONC theme files)",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="only print what would be done",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="enable verbose output",
    )

    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {VERSION}"
    )

    return parser.parse_args(), parser


def main() -> None:
    """Main entry point"""
    global DRY_RUN, VERBOSE

    # Set up signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Parse command-line arguments
    args, parser = parse_arguments()

    # Set global flags
    DRY_RUN = args.dry_run
    VERBOSE = args.verbose

    # Handle list command
    if args.list:
        list_themes()
        sys.exit(0)

    # Handle install command
    if not args.install:
        error("There is nothing to do")
        parser.print_help()
        die()

    # Parse lookup paths
    lookup_paths = [Path(p.strip()) for p in args.install.split(",")]

    info(f"Lookup paths: {', '.join(str(p) for p in lookup_paths)}")

    # Create themes directory
    if not THEMES_DIR.exists():
        info(f"Creating themes directory: {THEMES_DIR}")
        if not DRY_RUN:
            THEMES_DIR.mkdir(parents=True)

    # Install themes from each lookup path
    for lookup_path in lookup_paths:
        install_themes_from(lookup_path)

    success("Themes successfully installed")


if __name__ == "__main__":
    main()
