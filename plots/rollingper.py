import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from loaddata import *

# -----------------------------------------
# Rolling 20th Percentile
# -----------------------------------------

rolling20 = (
    pd.Series(counts)
      .rolling(window=1801, center=True, min_periods=1)
      .quantile(0.20)
      .to_numpy()
)

# -----------------------------------------
# Plot
# -----------------------------------------

plt.figure(figsize=(16,6))

# Raw Light Curve
plt.plot(
    time_dt,
    counts,
    color="lightgray",
    linewidth=1,
    label="Raw Light Curve"
)

# Rolling 20th Percentile
plt.plot(
    time_dt,
    rolling20,
    color="green",
    linewidth=2,
    label="Rolling 20th Percentile"
)

plt.title("Raw Light Curve with Rolling 20th Percentile")
plt.xlabel("UTC Time")
plt.ylabel("Counts/sec")

plt.grid(True)
plt.legend()

plt.gca().xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M")
)

plt.tight_layout()
plt.show()

# -----------------------------------------
# Statistics
# -----------------------------------------

print("="*45)
print("Rolling 20th Percentile")
print("Minimum :", rolling20.min())
print("Maximum :", rolling20.max())
print("Mean    :", rolling20.mean())
print("="*45)