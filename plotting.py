import matplotlib.pyplot as plt

def plot_migration_trend(filtered_df, title="Out-Migration Trends"):
    """
    This function takes a filtered dataframe (MultiIndex removed),
    reshapes it using pivot, and plots the Out-Migrants trends.
    
    Parameters:
    - filtered_df: dataframe with REF_DATE, GEO, and ('Migration', 'Out-migrants') columns.
    - title: plot title (default = 'Out-Migration Trends')
    """
    
    # Reset index to flatten for pivoting
    filtered_df = filtered_df.reset_index()
    
    # Pivot table: rows = REF_DATE, columns = GEO
    pivot = filtered_df.pivot(index='REF_DATE', columns='GEO', values=('Migration', 'Out-migrants'))
    
    # Sort index just in case (ensures chronological order)
    pivot = pivot.sort_index()

    # Plotting
    pivot.plot(figsize=(10, 6))
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Out-Migrants')
    plt.legend(title='Province')
    plt.grid(True)
    plt.tight_layout()
    plt.show()