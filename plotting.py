import matplotlib.pyplot as plt


def plot_two_trend_comparison(
    filtered_df, main_column, sub_column, title="Out-Migration Trends"
):
    """
    Plots a comparison between Out-Migration trends and another cross-referenced
    data trend over time, based on the selected columns.

    Parameters:
    - filtered_df: pd.DataFrame
        DataFrame with 'REF_DATE', 'GEO', ('Migration', 'Out-migrants'), and
        selected cross-reference data.
    - main_column: str
        Top-level column label of the cross-referenced data (MultiIndex).
    - sub_column: str
        Sub-level column label of the cross-referenced data (MultiIndex).
    - title: str, optional
        Title for the out-migration plot (default is 'Out-Migration Trends').
    """
    # Reset index for pivoting
    filtered_df = filtered_df.reset_index()
    crossref_data = (main_column, sub_column)

    # Pivot migration data
    migration_pivot = filtered_df.pivot(
        index="REF_DATE", columns="GEO", values=("Migration", "Out-migrants")
    )
    migration_pivot = migration_pivot.sort_index()

    # Pivot cross-reference data
    other_pivot = filtered_df.pivot(
        index="REF_DATE", columns="GEO", values=crossref_data
    )
    other_pivot = other_pivot.sort_index()

    # Create subplots
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10), sharex=True)

    # Plot Out-Migration trend
    migration_pivot.plot(ax=axes[0])
    axes[0].set_title(title)
    axes[0].set_ylabel("Out-Migrants")
    axes[0].legend(title="Province")
    axes[0].grid(True)

    # Plot cross-reference data trend
    other_pivot.plot(ax=axes[1])
    other_title = f"Trend of {main_column} - {sub_column}"
    axes[1].set_title(other_title)
    axes[1].set_xlabel("Date")
    axes[1].set_ylabel(sub_column)
    axes[1].legend(title="Province")
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()


import matplotlib.pyplot as plt


def plot_net_migration(filtered_df, province_of_interest, title="Net-Migration Trends"):
    """
    Plots net migration trends for provinces, split into two time periods:
    before and after January 2020 (COVID onset).

    Parameters:
    - filtered_df: pd.DataFrame
        DataFrame with MultiIndex including 'REF_DATE' and 'GEO',
        and a ('Migration', 'Net-migrants') column.
    - expensiv_province: list of str
        Provinces considered expensive (not directly used here, but could be for filtering).
    - inexpensive_province: list of str
        Provinces considered inexpensive (not directly used here, but could be for filtering).
    - title: str
        Overall title of the plot.
    """
    # Split data into before and after COVID
    before_covid = filtered_df[
        filtered_df.index.get_level_values("REF_DATE") < "2020-01"
    ]
    after_covid = filtered_df[
        filtered_df.index.get_level_values("REF_DATE") >= "2020-01"
    ]

    # Reset index
    before_covid = before_covid.reset_index()
    after_covid = after_covid.reset_index()

    # Pivot both sets
    pivot_before = before_covid.pivot(
        index="REF_DATE", columns="GEO", values=("Migration", "Net-migrants")
    ).sort_index()

    pivot_after = after_covid.pivot(
        index="REF_DATE", columns="GEO", values=("Migration", "Net-migrants")
    ).sort_index()


    # Plotting
    plt.ion()
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10), sharex=False)

    # Plot before COVID
    pivot_before[province_of_interest].plot(ax=axes[0])
    axes[0].set_title(f"{title} (Before COVID)")
    axes[0].set_xlabel("Date")
    axes[0].set_ylabel("Net-Migrants")
    axes[0].legend(title="Province")
    axes[0].grid(True)


    # Plot after COVID
    pivot_after[province_of_interest].plot(ax=axes[1])
    axes[1].set_title(f"{title} (After COVID)")
    axes[1].set_xlabel("Date")
    axes[1].set_ylabel("Net-Migrants")
    axes[1].legend(title="Province")
    axes[1].grid(True)


    plt.tight_layout()
    plt.show()
