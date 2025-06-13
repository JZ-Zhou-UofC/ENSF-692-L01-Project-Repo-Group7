# Data_Scripts

# ENSF-692 Project
# John Zhou & Jack Shenfield

# imported libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

Provinces = ["British Columbia", 
             "Ontario", 
             "Prince Edward Island", 
             "Manitoba", 
             "Saskatchewan", 
             "New Brunsick", 
             "Newfoundland and Labrador", 
             "Quebec", 
             "Nova Scotia", 
             "Alberta"]

# House Index data processing

raw_data = pd.read_csv("HousingIndexData.csv")
df = pd.DataFrame(raw_data)

filtered = df[df["GEO"].isin(Provinces)]
filtered = filtered[(filtered["REF_DATE"] <= "2025-01")]
filtered = filtered[(filtered["REF_DATE"] >= "2005-01")]
filtered = filtered[["REF_DATE", "GEO", "VALUE"]]

#print(filtered)

# Consumer Price Index data processing



raw_data = pd.read_csv("ConsumerPriceIndexData.csv")

# Data file was too large to upload to github so it had to be trimmed

#raw_data_trimmed = raw_data.iloc[600000:]
#raw_data_trimmed.to_csv("ConsumerPriceIndexData_smaller.csv", index=False)
#print(raw_data_trimmed)

df = pd.DataFrame(raw_data)

filtered = df[df["GEO"].isin(Provinces)]
filtered = filtered[(filtered["REF_DATE"] <= "2025-01")]
filtered = filtered[(filtered["REF_DATE"] >= "2005-01")]
filtered = filtered[(filtered["UOM"] == "2002=100")]
filtered = filtered[(filtered["Products and product groups"] == "All-items")]
filtered = filtered[["REF_DATE", "GEO", "VALUE"]]

#print(filtered)


# Wage & Salary data processing

raw_data = pd.read_csv("WagesData.csv")
df = pd.DataFrame(raw_data)

filtered = df[df["GEO"].isin(Provinces)]
filtered = filtered[(filtered["REF_DATE"] <= "2025-01")]
filtered = filtered[(filtered["REF_DATE"] >= "2005-01")]
filtered = filtered[(filtered["Seasonal adjustment"] == "Unadjusted")]
filtered = filtered[(filtered["Sector"] == "Compensation of employees")]
filtered["VALUE"] = filtered["VALUE"] * 1000 # Values are in units of thousands of dollars
filtered = filtered[["REF_DATE", "GEO", "VALUE"]]

#print(filtered)


