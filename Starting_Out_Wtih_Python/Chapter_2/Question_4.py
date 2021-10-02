TAXRATE = 0.07

item1 = float(input("What is the price of the first item?"))
item2 = float(input("What is the price of the second item?"))
item3 = float(input("What is the price of the third item?"))
item4 = float(input("What is the price of the fourth item?"))
item5 = float(input("What is the price of the fifth item?"))

subTotal = item1+item2+item3+item4+item5
salesTax = subTotal * TAXRATE
total = subTotal + salesTax

print("The subtotal is \t\t $", format(subTotal, '10,.2f'), sep='')
print("The sales tax is \t\t $", format(salesTax, '10,.2f'), sep='')
print("The total for your sale is \t $", format(total, '10,.2f'), sep='')
