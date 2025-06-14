from data_processing import load_data, process_data
from plotting import plot_data

def run_cli():
    print("Welcome to the Data Analysis Project")

    # Ask user for file name
    file_path = input("Enter the path to your data file (e.g. data/data.csv): ").strip()

    try:
        data = load_data(file_path)
        processed_data = process_data(data)
        print("Data processing complete.")

        plot_data(processed_data)
        print("Plotting complete.")

    except Exception as e:
        print(f"An error occurred: {e}")
