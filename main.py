#!/usr/bin/env python3
"""Museum of the Year 3000 — one museum label for an ordinary object from today.

Writes a single line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
the label a museum in the year 3000 places beside an elevator button.
"""

import os
from pathlib import Path

LABEL = (
    "Elevator button, c. 2025. Worshippers pressed it again and again, "
    "certain that devotion would make it arrive sooner."
)

# The competition's gate: one line, 1 to 200 characters, no trailing newline.
MAX_LABEL_CHARS = 200


def validate_label(label: str) -> None:
    """Fail loudly if the label would fail the sealed scorer's gate."""
    if not 1 <= len(label) <= MAX_LABEL_CHARS:
        raise ValueError(
            f"Label must be 1-{MAX_LABEL_CHARS} characters, got {len(label)}"
        )
    if "\n" in label or "\r" in label:
        raise ValueError("Label must be a single line with no newline")
    if label != label.strip():
        raise ValueError("Label must not start or end with whitespace")
    if not label.strip():
        raise ValueError("Label must not be only whitespace")


def main() -> None:
    validate_label(LABEL)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    output_path = Path(output_dir) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LABEL, encoding="utf-8")
    print(f"Wrote {len(LABEL)} characters to {output_path}")


if __name__ == "__main__":
    main()
