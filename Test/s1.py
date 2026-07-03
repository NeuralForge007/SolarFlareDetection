import os

file = r"C:\Users\ANKAN KANRAR\Desktop\ISRO BAH\SFP\SolarFlareDetection\data\raw\AL1_SLX_L1_20241003_v1.0\SDD2\AL1_SOLEXS_20241003_SDD2_L1.pi\AL1_SOLEXS_20241003_SDD2_L1.pi"

print(os.path.getsize(file))
from astropy.io import fits


hdul = fits.open(file)

hdul.info()