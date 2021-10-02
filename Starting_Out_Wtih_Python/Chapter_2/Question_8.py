tipPrecentage = 18
taxPercentage = 7

foodCost = float(input("What is the total cost of your meal? $"))

tipAmount = foodCost * (tipPrecentage / 100)
taxAmount = foodCost * (taxPercentage / 100)
total = foodCost + tipAmount + taxAmount

print("Food cost: \t$", format(foodCost, '7.2f'), sep='')
print("Tip amount: \t$", format(tipAmount, '7.2f'),sep='')
print("Tax amount: \t$", format(taxAmount, '7.2f'), sep='')
print("Total amount:\t$", format(total, '7.2f'), sep='')