import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.ndimage import uniform_filter1d

from loaddata import *

# ======================================================
# Smooth the signal first
# ======================================================

smooth = uniform_filter1d(counts, size=15)

# ======================================================
# First Derivative
# ======================================================

# Counts change per second
derivative = np.gradient(smooth)
max_index = np.argmax(derivative)
min_index = np.argmin(derivative)

# ======================================================
# Plot
# ======================================================
plt.figure(figsize=(18,6))

plt.plot(
    time_dt,
    derivative,
    color="purple",
    linewidth=1,
    label="Derivative"
)

plt.scatter(
    time_dt[max_index],
    derivative[max_index],
    color="green",
    s=120,
    label="Fastest Rise"
)

plt.scatter(
    time_dt[min_index],
    derivative[min_index],
    color="red",
    s=120,
    label="Fastest Decay"
)

plt.axhline(
    0,
    color="black",
    linestyle="--"
)

plt.legend()

plt.grid(True)

plt.gca().xaxis.set_major_formatter(
    mdates.DateFormatter("%H:%M")
)

plt.title("Rate of Change of SoLEXS Counts")

plt.xlabel("UTC Time")

plt.ylabel("dCounts/dt")

plt.tight_layout()

plt.show()