day_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

def is_leap_year (year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
def get_days_in_month (month, year):
    days = 0

    if (month in(9,4,6,11)):
        days = 30
    elif (month in (1, 3, 5, 7, 8, 10, 12)):
        days = 31
    elif month == 2:
        if (is_leap_year(year)):
            days = 29
        else:
            days = 28
    else:
        print ("Bad month!", month)

    return days
def GetDaysInMonths(start, end , year):
    total = 0

    for i in range(start, end, 1):
        total +=GetDaysInMonths(i, year)
def GetDaysInYears(start, end):
    total = 0
    for i in range(start, end, 1):
        if is_leap_year(i):
            total += 366
        else:
            total += 365

        return total
    
def get_day_in_week (day, month, year):
    elapsed = get_days_in_years(1004,year)
    elapsed += get_days_in_month(1004, month, year)
    elapsed += day - 1

    day_of_week = elapsed%7

    return DAY_OF_WEEK[day_of_week]

def main():
    year = int(input("Year?"))
    month = int(input("Month?"))
    day = int(input("Day?"))

    print(get_day_in_week(day, month, year))

main()
