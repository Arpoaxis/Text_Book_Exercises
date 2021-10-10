vegetarian = False
vegan = False
gluten_free = False

response = input("Is anyone in your party vegetarian? ")
if (response == "yes"):
    vegetarian = True

response = input("Is anyone in your party vegan? ")
if (response == "yes"):
    vegan = True

response = input("Is anyone in your party gluten-free? ")
if (response == "yes"):
    gluten_free = True

if not(vegetarian or vegan or gluten_free):
    print("Joe's Gourmet Burgers.")
if not(vegan):
    print("Main Street Pizza Company.")
print("Corner Cafe")
if not(vegan or gluten_free):
    print("Mama's Fine Italian")
print("The Chef's Kitchen")