import os

MAX_CHARS = 200

PART1 = "Group chat, c. 2025. "
PART2 = "A sacred scroll on which 47 humans "
PART3 = "typed 'lol' for eleven years. "
PART4 = "Nobody ever left."
LINE = PART1 + PART2 + PART3 + PART4

assert 1 <= len(LINE) <= MAX_CHARS, "entry must be 1-200 characters"
assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    assert f.read() == LINE, "round-trip mismatch"
print(len(LINE))
