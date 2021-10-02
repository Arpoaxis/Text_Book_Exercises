milesDriven = float(input("What is your total miles driven? "))
gasUsed = float(input("How much gas have you used? "))

print("Total miles per gallon is: ", format((milesDriven/gasUsed), '.2f'), "mpg", sep='')