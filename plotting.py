import matplotlib.pyplot as plt


def plot_provinces_comparison(
    filtered_df, main_column, sub_column, title="plot_provinces_comparison"
):
    
    # TODO we will need to figure out how to get the correct unit for each graph
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
        index="REF_DATE", columns="GEO", values=(main_column, sub_column)
    )
    migration_pivot = migration_pivot.sort_index()

    # Pivot cross-reference data
    other_pivot = filtered_df.pivot(
        index="REF_DATE", columns="GEO", values=crossref_data
    )
    other_pivot = other_pivot.sort_index()

    plt.ion()   # this is needed to make the plot not to block cli process
    # Create subplots
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10), sharex=True)

    
    migration_pivot.plot(ax=axes[0])
    axes[0].set_title(title)
    axes[0].set_ylabel(sub_column)
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









def plot_to_prove_trends_in_province_of_interest(filtered_df, province_of_interest, title,main_column,sub_column):
    """
    Plots net migration trends in a 2x2 subplot layout:
    1. All provinces before COVID
    2. All provinces after COVID
    3. Alberta & Saskatchewan after COVID
    4. Ontario & British Columbia after COVID
    """

    # Split data
    before_covid = filtered_df[filtered_df.index.get_level_values("REF_DATE") < "2020-01"]
    after_covid = filtered_df[filtered_df.index.get_level_values("REF_DATE") >= "2020-01"]

    # Reset index
    before_covid = before_covid.reset_index()
    after_covid = after_covid.reset_index()

    # Pivot data
    pivot_before = before_covid.pivot(index="REF_DATE", columns="GEO", values=(main_column, sub_column)).sort_index()
    pivot_after = after_covid.pivot(index="REF_DATE", columns="GEO", values=(main_column, sub_column)).sort_index()

 
    plt.ion()   # this is needed to make the plot not to block cli process
    # Create subplots
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 10))
    fig.suptitle(title, fontsize=16)

    # --- Plot 1: Before COVID - All provinces ---
    pivot_before[province_of_interest].plot(ax=axes[0, 0])
    axes[0, 0].set_title("Before COVID")
    axes[0, 0].set_ylabel(sub_column)
    axes[0, 0].set_xlabel("Date")
    axes[0, 0].legend(title="Province")
    axes[0, 0].grid(True)

    # --- Plot 2: After COVID - All provinces ---
    pivot_after[province_of_interest].plot(ax=axes[0, 1])
    axes[0, 1].set_title("After COVID")
    axes[0, 1].set_ylabel(sub_column)
    axes[0, 1].set_xlabel("Date")
    axes[0, 1].legend(title="Province")
    axes[0, 1].grid(True)

    # --- Plot 3: After COVID - Alberta & Saskatchewan ---
    pivot_after[["Alberta", "Saskatchewan"]].plot(ax=axes[1, 0], color=["green", "lightgreen"])
    axes[1, 0].set_title("AB & SK (After COVID)")
    axes[1, 0].set_ylabel(sub_column)
    axes[1, 0].set_xlabel("Date")
    axes[1, 0].legend(title="Province")
    axes[1, 0].grid(True)

    # --- Plot 4: After COVID - Ontario & BC ---
    pivot_after[["Ontario", "British Columbia"]].plot(ax=axes[1, 1], color=["orange", "red"])
    axes[1, 1].set_title("ON & BC (After COVID)")
    axes[1, 1].set_ylabel(sub_column)
    axes[1, 1].set_xlabel("Date")
    axes[1, 1].legend(title="Province")
    axes[1, 1].grid(True)

    # Layout adjustment
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

if __name__ == "__main__":
    pass