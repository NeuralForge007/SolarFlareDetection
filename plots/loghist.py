import matplotlib.pyplot as plt

from loaddata import *

plt.figure(figsize=(9,6))

plt.hist(
    counts,
    bins=100,
    log=True,
    edgecolor="black"
)

plt.title("Log Histogram of SoLEXS Counts")

plt.xlabel("Counts/sec")

plt.ylabel("Log Frequency")

plt.grid(True)

plt.tight_layout()

plt.show()

# ------------------------------
# Statistics
# ------------------------------

print("="*45)

print("Minimum Counts :", counts.min())

print("Maximum Counts :", counts.max())

print("Mean Counts    :", counts.mean())

print("Median Counts  :", float(__import__("numpy").median(counts)))

print("Std Deviation  :", counts.std())

print("="*45)