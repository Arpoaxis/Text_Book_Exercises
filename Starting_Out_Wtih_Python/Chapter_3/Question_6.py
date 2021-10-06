#Magic Dates

day = int(input("Please enter a day in numeric form: "))
month = int(input("Please enter a month in numeric form: "))
year = int(input("Please enter a two digit year: "))

if((day * month) == year):
    print("This is a magic date!")
else:
    print("This is not a magic date.")
