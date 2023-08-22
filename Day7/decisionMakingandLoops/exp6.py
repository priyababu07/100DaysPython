# author     : Priya Babu
# description: Progarm to print prime number between the limit
# date        : 22/08/2023

limit = int(input("Enter the limit:"))

for num in range(2, limit):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
