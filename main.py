#!/usr/bin/env python3
"""Write the single-emoji entry to MAKEFUN_OUTPUT_DIR (default /output/entry.txt)."""

import os

ENTRY_TEXT = "\U0001F4CE"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        raise SystemExit(f"cannot create output directory {out_dir!r}: {exc}")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
