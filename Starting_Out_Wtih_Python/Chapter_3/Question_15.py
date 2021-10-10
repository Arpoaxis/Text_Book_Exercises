total_time = int(input("Whats the total amount of seconds? "))


seconds = total_time % 60
minutes = (total_time % 3600) // 60
hours = (total_time % 86400) // 3600
days = total_time // 86400

if (total_time > 86400):
    print(days, "days : ", hours, " hours : ", minutes, "minutes : ", seconds, "seconds.")
elif (total_time > 3600):
    print(hours, " hours : ", minutes, "minutes : ", seconds, "seconds.")
elif(total_time > 60):
    print(minutes, " minutes : ", seconds, "seconds.")