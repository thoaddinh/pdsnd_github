import time
import pandas as pd
import numpy as np

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york": "new_york_city.csv",
    "washington": "washington.csv",
}

months = [
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "all",
        ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Add comment 
    """
    print("-" * 40)
    print("Hello! Let's explore some US bikeshare data!")

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input(
            "\nWould you like to see data for Chicago, New York, or Washington: \n"
        ).lower()
        if city in CITY_DATA:
            filters = [1, 2, 0]
            month = "all"
            day = "all"
            while True:
                filterType = int(
                    input(
                        "\nWould you like to filter the data by month(1), day(2) or both(0): \n"
                    )
                )
                if filterType in filters:
                    break

            # TO DO: get user input for month (all, january, february, ... , june)

            if filterType == 0 or filterType == 1:
                while True:
                    month = input(
                        "\nWhich month? - January, February, March, April, May, June or all: \n"
                    ).lower()
                    if month in months:
                        break

            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

            if filterType == 0 or filterType == 2:
                days = [
                    "monday",
                    "tuesday",
                    "wednesday",
                    "thursday",
                    "friday",
                    "saturday",
                    "sunday",
                    "all",
                ]
                while True:
                    day = input(
                        "\nWhich day? - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all: "
                    ).lower()
                    if day in days:
                        break

            return (city, month, day)


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime

    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns

    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    # filter by month if applicable

    if month != "all":

        # use the index of the months list to get the corresponding int
        
        month = months.index(month) + 1

        # filter by month to create the new dataframe

        df = df[df["month"] == month]

    # filter by day of week if applicable

    if day != "all":

        # filter by day of week to create the new dataframe

        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print("-" * 40)
    print("\nCalculating The Most Frequent Times of Travel...\n")

    start_time = time.time()

    # TO DO: display the most common month

    commonMonth = df["month"].mode()[0]

    print("The most common month: ", commonMonth)

    # TO DO: display the most common day of week

    commonDoW = df["day_of_week"].mode()[0]

    print("The most common day of week: ", commonDoW)

    # TO DO: display the most common start hour

    df["hour"] = df["Start Time"].dt.hour
    commonHour = df["hour"].mode()[0]

    print("The most common start time: ", commonHour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # TO DO: display most commonly used start station

    commonStartStation = df["Start Station"].mode()[0]

    print("The most commonly used start station: ", commonStartStation)

    # TO DO: display most commonly used end station

    commonEndStation = df["End Station"].mode()[0]

    print("The most commonly used end station: ", commonEndStation)

    # TO DO: display most frequent combination of start station and end station trip

    commonTrip = (df["Start Station"] + " AND " + df["End Station"]).mode()[0]

    print("The most frequent combination of start station and end station trip: ", commonTrip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df["Trip Duration"].sum()
    print("Total travel time", total_duration)

    # TO DO: display mean travel time
    average_trip_duration = df["Trip Duration"].mean()
    print("Mean travel time", average_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of user types

    userTypeCounts = df["User Type"].value_counts() 

    print("\nCounts of user types: \n", userTypeCounts)

    if city == "washington":
        print("\nNo data gender to share!\n")
    else:
        # TO DO: Display counts of gender

        genderCounts = df["Gender"].value_counts()

        print("\nCounts of gender: \n", genderCounts)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliestYob = int(df["Birth Year"].max())

        print("\nErliest year of birth:", earliestYob)

        mostRecentYob = int(df["Birth Year"].min())

        print("Most recent year of birth: ", mostRecentYob)

        mostCommonYob = int(df["Birth Year"].mode()[0])

        print("Most common year of birth: ", mostCommonYob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)

def view_data(df):
    """ Display raw data by the user requet"""
    
    viewData = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    
    #TO DO: Display raw data
    
    start_loc = 0

    while viewData == "yes":
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        viewData = input("Do you wish to continue?: ").lower()

        
def main():
    while True:

        city, month, day = get_filters()

        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        view_data(df)
        
        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()

    
