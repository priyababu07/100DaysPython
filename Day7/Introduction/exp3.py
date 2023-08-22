# author     : Priya Babu
# description: Add two numbers
# date        : 22/08/2023

import math
num = int(input("Enter the number to find the square root"))
square_root = num**0.5
using_import = math.sqrt(num)
print(f"Using the normal method {square_root}")
print(f"Using importing math library {using_import}")