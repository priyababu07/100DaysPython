# author     : Priya Babu
# description: Progarm to find the number to be divisible by other using function
# date        : 22/08/2023

def divisible(num):
    for i in range(1,10):
        if num%i ==0:
            print(i)
            
print(divisible(5))