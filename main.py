# ENSF 692 Project by Group 7: John Zhou & Jack Shenfield

from cli import run_cli
from data_processing import *

if __name__ == "__main__":
    """
    Main execution block for the ENSF 692 data analysis application.

    This script performs the following steps:
    1. Loads and merges cleaned Excel datasets into a single DataFrame.
    2. Applies multi-indexing to organize the data.
    3. Adds computed columns for average monthly wage and net migration.
    4. Launches an interactive CLI for user-driven data exploration.

    Args:
        None

    Returns:
        None
    """
    df = create_dataframe()
    df = create_multi_indexing(df)
    df = adding_average_monthly_wage_column(df)
    df = adding_net_migration_column(df)

    run_cli(df)
