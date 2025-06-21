# Data_Scripts

# ENSF 692 Project by Group 7: John Zhou & Jack Shenfield

# imported libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from provinces import PROVINCE
# House Index data processing

# Wage & Salary data processing

raw_data = pd.read_csv("./data/WagesData.csv")
df = pd.DataFrame(raw_data)

filtered = df[df["GEO"].isin(PROVINCE)]
filtered = filtered[(filtered["REF_DATE"] <= "2025-01")]
filtered = filtered[(filtered["REF_DATE"] >= "2005-01")]
filtered = filtered[(filtered["Seasonal adjustment"] == "Seasonally adjusted")]
filtered = filtered[(filtered["Sector"] == "Compensation of employees")]

filtered = filtered[["REF_DATE", "GEO", "VALUE"]]

filtered = filtered.rename(columns={"VALUE": "Total Wage in thousands dollars"})
print(filtered)

filtered.to_excel("./data/cleaned_wage_data.xlsx", index=False)
