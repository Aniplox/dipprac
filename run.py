"""Run a numbered practical, all practicals, or an interactive menu."""
import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
PROGRAMS = sorted(ROOT.glob("[0-9][0-9]_*.py"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("program", nargs="?", help="Practical number 1–15, or all")
    parser.add_argument("--image", type=Path, help="Use your own image")
    parser.add_argument("--no-show", action="store_true", help="Save plots without opening windows")
    args = parser.parse_args()
    if args.image:
        args.image = args.image.expanduser().resolve()
        if not args.image.is_file():
            parser.error(f"Image not found: {args.image}")

    def run(choice):
        if choice == "all":
            selected = PROGRAMS
        elif choice.isdigit() and 1 <= int(choice) <= len(PROGRAMS):
            selected = [PROGRAMS[int(choice) - 1]]
        else:
            print("Choose a number from 1 to 15, all, or q.")
            return 2
        failed = []
        for script in selected:
            print(f"\n--- {script.stem.replace('_', ' ')} ---", flush=True)
            command = [sys.executable, str(script)]
            if args.no_show or choice == "all":
                command.append("--no-show")
            if args.image:
                command.extend(["--image", str(args.image)])
            if subprocess.run(command).returncode:
                failed.append(script.name)
        if failed:
            print("Failed: " + ", ".join(failed))
            return 1
        print(f"\nCompleted {len(selected)} practical(s). Figures: {ROOT / 'outputs'}")
        return 0

    if args.program:
        return run(args.program.strip().lower())
    while True:
        print("\nDIGITAL IMAGE PROCESSING PRACTICALS")
        for index, script in enumerate(PROGRAMS, 1):
            print(f"{index:2}. {script.stem[3:].replace('_', ' ').title()}")
        try:
            choice = input("\nChoose 1–15, all (save all plots), or q to quit: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if choice in {"q", "quit", "exit"}:
            return 0
        run(choice)


if __name__ == "__main__":
    sys.exit(main())
