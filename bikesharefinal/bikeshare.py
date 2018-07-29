import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

print('Hello! Let\'s explore some US bikeshare data!')

def get_city():
        print("Enter the city whose Bikeshare Data you want to explore. Enter cities as listed only.");
        print("\n")
        city=input("\n 1. Chicago\n 2. New York\n 3. Washington\n 4. Quit.\n Enter full names only for cities.\n").title()
        while city!="":
            if city=="Chicago":
                    return chicago()
            elif city=="New York":
                    return newyork()
            elif city=="Washington":
                     return washington()
            elif city=="Quit": 
                    print("Thanks for stopping by and exiting the program, glad to have you onboard. Until next time, we see you again.")
                    exit()
            else:
                    print("Invalid choice, Please Choose Cities From List Provided. Start over please.")
                    return get_city()
          
def chicago():
        print("You have selected Chicago\n")
        return ("chicago.csv")
        
def newyork():
        print("You have selected New York\n")
        return ("new_york_city.csv")
        
def washington():
        print("You have selected Washington\n")
        return ("washington.csv")
       
    # get user input for month (all, january, february, ... , june)
def get_month():
        print('Enter the month whose Bikeshare Data You Want to Explore for - January, February, March, April, May, or June?. Please select months from the list mentioned specifically. Type "all" for ALL months')
        month=input(">>>").title()
        if month == 'January':
                    print("You selected {} to analyze.".format(month))
                    return 1 
        elif month == 'February':
                    print("You selected {} to analyze.".format(month))
                    return 2      
        elif month == 'March':
                    print("You selected {} to analyze.".format(month))
                    return 3             
        elif month == 'April':
                    print("You selected {} to analyze.".format(month))
                    return 4            
        elif month == 'May':
                    print("You selected {} to analyze.".format(month))
                    return 5
        elif month == 'June':
                    print("You selected {} to analyze.".format(month))
                    return 6
        elif month =='All':
                    print("You have selected {} months for computational evaluation".format(month))
                    return 'All'
        else:
                print("\nI'm sorry, I'm not sure which month you're trying to filter by. Let's try again. No numeric values for months please.")
                get_month()
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
def get_day():
        day = input('\nWhich day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? Type "all" for ALL days.\n').title()
        if day == 'Monday':
                print("You selected {} to analyze.".format(day))
                return 'Monday'
        elif day == 'Tuesday':
                print("You selected {} to analyze.".format(day))
                return 'Tuesday'
        elif day == 'Wednesday':
                print("You selected {} to analyze.".format(day))
                return 'Wednesday'
        elif day == 'Thursday':
                print("You selected {} to analyze.".format(day))
                return 'Thursday'
        elif day == 'Friday':
                print("You selected {} to analyze.".format(day))
                return 'Friday'
        elif day == 'Saturday':
                print("You selected {} to analyze.".format(day))
                return 'Saturday'
        elif day == 'Sunday':
                print("You selected {} to analyze.".format(day))
                return 'Sunday'
        elif day =='All':
                print("You have selected {} days for computational evaluation".format(day))
                return 'All'
        else:
                print("\nI'm sorry, I'm not sure which day of the week you're trying to filter by. Let's try again. No numeric values for days please.")
                return get_day()

   
def get_timefilters():
    '''Asks the user for a time period and returns the specified filter.
    Args:
        none.
    Returns:
        (list) with two str values:
            First value: the type of filter period (i.e. month, day or none)
            Second value: the specific filter period (e.g. March, Tuesday)
    '''
    time_filter = input('\nWould you like to filter the data by month, day. For only month as filter, "type month or m". For only day as filter, "type day or d". Type "none" for no time filter at all. \n').lower()
    if time_filter == 'month' or time_filter == 'm':
                return ['month', get_month()]
    elif time_filter == 'day' or time_filter == 'd':
               return ['day', get_day()]
    elif time_filter == 'none' or time_filter == 'n':
                print("You have selected no filter for month and day. Computation would be made taking both the month and date values for all times.")
                return ['none', 'no filter']
    else:
                print("\nI'm sorry, I'm not sure which time period you're trying to filter by. Let's try again.")
                return get_timefilters()
    

def load_data():

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df1=pd.read_csv(get_city())
    return df1

