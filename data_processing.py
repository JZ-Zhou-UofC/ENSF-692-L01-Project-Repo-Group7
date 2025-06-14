import pandas as pd

def load_data(file_path):
    print(f"Loading data from {file_path}...")
    df = pd.read_csv(file_path)
    return df

def process_data(df):
    print("Processing data...")
    # Example processing: remove nulls, reset index
    df = df.dropna().reset_index(drop=True)
    return df
