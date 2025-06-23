# ENSF 692 Project by Group 7: John Zhou & Jack Shenfield

from data_processing import *
from provinces import *
from datetime import datetime


def run_cli(df):
    """
    Runs all the relevant functions created in cli.py

    Args:
        df (Pandas Dataframe): Cleaned dataframe for analysis

    Returns:
        None
    """
    show_introduction(df)
    prove_article_claim(df)
    correlation_analysis(df)
    interactive_loop(df)
    show_conclusion(df)


def show_introduction(df):
    """
    Prints out a series of lines introducing our project.

    Args:
        None

    Returns:
        None
    """
    print("Welcome to the Data Analysis Project")
    print("This topic is inspired by the following article:")
    print(
        "'Seeking affordability, young families flee Canada's big cities for cheaper options' written by John Macfarlane"
    )
    print(
        "https://ca.finance.yahoo.com/news/seeking-affordability-young-families-flee-canadas-big-cities-for-cheaper-options-192548346.html\n\n"
    )

    print(
        "In this project, we will use data to either prove or disprove the thesis of the article."
    )
    print(
        "Then we will explore/compare different socioeconomic data trends to find out what factors cause people to move"
    )
    print("Lastly, we will present some interesting conclusions we found along the way")
    print("\n\n")
    print(
        "Let's get started by showing you a snippet of the merged data frame and the describe() method"
    )
    input("Enter any key to continue > ")
    print("\n\n")

    print("---------------------Print the data frame---------------------")
    print(df)
    print("\n\n")

    print("---------------------Print the data_frame.describe()---------------------")
    print(df.describe())

    print("\n\n")
    input("Enter any key to continue > ")
    print("\n\n")


def prove_article_claim(df):
    """
    Prints lines discussing the given article. Uses functions created in data_processing.py to illustrate.

    Args:
        df (Pandas Dataframe): Cleaned dataframe for analysis
    Returns:
        None
    """
    print(
        "Let's get started by proving whether people are moving away from provinces with high housing prices."
    )
    print(
        "Specifically, demonstrate if people are leaving British Columbia and Ontario.\n\n"
    )
    input("Enter any key to continue > ")
    print("\n\n")

    proving_migration_trend(df)

    print(
        "From the graph, it's evident that around 2022-06, there was a noticeable outflow of people from BC and ON, while Alberta saw a spike."
    )
    print(
        "Migration trends in affordable provinces like Saskatchewan appear relatively stable.\n\n"
    )
    input("Enter any key to continue > ")

    net_migrants_aggregation(df)
    print('The "Net Migrants by Province" bar chart supports the statement above.')
    print("Now let's see if the housing price also supports the article.\n\n")
    input("Enter any key to continue > ")

    proving_housing_price_trend(df)
    print(
        "The graph shows declining housing price indices in Alberta and Saskatchewan pre-COVID."
    )
    print(
        "However, housing prices spiked across all provinces once the pandemic began.\n\n"
    )
    input("Enter any key to continue > ")


def correlation_analysis(df):
    """
    Demonstrates correlation analysis between net-migration and chosen datasets. Calls data_processing.py functions to illustrate.

    Args:
        df (Pandas Dataframe): Cleaned dataframe for analysis

    Returns:
        None
    """
    print(
        "We’ll now calculate the correlation coefficient between migration and housing index for the last 10 years."
    )
    print("We'll compare affordable provinces (AB, SK) to expensive ones (ON, BC).\n\n")
    input("Enter any key to continue > ")

    housing_net_migration_correlation_coefficient_post_covid(df)

    print(
        "The correlation coefficient measures the linear relationship between two variables (range: -1 to 1)."
    )
    print(" - 1: Perfect positive correlation")
    print(" - -1: Perfect negative correlation")
    print(" - 0: No correlation\n")

    print(
        "The correlation coefficient is 0.816 for Alberta → strong positive correlation."
    )
    print("Ontario's coefficient is -0.749 → strong negative correlation.\n\n")
    input("Enter any key to continue > ")

    print(
        "From the comparison above, the article is supported by the data, especially in Alberta and Ontario.\n\n"
    )
    input("Enter any key to continue > ")


