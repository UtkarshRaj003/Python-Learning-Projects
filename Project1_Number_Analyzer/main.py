print("================================")
print("Number Analyzer")
print("================================")

number = int(input("Enter a number: "))

print("Result")
print("-------------------------")

num_type = type(number).__name__.replace("int", "Integer").capitalize()

if number > 0:
    sign = "Positive"
elif number < 0:
    sign = "Negative"
else:
    sign = "Zero"


if number % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"


if number % 5 == 0:
    db5 = "Yes"
else:
    db5 = "No"


if number % 10 == 0:
    db10 = "Yes"
else:
    db10 = "No"


if number > 100:
    gt100 = "Yes"
else:
    gt100 = "No"


print(f"Number       : {number}")
print(f"Type       : {num_type}")
print(f"Sign       : {sign}")
print(f"Parity       : {parity}")
print(f"Square       : {number**2}")
print(f"Cube       : {number**3}")
print(f"Divisible by 5       : {db5}")
print(f"Divisible by 10       : {db10}")
print(f"Greater than 100       : {gt100}")
