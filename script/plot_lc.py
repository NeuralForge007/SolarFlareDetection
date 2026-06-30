from datetime import datetime
import matplotlib.dates as mdates

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

file = r"C:\\Users\\Ahona Sarkar\\solex\\data\\raw\\AL1_SLX_L1_20260623_v1.0\\AL1_SLX_L1_20260623_v1.0\\SDD2\\AL1_SOLEXS_20260623_SDD2_L1.lc.gz"


hdul = fits.open(file)

rate = hdul["RATE"].data

time = rate["TIME"]
counts = rate["COUNTS"]
time_dt = [datetime.utcfromtimestamp(t) for t in time]
plt.figure(figsize=(15,5))

plt.plot(time_dt, counts)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))

plt.xlabel("UTC Time")
plt.ylabel("Counts/sec")
plt.title("SoLEXS Light Curve")

plt.grid(True)

plt.tight_layout()

plt.show()
print(hdul[0].header)
print(hdul["RATE"].header)