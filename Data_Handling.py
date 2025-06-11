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
            val = val.strip().lower() # removes whitespace, makes any letters lowercase
            multiplier = 1 # initialize multiplier to 1 
            if val.endswith('k'): # thousand
                multiplier = 1_000
                val = val[:-1]
            elif val.endswith('m'): # million
                multiplier = 1_000_000
                val = val[:-1]
            elif val.endswith('b'): # billion
                multiplier = 1_000_000_000
                val = val[:-1]
            return float(val) * multiplier # return the value multiplied by required multiplier
        elif isinstance(val, (int, float)): # if it is already numerical, leave it as is
            return val
        else:
            return np.nan # otherwise return not a number
    except Exception:
        return np.nan

# slice data into only the selected countries
# Not meant to be called directly, but just used in datacombiner()
def data_processing(excel_file, selected_countries):

    # Read data and make dataframe
    raw_data = pd.read_excel(excel_file)
    data = pd.DataFrame(raw_data)

    # Extract filename to be added to data eventually
    filename = os.path.basename(excel_file)
    data['type'] = filename

    # list comprehension for normalizing country names to lowercase
    selected_countries = [country.lower() for country in selected_countries]
    data['country'] = data['country'].str.lower()
    data = data[data['country'].isin(selected_countries)] # check if the inputted country is in the list
    
    # use convert to number function on numerical columns
    for col in data.columns:
        if col not in ['country', 'type']:
            data[col] = data[col].apply(convert_to_number)

    # null values check in dataframe. If any null values exist, return True
    null_values = False
    null_values = bool(data.isnull().values.any()) # return python boolean, not np.boolean

    # numberical values check in dataframe. If any non-numericals exsit, return True
    numerical_values = False
    for col in data.columns: # check for non-numeric values in the the columns that should be numeric
        if col not in ['country', 'type']:  # skip non-numeric columns
            converted = pd.to_numeric(data[col], errors='coerce') # Force conversion to a numeric value, coercing errors to NaN
            if converted.notnull().sum() != data[col].notnull().sum(): # Compare initial of non-nulls to converted column
                numerical_values = True
                break

    # Check if null values or numerical values were found
    if (null_values or numerical_values):
        print("There are either null values or non-numerical values in the data.")
        return data # return the data either way. It can still be used even if it is missing some values.
    else:
        return data
    
# combine the three dataframes into one larger dataframe
def data_combiner(data1, data2, data3, country_list):
    try:
        data1 = data_processing(data1, country_list)
        data2 = data_processing(data2, country_list)
        data3 = data_processing(data3, country_list)

        combined = pd.concat([data1, data2, data3], ignore_index=True)
        return combined
    
    except Exception as e:
        print(f"Error combining the data: {e}")
        return None
    

# prompts for user input and extracts the data for the country.
def extract_initial_country(dataframe):
    while True: # loops until valid input is received
        user_input = input("Please enter a country in the G20: ") # ask for input

        user_input = user_input.lower()# normalizes the input string
        data_lower = dataframe['country'].str.lower() # lowercase the breeds for comparison

        if user_input in data_lower.values:
            return(dataframe[data_lower == user_input]) # return data in dataframe where datalower is equal to userinput
        else:
            print("Country not found in G20 data. Please try again.")
            

# List of G20 countries
# Not including European Union, as it is not in the data
G20_LIST = ["Argentina", "Australia", "Brazil", "Canada", "China", "France",
            "Germany", "India", "Indonesia", "Italy", "Japan", "Mexico", "Russia",
            "Saudi Arabia", "South Africa", "South Korea", "Turkey", "United Kingdom",
            "United States"]


def main():

    dataframe = data_combiner("lex.xlsx", "gdp_pcap.xlsx", "pop.xlsx", G20_LIST)

    print(dataframe)
    print(extract_initial_country(dataframe))


if __name__ == '__main__':
    main()
