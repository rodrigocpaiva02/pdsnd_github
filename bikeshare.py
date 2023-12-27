import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

DAY_DATA = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')

    while True: 
        city = input('Enter with the city - Chicago, New York City or Washington: ').lower()
        
        if city != 'chicago' and city != 'new york city' and city != 'washington':
            print('Invalid city! Enter with name of the city as instructed.\n')
        else:
            break

    while True: 
        month = input('Enter with month - All, January, February, ... , November, December: ').lower()
        
        if month != 'all' and month not in MONTH_DATA:
            print('Invalid month! Enter with name of the month as instructed.\n')
        else:
            break

    while True: 
        day = input('Enter with day - All, Sunday, Monday, ... , Friday, Saturday: ').lower()
        
        if day != 'all' and day not in DAY_DATA:
            print('Invalid day! Enter with name of the day as instructed.\n')
        else:
            break

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
    df = pd.read_csv(CITY_DATA[city], parse_dates=True)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour
    df['Start End Stations'] = df['Start Station'] + ' -> ' + df['End Station']

    if month != 'all':
        month = MONTH_DATA.index(month) + 1
        df = df.loc[df['Month'] == month]

    if day != 'all':
        df = df.loc[df['Day of Week'] == day.capitalize()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    # Code that optimizes time statistics...
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Display the most common month.
    print('Most common month:', MONTH_DATA[int(df['Month'].mode()[0]) - 1].capitalize() )

    #Display the most common day of week.
    print('Most common day of weeek:', df['Day of Week'].mode()[0] )

    #Display the most common start hour.
    print('Most common start hour:', df['Hour'].mode()[0] )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    # Code that optimizes station statistics...

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Display most commonly used start station.
    print('Most commonly used start station:', df['Start Station'].mode()[0] )

    #Display most commonly used end station.
    print('Most commonly used end station:', df['End Station'].mode()[0] )

    #Display most frequent combination of start station and end station trip.
    print('Most frequent combination of start and end station trip:', df['Start End Stations'].mode()[0] )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    # Code that optimizes trip duration statistics...

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Display total travel time.
    total_time = df['Trip Duration'].sum()
    total_days = int(total_time / 86400)
    total_hours = int((total_time % 86400) / 3600)
    total_minutes = int(((total_time % 86400) % 3600) / 60)
    total_seconds = int(((total_time % 86400) % 3600) % 60)
    print('Total travel time:', total_days, 'days and', total_hours, 'hours and', total_minutes, 'minutes and', total_seconds, 'seconds.')

    #Display mean travel time.
    mean_time = df['Trip Duration'].mean()
    mean_hours = int(mean_time / 3600)
    mean_minutes = int((mean_time % 3600) / 60)
    mean_seconds = int((mean_time % 3600) % 60)
    print('Mean travel time:', mean_hours, 'hours and', mean_minutes, 'minutes and', mean_seconds, 'seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types.
    print('Counts of user types:')
    print(df['User Type'].value_counts())

    if 'Gender' in df:
        #Display counts of gender.
        print('\nCounts of gender:')
        print(df['Gender'].value_counts())
    else:
        print('\nGender analysis not possible, since data is not available.')

    if 'Birth Year' in df:
        #Display earliest, most recent, and most common year of birth.
        print('\nEarliest year of birth:', int(df['Birth Year'].min()))
        print('Most recent year of birth:', int(df['Birth Year'].max()))
        print('Most common year of birth:', int(df['Birth Year'].mode()[0]))
    else:
        print('\nBirth year analysis not possible, since data is not available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def displayRawData(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no: ').lower()

    startLoc = 0
    while view_data == 'yes':
        print(df.iloc[startLoc:(startLoc+5)])
        startLoc += 5
        view_data = input('\nDo you wish to continue and see more 5 rows? Enter yes or no: ').lower()


def main():
    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        displayRawData(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
