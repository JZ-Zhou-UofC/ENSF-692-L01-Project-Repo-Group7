from data_processing import *

def run_cli():
    print("Welcome to the Data Analysis Project")



    df=create_dataframe()
    print(df.head())
    df=create_multi_indexing(df)
   
    df=adding_average_monthly_wage_column(df)
    print("_____________________________add column____________")
    print(df)
    
    input_province_array=["Alberta","British Columbia"]
    covid_period=True
    create_graph_to_compare_migration_trends_for_two_province(input_province_array,df,covid_period)