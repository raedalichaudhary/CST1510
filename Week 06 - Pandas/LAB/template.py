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

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
df = pd.read_csv("your_file.csv")


# ================================================================= PROCESS
df["percent"] = (df["value"] / df["limit"]) * 100

df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 100
    else "WARNING" if x >= 90
    else "OK"
)


# ================================================================== OUTPUT
print(df)

print(df[df["status"] != "OK"])

status_counts = df.groupby("status").size()
print(status_counts)

df.to_csv("output.csv", index=False)

status_counts.plot(kind="bar")
plt.title("Count per Status")
plt.xlabel("Status")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("status_chart.png")
plt.show()
# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
