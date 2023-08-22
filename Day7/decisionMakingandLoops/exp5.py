# author     : Priya Babu
# description: Progarm to check number is prime
# date        : 22/08/2023

number = int(input("Enter the number:"))
flag = 0  

for i in range(2, number):
    if number % i == 0:
        flag = 1  
        break     

if flag == 1:
    print("Not a prime number")
else:
    print("Is a prime number")
