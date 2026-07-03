import pandas as pd

from astropy.io import fits
import numpy as np
from datetime import datetime, UTC

FILE = r"C:\Users\ANKAN KANRAR\Desktop\ISRODD2\AL1_SOLEXS_20241003_SDD2_L1.lc\AL1_SOLEXS_20241003_SDD2_L1.lc"

hdul = fits.open(FILE)

rate = hdul["RATE"].data

time = np.array(rate["TIME"], dtype=np.float64)
counts = np.array(rate["COUNTS"], dtype=np.float64)

hdul.close()

mask = ~np.isnan(counts)

time = time[mask]
counts = counts[mask]

time_dt = np.array(
    [datetime.fromtimestamp(t, UTC) for t in time]
)
