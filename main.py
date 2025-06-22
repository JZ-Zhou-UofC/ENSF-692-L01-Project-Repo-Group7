# ENSF 692 Project by Group 7: John Zhou & Jack Shenfield

from cli import run_cli
from data_processing import *

if __name__ == "__main__":
    df = create_dataframe()
    df = create_multi_indexing(df)
    df = adding_average_monthly_wage_column(df)
    df = adding_net_migration_column(df)

    run_cli(df)
