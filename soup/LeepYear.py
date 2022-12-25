# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.

year = int(input("Enter a year: "))

# if year % 4 != 0:
#     common_ = print(year, "Common year")
# elif year % 100 != 0:
#     leap_ = print(year, "Leap year")
# elif year % 400 != 0:
#     common_ = print(year, "Common year")
# else:
#     leap_ = print(year, "Leap year")

if year >= 1582:
    if year % 4 != 0:
        print(year, "Common year")
    elif year % 100 != 0:
        print(year, "Leap year")
    elif year % 400 != 0:
        print(year, "Common year")
    else:
        print(year, "Leap year")
else:
    print("Not within the Gregorian calendar period")
