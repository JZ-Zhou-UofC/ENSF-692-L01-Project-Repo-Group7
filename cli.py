from data_processing import *

def run_cli():
    print("Welcome to the Data Analysis Project")



    df=create_dataframe()
    print(df.head())
    df=create_multi_indexing(df)
   
    df=adding_average_monthly_wage_column(df)
    print("_____________________________add column____________")
    print(df)