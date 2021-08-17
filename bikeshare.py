# In addition to the Udacity Intro to Python source content also reviewed
# https://pandas.pydata.org/pandas-docs
# https://www.askpython.com/python/examples/convert-seconds-hours-minutes
# GitHub repos


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# function to get filtering requirements from the user
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city =input ("\nWhat is the name of the city you'd like to analyze data for? (Enter either Chicago, New York City or Washington)\n")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Sorry we could not get the name of the city to analyze data for.  Please enter either Chicago, New York City or Washington)\n")
                

        # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month =input ("\nWhat is the name of the month you'd like to filter by? (Enter either all (to apply no filter), January, February, March, April, May, June)\n")
        month = month.lower()
        if month in ['all','january','february','march','april','may','june']:
            break
        else:
            print("Sorry we could not get the name of the month to filter by.  Please enter either all, January, February, March, April, May, June)\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)    
    while True:
        day =input ("\nWhat is the name of the day you'd like to filter by? (Enter either all (to apply no filter), Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)\n")
        day = day.lower()
        if day in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            break
        else:
            print("Sorry we could not get the name of the day to filter by.  Please enter either all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)\n")

    print('-'*40)
    return city, month, day

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

   # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':       
        # filter by day of week to create new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month from the filtered data is (1 = January, 2 = February, 3 = March, 4 = April, 5 = May, 6 = June): " + str(common_month))

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week from the filtered data is: " + (common_day_of_week))

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour from the filtered data is: " + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station from the filtered data is: " + (common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station from the filtered data is: " + (common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + " || " + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip from the filtered data is: " + str(frequent_combination))
    print(' ')
    print('-'*20)
    
    # ADDITIONAL TO DO: Display counts of all start stations
    start_stations = df['Start Station'].value_counts()
    print("Frequency of all start stations from the filtered data is: \n" + str(start_stations))
    print(' ')
    print('-'*20)
    
    # ADDITIONAL TO DO: Display counts of all end stations
    end_stations = df['End Station'].value_counts()
    print("Frequency of all end stations from the filtered data is: \n" + str(end_stations))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time in seconds from the filtered data is: " + str(total_travel_time))
    total_travel_time_hr = total_travel_time/3600
    print("The total travel time in hours from the filtered data is: " + str(total_travel_time_hr))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time from the filtered data is: " + str(mean_travel_time))
    MTT_ty_res = time.gmtime(mean_travel_time)
    MTT_res = time.strftime("%H:%M:%S",MTT_ty_res)
    print("The mean travel time converted to HH:MM:SS from the filtered data is: " + str(MTT_res))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types from the filtered data is: \n" + str(user_types))

    if city == 'chicago' or city == 'new york city':
    # TO DO: Display counts of gender - only chicago and new york city have these data
        gender = df['Gender'].value_counts()
        print("The count of user gender from the filtered data is: \n" + str(gender))
        print(' ')
        
    # TO DO: Display earliest, most recent, and most common year of birth - only chicago and new york city have these data
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print("The earliest year of birth from the filtered data is: " + str(earliest_birth))
        print("The most recent year of birth from the filtered data is: " + str(most_recent_birth))
        print("The most common year of birth from the filtered data is: " + str(most_common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(df):    
    """Displays filtered raw data five rows at a time on user request."""
    
    print(df.head())
    next_rows = 0
    while True:
        view_raw_data = input('\nWould you like to view the next five rows of filtered raw data?  Enter yes or no.\n')
        # Note additional sets of raw data records looped here if requested by user after intitial request 
        if view_raw_data.lower() != 'yes':
            return
        next_rows = next_rows + 5
        print(df.iloc[next_rows:next_rows + 5])
        
# Define main function to call previous functions
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input('\nWould you like to view the first five rows of filtered raw data?  Enter yes or no.\n')
            # Note starting with first set of raw data records here if requested
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
