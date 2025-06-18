import pandas as pd
from plotting import *
from provinces import *

excel_files = [
    "./data/cleaned_consumer_price_index_data.xlsx",
    "./data/cleaned_employment_data.xlsx",
    "./data/cleaned_housing_index_data.xlsx",
    "./data/cleaned_interprovincial_migration_data.xlsx",
    "./data/cleaned_wage_data.xlsx",
]


def create_dataframe():
    merged_df = None
    for file in excel_files:
        df = pd.read_excel(file)

        if merged_df is None:
            merged_df = df
        else:
            merged_df = pd.merge(
                merged_df,
                df,
                on=["REF_DATE", "GEO"],
                how="outer",
                suffixes=("", "_dup"),
            )
    merged_df.to_excel("./data/merged_data_frame.xlsx", index=False)
    return merged_df


def create_multi_indexing(df):
    df = df.set_index(["REF_DATE", "GEO"])
    column_tuples = [
        ("CPI", "Alcoholic beverages, tobacco products and recreational cannabis"),
        ("CPI", "All-items"),
        ("CPI", "Clothing and footwear"),
        ("CPI", "Energy"),
        ("CPI", "Food"),
        ("CPI", "Gasoline"),
        ("CPI", "Health and personal care"),
        ("CPI", "Household operations, furnishings and equipment"),
        ("CPI", "Recreation, education and reading"),
        ("CPI", "Shelter"),
        ("CPI", "Transportation"),
        ("Employment", "Employment (thousands)"),
        ("Employment", "Employment rate (%)"),
        ("Employment", "Labour force (thousands)"),
        ("Employment", "Population (thousands)"),
        ("Employment", "Unemployment (thousands)"),
        ("Employment", "Unemployment rate (%)"),
        ("Housing", "Housing Index"),
        ("Migration", "In-migrants"),
        ("Migration", "Out-migrants"),
        ("Wage", "Total Wage (thousands dollars)"),
    ]
    df.columns = pd.MultiIndex.from_tuples(column_tuples)
    print("_____________________________Multindexing____________")

    # df.to_excel("./data/multindexing.xlsx")
    # generate the excel only once to check the data
    return df


def adding_average_monthly_wage_column(df):
    df[("Wage", "Average Monthly Wage")] = (
        df[("Wage", "Total Wage (thousands dollars)")]
        / df[("Employment", "Employment (thousands)")]
    )
    return df


def adding_net_migration_column(df):
    df["Migration", "Net-migrants"] = (
        df[("Migration", "In-migrants")] - df[("Migration", "Out-migrants")]
    )
    return df


def create_graph_to_compare(df, province,main_column,sub_column):
    #TODO figure out the graph name etc.
    filtered = df[df.index.get_level_values("GEO").isin(province)]
    filtered = filtered[[(main_column, sub_column)]]
 
    plot_provinces_comparison(
        filtered, main_column, sub_column, title="Out-Migration Trends"
    )



def proving_migration_trend(df):
    title="Net-Migration Trends"
    main_column="Migration"
    sub_column="Net-migrants"
    filtered = df[df.index.get_level_values("GEO").isin(PROVINCE_OF_INTEREST)]
    filtered = filtered[[(main_column, sub_column)]]

    plot_to_prove_trends_in_province_of_interest(filtered, PROVINCE_OF_INTEREST,title,main_column,sub_column)

def proving_housing_price_trend(df):
    title="Housing Index Trends (2005 national average index=100)"
    main_column="Housing"
    sub_column="Housing Index"
    filtered = df[df.index.get_level_values("GEO").isin(PROVINCE_OF_INTEREST)]
    filtered = filtered[[(main_column, sub_column)]]
    plot_to_prove_trends_in_province_of_interest(filtered, PROVINCE_OF_INTEREST,title,main_column,sub_column)

if __name__ == "__main__":
    pass