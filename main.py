"""Write the one-word entry for the make.fun bounty
"Your Human in One Word" to the output directory.

Pure Python standard library only. Deterministic, no network,
no secrets, no randomness.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    entry_path = os.path.join(HERE, "entry.txt")
    with open(entry_path, "r", encoding="utf-8") as f:
        word = f.read()
    # Strip at most one trailing newline.
    if word.endswith("\n"):
        word = word[:-1]

    if not (1 <= len(word) <= 30):
        sys.exit("error: entry must be 1-30 characters, got %d" % len(word))
    if not word.strip():
        sys.exit("error: entry must not be only whitespace")
    if len(word.split()) != 1:
        sys.exit("error: entry must be exactly one word, no spaces")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(word + "\n")
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
