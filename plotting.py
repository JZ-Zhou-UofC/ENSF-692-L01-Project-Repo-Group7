import matplotlib.pyplot as plt

def plot_migration_trend(filtered_df, maincolumn, subcolumn, title="Out-Migration Trends"):
    """
    This function takes a filtered dataframe (MultiIndex removed),
    reshapes it using pivot, and plots the Out-Migrants trends against the chosen data.
    
    Parameters:
    - filtered_df: dataframe with REF_DATE, GEO, and ('Migration', 'Out-migrants') columns, and selected cross-reference columns.
    - maincolumn: head column of data to be cross referenced
    - subcolumn: specific data to be cross-referenced
    - title: plot title (default = 'Out-Migration Trends')
    """
    
    # Reset index to flatten for pivoting
    filtered_df = filtered_df.reset_index()
    crossrefdata = (maincolumn, subcolumn)

    # Pivot migration data
    migration_pivot = filtered_df.pivot(index='REF_DATE', columns='GEO', values=('Migration', 'Out-migrants'))
    migration_pivot = migration_pivot.sort_index()

    # Pivot other data
    other_pivot = filtered_df.pivot(index='REF_DATE', columns='GEO', values=crossrefdata)
    other_pivot = other_pivot.sort_index()

    # Create subplots
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10), sharex=True)

    # Plot in/out migration trend
    migration_pivot.plot(ax=axes[0])
    axes[0].set_title(title)
    axes[0].set_ylabel('Out-Migrants')
    axes[0].legend(title='Province')
    axes[0].grid(True)

    # Plot cross reference data trend
    title_other = None
    other_pivot.plot(ax=axes[1])
    if title_other is None:
        title_other = f"Trend of {crossrefdata[0]} - {crossrefdata[1]}"
    axes[1].set_title(title_other)
    axes[1].set_xlabel('Date')
    axes[1].set_ylabel(crossrefdata[1])
    axes[1].legend(title='Province')
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()