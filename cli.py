from data_processing import *
from scripts.provinces import *


def run_cli(df):
    """
    Introduction
    """
    print("Welcome to the Data Analysis Project")
    print("This topic is inspired by the following article:")
    print(
        "Seeking affordability, young families flee Canada's big cities for cheaper options"
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
        "Then we will explore/compare different data trend to find out what factors cause people to move"
    )
    print("Lastly, we will present some interesting conclusion we found along the way ")

    print("\n\n")

    """
    Proving
    """
    print(
        "Let's get started by proving wether people are moving away from province with high housing prices to province with low housing prices"
    )
    ## John: I'm using this as a pause to the program. This is for the user to read the content above
    input("Enter any key to continue > ")

    proving_migration_trend(df)
    ##TODO We can probably do some aggregation here. Do aggregation of sum of people moved into places before covid after covid
    print(
        "From the graph, it's evident that around 2022, there was a noticeable outflow of people from British Columbia and Ontario, while Alberta saw an increase in in-migration."
    )
    print(
        "Migration trends in more affordable provinces like Saskatchewan appear relatively stable during this period."
    )
    print("\n\n")

    input("Enter any key to continue > ")
    proving_housing_price_trend(df)
    print(
        "The graph clearly shows that the housing price index for Alberta and Saskatchewan had been declining for several years before COVID."
    )
    print(
        "However, both affordable provinces and non-affordable provinces experienced a spike in housing prices once the pandemic began."
    )
    print("\n\n")
    input("Enter any key to continue > ")
    ##TODO say something....
    print("TODO is article telling the truth?.......")

    print("\n\n")
    input("Enter any key to continue > ")
    """
    Main interaction looping
    """

    while True:
        print(
            "let's explore some interesting comparisons based on other criteria."
        )
        print("You can select up to three provinces to compare a specific criterion.")
        print(
            'You can jump to see conclusion at any time by entering "exit" in the cmd.'
        )
        print("\n\n")
        number_of_prinvince = get_number_of_provinces()
        if number_of_prinvince == "exit":
            break
        province = get_province_input(number_of_prinvince)
        if province == "exit":
            break
        main_column = get_main_column(df)
        if main_column == "exit":
            break
        sub_column = get_sub_column(df, main_column)
        if sub_column == "exit":
            break
        #TODO give the ability to select time range
        create_graph_to_compare(df, province,main_column,sub_column)
        print("\n\n")
        print(
            'Anything else you want to see?'
        )
        ##TODO We can probably do some aggregation here
    ##TODO Here is something interesting we found
    print(
        "Thank you for using this User interactive cli. Hope you found something interesting"
    )
    print("Here are something we found")
    input("Enter any key to continue > ")


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
    while True:
        user_input = input(
            "Enter a main category name (e.g., 'Migration', 'Wage', 'Employment', 'CPI', 'Housing'): "
        )

        # Check if the input matches the outer level of the MultiIndex
        if user_input in df.columns.get_level_values(0):
            return user_input
        else:
            if user_input == "exit":
                return "exit"
            print(f"'{user_input}' is not a valid top-level column. Please try again.")


def get_sub_column(df, main_column):
    # Get the sub-columns corresponding to the main column
    sub_columns = df[main_column].columns.tolist()

    # Display sub-column options for the user
    print(f"Sub-columns under '{main_column}':")
    for idx, col in enumerate(sub_columns, 1):
        print(f"{idx}. {col}")

    # Ask the user to select a sub-column
    while True:
        try:
            user_input = input(
                f"Enter the number of the sub-category you want to choose (1-{len(sub_columns)}): "
            ).strip()

            # Check if the user wants to exit
            if user_input == "exit":
                return "exit"

            # Convert user input to integer. This may cause error
            user_input = int(user_input)

            # Validate the choice
            if 1 <= user_input <= len(sub_columns):
                sub_column = sub_columns[user_input - 1]
                return sub_column
            else:
                print(
                    f"Invalid choice. Please enter a number between 1 and {len(sub_columns)}."
                )

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_number_of_provinces():
    while True:
        try:
            # Prompt the user to enter the number of provinces
            user_input = input(
                "Enter number of provinces you want to compare. We can have up to 3 provinces. > "
            ).strip()
            if user_input == "exit":
                return "exit"
            # Convert the user input to an integer
            number_of_provinces = int(user_input)

            # Check if the input is within the allowed range
            if 1 <= number_of_provinces <= 3:
                return number_of_provinces
            else:
                print("Please enter a number between 1 and 3.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    pass
