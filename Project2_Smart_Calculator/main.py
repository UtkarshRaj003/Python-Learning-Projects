def add(fn, sn):
    return fn + sn


def sub(fn, sn):
    return fn - sn


def mul(fn, sn):
    return fn * sn


def div(fn, sn):
    return fn / sn


def mod(fn, sn):
    return fn % sn


def pow(fn, sn):
    return fn**sn


def fldiv(fn, sn):
    return fn // sn


def menu():
    print("================================")
    print("""\n1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Power
7. Floor Division
8. Exit\n""")


print("================================")
print("Smart Calculator")

while True:
    menu()
    try:
        number = int(input("Choose option: "))
    except ValueError:
        print("\nInvalid input. Please enter a number between 1-8.\n")
        continue

    if number == 8:
        print("Exited...")
        break
    elif number < 1 or number > 8:
        print("\nInvalid choice. Please select 1-8.\n")
    else:
        # Ek hi try block me saari calculation aur invalid inputs handle ho jayege
        try:
            first_number = int(input("\nEnter First number: "))
            second_number = int(input("Enter Second number: "))

            if number == 1:
                result = add(first_number, second_number)
            elif number == 2:
                result = sub(first_number, second_number)
            elif number == 3:
                result = mul(first_number, second_number)
            elif number == 4:
                result = div(first_number, second_number)
            elif number == 5:
                result = mod(first_number, second_number)
            elif number == 6:
                result = pow(first_number, second_number)
            elif number == 7:
                result = fldiv(first_number, second_number)

            print(f"\nResult: {result}")

        except ZeroDivisionError:
            print("\nError: Cannot divide by zero.")
        except ValueError:
            print("\nError: Please enter valid numbers only.")
