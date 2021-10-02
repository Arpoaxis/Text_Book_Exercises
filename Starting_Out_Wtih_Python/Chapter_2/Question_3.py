#Land Calculation

print("#3")
ACRE = 43560
landInFeet = float(input("What is the total area of land in square feet? "))
landInAcres = landInFeet / ACRE
print("The amout of land in acres is: ", format(landInAcres, ',.2f' ), "acres")