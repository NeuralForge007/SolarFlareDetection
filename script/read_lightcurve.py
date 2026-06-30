from astropy.io import fits

file = r"C:\\Users\\Ahona Sarkar\\solex\\data\\raw\\AL1_SLX_L1_20260623_v1.0\\AL1_SLX_L1_20260623_v1.0\\SDD2\\AL1_SOLEXS_20260623_SDD2_L1.lc.gz"

hdul = fits.open(file)

rate = hdul["RATE"].data

print(rate.columns)

print(rate[:10])

import numpy as np

counts = rate["COUNTS"]
time = rate["TIME"]
mask = ~np.isnan(counts)

time = time[mask]
counts = counts[mask]

print("Number of valid samples:", len(counts))
print("Minimum Counts :", np.min(counts))
print("Maximum Counts :", np.max(counts))
print("Average Counts :", np.mean(counts))
print("Median Counts  :", np.median(counts))
print("Standard Deviation :", np.std(counts))
import numpy as np
from datetime import datetime

peak_index = np.argmax(counts)

print("Peak Index :", peak_index)
print("Peak Counts:", counts[peak_index])

peak_time = datetime.utcfromtimestamp(time[peak_index])

print("Peak UTC :", peak_time)