import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from scipy.ndimage import uniform_filter1d
from datetime import datetime, UTC

from loaddata import *

# -------------------------------------------------
# Smooth Signal
# -------------------------------------------------

smooth = uniform_filter1d(
    counts,
    size=15
)

# -------------------------------------------------
# Background
# -------------------------------------------------

background = (
    pd.Series(counts)
    .rolling(window=1801, center=True, min_periods=1)
    .quantile(0.20)
    .to_numpy()
)

# -------------------------------------------------
# Zoom Window
# -------------------------------------------------

start = datetime(2026,6,23,23,20,0,tzinfo=UTC)

end = datetime(2026,6,23,23,30,0,tzinfo=UTC)

mask = (time_dt >= start) & (time_dt <= end)

# -------------------------------------------------
# Plot
# -------------------------------------------------

plt.figure(figsize=(14,6))

plt.plot(
    time_dt[mask],
    counts[mask],
    color="lightgray",
    label="Raw"
)

plt.plot(
    time_dt[mask],
    smooth[mask],
    color="black",
    linewidth=2,
    label="Smoothed"
)

plt.plot(
    time_dt[mask],
    background[mask],
    color="green",
    linewidth=2,
    label="Background"
)

plt.title("Zoomed View of Main Solar Flare")

plt.xlabel("UTC Time")

plt.ylabel("Counts/sec")

plt.grid(True)

plt.legend()

plt.gca().xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M:%S")
)

plt.tight_layout()

plt.show()