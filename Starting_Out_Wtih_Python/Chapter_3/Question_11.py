
books_bought = int(input("How many books have you bought? "))

if(books_bought < 2):
    points = 0
elif(books_bought < 4):
    points = 5
elif(books_bought < 6):
    points = 16
elif(books_bought < 8):
    points = 30
else:
    points = 60

print("You have earned", points, "points.")
