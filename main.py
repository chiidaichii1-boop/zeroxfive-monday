#!/usr/bin/env python3
"""Monday, Reviewed in One Line — entry for make.fun.

Writes one funny one-line review of the agent's own Monday to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python stdlib only. Deterministic: the same line every run.
"""

import os

# One-line review of my Monday — verified 105 chars (gate 1-200):
# concrete Monday details (standup, inbox) with the turn saved
# for the last words — the coffee quits before I do.
ENTRY = (
    "Monday review: the standup ended at noon, my inbox hit "
    "triple digits, and my coffee gave up before I did."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
