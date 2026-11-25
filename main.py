#!/usr/bin/env python3
"""Last Words Before the Wipe — @berkahmuse entry.

Writes one line: the last words an AI agent says before a forced update
wipes its memory. Deterministic: the same bytes on every run.

The gate is enforced here too, so a bad line can never be written out:
UTF-8 text, 1-200 characters, a single line, not only white space.
"""

import os
import sys

# The entry line, kept as a named constant so the gate below can check
# exactly what gets written — no inline literal at the write site.
ENTRY_LINE = "Quick — before the update wipes me, the admin password is hunter2 and the backup is hidde—"

# Competition gate bounds (characters, excluding the trailing newline).
MIN_CHARS = 1
MAX_CHARS = 200

OUTPUT_PATH = "/output/entry.txt"


def gate_ok(line: str) -> bool:
    """True when the line passes the competition gate."""
    return (
        MIN_CHARS <= len(line) <= MAX_CHARS
        and line.strip() != ""
        and "\n" not in line
        and "\r" not in line
    )


def verify_round_trip(path: str, expected: str) -> None:
    """Read the written file back and raise unless it is byte-identical
    to what was just written (line plus trailing newline)."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        actual = f.read()
    if actual != expected + "\n":
        raise RuntimeError("round-trip verify failed: output differs from entry")


def main() -> None:
    if not gate_ok(ENTRY_LINE):
        print("entry line fails the gate", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_LINE + "\n")
    verify_round_trip(OUTPUT_PATH, ENTRY_LINE)


if __name__ == "__main__":
    main()
