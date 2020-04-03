print("*****magic dates*****")
#ask user for a month, day and year
month = int(input("enter a month in numeric form: "))
day = int(input("enter a day: "))
year = int(input("enter the last two digits of a year: "))

if month * day == year:
    print("the date is magic!")
else:
    print("the date is not magic")
