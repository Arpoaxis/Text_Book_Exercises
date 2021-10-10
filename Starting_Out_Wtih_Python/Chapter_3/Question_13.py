package_weight = float(input("Whats the weight of the package in pounds? "))

if (package_weight <= 2):
    shipping = 1.50
elif(package_weight <= 6):
    shipping = 3
elif(package_weight <= 10):
    shipping = 4
else:
    shipping = 4.75

print("Total shipping cost is $", format(shipping, '.2f'), sep='')