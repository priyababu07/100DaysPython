# author     : Priya Babu
# description: Check year is leap year
# date        : 22/08/2023

year = int(input("Enter the year"))
if year%4==0 and year%100!=0:
    print("It is a leap year")
elif year%400==0:
    print("It is a leap year")
else:
    print("Not a leap year")
