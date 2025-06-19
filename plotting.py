import matplotlib.pyplot as plt
import pandas as pd

import matplotlib.pyplot as plt


def plot_housing_correlation_coefficients(correlation_results, provinces):
    values = [correlation_results[prov] for prov in provinces]

    plt.ion()  # Ensure plot is non-blocking for CLI
    plt.figure(figsize=(8, 5))

    bars = plt.bar(provinces, values, color="skyblue")

    # Add text labels above each bar
    for bar, value in zip(bars, values):
        plt.text(
            bar.get_x() + bar.get_width() / 2,  # x-position (center of bar)
            (
                value + 0.02 if value >= 0 else value - 0.05
            ),  # y-position slightly above (or below for negative)
            f"{value:.3f}",  # formatted value
            ha="center",
            va="bottom" if value >= 0 else "top",
            fontsize=9,
        )

    plt.title("Correlation Coefficients: Housing vs Net-migration (2015–2025)")
    plt.ylabel("Correlation Coefficient")
    plt.xlabel("Province")
    plt.ylim(-1, 1)
    plt.axhline(0, color="gray", linewidth=0.8)
    plt.tight_layout()
    plt.show()


def plot_sum_of_net_migrants(df, provinces):
    """
    Bar plot of net migrants by province for two periods:
    2015-01 to 2020-01, and 2020-01 to 2025-01.

    Parameters:
    - df: MultiIndex DataFrame with REF_DATE and GEO levels.
    - provinces: List of province names to include in the plot.
    """

    # Filter and sum by period
    period1 = (
        df[
            (df.index.get_level_values("REF_DATE") >= "2015-01")
            & (df.index.get_level_values("REF_DATE") < "2020-01")
            & (df.index.get_level_values("GEO").isin(provinces))
        ]
        .groupby("GEO")
        .sum()
    )

    period2 = (
        df[
            (df.index.get_level_values("REF_DATE") >= "2020-01")
            & (df.index.get_level_values("REF_DATE") < "2025-01")
            & (df.index.get_level_values("GEO").isin(provinces))
        ]
        .groupby("GEO")
        .sum()
    )

    # Create the result DataFrame
    summary_df = pd.DataFrame(
        {"2015–2020": period1.iloc[:, 0], "2020–2025": period2.iloc[:, 0]}
    ).loc[provinces]

    # Plot the bar chart
    ax = summary_df.plot(
        kind="bar",
        figsize=(10, 6),
        title="Net Migrants by Province (2015–2020 vs 2020–2025)",
    )

    # Add value labels
    for bars in ax.containers:
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height + (0.02 * height if height >= 0 else -0.05 * abs(height)),
                f"{height:,.0f}",  # format with comma, no decimals
                ha="center",
                va="bottom" if height >= 0 else "top",
                fontsize=9,
            )

    # Final touches
    plt.xlabel("Province")
    plt.ylabel("Sum of Net Migrants")
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()


def plot_provinces_comparison(
    df_period1,df_period2, main_column, sub_column,time_period_1, time_period_2
):
    title1=f"{main_column} for {sub_column} between {time_period_1[0]} to {time_period_1[1]}"
    title2=f"{main_column} for {sub_column} between {time_period_2[0]} to {time_period_2[1]}"
    # Reset index for pivoting
    df_period1 = df_period1.reset_index()
    crossref_data = (main_column, sub_column)

    # Pivot migration data
    df_period1 = df_period1.pivot(
        index="REF_DATE", columns="GEO", values=(main_column, sub_column)
    )
    df_period1 = df_period1.sort_index()

    # Pivot cross-reference data
    df_period2 = df_period2.reset_index()
    df_period2 = df_period2.pivot(
        index="REF_DATE", columns="GEO", values=crossref_data
    )
    df_period2 = df_period2.sort_index()

    plt.ion()  # this is needed to make the plot not to block cli process
    # Create subplots
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10), sharex=True)

    df_period1.plot(ax=axes[0])
    axes[0].set_title(title1)
    axes[0].set_ylabel(sub_column)
    axes[0].legend(title="Province")
    axes[0].grid(True)

    # Plot cross-reference data trend
    df_period2.plot(ax=axes[1])

    axes[1].set_title(title2)
    axes[1].set_xlabel("Date")
    axes[1].set_ylabel(sub_column)
    axes[1].legend(title="Province")
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()


def plot_to_prove_trends_in_province_of_interest(
    filtered_df, province_of_interest, title, main_column, sub_column
):
    """
    Plots net migration trends in a 2x2 subplot layout:
    1. All provinces before COVID
    2. All provinces after COVID
    3. Alberta & Saskatchewan after COVID
    4. Ontario & British Columbia after COVID
    """

    # Split data
    before_covid = filtered_df[
        filtered_df.index.get_level_values("REF_DATE") < "2020-01"
    ]
    after_covid = filtered_df[
        filtered_df.index.get_level_values("REF_DATE") >= "2020-01"
    ]

    # Reset index
    before_covid = before_covid.reset_index()
    after_covid = after_covid.reset_index()

    # Pivot data
    pivot_before = before_covid.pivot(
        index="REF_DATE", columns="GEO", values=(main_column, sub_column)
    ).sort_index()
    pivot_after = after_covid.pivot(
        index="REF_DATE", columns="GEO", values=(main_column, sub_column)
    ).sort_index()

    plt.ion()  # this is needed to make the plot not to block cli process
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
    pivot_after[["Alberta", "Saskatchewan"]].plot(
        ax=axes[1, 0], color=["green", "lightgreen"]
    )
    axes[1, 0].set_title("AB & SK (After COVID)")
    axes[1, 0].set_ylabel(sub_column)
    axes[1, 0].set_xlabel("Date")
    axes[1, 0].legend(title="Province")
    axes[1, 0].grid(True)

    # --- Plot 4: After COVID - Ontario & BC ---
    pivot_after[["Ontario", "British Columbia"]].plot(
        ax=axes[1, 1], color=["orange", "red"]
    )
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
