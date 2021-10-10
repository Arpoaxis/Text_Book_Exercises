PACKAGE_COST = 99

packages_bought = int(input("How many packages have you purchased? "))

if(packages_bought < 10):
    discount = 0
elif (packages_bought < 20):
    discount = 10
elif(packages_bought < 50):
    discount = 20
elif(packages_bought < 100):
    discount = 30
else:
    discount = 40

subtotal = PACKAGE_COST * packages_bought 
discount_applied = subtotal * (discount / 100)
total = subtotal - discount_applied

print("You recieve a", discount,"%")
print("Your total discount is $", format(discount_applied, ',.2f'), sep='')
print("Your total is $", format(total, '7,.2f'), sep='')