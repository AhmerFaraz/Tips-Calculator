print("Welcome to the tip calculator")
bill = int(input("How much bill do you get: "))
tip = int(input("How much tip do you want to give: 10, 12 or 15?:"))
person = int(input("How many person to split the bill !!: "))
tip_as_percent = tip/100
total_tip = tip_as_percent * bill
total_bill = total_tip + bill
split_amount = total_bill / person
final_amount = round(split_amount, 2)
print(f"Each person should pay: {final_amount}")