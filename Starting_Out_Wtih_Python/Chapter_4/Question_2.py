CALORIES_BURNED_PM = 4.2
print("Time\t Calories ")
print("(min)\t  Burned")
print("-----------------")
for i in range(10, 31, 5):
    print(i, "\t", int(i * CALORIES_BURNED_PM))