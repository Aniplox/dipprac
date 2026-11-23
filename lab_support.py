"""Command-line image selection and portable plot output for the DIP practicals."""
import argparse
import os
from pathlib import Path
import subprocess
import sys


def configure(script):
    root = Path(script).resolve().parent
    os.environ.setdefault("MPLCONFIGDIR", str(root / ".mplconfig"))
    os.environ.setdefault("XDG_CACHE_HOME", str(root / ".cache"))
    parser = argparse.ArgumentParser(description=Path(script).stem.replace("_", " "))
    parser.add_argument("--image", type=Path, help="Optional input image; uses the built-in astronaut otherwise")
    parser.add_argument("--no-show", action="store_true", help="Save the figure without opening a window")
    args = parser.parse_args()
    if args.image is not None:
        args.image = args.image.expanduser().resolve()
        if not args.image.is_file():
            parser.error(f"Image not found: {args.image}")
    # Save with Agg on macOS, then open the PNG in Preview. This also works
    # with Python builds whose native Matplotlib GUI backend cannot start.
    if args.no_show or sys.platform == "darwin":
        import matplotlib
        matplotlib.use("Agg")
    output = root / "outputs" / (Path(script).stem + ".png")
    output.parent.mkdir(exist_ok=True)
    return args.image, output, args.no_show


def finish_plot(plt, output, no_show):
    plt.savefig(output, dpi=150)
    print(f"Plot saved: {output}")
    if not no_show:
        if sys.platform == "darwin":
            result = subprocess.run(["open", str(output)], capture_output=True, text=True)
            if result.returncode:
                print("Could not open the viewer automatically; open the saved PNG from outputs/.")
        else:
            plt.show()
    plt.close("all")
