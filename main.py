"""World News, 19 November 2026 — make.fun entry.

Copies the image beside this file to the output directory.
Standard library only, no network, deterministic: the same input
bytes always produce the same output bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
SRC = HERE / "entry.png"

if not SRC.is_file():
    raise SystemExit("entry.png not found beside main.py")

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, OUT_DIR / "entry.png")
