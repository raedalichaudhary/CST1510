"""
RECORD CHECK  -  my version
===========================

Name  : Raed Ali Chaudhry
Lane  : IT      (delete two)
Date  : 22/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def check_record(value, limit):
    """Check a value against its limit and return the results."""
    difference = value - limit
    percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "WITHIN LIMIT"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print a one-line report for a record."""
    print(f"{label}: Value={value}, Limit={limit}, "
          f"Difference={difference}, "
          f"Percent={percent:.1f}%, Status={status}")



# ====================================================================== STORE
records = [
    {"label": "Record 1", "value": 120, "limit": 100},
    {"label": "Record 2", "value": 80, "limit": 100},
    {"label": "Record 3", "value": 150, "limit": 120},
    {"label": "Record 4", "value": 90, "limit": 100}
]

# =============================================================== PROCESS + OUTPUT
over_limit_count = 0

for record in records:

    label = record["label"]
    value = record["value"]
    limit = record["limit"]

    difference, percent, status = check_record(value, limit)

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1

print("\nTotal records over limit:", over_limit_count)
# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
