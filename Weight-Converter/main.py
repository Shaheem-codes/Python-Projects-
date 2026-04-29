#weight converter

weight = float(input("Enter your weight: "))
unit = input("Enter your unit (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight is {round(weight,1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is {round(weight,1)} {unit}")
else:
    print("Invalid unit entered")

# CONDITIONAL STATEMENTS REMEMBER 
num = 5

result = "Even" if num % 2 == 0 else "Odd"
print(result)
