"""
RECORD CHECK  -  my version
===========================

Name  : Raed Ali Chaudhry
Lane  : IT      (delete two)
Date  : 29/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
class Record:
    over_limit_count = 0  # Class-level running total

    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on value compared with limit."""

        percentage = (self.value / self.limit) * 100

        if percentage >= 100:
            Record.over_limit_count += 1
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"

# ==================================================================== RECORDS
records = [
    Record("Electricity", 120, 100),
    Record("Water", 95, 100),
    Record("Internet", 85, 100),
    Record("Gas", 90, 100),
    Record("Rent", 500, 600)
]


# ==================================================================== OUTPUT
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)

    print(f"  Label  : {record.label}")
    print(f"  Value  : {record.value}")
    print(f"  Limit  : {record.limit}")
    print(f"  Status : {record.status()}")

    print("=" * 34)

print()
print(f"Total records OVER LIMIT: {Record.over_limit_count}")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
