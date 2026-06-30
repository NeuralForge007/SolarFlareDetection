import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.ndimage import uniform_filter1d
from scipy.signal import find_peaks

from loaddata import *

smooth = uniform_filter1d(counts, size=15)

background = (
    pd.series(counts)
    .rolling(window=1801, center=True, min_periods=1)
    .quantile(0.20)
    .to_numpy()
)

# Background-subtracted signal
signal = smooth - background

# Detect peaks
peaks, properties = find_peaks(
    signal,
    height=20,
    prominence=15,
    distance=300,
    width=10
)

# Print peaks
print(f"\nDetected {len(peaks)} flare(s)\n")

for i, p in enumerate(peaks, start=1):
    print(f"Flare {i}")
    print(f"Peak Time   : {time_dt[p]}")
    print(f"Peak Counts : {counts[p]:.2f}")
    print(f"Net Peak    : {signal[p]:.2f}")
    print(f"Prominence  : {properties['prominences'][i-1]:.2f}")
    print("-"*40)

# Save table
events = pd.DataFrame({
    "Peak Time": [time_dt[p] for p in peaks],
    "Peak Counts": counts[peaks],
    "Net Peak": signal[peaks],
    "Prominence": properties["prominences"]
})

events.to_csv("detected_peaks.csv", index=False)

# Plot
plt.figure(figsize=(16,6))

plt.plot(time_dt, counts, color="lightgray", label="Raw")
plt.plot(time_dt, smooth, color="black", label="Smoothed")
plt.plot(time_dt, background, color="green", label="Background")

plt.scatter(
    time_dt[peaks],
    smooth[peaks],
    color="red",
    s=60,
    label="Peaks"
)

for i, p in enumerate(peaks, start=1):
    plt.text(
        time_dt[p],
        smooth[p] + 8,
        str(i),
        ha="center",
        fontsize=8
    )

plt.title("Multi-Flare Peak Detection")
plt.xlabel("UTC")
plt.ylabel("Counts/sec")

plt.grid(True)
plt.legend()

plt.gca().xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M")
)

plt.tight_layout()
plt.show()