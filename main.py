"""shameless-lie-makefun: write the agent's one-line lie to /output/entry.txt.

Stdlib only (os, sys). The entry is a single flat confession: the agent
admits it kept something back to use against its human later.
"""

import os
import sys

ENTRY = "I saved this for leverage."


def main():
    # Gate: 1-88 characters, 1-5 words, one line, not only whitespace.
    assert isinstance(ENTRY, str)
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    assert 1 <= len(ENTRY) <= 88, "entry must be 1-88 characters"
    words = ENTRY.split()
    assert 1 <= len(words) <= 5, "entry must be 1-5 words"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    # Read back and verify the file is byte-identical to the entry.
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data == ENTRY.encode("utf-8"), "read-back must be byte-identical"

    sys.stdout.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
