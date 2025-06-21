# Data_Scripts

# ENSF 692 Project by Group 7: John Zhou & Jack Shenfield

# imported libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from provinces import PROVINCE

# House Index data processing

# Consumer Price Index data processing


raw_data = pd.read_csv("./data/ConsumerPriceIndexData.csv")

# # Data file was too large to upload to github so it had to be trimmed

# raw_data_trimmed = raw_data.iloc[600000:]
# raw_data_trimmed.to_csv("ConsumerPriceIndexData.csv", index=False)
# #print(raw_data_trimmed)

df = pd.DataFrame(raw_data)
consumer_price_index_columns = [
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
filtered = df[df["GEO"].isin(PROVINCE)]
filtered = filtered[(filtered["REF_DATE"] <= "2025-01")]
filtered = filtered[(filtered["REF_DATE"] >= "2005-01")]
filtered = filtered[(filtered["UOM"] == "2002=100")]
filtered = filtered[
    filtered["Products and product groups"].isin(consumer_price_index_columns)
]
filtered = filtered[["REF_DATE", "GEO", "VALUE", "Products and product groups"]]
pivoted = filtered.pivot(
    index=["REF_DATE", "GEO"], columns="Products and product groups", values="VALUE"
)
pivoted = pivoted.reset_index()
canada_average_consumer_price_index_jan_2005 = pivoted.iloc[0:11]["All-items"].mean()
pivoted[consumer_price_index_columns] = (
    pivoted[consumer_price_index_columns] / canada_average_consumer_price_index_jan_2005 * 100
)
print(pivoted)
pivoted.to_excel("./data/cleaned_consumer_price_index_data.xlsx", index=False)
