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


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    output_path = Path(output_dir) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LABEL, encoding="utf-8")
    print(f"Wrote {len(LABEL)} characters to {output_path}")


if __name__ == "__main__":
    main()
