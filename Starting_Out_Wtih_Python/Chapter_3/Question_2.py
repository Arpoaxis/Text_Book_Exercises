#Shape A
length_A = float(input("What is the length of shape A?"))
width_A = float(input("What is the width of shape A?"))
area_A = length_A * width_A
#Shape B
length_B = float(input("What is the length of shape B?"))
width_B = float(input("What is the width of shape B?"))
area_B = length_B * width_B

if (area_A == area_B):
    print("Both shapes have the same area.")
elif(area_A > area_B):
    print("Shape A is bigger.")
else:
    print("Shape B is bigger.")

