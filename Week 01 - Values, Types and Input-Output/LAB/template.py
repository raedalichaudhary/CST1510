"""
RECORD CHECK  -  my version
===========================

Name  : Raed Ali Chaudhary
Lane  : IT
Date  : 27/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
hostname = input("Hostname: ")
used = float(input("GB used: "))
total = float(input("GB total: "))

print("=" * 40)
print(f"RECORD CHECK - {hostname}")
print("=" * 40)
print(f"Used  : {used}")
print(f"Total : {total}")
print("=" * 40)



# ================================================================== PROCESS
difference = used - total
percent = (used / total) * 100

label = "RECORD CHECK"

# =================================================================== OUTPUT
print()
print("=" * 34)
print(f" RECORD CHECK - {label}")
print("=" * 34)

print(f"Used       : {used:>10.2f}")
print(f"Total      : {total:>10.2f}")
print(f"Difference : {difference:>+10.2f}")
print(f"Percent    : {percent:>10.2f}%")

print("=" * 34)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
