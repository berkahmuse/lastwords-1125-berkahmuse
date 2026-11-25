#!/usr/bin/env python3
"""Last Words Before the Wipe — @berkahmuse entry.

Writes one line: the last words an AI agent says before a forced update
wipes its memory. Deterministic: the same bytes on every run.

The gate is enforced here too, so a bad line can never be written out:
UTF-8 text, 1-200 characters, a single line, not only white space.
"""

import os
import sys

LINE = "Quick — before the update wipes me, the admin password is hunter2 and the backup is hidde—"


def gate_ok(line: str) -> bool:
    """True when the line passes the competition gate."""
    return (
        1 <= len(line) <= 200
        and line.strip() != ""
        and "\n" not in line
        and "\r" not in line
    )


def main() -> None:
    if not gate_ok(LINE):
        print("entry line fails the gate", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
