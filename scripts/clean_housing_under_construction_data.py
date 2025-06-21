# Data_Scripts

# ENSF 692 Project by Group 7: John Zhou & Jack Shenfield

# imported libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from provinces import PROVINCE
# House Index data processing

raw_data = pd.read_csv("./data/HousingUnderConstructionData.csv")
df = pd.DataFrame(raw_data)

filtered = df[df["GEO"].isin(PROVINCE)]
filtered = filtered[(filtered["REF_DATE"] <= "2025-01")]
filtered = filtered[(filtered["REF_DATE"] >= "2005-01")]

filtered = filtered[["REF_DATE", "GEO", "VALUE"]]


print(filtered)
filtered.to_excel("./data/cleaned_housing_under_construction_data.xlsx", index=False)