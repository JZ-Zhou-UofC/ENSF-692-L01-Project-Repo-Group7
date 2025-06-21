# ENSF 692 Project by Group 7: John Zhou & Jack Shenfield

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

    """
    Creates Pandas Dataframe from chosen data source.

    Args:
        None

    Returns:
        merged_df (Pandas Dataframe): The dataframe created from the excel file.
    """
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
    """
    Make the newly created dataframe multi-indexed, as per project requirements.

    Args:
        df (Pandas Dataframe): Cleaned dataframe for analysis

    Returns:
        df (Pandas Dataframe): The same dataframe, now multi-indexed by Date & Province.
    """
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

    """
    Calculate & add average monthly wage column to multi-indexed dataframe.

    Args:
        df (Pandas Dataframe): Cleaned dataframe for analysis

    Returns:
        df (Pandas Dataframe): The same dataframe, now with the new column.
    """

    df[("Wage", "Average Monthly Wage")] = (
        df[("Wage", "Total Wage (thousands dollars)")]
        / df[("Employment", "Employment (thousands)")]
    )
    return df


def adding_net_migration_column(df):

    """
    Calculate & add net migration column to multi-indexed dataframe.

    Args:
        df (Pandas Dataframe): Cleaned dataframe for analysis

    Returns:
        df (Pandas Dataframe): The same dataframe, now with the new column.
    """

    df["Migration", "Net-migrants"] = (
        df[("Migration", "In-migrants")] - df[("Migration", "Out-migrants")]
    )
    return df


def create_graph_to_compare(
    df, province, main_column, sub_column, time_period_1, time_period_2
):
    

    """
    Create the two separate dataframes for the two periods, column of interest, province, and plot them.

    Args:
        df (Pandas Dataframe): MultiIndex DataFrame with REF_DATE and GEO levels for plotting.
        province (String): Input province
        main_column (String): Name of the main column of interest.
        sub_column (String): Name of the sub-column of interest.
        time_period_1 (list): List of start and end time period for plot1.
        time_period_2 (list): List of start and end time period for plot2.

    Returns:
        None
    """

    filtered = df[df.index.get_level_values("GEO").isin(province)]
    filtered = filtered[[(main_column, sub_column)]]
    df_period1 = filtered[
        (filtered.index.get_level_values("REF_DATE") > time_period_1[0])
        & (filtered.index.get_level_values("REF_DATE") < time_period_1[1])
    ]

    df_period2 = filtered[
        (filtered.index.get_level_values("REF_DATE") > time_period_2[0])
        & (filtered.index.get_level_values("REF_DATE") < time_period_2[1])
    ]
    plot_provinces_comparison(
        df_period1, df_period2, main_column, sub_column, time_period_1, time_period_2
    )


def proving_migration_trend(df):

    """
    Plots migration trend.

    Args:
        df (Pandas Dataframe): MultiIndex DataFrame with REF_DATE and GEO levels for plotting.

    Returns:
        None
    """

    title = "Net-Migration Trends"
    main_column = "Migration"
    sub_column = "Net-migrants"
    filtered = df[df.index.get_level_values("GEO").isin(PROVINCE_OF_INTEREST)]
    filtered = filtered[[(main_column, sub_column)]]

    plot_to_prove_trends_in_province_of_interest(
        filtered, PROVINCE_OF_INTEREST, title, main_column, sub_column
    )


def net_migrants_aggregation(df):

    """
    Plots migration trend for aggregated data.

    Args:
        df (Pandas Dataframe): MultiIndex DataFrame with REF_DATE and GEO levels for plotting.

    Returns:
        None
    """

    title = "Net-Migration Trends"
    main_column = "Migration"
    sub_column = "Net-migrants"
    filtered = df[df.index.get_level_values("GEO").isin(PROVINCE_OF_INTEREST)]
    filtered = filtered[[(main_column, sub_column)]]

    plot_sum_of_net_migrants(filtered, PROVINCE_OF_INTEREST)


def proving_housing_price_trend(df):

    """
    Plots housing price trend.

    Args:
        df (Pandas Dataframe): MultiIndex DataFrame with REF_DATE and GEO levels for plotting.

    Returns:
        None
    """

    title = "Housing Index Trends (2005 national average index=100)"
    main_column = "Housing"
    sub_column = "Housing Index"
    filtered = df[df.index.get_level_values("GEO").isin(PROVINCE_OF_INTEREST)]
    filtered = filtered[[(main_column, sub_column)]]
    plot_to_prove_trends_in_province_of_interest(
        filtered, PROVINCE_OF_INTEREST, title, main_column, sub_column
    )


def housing_net_migration_correlation_coefficient_post_covid(df):

    """
    Plots correlation coefficients for chosen data.

    Args:
        df (Pandas Dataframe): MultiIndex DataFrame with REF_DATE and GEO levels for plotting.

    Returns:
        None
    """


    main_column = "Housing"
    sub_column = "Housing Index"
    filtered = df[df.index.get_level_values("GEO").isin(PROVINCE_OF_INTEREST)]
    filtered = filtered[filtered.index.get_level_values("REF_DATE") >= "2015-01"]

    filtered = filtered[[(main_column, sub_column), ("Migration", "Net-migrants")]]

    correlation_results = {}
    for province in PROVINCE_OF_INTEREST:

        province_data = filtered[filtered.index.get_level_values("GEO") == province]
        province_data = province_data.dropna()  # drop empty values

        x = province_data[(main_column, sub_column)]
        y = province_data[("Migration", "Net-migrants")]
        corr = x.corr(y)

        correlation_results[province] = corr
    print(correlation_results)

    plot_housing_correlation_coefficients(correlation_results, PROVINCE_OF_INTEREST)


if __name__ == "__main__":
    pass
