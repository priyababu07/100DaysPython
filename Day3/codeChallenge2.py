# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_val = round(weight/(height**2))
if bmi_val<18.5:
    print(f"Your BMI is {bmi_val}, you are underweight.")
elif 18.5<=bmi_val<25:
    print(f"Your BMI is {bmi_val}, you have a normal weight.")
elif 25<=bmi_val<30:
    print(f"Your BMI is {bmi_val}, you are slightly overweight.")
elif 30<=bmi_val<35:
    print(f"Your BMI is {bmi_val}, you are obese.")
else:
    print(f"Your BMI is {bmi_val}, you are clinically obese.")