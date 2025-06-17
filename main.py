from cli import run_cli
from data_processing import *
if __name__ == "__main__":
    df=create_dataframe()
    df=create_multi_indexing(df)
    df=adding_average_monthly_wage_column(df)
    run_cli(df)
