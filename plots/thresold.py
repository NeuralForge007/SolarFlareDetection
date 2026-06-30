import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from loaddata import *
from scipy.ndimage import uniform_filter1d



# =====================================================
# Parameters
# =====================================================

WINDOW = 1801      # 30-minute window (seconds)
     # 30-minute window (seconds)     
K=2   

# =====================================================
# Background Flux (Moving Median)
# =====================================================

background = (
    pd.Series(counts)
      .rolling(window=WINDOW,
               center=True,
               min_periods=1)
      .median()
      .to_numpy()
)
background = uniform_filter1d(background, size=301)
# =====================================================
# Local Standard Deviation
# =====================================================
residual = counts - background
rolling_sd = (
    pd.Series(residual)
      .rolling(window=WINDOW,
               center=True,
               min_periods=1)
      .std()
      .fillna(0)
      .to_numpy()
)

# =====================================================
# Adaptive Threshold
# =====================================================

threshold = background + K * rolling_sd

# =====================================================
# Plot
# =====================================================

plt.figure(figsize=(18,6))

plt.plot(
    time_dt,
    counts,
    color="lightgray",
    linewidth=1,
    label="Raw Counts"
)

plt.plot(
    time_dt,
    background,
    color="green",
    linewidth=2,
    label="Moving Median (Background)"
)

plt.plot(
    time_dt,
    threshold,
    color="red",
    linewidth=2,
    linestyle="--",
    label=f"Threshold = Background + {K} × SD"
)

plt.title("Adaptive Background and Threshold")

plt.xlabel("UTC Time")
plt.ylabel("Counts/sec")

plt.grid(True)
plt.legend()

plt.gca().xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M")
)

plt.tight_layout()
plt.show()