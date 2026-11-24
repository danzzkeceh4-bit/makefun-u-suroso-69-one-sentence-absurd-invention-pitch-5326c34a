#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — The Apologizer.

Writes exactly one sentence (204 characters, no trailing newline) to
/output/entry.txt, then reads it back and asserts it matches exactly.
No network, no external input. Python 3.13.
"""

ENTRY = (
    "The Apologizer: a self-blaming alarm clock that says sorry, brews your "
    "coffee, and takes the guilt for Monday, so you can snooze in peace while "
    "it files a formal complaint against mornings on your behalf."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, (
        f"entry.txt mismatch: expected {len(ENTRY)} chars, got {len(written)}"
    )
    assert len(written) == 204, f"expected 204 chars, got {len(written)}"
    print(f"Wrote {len(written)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
