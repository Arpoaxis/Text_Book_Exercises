number_of_bugs = 0
number_of_days = 5
for i in range(number_of_days):
    bugs_collected = int(input("How many bugs have you collected today? "))
    number_of_bugs += bugs_collected
print("You collected", number_of_bugs, "bugs in total.")
