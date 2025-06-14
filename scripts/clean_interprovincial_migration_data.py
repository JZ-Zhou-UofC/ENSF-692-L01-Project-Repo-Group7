# Data_Scripts

# ENSF-692 Project
# John Zhou & Jack Shenfield

# imported libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from provinces import Provinces
# House Index data processing

raw_data = pd.read_csv("InterprovincialMigrationData.csv")
df = pd.DataFrame(raw_data)

filtered = df[df["GEO"].isin(Provinces)]
filtered = filtered[(filtered["REF_DATE"] <= "2025-01")]
filtered = filtered[(filtered["REF_DATE"] >= "2005-01")]

pivoted = filtered.pivot(
    index=["REF_DATE", "GEO"], columns="Interprovincial migration", values="VALUE"
)
pivoted = pivoted.reset_index()
filtered = filtered[["REF_DATE", "GEO", "VALUE","Interprovincial migration"]]

pivoted = filtered.pivot(
    index=["REF_DATE", "GEO"], columns="Interprovincial migration", values="VALUE"
)
pivoted = pivoted.reset_index()
print(pivoted)
pivoted.to_excel("cleaned_interprovincial_migration_data.xlsx", index=False)