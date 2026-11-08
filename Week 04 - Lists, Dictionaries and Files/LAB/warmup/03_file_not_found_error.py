# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

from pathlib import Path

file_path = Path(__file__).parent / "records_sample.txt"

with open(file_path, "r") as f:
    print(f.read())