#Mean Hard Energy Extraction
import pandas as pd

solex = pd.read_csv(r"C:\Users\ANKAN KANRAR\Desktop\ISRO BAH\SFP\SolarFlareDetection\FeatureEngineering\Updated_data.csv")
helios = pd.read_csv(r"C:\Users\ANKAN KANRAR\Desktop\ISRO BAH\SFP\SolarFlareDetection\FeatureEngineering\heliosMeanEnergy.csv")

# -------------------------
# Convert timestamps
# -------------------------

# SoLEXS uses UNIX_TIME (1-second accurate)
solex["UTC"] = pd.to_datetime(solex["UNIX_TIME"], unit="s")

# HEL1OS already has UTC timestamps
helios["UTC"] = pd.to_datetime(helios["UTC"])

# Create minute key
solex["MINUTE"] = solex["UTC"].dt.floor("min")
helios["MINUTE"] = helios["UTC"].dt.floor("min")


# Mean energy per minute
minute_energy = (
    helios
    .groupby("MINUTE")["MEAN_HARD_ENERGY"]
    .mean()
    .reset_index()
)


# Merge
final = pd.merge(
    solex,
    minute_energy,
    on="MINUTE",
    how="left"
)

# Remove helper column
final.drop(columns=["MINUTE"], inplace=True)

final.to_csv(r"C:\Users\ANKAN KANRAR\Desktop\ISRO BAH\SFP\SolarFlareDetection\FeatureEngineering\Updated_data.csv", index=False)


print(final.head())
