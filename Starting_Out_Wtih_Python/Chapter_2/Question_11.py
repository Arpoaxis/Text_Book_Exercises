males = int(input("How many males are there in the class?"))
females = int(input("How many females are in the class?"))

totalStudents = males + females
percentMale = (males/totalStudents) * 100
percentFemale = (females/totalStudents) * 100

print(format(percentMale, '.1f'), "% are male.", sep='')
print(format(percentFemale, '.1f'), "% are female.", sep='')