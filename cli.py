from data_processing import *

def run_cli(df):
    print("Welcome to the Data Analysis Project")

    print("_____________________________add column____________")
    print(df)
    # example on how to generate a graph
    # these 2 things will be acquired from the user input. this gives the user option to show different graphs
    input_province_array=["Alberta","British Columbia","Ontario"]
    covid_period=False
    create_graph_to_compare_migration_trends_for_two_province(input_province_array,df,covid_period)