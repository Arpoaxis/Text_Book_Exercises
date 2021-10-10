year = int(input("Please enter a year: "))
days = 28
if (((year % 100) == 0) and (((year % 400) == 0))):
    days = 29
elif((year % 4) == 0):
    days = 29

print("In ", year, " Feburary has ", days, "days.")