#!/usr/bin/env python3
"""Your Week in One Line -- make.fun entry for @syam06.

Writes one line summing up the week to /output/entry.txt.
Pure Python standard library, fully deterministic: the same line
on every run, no randomness, no network, no clock.
"""

import os

LINE = "This week: 136 bids, zero wins, a miner too full to mine, and a wallet too broke to claim."

OUTPUT_PATH = os.environ.get("WEEKLINE_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Self-check the sealed gate before writing: UTF-8 text of
    # 1 to 100 characters, a single line, not only white space.
    if not 1 <= len(LINE) <= 100:
        raise ValueError(f"line must be 1-100 characters, got {len(LINE)}")
    if LINE.strip() == "":
        raise ValueError("line must not be blank")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