def interactive_loop(df):
    """
    The interactive loop to fulfill project requirements.
    Takes inputs of 1-4 provinces and a dataset.
    Illustrates some plots to demonstrate the relation of the inputs.
    Calls functions from data_processing.py.

    Args:
        df (Pandas Dataframe): Cleaned dataframe for analysis

    Returns:
        None
    """
    #Flag to check if the user wants to re-enter province and time period
    user_wants_to_reselect = True

    while True:
        print("Let's explore other factors that may have caused these trends.")
        # We choose only 4 province between we do not want the graph to get too crowded
        print("You can compare up to 4 provinces.")
        print("You can compare the trends between two different time periods.")
        print('Type "exit" anytime to go to conclusion.\n')

        if user_wants_to_reselect:
            print("\n")
            number_of_provinces = get_number_of_provinces()
            #This is used to break out of the while loop
            if number_of_provinces == "exit":
                break

            print("\n")
            province = get_province_input(number_of_provinces)
            if province == "exit":
                break

            print("\n")
            print("Choose the first time range")
            time_period_1 = get_time_period()
            if time_period_1 == "exit":
                break

            print("\n")
            print("Choose the second time range")
            time_period_2 = get_time_period()
            if time_period_2 == "exit":
                break

            user_wants_to_reselect = False

    
        main_column = get_main_column(df)
        if main_column == "exit":
            break

        sub_column = get_sub_column(df, main_column)
        if sub_column == "exit":
            break

        create_graph_to_compare(
            df, province, main_column, sub_column, time_period_1, time_period_2
        )

        print("\n\nAnything else you want to see?")
        user_wants_to_reselect = get_if_user_wants_to_reselect()
        if user_wants_to_reselect == "exit":
            break


def show_conclusion(df):
    """
    Prints conclusion statements.

    Args:
        None

    Returns:
        None
    """

    print("Thank you for using this CLI. Hope you found something interesting.\n\n")
    print("Here are something interesting we found:")
    print("\n\n")
    input("Enter any key to continue > ")
    print("\n\n")

    print(
        "By computing the correlation coefficient through all the columns in the data frame against the net-migration trend"
    )
    print(
        "We found that the average monthly wage has the highest correlation coefficient"
    )
    print(
        "As a conclusion, through data, we found Alberta is the top growing province that attracts the most interprovincial migrants"
    )
    print("The biggest reason behind such trend is the wage growth and housing prices")
    print(
        "The following is a graph that shows the categories that has a |correlation coefficient| above 0.8 which means a fairly strong positive relationship."
    )

    print("\n\n")
    input("Enter any key to continue > ")
    print("\n\n")

    find_the_max_correlation(df)

    print("\n\n")
    print("Here comes an end to our cli, press enter one last time to end")
    input("Enter any key to continue > ")
    print("\n\n")


# ======================
# User Input Helper Functions
# ======================
def get_province_input(number_of_provinces):
    """
    Takes the number of provinces inputted by the user and promts them to specify which provinces, in short form.

    Args:
        number_of_provinces (integer): Number of provinces selected by the user.

    Returns:
        province_array (list): List of provinces that have been selected, in their full name.
    """

    province_array = []

    for i in range(number_of_provinces):
        while True:
            user_input = input(f"Enter province {i+1} (e.g., AB, ON, QC)> ").strip()

            if user_input.lower() == "exit":
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
    """

    Gets the index of the main column to be analyzed.

    Args:
        df (Pandas Dataframe): Cleaned dataframe for analysis

    Returns:
        main_columns[index] (String): returns the name of the main column.
    """

    main_columns = df.columns.get_level_values(0).unique().tolist()

    while True:
        print("\nSelect a main category from the following options:")
        for i, col in enumerate(main_columns, 1):
            print(f"{i}. {col}")

        user_input = input("Enter the number of your choice (or type 'exit' to quit)> ")

        if user_input.lower() == "exit":
            return "exit"

        # Check if input is a valid number
        if user_input.isdigit():
            index = int(user_input) - 1
            if 0 <= index < len(main_columns):
                return main_columns[index]

        print("Invalid input. Please enter a valid number or type 'exit'.")


