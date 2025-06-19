from data_processing import *
from provinces import *

def run_cli(df):
    show_introduction()
    prove_article_claim(df)
    correlation_analysis(df)
    interactive_loop(df)
    show_conclusion()


def show_introduction():
    print("Welcome to the Data Analysis Project")
    print("This topic is inspired by the following article:")
    print(
        "'Seeking affordability, young families flee Canada's big cities for cheaper options' written by John Macfarlane"
    )
    print("https://ca.finance.yahoo.com/news/seeking-affordability-young-families-flee-canadas-big-cities-for-cheaper-options-192548346.html\n\n")

    print("In this project, we will use data to prove to you if the article was telling the truth.")
    print("Then we will explore/compare different data trends to find out what factors cause people to move")
    print("Lastly, we will present some interesting conclusions we found along the way\n\n")
    input("Enter any key to continue > ")
    print("\n\n")


def prove_article_claim(df):
    print("Let's get started by proving whether people are moving away from provinces with high housing prices.")
    print("Specifically, demonstrate if people are leaving British Columbia and Ontario.\n\n")
    input("Enter any key to continue > ")
    print("\n\n")

    proving_migration_trend(df)

    print("From the graph, it's evident that around 2022-06, there was a noticeable outflow of people from BC and ON, while Alberta saw a spike.")
    print("Migration trends in affordable provinces like Saskatchewan appear relatively stable.\n\n")
    input("Enter any key to continue > ")

    net_migrants_aggregation(df)
    print('The "Net Migrants by Province" bar chart supports the statement above.')
    print("Now let's see if the housing price also supports the article.\n\n")
    input("Enter any key to continue > ")

    proving_housing_price_trend(df)
    print("The graph shows declining housing price indices in Alberta and Saskatchewan pre-COVID.")
    print("However, housing prices spiked across all provinces once the pandemic began.\n\n")
    input("Enter any key to continue > ")


def correlation_analysis(df):
    print("We’ll now calculate the correlation coefficient between migration and housing index for the last 10 years.")
    print("We'll compare affordable provinces (AB, SK) to expensive ones (ON, BC).\n\n")
    input("Enter any key to continue > ")

    housing_net_migration_correlation_coefficient_post_covid(df)

    print("The correlation coefficient measures the linear relationship between two variables (range: -1 to 1).")
    print(" - 1: Perfect positive correlation")
    print(" - -1: Perfect negative correlation")
    print(" - 0: No correlation\n")

    print("The correlation coefficient is 0.816 for Alberta → strong positive correlation.")
    print("Ontario's coefficient is -0.749 → strong negative correlation.\n\n")
    input("Enter any key to continue > ")

    print("From the comparison above, the article is supported by the data, especially in Alberta and Ontario.\n\n")
    input("Enter any key to continue > ")


def interactive_loop(df):
    provinces_selected = False
    province = []

    while True:
        print("Let's explore other factors that may have caused these trends.")
        print("You can compare up to 3 provinces.")
        print('Type "exit" anytime to go to conclusion.\n')

        if not provinces_selected:
            number_of_provinces = get_number_of_provinces()
            if number_of_provinces == "exit":
                break

            province = get_province_input(number_of_provinces)
            if province == "exit":
                break

            provinces_selected = True

        main_column = get_main_column(df)
        if main_column == "exit":
            break

        sub_column = get_sub_column(df, main_column)
        if sub_column == "exit":
            break

        create_graph_to_compare(df, province, main_column, sub_column)

        print("\n\nAnything else you want to see?")
        user_wants_to_reselect = should_reselect_provinces()
        if user_wants_to_reselect == "exit":
            break

        provinces_selected = not user_wants_to_reselect


def show_conclusion():
    print("Thank you for using this CLI. Hope you found something interesting.\n\n")
    print("Here are some conclusions we found:\n")
    input("Enter any key to continue > ")
    print("\n\n")



# ======================
# User Input Helper Functions
# ======================
def get_province_input(number_of_provinces):
    province_array = []

    for i in range(number_of_provinces):
        while True:
            user_input = input(f"Enter province {i+1} (e.g., AB, ON, QC): ").strip()

            if user_input == "exit":
                return "exit"

            province_name = PROVINCE_MAP.get(user_input)

            if province_name and province_name not in province_array:
                province_array.append(province_name)
                break
            else:
                print(
                    "Invalid province code. Please try again. You can enter exit to see conclusion"
                )

    return province_array


def get_main_column(df):
    main_columns = df.columns.get_level_values(0).unique().tolist()

    while True:
        print("\nSelect a main category from the following options:")
        for i, col in enumerate(main_columns, 1):
            print(f"{i}. {col}")

        user_input = input("Enter the number of your choice (or type 'exit' to quit): ")

        if user_input.lower() == "exit":
            return "exit"

        # Check if input is a valid number
        if user_input.isdigit():
            index = int(user_input) - 1
            if 0 <= index < len(main_columns):
                return main_columns[index]

        print("Invalid input. Please enter a valid number or type 'exit'.")


def get_sub_column(df, main_column):
    # Get the sub-columns corresponding to the main column
    sub_columns = df[main_column].columns.tolist()

    # Display sub-column options for the user
    print(f"\nSub-columns under '{main_column}':")
    for idx, col in enumerate(sub_columns, 1):
        print(f"{idx}. {col}")

    # Ask the user to select a sub-column
    while True:
        user_input = input(
            f"Enter the number of the sub-category you want to choose (1-{len(sub_columns)}), or type 'exit' to quit: "
        ).strip()

        # Check if the user wants to exit
        if user_input.lower() == "exit":
            return "exit"

        # Validate that the input is a valid number
        if user_input.isdigit():
            user_input = int(user_input)

            # Validate the choice within range
            if 1 <= user_input <= len(sub_columns):
                sub_column = sub_columns[user_input - 1]
                return sub_column
            else:
                print(
                    f"Invalid choice. Please enter a number between 1 and {len(sub_columns)}."
                )
        else:
            print("Invalid input. Please enter a valid number or 'exit' to quit.")


def get_number_of_provinces():
    while True:
        # Prompt the user to enter the number of provinces
        user_input = input(
            "Enter the number of provinces you want to compare. We can have up to 3 provinces. > "
        ).strip()

        # Check if the user wants to exit
        if user_input.lower() == "exit":
            return "exit"

        # Validate if the input is a number
        if user_input.isdigit():
            number_of_provinces = int(user_input)

            # Check if the input is within the allowed range (1 to 3)
            if 1 <= number_of_provinces <= 3:
                return number_of_provinces
            else:
                print("Please enter a number between 1 and 3.")
        else:
            print("Invalid input. Please enter a valid number or type 'exit' to quit.")
def should_reselect_provinces():
    while True:
        user_input = input("Would you like to re-select provinces? (y for yes, n for no, or type 'exit' to quit): ").strip().lower()

        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        elif user_input == 'exit':
            return "exit"
        else:
            print("Invalid input. Please enter 'y', 'n', or 'exit'.")



if __name__ == "__main__":
    pass
