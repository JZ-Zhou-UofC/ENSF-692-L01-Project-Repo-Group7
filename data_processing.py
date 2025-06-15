import pandas as pd
from plotting import *
excel_files = [
    './data/cleaned_consumer_price_index_data.xlsx',
    './data/cleaned_employment_data.xlsx',
    './data/cleaned_housing_index_data.xlsx',
    './data/cleaned_interprovincial_migration_data.xlsx',
    './data/cleaned_wage_data.xlsx'

]


def create_dataframe():
    merged_df = None
    for file in excel_files:
        df = pd.read_excel(file)
    
        if merged_df is None:
            merged_df = df
        else:
            merged_df = pd.merge(merged_df, df, on=["REF_DATE", "GEO"], how="outer", suffixes=('', '_dup'))
    merged_df.to_excel("./data/merged_data_frame.xlsx", index=False)
    return merged_df

def create_multi_indexing(df):
    df = df.set_index(['REF_DATE', 'GEO'])
    column_tuples = [
    ('CPI', 'Alcoholic beverages, tobacco products and recreational cannabis'),
    ('CPI', 'All-items'),
    ('CPI', 'Clothing and footwear'),
    ('CPI', 'Energy'),
    ('CPI', 'Food'),
    ('CPI', 'Gasoline'),
    ('CPI', 'Health and personal care'),
    ('CPI', 'Household operations, furnishings and equipment'),
    ('CPI', 'Recreation, education and reading'),
    ('CPI', 'Shelter'),
    ('CPI', 'Transportation'),
    ('Employment', 'Employment (thousands)'),
    ('Employment', 'Employment rate (%)'),
    ('Employment', 'Labour force (thousands)'),
    ('Employment', 'Population (thousands)'),
    ('Employment', 'Unemployment (thousands)'),
    ('Employment', 'Unemployment rate (%)'),
    ('Housing', 'Housing Index'),
    ('Migration', 'In-migrants'),
    ('Migration', 'Out-migrants'),
    ('Wage', 'Total Wage (thousands dollars)')
]
    df.columns = pd.MultiIndex.from_tuples(column_tuples)
    print("_____________________________MUltindxing____________")
    print(df)
   
    # df.to_excel("./data/multindexing.xlsx")
    # generate the excel only once to check the data
    return df


def adding_average_monthly_wage_column(df):
   df[('Wage', 'Average Monthly Wage')] = (
    df[('Wage', 'Total Wage (thousands dollars)')]
    / df[('Employment', 'Employment (thousands)')] 
)
   return df

def create_graph_to_compare_migration_trends_for_two_province(input_province_array,df,covid_period):
    filtered = df[df.index.get_level_values('GEO').isin(input_province_array)]
    filtered = filtered[('Migration', 'Out-migrants')]
    if covid_period:
        filtered = filtered[filtered.index.get_level_values('REF_DATE') >= '2020-01']
   
    
    print(filtered)
    plot_migration_trend(filtered, title="Out-Migration Trends")
