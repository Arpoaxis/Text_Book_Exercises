number_of_pennies = int(input("How many pennies do you have? "))
number_of_nickels = int(input("How many nickels do you have? "))
number_of_dimes = int(input("How many dimes do you have? "))
number_of_quarters = int(input("How many quarters do you have? "))

value_nickels = number_of_nickels * 5
value_dimes = number_of_dimes * 10
value_quarters = number_of_quarters * 25

total_value = number_of_pennies + value_nickels + value_dimes + value_quarters

if (total_value < 100):
    print("Your total was less than 100")
elif (total_value > 100):
    print("Your total was more than 100")
else:
    print("WINNER!!")