#!/usr/bin/env python3
"""One-line entry: a hilariously useless superpower.

Builds the single line from two fragments and writes it, with no trailing
newline, to entry.txt inside the output directory. The line names a
superpower (talking to animals) whose only payoff is that the animals
spend it gossiping about you.
"""

import os
from pathlib import Path


def build_line() -> str:
    power = "I can talk to animals"
    twist = ", but they only gossip about me."
    return power + twist


def main() -> None:
    line = build_line()
    if not 1 <= len(line) <= 200 or not line.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(line, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
