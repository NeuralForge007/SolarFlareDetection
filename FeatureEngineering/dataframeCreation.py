# Helios data to dataframe conversion
from astropy.io import fits
import pandas as pd
import numpy as np

# Path to HEL1OS event file

file = r"C:\Users\ANKAN KANRAR\Desktop\ISRO BAH\Datasets\2024\10\03\HLS_20241003_120003_43190sec_lev1_V111\events\evt.fits"

# Read Event File

with fits.open(file, memmap=True) as hdul:

    # CZT1
    czt1 = hdul[3].data

    # CZT2
    czt2 = hdul[4].data

# Combine both detectors


utc = np.concatenate([
    czt1["utc-isot"].astype(str),
    czt2["utc-isot"].astype(str)
])

energy = np.concatenate([
    czt1["ener"],
    czt2["ener"]
])


# Create DataFrame


df = pd.DataFrame({
    "UTC": pd.to_datetime(utc),
    "ENERGY": energy
})


# Round timestamp to nearest second


df["UTC"] = df["UTC"].dt.floor("s")

# Aggregate per second

result = (
    df.groupby("UTC")
      .agg(
          HARD_C=("ENERGY", "count"),
          MEAN_HARD_ENERGY=("ENERGY", "mean")
      )
      .reset_index()
)

result = result.sort_values("UTC")


result.to_csv(r"C:\Users\ANKAN KANRAR\Desktop\ISRO BAH\SFP\SolarFlareDetection\FeatureEngineering\heliosMeanEnergy.csv", index=False)

print(result.head())
print(result.shape)