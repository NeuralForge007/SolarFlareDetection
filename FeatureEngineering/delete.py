import pandas as pd

df = pd.read_csv(r"C:\\Users\\ANKAN KANRAR\\Desktop\\ISRO BAH\\SFP\\SolarFlareDetection\\FeatureEngineering\\Updated_data.csv")

df.drop(columns=["MEAN_H_E_x","MEAN_H_E_y"], inplace=True)
print(df.head())
df.to_csv(r"C:\\Users\\ANKAN KANRAR\\Desktop\\ISRO BAH\\SFP\\SolarFlareDetection\\FeatureEngineering\\Updated_data.csv", index=False)