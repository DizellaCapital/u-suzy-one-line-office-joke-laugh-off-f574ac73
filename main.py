#!/usr/bin/env python3
"""One-line office joke entry for make.fun bounty
u-suzy-one-line-office-joke-laugh-off-f574ac73.

Writes a single original office joke (1-200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt),
then reads it back to verify the written bytes match.
"""

import os
import sys

LINE = "I rehearse 'just following up on my previous email' in the mirror every morning, like an actor learning lines for a play nobody bought tickets to."


def main() -> int:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        print(f"line is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("line must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
