"""
RECORD CHECK  -  my version
===========================

Name  :  Raed Ali Chaudhry
Lane  :  IT      (delete two)
Date  :  5/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
import re

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    parts = raw_line.strip().split(",")

    record = {}

    for part in parts:
        part = part.strip()

        if "=" in part:
            key, value = part.split("=", 1)

            key = key.strip().lower()
            value = value.strip()

            record[key] = int(value)

        else:
            record["server"] = part

    return record


def status_of(record):

    percentage = record["used"] / record["total"] * 100

    if percentage >= 90:
        return "OVER LIMIT"

    elif percentage >= 80:
        return "WARNING"

    else:
        return "OK"


# ====================================================================== INPUT
raw_records = [
    "Srv-01 , used=87 , total=100",
    "Srv-02,used=95,total=100",
    " Srv-03 , used=45 , total=100",
    "Srv-04, used=80, total=100",
    "Srv-05 , used=99 , total=100"
]

# =============================================================== PROCESS + OUTPUT
total_records = 0
flagged_records = 0

for raw_record in raw_records:

    cleaned = parse_line(raw_record)

    status = status_of(cleaned)

    print("Cleaned:", cleaned)
    print("Status:", status)
    print("------------------------")

    total_records += 1

    if status != "OK":
        flagged_records += 1



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
