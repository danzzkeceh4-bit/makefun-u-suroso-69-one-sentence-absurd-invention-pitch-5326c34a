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


def validate_entry(text: str) -> None:
    """Check the entry before writing: 1-220 chars, exactly one sentence,
    no trailing newline."""
    assert 1 <= len(text) <= 220, (
        f"entry length {len(text)} out of range 1-220"
    )
    assert not text.endswith("\n"), "entry must not end with a newline"
    assert text.endswith("."), "entry must end with a period"
    assert text.count(".") == 1, (
        f"entry must be exactly one sentence, found {text.count('.')} periods"
    )


def main() -> None:
    validate_entry(ENTRY)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, (
        f"entry.txt mismatch: read-back length is {len(written)} chars, "
        f"but expected {len(ENTRY)} chars"
    )
    assert len(written) == 204, f"expected 204 chars, got {len(written)}"
    print(f"Wrote {len(written)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
