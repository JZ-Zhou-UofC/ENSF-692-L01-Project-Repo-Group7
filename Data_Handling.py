# ENSF-692 Project
# John Zhou & Jack Shenfield

# imported libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Data processing


# Takes values like 42k and converts to 42,000
# Works for thousands (k), millions (m), billions(b)
# some logic inspired by chatgpt here.
def convert_to_number(val):
    try:
        if isinstance(val, str):
            val = val.strip().lower()  # removes whitespace, makes any letters lowercase
            multiplier = 1  # initialize multiplier to 1
            if val.endswith("k"):  # thousand
                multiplier = 1_000
                val = val[:-1]
            elif val.endswith("m"):  # million
                multiplier = 1_000_000
                val = val[:-1]
            elif val.endswith("b"):  # billion
                multiplier = 1_000_000_000
                val = val[:-1]
            return (
                float(val) * multiplier
            )  # return the value multiplied by required multiplier
        elif isinstance(
            val, (int, float)
        ):  # if it is already numerical, leave it as is
            return val
        else:
            return np.nan  # otherwise return not a number
    except Exception:
        return np.nan



def data_processing(excel_file, selected_countries, value_column_name):
    raw_data = pd.read_excel(excel_file)
    data = pd.DataFrame(raw_data)

    selected_countries = [country.lower() for country in selected_countries]
    data["country"] = data["country"].str.lower()
    data = data[data["country"].isin(selected_countries)]

    # Melt to long format
    data_melted = data.melt(id_vars=["country"], var_name="year", value_name=value_column_name)
    data_melted["year"] = data_melted["year"].astype(int)
    data_melted[value_column_name] = data_melted[value_column_name].apply(convert_to_number)
    print(data_melted)

    return data_melted

# combine the three dataframes into one larger df
def data_combiner(file_column_pairs, country_list):
    merged_df = None

    for file, column_name in file_column_pairs:
        processed_df = data_processing(file, country_list, column_name)
        if merged_df is None:
            merged_df = processed_df
        else:
            merged_df = pd.merge(
                merged_df, processed_df, on=["country", "year"], how="outer"
            )

    merged_df.set_index(["country", "year"], inplace=True)
    return merged_df


# prompts for user input and extracts the data for the country.
def extract_initial_country(df):
    while True:  # loops until valid input is received
        user_input = input("Please enter a country in the G20: ")  # ask for input

        user_input = user_input.lower()  # normalizes the input string
        data_lower = df["country"].str.lower()  # lowercase the breeds for comparison

        if user_input in data_lower.values:
            return df[
                data_lower == user_input
            ]  # return data in df where datalower is equal to userinput
        else:
            print("Country not found in G20 data. Please try again.")


# List of G20 countries
# Not including European Union, as it is not in the data
G20_LIST = [
    "Argentina",
    "Australia",
    "Brazil",
    "Canada",
    "China",
    "France",
    "Germany",
    "India",
    "Indonesia",
    "Italy",
    "Japan",
    "Mexico",
    "Russia",
    "Saudi Arabia",
    "South Africa",
    "South Korea",
    "Turkey",
    "United Kingdom",
    "United States",
]


def main():
    file_column_pairs = [
        ("lex.xlsx", "LifeExpectancy"),
        ("gdp_pcap.xlsx", "GDP"),
        ("pop.xlsx", "Population"),
    ]
    df = data_combiner(file_column_pairs, G20_LIST)

    print(df)

    data_2025 = df[df.index.get_level_values('year') == 2025]
    print(data_2025)

    print(extract_initial_country(df))
if __name__ == "__main__":
    main()
