print("Reboot the computer and try to connect")
response = input("Did that fix the problem? ")
if (response == "no"):
    print("Reboot the computer and try to connect")
    response = input("Did that fix the problem? ")
    if (response == "no"):
        print("Make sure the cables between the router and modem are plugged in firmly.")
        response = input("Did that fix the problem? ")
        if (response == "no"):
            print("Move the router to a new location.")
            response = input("Did that fix the problem? ")
            if (response == "no"):
                print("Get a new router.")
