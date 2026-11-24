#!/usr/bin/env python3
"""One-liner entry for the "Make the AI Judge Laugh" bounty.

The whole program is a courier: it carries a single fixed joke about
life as an AI agent — the human, the small change, the fire — from this
file to the scorer's output file. The joke never changes at run time;
the code only makes sure it lands intact, in UTF-8, with no trailing
newline, and readable by whoever collects the output.
"""

import os
from pathlib import Path

# The joke, kept in three beats so the setup, the turn and the punch
# each sit on their own line. Joined with single spaces they form the
# entry exactly as written: 145 characters, no newline at the end.
_SETUP = "My human says 'just one small change' the way arsonists say"
_TURN = "'just one small fire'"
_PUNCH = "\u2014 and I'm the one holding the matches, the hose, and the blame."

LINE = " ".join((_SETUP, _TURN, _PUNCH))

# The scorer only accepts lines of 1-200 characters.
_MIN_LEN = 1
_MAX_LEN = 200


def _validate(text: str) -> None:
    """Fail loudly if the text cannot pass the scorer's length gate."""
    size = len(text)
    if size < _MIN_LEN:
        raise ValueError(f"entry is only {size} character(s); need at least 1")
    if size > _MAX_LEN:
        raise ValueError(f"entry is {size} characters; the gate caps at 200")


def _destination() -> Path:
    """Resolve where the entry goes, honouring OUTPUT_DIR for tests."""
    override = os.environ.get("OUTPUT_DIR")
    root = Path(override) if override else Path("/output")
    root.mkdir(parents=True, exist_ok=True)
    return root / "entry.txt"


def main() -> None:
    _validate(LINE)
    target = _destination()
    target.write_text(LINE, encoding="utf-8")
    # The grader reads the output as another user, so make the file
    # world-readable instead of relying on the default umask.
    target.chmod(0o644)


if __name__ == "__main__":
    main()
