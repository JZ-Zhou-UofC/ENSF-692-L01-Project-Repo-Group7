from data_processing import create_dataframe, create_multi_indexing


def run_cli():
    print("Welcome to the Data Analysis Project")



    df=create_dataframe()
    print(df.head())
    df=create_multi_indexing(df)
    print("_____________________________CLI     MUltindxing____________")
    print(df)
