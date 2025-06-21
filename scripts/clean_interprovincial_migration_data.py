# Data_Scripts

# ENSF 692 Project by Group 7: John Zhou & Jack Shenfield


import pandas as pd
from provinces import PROVINCE

# House Index data processing

# Read data
raw_data = pd.read_csv("./data/InterprovincialMigrationData.csv")
df = pd.DataFrame(raw_data)

# Preparing the data for month filing
df["VALUE"] = (df["VALUE"] / 3).round()

# Filter by province and date
filtered = df[df["GEO"].isin(PROVINCE)]
filtered = filtered[(filtered["REF_DATE"] <= "2025-01")]
filtered = filtered[(filtered["REF_DATE"] >= "2005-01")]
filtered

# Pivot to get In-migrants and Out-migrants in columns
pivoted = filtered.pivot(
    index=["REF_DATE", "GEO"], columns="Interprovincial migration", values="VALUE"
).reset_index()

# Convert REF_DATE to datetime
pivoted["REF_DATE"] = pd.to_datetime(pivoted["REF_DATE"])

# Generate full list of months
full_dates = pd.date_range(start="2005-01", end="2025-01", freq="MS")

# Create full combination of dates and provinces
provinces = pivoted["GEO"].unique()
full_index = pd.MultiIndex.from_product([full_dates, provinces], names=["REF_DATE", "GEO"])
full_df = pd.DataFrame(index=full_index).reset_index()

# Merge full data with existing pivoted data
merged = pd.merge(full_df, pivoted, on=["REF_DATE", "GEO"], how="left")

# Sort for proper forward filling
merged = merged.sort_values(by=["GEO", "REF_DATE"])

# Forward fill missing values by province
merged[["In-migrants", "Out-migrants"]] = merged.groupby("GEO")[["In-migrants", "Out-migrants"]].ffill()

# Optional: format REF_DATE back to year-month string
merged["REF_DATE"] = merged["REF_DATE"].dt.strftime('%Y-%m')

# Export cleaned data
merged.to_excel("./data/cleaned_interprovincial_migration_data.xlsx", index=False)

print(merged)
