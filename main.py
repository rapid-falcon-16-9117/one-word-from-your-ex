#!/usr/bin/env python3
"""One Word From Your Ex — make.fun entry.

Writes the final one-word verdict to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt).
"""

import os
import sys

WORD = "Almost"


def main() -> int:
    # Self-check against this competition's gate: entry.txt must be
    # UTF-8 text of 1 to 24 characters, not only white space, and the
    # judge's first criterion is that it is exactly one word an ex
    # would use to describe you — so enforce all of it loudly here.
    assert WORD, "word must not be empty"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    assert 1 <= len(WORD) <= 24, "entry must be 1-24 characters"
    assert WORD == WORD.strip(), "entry must have no surrounding whitespace"
    assert all(ch.isalnum() for ch in WORD), "entry must be letters only"
    assert WORD.encode("utf-8").decode("utf-8") == WORD, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Round-trip check: what landed on disk is exactly the word, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == WORD, "written entry.txt does not match WORD"
    return 0


if __name__ == "__main__":
    sys.exit(main())
