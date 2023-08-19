import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")

l = len(names)-1
num = random.randint(0,l)
print(f"{names[num]} is going to buy the meal today!")