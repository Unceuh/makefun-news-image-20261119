#!/usr/bin/env python3
"""Entry program for the make.fun news-image bounty (19 November 2026).

The front page (entry.png) was composed ahead of time by the agent that
built this entry. This program only delivers that finished image to the
grader: it copies entry.png, stored beside this script, into the output
directory named by MAKEFUN_OUTPUT_DIR (default /output).

Standard library only, no network, no randomness. Running it twice writes
the same bytes both times.
"""

import hashlib
import os
import sys
from pathlib import Path

IMAGE = "entry.png"
CHUNK = 65536


def _sha256(path):
    """Hex SHA-256 digest of a file, read in blocks."""
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        while True:
            block = fh.read(CHUNK)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def main():
    here = Path(__file__).resolve().parent
    src = here / IMAGE
    if not src.is_file():
        print("error: %s missing next to %s" % (IMAGE, __file__), file=sys.stderr)
        return 1
    outdir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    outdir.mkdir(parents=True, exist_ok=True)
    dst = outdir / IMAGE
    data = src.read_bytes()
    dst.write_bytes(data)
    if _sha256(dst) != _sha256(src):
        print("error: copied file failed its checksum", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)" % (dst, len(data), _sha256(dst)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
