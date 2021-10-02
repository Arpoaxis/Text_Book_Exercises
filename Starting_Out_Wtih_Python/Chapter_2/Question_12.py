numberOfShares = 2000
purchasePrice = 40
salePrice = 42.75
comission = 0.03

purchaseSubTotal = numberOfShares * purchasePrice
purchaseComission = purchaseSubTotal * comission
purchaseTotal = purchaseSubTotal + purchaseComission

saleSubTotal = numberOfShares * salePrice
saleComission = saleSubTotal * comission
saleTotal = saleSubTotal + saleComission

print("Amount paid $", format((purchaseSubTotal), '8,.2f'), sep='')
print("Purchase comission $", format((purchaseComission), '8,.2f'), sep='')
print("Amount sold $", format((saleSubTotal), '8,.2f'), sep='')
print("Sale comission $", format((saleComission), '8,.2f'), sep='')
print("Joe made $", format((saleTotal - purchaseTotal), '2,.2f'), sep='')
