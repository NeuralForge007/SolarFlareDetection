from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.ndimage import uniform_filter1d, median_filter
from scipy.signal import find_peaks
from datetime import datetime, UTC

FILE = r"C:\\Users\\Ahona Sarkar\\solex\\data\\raw\\AL1_SLX_L1_20260623_v1.0\\AL1_SLX_L1_20260623_v1.0\\SDD2\\AL1_SOLEXS_20260623_SDD2_L1.lc.gz"
with fits.open(FILE) as hdul:
    rate = hdul["RATE"].data
    time = np.asarray(rate["TIME"])
    counts = np.asarray(rate["COUNTS"])

mask = (~np.isnan(time)) & (~np.isnan(counts))
time = time[mask]
counts = counts[mask]

_, idx = np.unique(time, return_index=True)
time = time[idx]
counts = counts[idx]
mask = counts > 0
time = time[mask]
counts = counts[mask]

# Convert timestamps to UTC
time_dt = np.array([datetime.fromtimestamp(t, UTC) for t in time])

# ==========================================================
# PREPROCESSING
# ==========================================================

# Smooth signal (15-second moving average)
smooth_counts = uniform_filter1d(counts, size=15)

# Variable background (10-minute moving median)
background = median_filter(smooth_counts, size=600)

# ==========================================================
# PEAK DETECTION
# ==========================================================

peaks, properties = find_peaks(
    smooth_counts,
    prominence=30,
    distance=600,
    width=20
)

if len(peaks) == 0:
    print("No flare detected.")
    exit()

# Largest flare
peak = peaks[np.argmax(smooth_counts[peaks])]
peak_counts = smooth_counts[peak]

# ==========================================================
# FIND START
# ==========================================================

start = peak

while start > 0:
    if smooth_counts[start] <= background[start]:
        break
    start -= 1

# ==========================================================
# FIND END
# ==========================================================

end = peak

while end < len(smooth_counts) - 1:
    if smooth_counts[end] <= background[end]:
        break
    end += 1

# ==========================================================
# CHECK IF TRUNCATED
# ==========================================================

truncated = (end == len(smooth_counts) - 1)

rise_time = peak - start

if truncated:
    decay_time = None
    duration = None
else:
    decay_time = end - peak
    duration = end - start

# ==========================================================
# RESULTS
# ==========================================================

print("\n" + "=" * 60)
print("FLARE EVENT")
print("=" * 60)

print(f"Background at Peak : {background[peak]:.2f} counts/s")
print(f"Peak Counts        : {peak_counts:.2f}")
print(f"Start Time         : {time_dt[start]}")
print(f"Peak Time          : {time_dt[peak]}")

if truncated:
    print("End Time           : Truncated (continues into next file)")
else:
    print(f"End Time           : {time_dt[end]}")

print(f"Rise Time          : {rise_time} sec")

if truncated:
    print("Decay Time         : Unknown")
    print("Duration           : Unknown")
else:
    print(f"Decay Time         : {decay_time} sec")
    print(f"Duration           : {duration} sec")

print(f"Status             : {'TRUNCATED' if truncated else 'COMPLETE'}")
print("=" * 60)

# ==========================================================
# PLOT
# ==========================================================

plt.figure(figsize=(18, 6))

# Raw counts
plt.plot(
    time_dt,
    counts,
    color="lightgray",
    linewidth=0.6,
    label="Raw Counts"
)

# Smoothed counts
plt.plot(
    time_dt,
    smooth_counts,
    color="black",
    linewidth=1.5,
    label="Smoothed Counts"
)

# Variable background
plt.plot(
    time_dt,
    background,
    color="orange",
    linestyle="--",
    linewidth=2,
    label="Variable Background"
)

# Start
plt.axvline(
    time_dt[start],
    color="green",
    linestyle="--",
    linewidth=2,
    label="Start"
)

# Peak
plt.axvline(
    time_dt[peak],
    color="red",
    linestyle="--",
    linewidth=2,
    label="Peak"
)

# End
if not truncated:
    plt.axvline(
        time_dt[end],
        color="blue",
        linestyle="--",
        linewidth=2,
        label="End"
    )

# Peak marker
plt.scatter(
    time_dt[peak],
    peak_counts,
    color="red",
    s=120,
    zorder=5
)

plt.annotate(
    f"{peak_counts:.0f}",
    (time_dt[peak], peak_counts),
    xytext=(10, 10),
    textcoords="offset points"
)

plt.title("SoLEXS Flare Detection (Variable Background)")
plt.xlabel("UTC Time")
plt.ylabel("Counts/s")

plt.gca().xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M")
)

plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()

plt.show()