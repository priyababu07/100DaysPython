print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
cross = input("You are at crossroad,Where do you want to go ? Type 'left' or 'right'")
if cross=="left":
    dis = input("You reached near a lake,what to do next ? Type 'swim' or 'wait' ")
    if dis =="wait":
        door = input("Here appearing 3 doors which one do you prefer ? Type 'red' 'blue' and 'green'")
        if door=="blue":
            print("You are fired,Game over")
        elif door=="red":
            print("You fall from a cliff,Game over")
        elif door=="green":
            print("You Won!!")
        else:
            print("Invalid input")
    elif dis=="swim":
        print("Game Over")
    else:
        print("Invalid input")
elif cross=="right":
    print("Game Over")
else:
    print("Invalid input")
