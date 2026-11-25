#!/usr/bin/env python3
"""Writes one sick-day excuse to /output/entry.txt."""

import os

EXCUSE = "My neighbour's parrot learned to mimic my alarm clock and has been snoozing it for a week \u2014 I only found out when it started doing my boss's voice telling me to sleep in."

def main():
    # The gate is 1-200 characters, one line, UTF-8. Fail loudly here
    # rather than shipping an entry the sealed scorer would refuse.
    assert 1 <= len(EXCUSE) <= 200, len(EXCUSE)
    assert "\n" not in EXCUSE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)

if __name__ == "__main__":
    main()
