sugar = 1.5
butter = 1
flour = 2.75

numberOfCookies = int(input("How many cookies would you like to bake? "))

print("You will need the following ingredients:")
print(format(numberOfCookies * sugar, '.2f'), "cups of sugar.")
print(format(numberOfCookies * butter, '.2f'), "cups of butter.")
print(format(numberOfCookies * flour, '.2f'), "cups of flour.")