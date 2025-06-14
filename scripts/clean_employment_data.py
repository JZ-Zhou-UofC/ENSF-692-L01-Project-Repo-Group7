# Data_Scripts

# ENSF-692 Project
# John Zhou & Jack Shenfield

# imported libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from provinces import Provinces
# House Index data processing

raw_data = pd.read_csv("./data/EmploymentData.csv")


df = pd.DataFrame(raw_data)

filtered = df[df["GEO"].isin(Provinces)]
filtered = filtered[(filtered["REF_DATE"] <= "2025-01")]
filtered = filtered[(filtered["REF_DATE"] >= "2005-01")]
filtered = filtered[(filtered["Data type"] == "Seasonally adjusted")]
filtered = filtered[(filtered["Gender"] == "Total - Gender")]
filtered = filtered[(filtered["Age group"] == "15 years and over")]
filtered = filtered[(filtered["Statistics"] == "Estimate")]

filtered = filtered[
    filtered["Labour force characteristics"].isin(
        [
            "Population",
            "Labour force",
            "Employment",
            "Unemployment",
            "Employment rate",
            "Unemployment rate",
        ]
    )
]

filtered = filtered[["REF_DATE", "GEO", "VALUE","Labour force characteristics"]]


pivoted = filtered.pivot(
    index=["REF_DATE", "GEO"], columns="Labour force characteristics", values="VALUE"
)
pivoted = pivoted.reset_index()
print(pivoted)
pivoted.to_csv("cleaned_employment_data.csv", index=False)
# filtered = filtered[(filtered["New housing price indexes"] == "Total (house and land)")]
# filtered = filtered[["REF_DATE", "GEO", "VALUE"]]
# # Setting the housing index in Jan 2005 to be the reference index
# canada_average_housing_index_jan_2005 = filtered.iloc[0:11]["VALUE"].mean()
# filtered["VALUE"] = filtered["VALUE"] / canada_average_housing_index_jan_2005 * 100

# print(filtered)
# filtered.to_excel("./data/cleaned_housing_index_data.xlsx", index=False)