def month_stats(modified_df):
    """Displays statistics on the most frequent times of travel."""
    print("\nCalculating the time statistics.....\n")

    # display the most common month
    start_time = time.time()
    print("\nCalculating the most common month.....\n")
    popular_month = modified_df['Start Time'].dt.month.mode()[0]
    print('Most Common Month:{}'.format(popular_month))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def day_stats(modified_df):
    # display the most common day of week
    start_time = time.time()
    print("\nCalculating the most common day of the week.....\n")
    popular_day = modified_df['Start Time'].dt.strftime('%w').mode()[0]
    print('Most Common Day:{}'.format(popular_day))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def time_stats(modified_df):
    # display the most common start hour
    start_time = time.time()
    print("\nCalculating the most common start hour.....\n")
    modified_df['hour'] = modified_df['Start Time'].dt.hour
    popular_hour = modified_df['hour'].mode()[0]
    print('Most Common Start Hour:{}'.format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(modified_df):
    """Displays statistics on the most popular stations and trip."""
    print("Calculating the station stats.........")
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    print("\nCalculating the most commonly used station.....\n")
    commonly_used_Start_station=modified_df['Start Station'].mode()[0]
    print('Most commonly used Start Station:{}'.format(commonly_used_Start_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    # display most commonly used end station
    start_time = time.time()
    print("\nCalculating the most common end station....\n")
    commonly_used_End_station=modified_df['End Station'].mode()[0]
    print('Most commonly used End Station:{}'.format(commonly_used_End_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    # display most frequent combination of start station and end station trip
    start_time = time.time()
    print("\nCalculating the most common combination of start and end station....\n")
    modified_df['start-end_StationInfo'] = modified_df['Start Station'].str.cat(modified_df['End Station'], sep=' to ')
    frequent_combo=modified_df['start-end_StationInfo'].mode()[0]
    print('Most frequent combination of start station and end station trip:{} '.format(frequent_combo))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(modified_df):
    """Displays statistics on the total and average trip duration."""
    print("\nCalculating the trip duration stats.........\n")
    print('\nThere you have the results...\n')
    start_time = time.time()
    # display total travel time
    print("\nCalculating the total travel time.....\n")
    sum_total_trip=modified_df['Trip Duration'].sum()
    print("Total Travel Time:",sum_total_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    # display mean travel time
    start_time = time.time()
    print("\nCalculating the mean or average travel time.....\n")
    mean_total_trip=modified_df['Trip Duration'].mean()
    print("Average Travel Time:",mean_total_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("\nLet\'s do the trip_duration in Hours, Minutes and Seconds\n")
    m, s = divmod(sum_total_trip, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)
    sum_total_trip= "\nTotal trip duration: %d years %02d days %02d hrs %02d min %02d sec" % (y, d, h, m, s)
    print("Total Travel Time:",sum_total_trip)
    m, s = divmod(mean_total_trip, 60)
    h, m = divmod(m, 60)
    mean_total_trip = "Average trip duration: %d hrs %02d min %02d sec" % (h, m, s)
    print("Average Travel Time:",mean_total_trip)

def user_stats(modified_df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    print('\nCalculating User Type Count...\n')
    start_time = time.time()
    # Display counts of user types
    user_type_totalcount=modified_df['User Type'].value_counts()
    print("Count of User Types:", user_type_totalcount)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def gender_stats(modified_df):
    # Display counts of gender
    start_time = time.time()
    if 'Gender' in modified_df:
        gender_type_totalcount=modified_df['Gender'].value_counts()
        print("Count of User Types:", gender_type_totalcount)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
def birthyear_stats(modified_df):
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in modified_df:
         print("\nCalculating the stats based on birth year\n")
         start_time = time.time()
         print("\nCalculating the most earliest birth year\n")
         most_earliest_year=modified_df['Birth Year'].min()
         print('Most Earliest birth year:{}'.format(most_earliest_year))
         print("\nThis took %s seconds." % (time.time() - start_time))
         print('-'*40)
         start_time = time.time()
         print("\nCalculating the most recent birth year\n")
         most_recent_year=modified_df['Birth Year'].max()
         print('Most Recent birth year:{}'.format(most_recent_year))
         print("\nThis took %s seconds." % (time.time() - start_time))
         print('-'*40)
         start_time = time.time()
         print("\nCalculating the most frequent birth year\n")
         most_frequent_year=modified_df['Birth Year'].mode()[0]
         print('Most Frequent Birth Year:{}'.format(most_frequent_year))
         print("\nThis took %s seconds." % (time.time() - start_time))
         print('-'*40)


def individual_data(modified_df,control_onfirstline):
    choice=input(" \n You are heading to compute individual data. Sure, you want to give it a try? Enter yes and no, we will proceed then.\n").lower()
    if choice=='yes':
        print(modified_df.iloc[control_onfirstline:control_onfirstline+5]) #. Displaying the initial 5 lines of the dataframe. Using iloc, we point to the first row in the dataframe and prints the first 5 lines.
        control_onfirstline=control_onfirstline+5
        return individual_data(modified_df,control_onfirstline)             
    elif choice=='no':
         print("You have opted not to go for individual data evaluation")
         restarting()
    else:
        print("We are not sure what exactly are you meaning to do. Let's start again.")
        individual_data(modified_df,0)

def main():     
    while True:
        df=load_data()
        time_filters(df)
        print("Thanks for stopping by. Hope the numbers amazed you.")
        exit()
    
def time_filters(df):
   
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    print(df['day_of_week'])


 
# Filter by time period that the user specifies (month, day, none)
    select_filters = get_timefilters()
    filter_period_type=select_filters[0]
    filter_period_value=select_filters[1]

        
    if filter_period_type == 'none':
            modified_df = df
            # Popular Month,Day,Hour of the Day - Please note I am calling the same functions with the modified dataframe based on the filters chosen by the user into the functions that I have defined in the later sections. 
            month_stats(modified_df)
            day_stats(modified_df)
            time_stats(modified_df)
             # Station Start and End Points Traffic Assessment- Please note calling the station_stats functions here, by passing the modified_df as the parameter into it. Scroll down for function body defination.
            station_stats(modified_df)
            # Trip Duration Specifics - Please note calling the station_stats functions here, by passing the modified_df as the parameter into it. Scroll down for function body defination.
            trip_duration_stats(modified_df)
            # User Statistics -  Please note calling the user_stats functions here, by passing the modified_df as the parameter into it. Scroll down for function body defination.
            user_stats(modified_df)
            if 'Gender' in modified_df: # Plese note only chicago and NY have gender and Birth Year columns. Hence, the condition.
                gender_stats(modified_df)
            if 'Birth Year' in modified_df:
                birthyear_stats(modified_df)
            individual_data(modified_df,0)
    elif filter_period_type=='month':
            if filter_period_value=='All':
                modified_df=df
                month_stats(modified_df)
                day_stats(modified_df)
                time_stats(modified_df)
                station_stats(modified_df)
                trip_duration_stats(modified_df)
                user_stats(modified_df)
                if 'Gender' in modified_df: # Plese note only chicago and NY have gender and Birth Year columns. Hence, the condition.
                    gender_stats(modified_df)
                if 'Birth Year' in modified_df:
                    birthyear_stats(modified_df)
                individual_data(modified_df,0)
            else:
                    modified_df = df.loc[df['month']==filter_period_value]
                   
                    # Popular Month,Day,Hour of the Day - Please note I am calling the same functions with the modified dataframe based on the filters chosen by the user into the functions that I have defined in the later sections. 
                    month_stats(modified_df)
                    day_stats(modified_df)
                    time_stats(modified_df)
                     # Station Start and End Points Traffic Assessment- Please note calling the station_stats functions here, by passing the modified_df as the parameter into it. Scroll down for function body defination.
                    station_stats(modified_df)
                    # Trip Duration Specifics - Please note calling the station_stats functions here, by passing the modified_df as the parameter into it. Scroll down for function body defination.
                    trip_duration_stats(modified_df)
                    # User Statistics -  Please note calling the user_stats functions here, by passing the modified_df as the parameter into it. Scroll down for function body defination.
                    user_stats(modified_df)
                    if 'Gender' in modified_df: # Plese note only chicago and NY have gender and Birth Year columns. Hence, the condition.
                        gender_stats(modified_df)
                    if 'Birth Year' in modified_df:
                        birthyear_stats(modified_df)
                    individual_data(modified_df,0)
    elif filter_period_type=='day':
        if filter_period_value=='All':
            modified_df=df
            time_stats(modified_df)
            station_stats(modified_df)
            trip_duration_stats(modified_df)
            user_stats(modified_df)
            if 'Gender' in modified_df: # Plese note only chicago and NY have gender and Birth Year columns. Hence, the condition.
                      gender_stats(modified_df)
            if 'Birth Year' in modified_df:
                      birthyear_stats(modified_df)
            individual_data(modified_df,0)
        else:
                modified_df = df.loc[df['day_of_week']==str(filter_period_value)]
                print(modified_df)
                # Popular Month,Day,Hour of the Day - Please note I am calling the same functions with the modified dataframe based on the filters chosen by the user into the functions that I have defined in the later sections. 
                day_stats(modified_df)
                time_stats(modified_df)
                 # Station Start and End Points Traffic Assessment- Please note calling the station_stats functions here, by passing the modified_df as the parameter into it. Scroll down for function body defination.
                station_stats(modified_df)
                # Trip Duration Specifics - Please note calling the station_stats functions here, by passing the modified_df as the parameter into it. Scroll down for function body defination.
                trip_duration_stats(modified_df)
                # User Statistics -  Please note calling the user_stats functions here, by passing the modified_df as the parameter into it. Scroll down for function body defination.
                user_stats(modified_df)
                if 'Gender' in modified_df: # Plese note only chicago and NY have gender and Birth Year columns. Hence, the condition.
                    gender_stats(modified_df)
                if 'Birth Year' in modified_df:
                    birthyear_stats(modified_df)
                individual_data(modified_df,0)


def restarting():
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart =='yes':
            print("Let's get you all started up.Restarting Bikeshare analytics.")
            main()
        elif restart =='no':
            print("Thanks for stopping by. Hope the numbers amazed you.")
            exit()
        else:
            print("We are not sure what exactly you have been meaning to do. Let's start over:)")
            restarting()


if __name__ == "__main__":
	main()


