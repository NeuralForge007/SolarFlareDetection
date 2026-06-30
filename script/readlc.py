from astropy.io import fits

file = r"C:\\Users\\Ahona Sarkar\\solex\\data\\raw\\AL1_SLX_L1_20260623_v1.0\\AL1_SLX_L1_20260623_v1.0\\SDD2\\AL1_SOLEXS_20260623_SDD2_L1.lc.gz"

hdul = fits.open(file)

print(hdul[0].header)

print(hdul["RATE"].header)