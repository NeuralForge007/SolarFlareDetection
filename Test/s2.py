from astropy.io import fits

file = r"C:\Users\ANKAN KANRAR\Desktop\ISRO BAH\SFP\SolarFlareDetection\data\raw\AL1_SLX_L1_20241003_v1.0\SDD2\AL1_SOLEXS_20241003_SDD2_L1.pi\AL1_SOLEXS_20241003_SDD2_L1.pi"

hdul = fits.open(file)

data = hdul[1].data

print(len(data["CHANNEL"][0]))
print(len(data["COUNTS"][0]))
import matplotlib.pyplot as plt

plt.plot(data["CHANNEL"][0], data["COUNTS"][0])
plt.xlabel("Channel")
plt.ylabel("Counts")
plt.title("One SoLEXS Spectrum")
plt.show()