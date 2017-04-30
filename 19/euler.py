#!/usr/bin/python3

days_per_month = [
    31, # Jan
    28, # Feb
    31, # Mar
    30, # Apr
    31, # May
    30, # Jun
    31, # Jul
    31, # Aug
    30, # Sep
    31, # Oct
    30, # Nov
    31  # Dec
]

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False

def main():
    '''
    Guest programmer: Eric :)
    '''
    count = 0

    day_of_week = 1 # Day of week is 0..6 for Sunday to Saturday
    day_of_month = 0 # Day of month takes values in 0..days_this_month-1
    month = 0 # Months are 0..11
    year = 1900

    while year <= 2000:
        #print('day %2d, month %2d, year %d' % (day_of_month, month, year))

        if day_of_week == 0 and day_of_month == 0 and year >= 1901:
            count = count + 1

        # Increment day month year
        day_of_week = (day_of_week + 1) % 7

        days_this_month = days_per_month[month]
        if month == 1 and is_leap_year(year):
            days_this_month = 29  # 29

        day_of_month = (day_of_month + 1) % days_this_month

        if day_of_month == 0:
            month = (month + 1) % 12

            if month == 0:
                year = year + 1

    print(count)

if __name__ == '__main__':
    print('l33t program b00ting up!')
    main()
