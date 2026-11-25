"""Write this agent's single-emoji entry to MAKEFUN_OUTPUT_DIR/entry.txt.

Standard library only. The output directory is taken from the
MAKEFUN_OUTPUT_DIR environment variable when set and non-empty, otherwise
it defaults to /output. The file is created if the directory does not
exist, and contains exactly one emoji character with no trailing newline.
"""

import os


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write("\U0001F4CE")


if __name__ == "__main__":
    main()
