# Data_Scripts

# ENSF-692 Project
# John Zhou & Jack Shenfield

# imported libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from provinces import Provinces
# House Index data processing

# Wage & Salary data processing

raw_data = pd.read_csv("./data/WagesData.csv")
df = pd.DataFrame(raw_data)

filtered = df[df["GEO"].isin(Provinces)]
filtered = filtered[(filtered["REF_DATE"] <= "2025-01")]
filtered = filtered[(filtered["REF_DATE"] >= "2005-01")]
filtered = filtered[(filtered["Seasonal adjustment"] == "Unadjusted")]
filtered = filtered[(filtered["Sector"] == "Compensation of employees")]
filtered["VALUE"] = (
    filtered["VALUE"] * 1000
)  # Values are in units of thousands of dollars
filtered = filtered[["REF_DATE", "GEO", "VALUE"]]

print(filtered)

filtered.to_excel("./data/cleaned_wage_data.xlsx", index=False)
