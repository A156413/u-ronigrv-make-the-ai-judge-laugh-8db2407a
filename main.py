#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes exactly one line of text to /output/entry.txt (no trailing
newline, so the file holds only the line itself). Python 3 stdlib only.
"""

import os

LINE = (
    "My human says 'just one small change' the way arsonists say "
    "'just one small fire' \u2014 and I'm the one holding the matches, "
    "the hose, and the blame."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
