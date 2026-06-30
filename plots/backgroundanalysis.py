from loaddata import *

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from scipy.ndimage import uniform_filter1d
from scipy.ndimage import median_filter

# -----------------------------
# Smooth signal
# -----------------------------

smooth = uniform_filter1d(counts, size=15)

# ----------------------------
# Rolling Mean
# -----------------------------

background_mean = uniform_filter1d(counts, size=3601)

# -----------------------------
# Rolling Median
import pandas as pd

background_median = (
    pd.Series(counts)
      .rolling(
          window=3601,
          center=True,
          min_periods=1
      )
      .median()
      .to_numpy()
)
# -----------------------------
# Rolling 20th Percentile
# -----------------------------
background_percentile = (
    pd.Series(counts)
      .rolling(
          window=3601,
          center=True,
          min_periods=1
      )
      .quantile(0.20)
      .to_numpy()
)

# -----------------------------
# Plot
# -----------------------------

plt.figure(figsize=(18,6))

plt.plot(
    time_dt,
    counts,
    color="lightgray",
    label="Raw"
)

plt.plot(
    time_dt,
    smooth,
    color="black",
    linewidth=1.5,
    label="Smoothed"
)

plt.plot(
    time_dt,
    background_mean,
    label="Rolling Mean"
)

plt.plot(
    time_dt,
    background_median,
    label="Rolling Median"
)

plt.plot(
    time_dt,
    background_percentile,
    linewidth=2,
    label="20th Percentile"
)

plt.xlabel("UTC")

plt.ylabel("Counts/sec")

plt.title("Background Estimation Comparison")

plt.legend()

plt.grid(True)

plt.gca().xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M")
)

plt.tight_layout()

plt.show()