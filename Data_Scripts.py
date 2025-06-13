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

print(filtered)