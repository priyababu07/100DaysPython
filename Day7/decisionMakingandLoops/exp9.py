# author     : Priya Babu
# description: Progarm to find the fibanocci
# date        : 22/08/2023

a=0
b=1
limit = int(input("Enter the limit"))
print(a)
print(b)
for i in range(1,limit):
    
    k=a+b
    a=b
    b=k
    print(b)
    
    