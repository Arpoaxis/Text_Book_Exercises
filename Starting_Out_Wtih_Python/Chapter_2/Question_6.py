stateSalesTaxRate = .05
countySalesTaxRate = .025

purchaseAmount = float(input("What is the pruchase amount? $"))

stateTaxAmount = purchaseAmount * stateSalesTaxRate
countyTaxAmount = purchaseAmount * countySalesTaxRate
totalTaxAmount = stateTaxAmount + countyTaxAmount

print("Purchase amount \t $", format(purchaseAmount, '10,.2f'))
print("State sales tax \t $", format(stateTaxAmount, '10,.2f'))
print("County sales tax \t $", format(countyTaxAmount, '10,.2f'))
print("Total sales tax \t $", format(totalTaxAmount, '10,.2f'))
print("Total sale amount \t $", format((purchaseAmount + totalTaxAmount), '10,.2f'))