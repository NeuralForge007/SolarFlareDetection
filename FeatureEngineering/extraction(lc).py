import pandas as pd
import numpy as np
df= pd.read_csv(r"C:\Users\ANKAN KANRAR\Desktop\ISRO BAH\SFP\SolarFlareDetection\FeatureEngineering\Updated_data.csv")

df.drop(columns=["CDTE1", "CDTE2", "CZT1", "CZT2"],
        errors="ignore",
        inplace=True)

# deleting rows upto 43198
df1 = df.iloc[43197:].reset_index(drop=True)
# Counting values before interpolation
print("Zeros before :", (df1["HARD_C"] == 0).sum())
print("NaNs before  :", df1["HARD_C"].isna().sum())
# Replacing zeros with NaN
df1["HARD_C"] = df1["HARD_C"].replace(0, np.nan)
# Performing linear interpolation
df1["HARD_C"] = df1["HARD_C"].interpolate(
    method="linear",
    limit_direction="both"
)

#Physics informed Features

# 1. Background Photon Count (Moving Median)
WINDOW = 300        # 300-second background
df["BACKGROUND"] = (
    df["SOFT_C"]
    .rolling(window=WINDOW, min_periods=1)
    .median()
)

# 2. Rolling Standard Deviation
df["ROLLING_STD"] = (
    df["SOFT_C"]
    .rolling(window=WINDOW, min_periods=1)
    .std()
)
df["ROLLING_STD"] = df["ROLLING_STD"].fillna(0)

# 3. Adaptive Threshold
# T = Background + k × sigma
k =0.4
df["THRESHOLD"] = (
    df["BACKGROUND"]
    +
    k * df["ROLLING_STD"]
)

# 4. Excess Photon Count
df["EXCESS_SOFT_PHOTON"] = (
    df["SOFT_C"]
    -
    df["THRESHOLD"]
)


# 5. change of photon count of Soft Xrays every second
df["Slope"] = df["SOFT_C"].diff()


# 6. Pre-heating Index
background_safe = df["BACKGROUND"].replace(0, np.nan)

df["PREHEATING_INDEX"] = (
    (
        (df["SOFT_C"] - background_safe)
        /
        background_safe
    )
    *
    df["Slope"]
)

df["PREHEATING_INDEX"] = (
    df["PREHEATING_INDEX"]
    .fillna(0)
)



df.to_csv(
    r"C:\Users\ANKAN KANRAR\Desktop\ISRO BAH\SFP\SolarFlareDetection\FeatureEngineering\Updated_data.csv",
    index=False
)
print(df.head())
