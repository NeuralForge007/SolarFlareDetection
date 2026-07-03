import pandas as pd
import numpy as np
df= pd.read_csv(r"C:\Users\ANKAN KANRAR\Desktop\ISRO BAH\SFP\SolarFlareDetection\FeatureEngineering\Updated_data.csv")

df.drop(columns=["CDTE1", "CDTE2", "CZT1", "CZT2"],
        errors="ignore",
        inplace=True)

df1 = df.iloc[43197:].reset_index(drop=True)
# Count values before interpolation
print("Zeros before :", (df1["HARD_C"] == 0).sum())
print("NaNs before  :", df1["HARD_C"].isna().sum())

# Replacing zeros with NaN
df1["HARD_C"] = df1["HARD_C"].replace(0, np.nan)

# Performing linear interpolation
df1["HARD_C"] = df1["HARD_C"].interpolate(
    method="linear",
    limit_direction="both"
)
print(df1.head(20))
df1.to_csv(
    r"C:\Users\ANKAN KANRAR\Desktop\ISRO BAH\SFP\SolarFlareDetection\FeatureEngineering\Updated_data.csv",
    index=False
)