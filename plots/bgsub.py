import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

from loaddata import *

# -------------------------------------------------
# Rolling 20th Percentile Background
# -------------------------------------------------

background = (
    pd.Series(counts)
    .rolling(window=1801, center=True, min_periods=1)
    .quantile(0.20)
    .to_numpy()
)

# -------------------------------------------------
# Background Subtraction
# -------------------------------------------------

net_counts = counts - background

# -------------------------------------------------
# Plot
# -------------------------------------------------

plt.figure(figsize=(18,6))

plt.plot(
    time_dt,
    net_counts,
    color="black",
    linewidth=1
)

plt.axhline(
    0,
    color="red",
    linestyle="--"
)

plt.title("Background Subtracted SoLEXS Light Curve")

plt.xlabel("UTC Time")

plt.ylabel("Net Counts/sec")

plt.grid(True)

plt.gca().xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M")
)

plt.tight_layout()

plt.show()