import matplotlib.pyplot as plt

def plot_data(df):
    print("Plotting data...")

    # Example: plot first two columns
    plt.figure(figsize=(10,6))
    plt.plot(df[df.columns[0]], df[df.columns[1]], marker='o')
    plt.title("Sample Plot")
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.grid(True)
    plt.show()
