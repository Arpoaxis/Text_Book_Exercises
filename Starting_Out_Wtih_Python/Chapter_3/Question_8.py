PKHOTDOGS = 10
PKHOTDOGBUNS = 8

people_at_party = int(input("How many people will be at the party? "))
hot_dogs_each = int(input("How many hot dogs will each person eat? "))

total_hot_dogs_eaten = people_at_party * hot_dogs_each

##Hotdogs
packets_of_hotdogs = (total_hot_dogs_eaten // PKHOTDOGS)
if ((total_hot_dogs_eaten % PKHOTDOGS) > 0):
    packets_of_hotdogs += 1
extra_hotdogs = (packets_of_hotdogs * PKHOTDOGS) - total_hot_dogs_eaten

#Hotdog buns
packets_of_hotdogbuns = (total_hot_dogs_eaten // PKHOTDOGBUNS)
if ((total_hot_dogs_eaten % PKHOTDOGBUNS) > 0):
    packets_of_hotdogbuns += 1
extra_hotdogbuns = (packets_of_hotdogbuns * PKHOTDOGBUNS) - total_hot_dogs_eaten

print("You will need", packets_of_hotdogs, "packets of hotdogs.")
print("You will need", packets_of_hotdogbuns, "packets of hot dog buns.")
print("There will be", extra_hotdogs, "extra hot dogs and", extra_hotdogbuns, "extra hot dog buns.")