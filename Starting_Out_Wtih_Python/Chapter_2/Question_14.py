# Compound Intrest

deposit = float(input("How much money would you like to deposit? "))
intrest = float(input("What is the intrest rate? "))
compounded = int(input("How many times a year is the intrest applied? "))
years = float(input("How many years will the money be in the account?"))

amount = deposit * ((1 + ((intrest /100) / compounded))**(compounded * years))

print("The amount recieved after ", years, " years is $",format(amount, '9,.2f'), ".", sep='')