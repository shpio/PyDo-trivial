def is_year_leap(year):
    leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    print(leap_year)
    return leap_year

def days_in_month(year, month):
    thirty = [ 4, 6, 9, 11 ]
    thirtyone = [ 1, 3, 5, 7, 8, 10, 12 ]
    leap = is_year_leap(year) == True

    if month in thirtyone:
        print(31)
        return 31
    if month in thirty:
        print(30)
        return 30
    if month == 2 and leap:
        print(29)
        return 29
    if month == 2 and not leap:
        print(28)
        return 28

def day_of_year(year, month, day):



print(day_of_year(2000, 12, 31))