speed = int(input("What is the speed of your vehicle in mph? "))
time = int(input("How many hours has it traveled? "))
print("Hour\t Distance Traveled")
print("-------------------------")
for i in range(time):
    print((i + 1), "\t\t", ((i + 1) * speed))