#!/usr/bin/env python3
"""{e["title"]}.

Writes a single line of text to /output/entry.txt.
Pure stdlib, deterministic, no network, no input files.
"""

import os

ENTRY = (
    'Good morning, Nimbleville: light drizzle, heavy sighs, and a 40% chance your bus left two minutes ago.'
)
# Revision: v1 was only a weather setup (drizzle, sighs, rain) with no punchline.
# Revised: replaced the flat rain forecast with the commuter punchline — your bus left two minutes ago.


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
