# author     : Priya Babu
# description: Progarm to find the largest among 3 numbers
# date        : 22/08/2023

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the first number"))
num3 = int(input("Enter the first number"))
if num1>num2 and num1>num3:
    print(f"{num1} is the greatest number")
elif num2>num1 and num2>num3:
    print(f"{num2} is the greatest number")
else:
    print(f"{num3} is the greatest number")

