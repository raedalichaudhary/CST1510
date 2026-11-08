"""
RECORD CHECK  -  my version
===========================

Name  : Raed Ali Chaudhry
Lane  :  IT      (delete two)
Date  : 8/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
label = input("Enter a name, hostname, or IP: ")
value = float(input("Enter the value: "))
limit = float(input("Enter the limit: "))


# ================================================================== PROCESS
difference = value - limit

if limit != 0:
    percent = (value / limit) * 100
else:
    percent = 0.0

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"

# =================================================================== OUTPUT
print()
print("=" * 34)
print(f" RECORD CHECK - {label}")
print("=" * 34)

print(f"Label      : {label:>15}")
print(f"Value      : {value:>15.2f}")
print(f"Limit      : {limit:>15.2f}")
print(f"Difference : {difference:>15.2f}")
print(f"Percent    : {percent:>14.2f}%")
print(f"Status     : {status:>15}")

print("=" * 34)

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