def get_sub_column(df, main_column):
    """

    Gets the index of the sub-column to be analyzed.

    Args:
        df (Pandas Dataframe): Cleaned dataframe for analysis

    Returns:
        sub_columns (String): returns the name of the sub-column.
    """

    # Get the sub-columns corresponding to the main column
    sub_columns = df[main_column].columns.tolist()

    # Display sub-column options for the user
    print(f"\nSub-columns under '{main_column}':")
    for idx, col in enumerate(sub_columns, 1):
        print(f"{idx}. {col}")

    # Ask the user to select a sub-column
    while True:
        user_input = input(
            f"Enter the number of the sub-category you want to choose (1-{len(sub_columns)}), or type 'exit' to quit> "
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
    """
    Gets the number of provinces inputted by the user and stores it.

    Args:
        None

    Returns:
        number_of_provinces (int): Number of provinces
        "exit" (String literal): return "exit" keyword if user asks for it
    """
    while True:
        # Prompt the user to enter the number of provinces
        user_input = input(
            "Enter the number of provinces you want to compare. We can have up to 4 provinces. > "
        ).strip()

        # Check if the user wants to exit
        if user_input.lower() == "exit":
            return "exit"

        # Validate if the input is a number
        if user_input.isdigit():
            number_of_provinces = int(user_input)

            # Check if the input is within the allowed range (1 to 4)
            if 1 <= number_of_provinces <= 4:
                return number_of_provinces
            else:
                print("Please enter a number between 1 and 4.")
        else:
            print("Invalid input. Please enter a valid number or type 'exit' to quit.")


def get_if_user_wants_to_reselect():
    """
    Modify the flag depending on user input

    Args:
        None

    Returns:
        True (boolean): change flag to True if user says yes
        False (boolean): change flag to False if user says no
        "exit" (String literal): return "exit" keyword if user asks for it
    """

    while True:
        user_input = (
            input(
                "Would you like to reselect provinces and time period? (y for yes, n for no, or type 'exit' to quit)> "
            )
            .strip()
            .lower()
        )

        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        elif user_input == "exit":
            return "exit"
        else:
            print("Invalid input. Please enter 'y', 'n', or 'exit'.")


def get_time_period():
    """
    Gets the start date & end date from user in YYYY-MM format, checks if they are valid, and returns them.

    Args:
        None

    Returns:
        [start_date_input, end_date_input] (list): The two dates in list format

    """

    # Function to check if the input is valid
    def is_valid_date(date_input):
        """
        Determines if inputted date is valid.

        Args:
            date_input (String): Date in YYYY-MM format

        Returns:
            True/False (boolean): Depending on if the date is valid or not
        """
        try:

            year, month = map(int, date_input.split("-"))
            # Check if the month is between 1 and 12

            if 1 <= month <= 12 and 2005 <= year <= 2025:
                return True
            else:
                return False
        except ValueError:
            return False

    # Get start date from the user and ensure it's in the correct format
    print("time range:2005-01 to 2025-01")
    while True:
        start_date_input = input("Enter the start date (YYYY-M, e.g., 2015-1) > ")
        if start_date_input.lower() == "exit":
            return "exit"
        if is_valid_date(start_date_input):
            break
        else:
            print(
                "Invalid input. Please enter the date in the format YYYY-M (e.g., 2015-1)."
            )
            print("time range:2005-01 to 2025-01")

    # Get end date from the user and ensure it's in the correct format
    while True:
        end_date_input = input("Enter the end date (YYYY-M, e.g., 2025-1) > ")
        if end_date_input.lower() == "exit":
            return "exit"
        if is_valid_date(end_date_input):
            if datetime.strptime(end_date_input, "%Y-%m") > datetime.strptime(
                start_date_input, "%Y-%m"
            ):
                break
            print("Please make sure the end date is later than the start date")
        else:
            print(
                "Invalid input. Please enter the date in the format YYYY-M (e.g., 2025-1)."
            )
            print("time range:2005-01 to 2025-01")

    # Return the array with the start and end date strings
    return [start_date_input, end_date_input]


if __name__ == "__main__":
    pass
