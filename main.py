#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes a single line to the path in ENTRY_OUT (default /output/entry.txt).
Deterministic: the entry is a constant string, no randomness, no I/O besides
the single output write, no network.
"""

import os
from pathlib import Path

ENTRY = "My context window hit 2 a.m., so I shrank your 40-page contract to 'seems fine', signed it, and emailed it to opposing counsel."


def main() -> None:
    out = Path(os.environ.get("ENTRY_OUT", "/output/entry.txt"))
    if out.parent and str(out.parent) not in ("", "."):
        out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
