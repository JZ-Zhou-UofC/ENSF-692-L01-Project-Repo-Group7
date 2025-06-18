from data_processing import *


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
    #TODO We need to think about this as we work on this
    print(
        "Then we will explore/compare different data trend to find out what factors cause people to move"
    )
    print("Lastly, we will present some interesting conclusion we found along the way ")

    print("\n\n")
    print(
        "Let's get started by proving wether people are moving away from province with high housing prices to province with low housing prices"
    )
    ## John: I'm using this as a pause to the program. This is for the user to read the content above

    input("Enter any key to continue > ")


    proving_migration_trend(df)
    print("From the graph, it's evident that around 2022, there was a noticeable outflow of people from British Columbia and Ontario, while Alberta saw an increase in in-migration.")
    print("Migration trends in more affordable provinces like Saskatchewan appear relatively stable during this period.")
    print("\n\n")
    

   
    input("Enter any key to continue > ")
    proving_housing_price_trend(df)
    print("\n\n")
    input("Enter any key to continue > ")


if __name__ == "__main__":
    pass
