print("Welcome to the tip calculator.")

total = float(input("What was the total bill? $"))

tip_percent = int(input("What percentage tip would you like to give? 10,12, or 15?"))
spilt_no = int(input("How many people to split the bill?"))

include_tip = total*(tip_percent/100)
final_total = total +include_tip
amount = round(final_total/spilt_no,2)
print(f"Each person should pay ${amount}")