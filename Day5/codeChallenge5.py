import random

p = ""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
characters = ['@', '#', '$', '%', '^', '&', '*']

length = int(input("The length of the password: "))
char = int(input("The number of letters required: "))
num = int(input("The number of numbers required: "))
chara = int(input("The number of characters required: "))

for j in range(char):
    p += random.choice(letters)
    
for j in range(num):
    p += random.choice(numbers)
    
for j in range(chara):
    p += random.choice(characters)


remaining_length = length - (char + num + chara)
for j in range(remaining_length):
    p += random.choice(letters + numbers + characters)



print("Generated password:", p)

