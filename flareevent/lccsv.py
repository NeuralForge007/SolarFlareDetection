import pandas as pd
import numpy as np
from astropy.io import fits

lc_file = r"C:\\Users\\Ahona Sarkar\\OneDrive\\Desktop\\solar_repo\\SolarFlareDetection\\data\\raw\\AL1_SLX_L1_20241003_v1.0\\SDD2\\AL1_SOLEXS_20241003_SDD2_L1.lc\\AL1_SOLEXS_20241003_SDD2_L1.lc"
with fits.open(lc_file) as hdul:
    data = hdul["RATE"].data

    time = np.asarray(data["TIME"], dtype=np.float64).copy()
    counts = np.asarray(data["COUNTS"], dtype=np.float64).copy()

df = pd.DataFrame({
    "TIME": time,
    "COUNTS": counts
})

df.dropna(inplace=True)

df.to_csv("solexs_lightcurve.csv", index=False)

print(df.head())
print("CSV saved successfully!")