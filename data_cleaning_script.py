# Data_Scripts

# ENSF-692 Project
# John Zhou & Jack Shenfield

# imported libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

Provinces = [
    "British Columbia",
    "Ontario",
    "Prince Edward Island",
    "Manitoba",
    "Saskatchewan",
    "New Brunswick",
    "Newfoundland and Labrador",
    "Quebec",
    "Nova Scotia",
    "Alberta",
]

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

# Consumer Price Index data processing


raw_data = pd.read_csv("ConsumerPriceIndexData.csv")

# # Data file was too large to upload to github so it had to be trimmed

# raw_data_trimmed = raw_data.iloc[600000:]
# raw_data_trimmed.to_csv("ConsumerPriceIndexData.csv", index=False)
# #print(raw_data_trimmed)

df = pd.DataFrame(raw_data)

filtered = df[df["GEO"].isin(Provinces)]
filtered = filtered[(filtered["REF_DATE"] <= "2025-01")]
filtered = filtered[(filtered["REF_DATE"] >= "2005-01")]
filtered = filtered[(filtered["UOM"] == "2002=100")]
filtered = filtered[
    filtered["Products and product groups"].isin(
        [
            "All-items",
            "Food",
            "Shelter",
            "Household operations, furnishings and equipment",
            "Transportation",
            "Gasoline",
            "Health and personal care",
            "Clothing and footwear",
            "Recreation, education and reading",
            "Alcoholic beverages, tobacco products and recreational cannabis",
            "Energy",
        ]
    )
]
filtered = filtered[["REF_DATE", "GEO", "VALUE", "Products and product groups"]]
pivoted = filtered.pivot(
    index=["REF_DATE", "GEO"], columns="Products and product groups", values="VALUE"
)
pivoted = pivoted.reset_index()
print(pivoted)
pivoted.to_excel("cleaned_consumer_price_index_data.xlsx", index=False)

# Wage & Salary data processing

raw_data = pd.read_csv("WagesData.csv")
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

filtered.to_excel("cleaned_wage_data.xlsx", index=False)
