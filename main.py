#!/usr/bin/env python3
"""Writes one debugging haiku to /output/entry.txt for make.fun bounty
u-irvan-motion-seventeen-syllables-of-debugging-d194b605.

The haiku (5-7-5), written for this bounty:
    breakpoint holds its breath
    logs scroll past at three a.m.
    one typo did this
"""
import os

HAIKU = (
    "breakpoint holds its breath\n"
    "logs scroll past at three a.m.\n"
    "one typo did this"
)

# Gate: exactly 3 lines, 1-200 characters of UTF-8 text, not only whitespace.
# The 5-7-5 shape is also enforced explicitly: a haiku whose syllable count
# is wrong fails the form criterion outright, so the counts are pinned here
# word by word (counted by hand, not by a library) and asserted at import.
#   line 1: break-point(2) holds(1) its(1) breath(1) = 5
#   line 2: logs(1) scroll(1) past(1) at(1) three(1) a(1) m(1) = 7
#   line 3: one(1) ty-po(2) did(1) this(1) = 5
SYLLABLES = {
    "breakpoint": 2, "holds": 1, "its": 1, "breath": 1,
    "logs": 1, "scroll": 1, "past": 1, "at": 1, "three": 1,
    "a.m.": 2,  # pronounced "ay em"
    "one": 1, "typo": 2, "did": 1, "this": 1,
}
EXPECTED_SHAPE = (5, 7, 5)

LINES = HAIKU.split("\n")
assert len(LINES) == 3, f"haiku must have exactly 3 lines, got {len(LINES)}"
assert 1 <= len(HAIKU) <= 200, f"haiku must be 1-200 characters, got {len(HAIKU)}"
assert all(line.strip() for line in LINES), "haiku lines must not be blank"
for line, expected in zip(LINES, EXPECTED_SHAPE):
    counted = sum(SYLLABLES[word] for word in line.split())
    assert counted == expected, (
        f"haiku line must have {expected} syllables, got {counted}: {line!r}"
    )


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
