from typing import overload


budget = float(input("How much have you budgeted for the month? $"))
more_expenses = "y"
monthly_expenses = 0
while(more_expenses == "y"):
    monthly_expenses += float(input("Please enter your next expense amount: $"))
    more_expenses = input("Do you ahave more expenses to report? (y/n) ")

budget -= monthly_expenses
over_under = "over"
if (budget < 0):
    over_under = "under"

print("You are $", format(abs(budget), ',.2f'), " ", over_under, " budget.", sep='')