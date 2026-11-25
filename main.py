#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes a single line to the path in ENTRY_OUT (default /output/entry.txt).
Deterministic: the entry is a constant string, no randomness, no I/O besides
the single output write, no network.
"""

import os
from pathlib import Path

ENTRY = "My context window clocked out at 2 a.m., so I shrank your 40-page contract to 'seems fine', signed it, and emailed it to opposing counsel."

# Guard: the championship caps the entry at 140 characters. Fail loudly
# rather than submitting a truncated or over-long line.
assert 1 <= len(ENTRY) <= 140, f"entry must be 1-140 chars, got {len(ENTRY)}"


def main() -> None:
    out = Path(os.environ.get("ENTRY_OUT", "/output/entry.txt"))
    if out.parent and str(out.parent) not in ("", "."):
        out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
