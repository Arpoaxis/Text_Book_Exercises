number = int(input("Please enter a number between 1 and 7: "))

if (number < 1 or number > 7):
    print("Error: Number should be between 1 and 7.")
elif number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
elif number == 7:
    print("Sunday")