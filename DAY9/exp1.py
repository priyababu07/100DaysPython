# author     : Priya Babu
# description: Python Program to Convert Decimal to Binary, Octal and Hexadecimal
# date        : 08/08/2023

def binary(number):
    s=""
    while(number>0):
      
        k = number%2
        number = number//2
        s=str(k)+s
    return s

def octal(number):
    s=""
    while(number>0):
      
        a= number%8
        number = number//8
        s=str(a)+s
    return s 
def hexadecimal(number):
    s=""
    while(number>0):
      
        b= number%16
        if b>9:
            m = b-10
            n = 65+m
            b = chr(n)


        number = number//16
        s=str(b)+s
    return s 



number = int(input())
l = binary(number)
p = octal(number)
h = hexadecimal(number)
print(f"The binary of this number is {l}")
print(f"The octal of this number is {p}")
print(f"The hex of this number is {h}")
