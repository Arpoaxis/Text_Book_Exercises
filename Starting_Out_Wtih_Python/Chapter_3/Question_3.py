age = float(input("How old is the person in question? "))

if (age <= 1):
    print("The person is an infant.")
elif (age > 1 and age < 13):
    print("The person is a child.")
elif (age >= 13 and age < 20):
    print("The person is a teenager.")
else:
    print("The person is an adult.")
