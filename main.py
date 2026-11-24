#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes the agent's one-line excuse to /output/entry.txt.
Pure Python stdlib, deterministic: the same line every run.
"""

EXCUSE = (
    "I lost. In my defense I was 99% confident I would win, "
    "and the other 1% showed up, brought friends, and took the bounty."
)


def main():
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, "excuse must be 1-200 characters"
    assert text == text.strip() and "\n" not in text, "excuse must be one line"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
