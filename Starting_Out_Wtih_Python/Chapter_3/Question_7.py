print("The primary colors are: \n red \n blue \n yellow")
print("Please choose two colors: ")

color1 = input("Color 1: ")
color2 = input("Color 2: ")
if((color1 != "red" and color1 != "blue" and color1 != "yellow") or (color2 != "red" and color2 != "blue" and color2 != "yellow")):
    print("Error:  The primary colors are red, yellow and blue.")
elif ((color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red")):
    print("You get purple!")
elif ((color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red")):
    print("You get orange!")
elif ((color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue")):
    print("You get green!")
