number = int(input("Please enter a numnber between 0 and 36: "))
pocket = "Red"
if ((number < 0) or (number > 36)):
    print("Error: The number entered should be between 0 and 36.")
elif(number == 0):
    pocket = "Green"
elif(((number >= 1) and (number < 10)) or ((number >= 19) and (number < 28))):
    if ((number % 2) == 0):
        pocket = "Black"
elif(((number >= 11) and (number < 18)) or ((number >= 29) and (number < 36))):
    if ((number % 2) != 0):
        pocket = "Black"

print("The pocket is", pocket)