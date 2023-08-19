print("Welcome to the rollercoaster")
height = int(input("What is your height in cm ? "))
if height>120:
    print("You can ride rollercoaster")
    age = int(input("Enter your age:"))
    if age<=12:
        print("Pay $5")
    elif 12<=age<=18:
        print("Pay $7")
    else:
        print("Pay $12")
else:
    print("Sorry,You can'nt ride rollercoaster")