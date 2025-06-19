from data_processing import *
from provinces import *


def run_cli(df):
    # ======================
    # Introduction
    # ======================
    print("Welcome to the Data Analysis Project")
    print("This topic is inspired by the following article:")
    print(
        "'Seeking affordability, young families flee Canada's big cities for cheaper options' written by John Macfarlane"
    )
    print(
        "https://ca.finance.yahoo.com/news/seeking-affordability-young-families-flee-canadas-big-cities-for-cheaper-options-192548346.html"
    )

    print("\n\n")

    print(
        "In this project, we will use data to prove to you if the article was telling the truth."
    )
    # TODO We need to think about this as we work on this
    print(
        "Then we will explore/compare different data trends to find out what factors cause people to move"
    )
    print(
        "Lastly, we will present some interesting conclusions we found along the way "
    )

    print("\n\n")

    # ======================
    # Proving
    # ======================
    print(
        "Let's get started by proving whether people are moving away from provinces with high housing prices to province with low housing prices"
    )
    print(
        "Specifically, demonstrate if people are leaving British Columbia and Ontario, the two provinces with the largest & most expensive metropolitan areas in the country"
    )
    print("\n\n")
    input("Enter any key to continue > ")
    print("\n\n")

    proving_migration_trend(df)
    # TODO We can probably do some aggregation here. Do aggregation of sum of people moved into places before covid after covid
    print(
        "From the graph, it's evident that around 2022-06, there was a noticeable outflow of people from British Columbia and Ontario, while Alberta saw an spike in the in-flow of pleople."
    )
    print(
        "Migration trends in more affordable provinces like Saskatchewan appear relatively stable during this period."
    )
    print(
        "To print a more clear picture, let's aggregate these data from 2015-2020 and 2015-2025"
    )
    print("\n\n")
    input("Enter any key to continue > ")
    print("\n\n")
    net_migrants_aggregation(df)
    print('Seems "Net Migrants by Province" bar chart supports the statement above')
    print(
        "Now let's see if the housing price also supports the statement in the article"
    )
    print("\n\n")
    input("Enter any key to continue > ")
    print("\n\n")
    proving_housing_price_trend(df)
    print(
        "The graph clearly shows that the housing price index for Alberta and Saskatchewan had been declining for several years before COVID."
    )
    print(
        "However, both affordable provinces and non-affordable provinces experienced a spike in housing prices once the pandemic began."
    )
    print("\n\n")
    input("Enter any key to continue > ")
    print("\n\n")

    # TODO say something....
    print(
        "To demonstrate this, the correlation coefficient between migration and housing index will be calculated for each relevant province during the last 10 years."
    )
    print(
        "Alberta and Saskatchewan, with their more affordable housing, will be compared to Ontario and British Columbia."
    )
    print("\n\n")
    input("Enter any key to continue > ")
    print("\n\n")
    housing_net_migration_correlation_coefficient_post_covid(df)
    print(
        "The correlation coefficient measures the strength and direction of a linear relationship between two variables."
    )
    print("It ranges from -1 to 1:")
    print(
        " - A value of 1 means a perfect positive correlation: as one variable increases, the other increases proportionally."
    )
    print(
        " - A value of -1 means a perfect negative correlation: as one variable increases, the other decreases proportionally."
    )
    print(
        " - A value of 0 means no linear correlation: the variables do not have a predictable linear relationship."
    )
    print("\n\n")
    print(
        "The correlation coefficient is 0.819 for Alberta, which indicates a strong positive linear relationship"
    )
    print(
        "For Ontario, the correlation coefficient is -0.744, indicating a strong negative linear relationship"
    )

    print("\n\n")
    input("Enter any key to continue > ")
    print("\n\n")

    print("From the comparison above, it is evident that the article")
    print(
        "'Seeking affordability, young families flee Canada's big cities for cheaper options'"
    )
    print(
        "is supported by the data, particularly in provinces like Alberta and Ontario,"
    )
    print(
        "where significant migration trends reflect the search for more affordable living."
    )

    print("\n\n")
    input("Enter any key to continue > ")
    print("\n\n")

    # ======================
    # Main Interaction Loop
    # ======================

    provinces_selected = False  # Flag to track if provinces have been selected

    while True:
        print("Let's see what are the other factors that may have caused this trend.")
        print("You can select up to three provinces to compare a specific category.")
        print('You can jump to see the conclusion at any time by entering "exit" in the cmd.\n\n')

        if not provinces_selected:
            # Prompt for number of provinces only on first run
            number_of_provinces = get_number_of_provinces()
            if number_of_provinces == "exit":
                break
            province = get_province_input(number_of_provinces)
            if province == "exit":
                break
            provinces_selected = True  # Set the flag to indicate provinces were selected
        else:
            # If provinces were already selected, skip the province input
            print("You have already selected provinces.")
            province = "Your Selected Provinces"  # Or use previously selected provinces if needed

        # Proceed with the rest of the process
        main_column = get_main_column(df)
        if main_column == "exit":
            break
        sub_column = get_sub_column(df, main_column)
        if sub_column == "exit":
            break
        
        # TODO: Add functionality for selecting time range
        create_graph_to_compare(df, province, main_column, sub_column)
        print("\n\n")
        print("Anything else you want to see?")
        print("Anything else you want to see?")
        should_reselect_provinces = should_reselect_provinces()

        if should_reselect_provinces == "exit":
            break
        provinces_selected=not should_reselect_provinces   
        # TODO We can probably do some aggregation here

    print(
        "Thank you for using this User interactive CLI. Hope you found something interesting"
    )

    # ======================
    # Conclusion
    # ======================
    print("Here are something we found")
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
