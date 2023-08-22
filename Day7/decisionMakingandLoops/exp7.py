# author     : Priya Babu
# description: Progarm to find the factorial
# date        : 22/08/2023

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}")

