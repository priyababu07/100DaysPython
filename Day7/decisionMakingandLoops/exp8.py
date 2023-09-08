# author     : Priya Babu
# description: Print multiplication table
# date        : 22/08/2023

num  = int(input("Enter the number to find the multiplication:"))
for i in range(1,10+1):
    mul = i*num
    print(f"{i}X {num} = {mul}")
