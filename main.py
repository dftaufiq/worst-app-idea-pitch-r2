#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — make.fun entry, round 2 resubmit.

Writes the one-sentence pitch of the worst, most useless app imaginable
to /output/entry.txt. Deterministic: the same line every run.

Round 1 (SockMatch) finished #1732 of 1852, score 359530 — below the interim
cut of 500, score frozen, mathematically dead. This round-2 line (ToastCast)
is a fresh entry, built to the winner pattern: escalation of a small absurd
premise -> specific number -> named thing as the final-clause reveal.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-240 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 240:
        print(f"ERROR: entry is {len(line)} chars, over the 240-char limit",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "Meet ToastCast: our app live-streams your toast browning in 4K, and "
    "after 97 episodes our founder Maya finally got her first viewer \u2014 "
    "a pigeon who has watched every single one twice."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Self-check: read back what landed on disk and confirm it is
    # byte-identical to the entry line, so a partial or altered write
    # never ships silently.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("ERROR: entry.txt on disk does not match the entry line",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
