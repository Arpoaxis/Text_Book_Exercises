# weight = mass * 9.8

mass = float(input("What is the mass if the object? "))

weight = mass * 9.8

print("The weight if the object is", format(weight, ',.2f'), "newtons." )
if (weight > 500):
    print("The object is too heavy.")
elif(weight < 100):
    print("The object is too light.")

