# Data_Scripts

# ENSF-692 Project
# John Zhou & Jack Shenfield

# imported libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from provinces import Provinces
# House Index data processing

raw_data = pd.read_csv("HousingIndexData.csv")
df = pd.DataFrame(raw_data)

filtered = df[df["GEO"].isin(Provinces)]
filtered = filtered[(filtered["REF_DATE"] <= "2025-01")]
filtered = filtered[(filtered["REF_DATE"] >= "2005-01")]
filtered = filtered[(filtered["New housing price indexes"] == "Total (house and land)")]
filtered = filtered[["REF_DATE", "GEO", "VALUE"]]
# Setting the housing index in Jan 2005 to be the reference index
canada_average_housing_index_jan_2005 = filtered.iloc[0:11]["VALUE"].mean()
filtered["VALUE"] = filtered["VALUE"] / canada_average_housing_index_jan_2005 * 100

print(filtered)
filtered.to_excel("cleaned_housing_index_data.xlsx", index=False)