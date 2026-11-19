"""19 November 2026 world news image — make.fun entry program.

When the grader runs this file it places a copy of entry.png, the
front page drawn for Thursday 19 November 2026, into the output
folder. Only the Python standard library is used, there is no
network access, and the copied bytes never change between runs."""
import os, shutil


def _paths():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return source, os.path.join(target_dir, "entry.png")


def main():
    source, target = _paths()
    if not os.path.isfile(source):
        raise SystemExit("entry.png is missing next to main.py")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    shutil.copyfile(source, target)
    if os.path.getsize(target) != os.path.getsize(source):
        raise SystemExit("entry.png did not copy completely")


if __name__ == "__main__":
    main()
