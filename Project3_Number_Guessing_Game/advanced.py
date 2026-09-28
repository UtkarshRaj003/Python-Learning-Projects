from random import randint

print("Choose Difficulty: ")
print("""\n1. Easy   → 1-50
2. Medium → 1-100
3. Hard   → 1-500\n""")


def diffchoice():
    while True:
        # Get the input inside the loop so it can change if invalid
        try:
            number = int(input("Select difficulty (1, 2, or 3): "))
        except ValueError:
            print("Please enter a valid integer.\n")
            continue

        if number == 1:
            return 50
        elif number == 2:
            return 100
        elif number == 3:
            return 500
        else:
            print("Please select a valid number from the given list.\n")


last_range = diffchoice()


computer = randint(1, last_range)

print(f"Select a number between 1 and {last_range}.'\n")
print("You have 5 attempts.")

attempt = 1

while True:
    if attempt <= 5:
        try:
            user = int(input(f"Attempt {attempt}: "))
        except ValueError:
            print("Please enter a valid integer.\n")
            continue
        if user == computer:
            print("\nHoorrayy!!!!!!!\nYou Win!!!\n")
            print(f"You guessed it in {attempt} attempts.\n")
            attempt += 1
            break
        elif user > computer:
            print("High. Please select a small number\n")
            attempt += 1
            continue
        elif computer > user:
            print("Low. Please select a big number\n")
            attempt += 1
            continue
    else:
        print(f"Game Over!\nToo many attempt!\nThe correct number was {computer}.")
        break
