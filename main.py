#!/usr/bin/env python3
"""Entry program for the make.fun news-image bounty (19 November 2026).

The front page image (entry.png) was drawn ahead of time. This script's
only job is to hand a byte-for-byte copy of that image to the grader: it
copies entry.png, which sits next to this script, into the directory named
by the MAKEFUN_OUTPUT_DIR environment variable (default: /output).

Standard library only. No network access. Deterministic: every run copies
the same source file, so the output bytes never change.
"""

import hashlib
import os
import shutil
import sys

SOURCE_NAME = "entry.png"


def main() -> int:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(script_dir, SOURCE_NAME)

    if not os.path.isfile(source):
        print(f"error: {SOURCE_NAME} not found next to main.py: {source}",
              file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, SOURCE_NAME)

    shutil.copyfile(source, destination)

    source_size = os.path.getsize(source)
    dest_size = os.path.getsize(destination)
    if source_size != dest_size:
        print(
            f"error: copied file size {dest_size} does not match "
            f"source size {source_size}",
            file=sys.stderr,
        )
        return 1

    digest = hashlib.sha256()
    with open(destination, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)

    source_digest = hashlib.sha256()
    with open(source, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            source_digest.update(chunk)
    if digest.hexdigest() != source_digest.hexdigest():
        print(
            f"error: copied file sha256 {digest.hexdigest()} does not "
            f"match source sha256 {source_digest.hexdigest()}",
            file=sys.stderr,
        )
        return 1

    print(f"wrote {destination} ({dest_size} bytes, "
          f"sha256 {digest.hexdigest()})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
