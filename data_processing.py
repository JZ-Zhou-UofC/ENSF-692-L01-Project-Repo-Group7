import pandas as pd

excel_files = [
    './data/cleaned_consumer_price_index_data.xlsx',
    './data/cleaned_employment_data.xlsx',
    './data/cleaned_housing_index_data.xlsx',
    './data/cleaned_interprovincial_migration_data.xlsx',
    './data/cleaned_wage_data.xlsx'

]
def load_data(file_path):
    print(f"Loading data from {file_path}...")
    df = pd.read_csv(file_path)
    return df

def process_data(df):
    print("Processing data...")
    # Example processing: remove nulls, reset index
    df = df.dropna().reset_index(drop=True)
    return df

def creating_dataframe():
    merged_df = None
    for file in excel_files:
        df = pd.read_excel(file)
    
        if merged_df is None:
            merged_df = df
        else:
            merged_df = pd.merge(merged_df, df, on=["REF_DATE", "GEO"], how="outer", suffixes=('', '_dup'))
    merged_df.to_excel("./data/merged_data_frame.xlsx", index=False)
    return merged_df