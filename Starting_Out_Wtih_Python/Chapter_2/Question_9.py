celsius = float(input("Please enter the temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(celsius, "°C is ", format(fahrenheit, '.2f'),"°F", sep='')