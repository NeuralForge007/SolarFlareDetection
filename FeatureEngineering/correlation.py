# Coorelation Features of soft and hard X-rays
import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\ANKAN KANRAR\Desktop\ISRO BAH\SFP\SolarFlareDetection\FeatureEngineering\Updated_data.csv")

# 1. Rolling Soft-Hard Correlation

window = 60

df["ROLLING_SOFT_HARD_CORR"] = (
    df["SOFT_C"]
    .rolling(window)
    .corr(df["HARD_C"])
)

# 2. Hardness Ratio

soft_safe = df["SOFT_C"].replace(0, np.nan)

df["HARDNESS_RATIO"] = (
    df["HARD_C"] / soft_safe
)


# 3. Neupert Deviation Index (NDI)
# Formula:
# (dSoft/dt - Hard)/Hard

hard_safe = df["HARD_C"].replace(0, np.nan)

df["NDI"] = (
    (df["Slope"] - df["HARD_C"])
    /
    hard_safe
)


# 4. Neupert Consistency Indicator (NCI)
# Rolling correlation between dSoft/dt and Hard


df["NCI"] = (
    df["Slope"]
    .rolling(window)
    .corr(df["HARD_C"])
)


# Replace infinities


df.replace([np.inf, -np.inf], np.nan, inplace=True)


df.to_csv(r"C:\Users\ANKAN KANRAR\Desktop\ISRO BAH\SFP\SolarFlareDetection\FeatureEngineering\Updated_data.csv", index=False)

print(df.head())