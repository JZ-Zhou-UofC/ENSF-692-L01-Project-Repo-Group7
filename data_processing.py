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


def create_graph_to_compare(
    df, province, main_column, sub_column, time_period_1, time_period_2
):
    # TODO figure out the graph name etc.
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
    title = "Net-Migration Trends"
    main_column = "Migration"
    sub_column = "Net-migrants"
    filtered = df[df.index.get_level_values("GEO").isin(PROVINCE_OF_INTEREST)]
    filtered = filtered[[(main_column, sub_column)]]

    plot_to_prove_trends_in_province_of_interest(
        filtered, PROVINCE_OF_INTEREST, title, main_column, sub_column
    )


def net_migrants_aggregation(df):
    title = "Net-Migration Trends"
    main_column = "Migration"
    sub_column = "Net-migrants"
    filtered = df[df.index.get_level_values("GEO").isin(PROVINCE_OF_INTEREST)]
    filtered = filtered[[(main_column, sub_column)]]

    plot_sum_of_net_migrants(filtered, PROVINCE_OF_INTEREST)


def proving_housing_price_trend(df):
    title = "Housing Index Trends (2005 national average index=100)"
    main_column = "Housing"
    sub_column = "Housing Index"
    filtered = df[df.index.get_level_values("GEO").isin(PROVINCE_OF_INTEREST)]
    filtered = filtered[[(main_column, sub_column)]]
    plot_to_prove_trends_in_province_of_interest(
        filtered, PROVINCE_OF_INTEREST, title, main_column, sub_column
    )


def housing_net_migration_correlation_coefficient_post_covid(df):

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
