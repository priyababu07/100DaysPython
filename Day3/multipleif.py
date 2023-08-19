print("Welcome to the rollercoaster")
height = int(input("What is your height in cm ? "))
if height>120:
    print("You can ride rollercoaster")
    age = int(input("Enter your age:"))
    if age<=12:
        bill = 5
        print("Pay $5")
    elif 12<=age<=18:
        bill = 7
        print("Pay $7")
    else:
        bill = 12
        print("Pay $12")
    choice = input("Do you want photos, Enter Y or N")
    if choice=="Y" or "y":
        total = bill+3
        print(f"Total bill is : {total}")

else:
    print("Sorry,You can'nt ride rollercoaster")
