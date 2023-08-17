
age = input("What is your current age? ")

age_togo = 90 - int(age)
leftover_day=age_togo*365
leftover_week=age_togo*52
leftover_month=age_togo*12
print(f"You have {leftover_day} days, {leftover_week} weeks, and {leftover_month} months left.")
