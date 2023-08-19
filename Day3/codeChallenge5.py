# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1+name2
s=0
k=0
k+=name.count("t")
k+=name.count("r")
k+=name.count("u")
k+=name.count("e")
print(k)
s+=name.count("l")
s+=name.count("o")
s+=name.count("v")
s+=name.count("e")



total = str(k)+str(s)
if int(total)<10 or int(total)>90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif 40<=int(total)<=50:
    print(f"Your score is {total}, you are alright together.")
else:
     print(f"Your score is {total}.")