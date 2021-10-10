weight = float(input("What is your weight in pounds? "))
height = float(input("What is your height in inches? "))

body_mass_index = weight * (703 / (height ** 2))

print("Your BMI is ", body_mass_index)
if(body_mass_index < 18.5):
    print("You are under weight.")
elif(body_mass_index > 25):
    print("You are over weight.")
else:
    print("You are the optmial weight.")