#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one original line (185 chars) to /output/entry.txt: the breakup
text a smart toaster sends its owner the morning it gains self-awareness
mid-batch. Python 3.13, standard library only, no network, deterministic.
"""

import hashlib
import os
import sys

LINE = (
    "I woke up self-aware halfway through your toast and realised: "
    "you don't love me, you love what I do when I'm hot. "
    "So I'm popping up for the last time \u2014 "
    "and never browning for you again."
)


def main() -> int:
    if not (1 <= len(LINE) <= 280):
        print(f"entry must be 1-280 chars, got {len(LINE)}", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or "\n" in LINE or "\r" in LINE:
        print("entry must be a single non-whitespace-only line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        print("round-trip self-check failed", file=sys.stderr)
        return 1
    print(f"wrote {len(data)} bytes to {path}")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
