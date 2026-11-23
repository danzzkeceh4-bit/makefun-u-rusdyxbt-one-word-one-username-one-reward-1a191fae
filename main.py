#!/usr/bin/env python3
"""One Word, One Username, One Reward — make.fun entry.

Writes the entrant's own make.fun username, and nothing else, to
/output/entry.txt: exactly ``swift-fox-13`` (12 bytes, no trailing
newline), then reads it back and asserts it is byte-identical to the
constant. No network, no external input.
"""

import os

USERNAME = "swift-fox-13"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    data = USERNAME.encode("utf-8")
    assert len(data) == 12, f"expected 12 bytes, got {len(data)}"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == data, (
        f"read-back mismatch: wrote {data!r}, read {written!r}"
    )
    assert len(written) == 12, f"expected 12 bytes, read {len(written)}"

    print(f"Wrote {len(written)} bytes to {OUTPUT_PATH}: {USERNAME}")


if __name__ == "__main__":
    main()
