"""
RECORD CHECK  -  my version
===========================

Name  : Raed Ali Chaudhry
Lane  : IT      (delete two)
Date  : 15/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

def status_of(percent):
    """Returns the status based on percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Calculates the difference and percentage."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference,
                 percent, status):
    """Prints the record report."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("-" * 34)
    print(f"Value      : {value:>10.2f}")
    print(f"Limit      : {limit:>10.2f}")
    print(f"Difference : {difference:>10.2f}")
    print(f"Percentage : {percent:>9.2f}%")
    print(f"Status     : {status}")
    print("=" * 34)


# ==================================================================== INPUT

label = input("Enter name, hostname or IP: ")
value = float(input("Enter value: "))
limit = float(input("Enter limit: "))


# ================================================================== PROCESS

difference, percent = check(value, limit)

status = status_of(percent)


# =================================================================== OUTPUT

print_report(label, value, limit, difference,
             percent, status)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
