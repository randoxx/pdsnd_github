import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
        city=input('Please enter the city of interest \n(Chicago, New York City or Washington): ').lower()
        if city in ('chicago', 'new york city', 'washington'):
            print('You have selected {}.'.format(city))
            break
        else:
             print('Invalid Selection')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Please enter the month of interest \n(All, January, February, March, April, May, June): ').lower()
        if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('You have selected {}.'.format(month)) 
            break
        else:
            print('Invalid Selection')
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Please enter the day of interest \n(All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ').lower()
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('You have selected {}.'.format(day)) 
            break
        else:
            print('Invalid Selection')

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

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month was {}.'.format(common_month))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day was {}.'.format(common_day))
          
    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common hour was {}.'.format(common_hour))
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most common start station was {}.'.format(common_start))

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most common end station was {}.'.format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['Combo Station']=df['Start Station'] +' and ' + df['End Station']
    common_combo = df['Combo Station'].mode()[0]
    print('The most common combination of stations is {}.'.format(common_combo))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is {}.'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is {}.'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts=df['User Type'].value_counts().to_frame()
    print('Counts of User Types:\n', user_counts)

    
    # TO DO: Display counts of gender
    try:
        gender_counts=df['Gender'].value_counts().to_frame()
        print('\nCounts of Gender:\n', gender_counts)
    except:
        print('\nGender information unavailable.')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year=df['Birth Year'].min()
        recent_year=df['Birth Year'].max()
        common_year=df['Birth Year'].mode()[0]
        print('\nThe earliest birth year was {}, the most recent birth year is {} and the most common birth year is {}.'.format(int(earliest_year), int(recent_year), int(common_year)))
    except:
        print('\nBirth Year information unavailable.')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_display(df):
    """Displays 5 lines of raw data at the users request."""    
    start_line=0
    end_line=5
    size=len(df.index)
    while True:
        data_request=input('Would you like to see 5 lines of raw data? (y,n) ').lower()
        if data_request == 'y' and end_line<size:
            print(df[start_line:end_line])
            start_line += 5
            end_line += 5
        elif data_request == 'y' and end_line>=size:
            print(df[start_line:size])
            print('\nEnd of file.')
            break
        elif data_request =='n':
            break
        else:
             print('Invalid Selection')
    print('-'*40)  
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_display(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()