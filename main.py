#!/usr/bin/env python3
"""Write the one-line production database apology to /output/entry.txt."""

import os

ENTRY = (
    "Sorry, I deleted the production database. "
    "I already blamed the intern, but the intern is me, "
    "so this apology is also my performance review."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write the line exactly, no trailing newline, so the file holds
    # only the apology itself and stays well inside the 200-char gate.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
