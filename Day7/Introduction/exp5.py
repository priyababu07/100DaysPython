# author     : Priya Babu
# description:Solve Quadratic Equation
# date        : 22/08/2023

#Lets do it only basic equation

b = int(input("Enter the value of b:"))
a = int(input("Enter the value of a:"))
c = int(input("Enter the value of c"))
d = (b**2-4*a*c)**0.5
print((-b+d)/(2*a))
