import sys

# =====================================================================
# 1. GLOBAL CONFIGURATION & INITIAL STATE
# =====================================================================
pin = 1234
currentBalance = 25000
history = []


# =====================================================================
# 2. CORE ATM FUNCTIONS (ACTION MODULES)
# =====================================================================
def checkBalance():
    print(f"\nCurrent Balance: ₹{currentBalance}")


def depositMoney():
    global currentBalance
    while True:
        try:
            userAmount = int(input("Enter Amount to Deposit: "))
            if userAmount <= 0:
                print("Please enter an amount greater than 0.")
                continue

            currentBalance += userAmount
            print(f"\n₹{userAmount} deposited Successfully.")
            print(f"New Balance: ₹{currentBalance}")
            history.append(f"Deposit        +₹{userAmount}")
            break
        except ValueError:
            print("Invalid Input! Please enter numbers only (e.g., 500).")


def withdrawMoney():
    global currentBalance
    while True:
        try:
            userAmount = int(input("Enter Amount to Withdraw: "))
            if userAmount <= 0:
                print("Please enter an amount greater than 0.")
                continue
            if userAmount > currentBalance:
                print(f"\nInsufficient balance. Available Balance: ₹{currentBalance}")
                break  # Returns to main menu instead of getting stuck in loop

            currentBalance -= userAmount
            print(f"\n₹{userAmount} withdrawn Successfully.")
            print(f"New Balance: ₹{currentBalance}")
            history.append(f"Withdraw       -₹{userAmount}")
            break
        except ValueError:
            print("Invalid Input! Please enter numbers only (e.g., 500).")


def transactionHistory():
    print("\nTransaction History")
    print("-------------------------")
    if not history:
        print("No transactions yet.")
    for item in history:
        print(item)
    print("-------------------------")
    print(f"Current Balance: ₹{currentBalance}")


# =====================================================================
# 3. SECURITY & AUTHENTICATION MODULES
# =====================================================================
def changePIN():
    global pin
    change_attempts = 3
    while change_attempts > 0:
        try:
            print(f"\nYou have {change_attempts} attempt(s) left.")
            oldPin = int(input("Enter current PIN: "))

            if oldPin == pin:
                newPin = int(input("Enter New 4-Digit PIN: "))
                # Basic validation for 4-digit requirement
                if len(str(newPin)) != 4:
                    print("PIN must be exactly 4 digits long.")
                    continue

                pin = newPin
                print("PIN Changed Successfully!")
                return True
            else:
                print("Incorrect Current PIN!")
                change_attempts -= 1
        except ValueError:
            print("Invalid Input! PIN must be numeric numbers only.")
            change_attempts -= 1

    print("\nMaximum attempts reached during PIN change! Account Blocked.")
    return False


def verifyLogin():
    login_attempts = 3
    while login_attempts > 0:
        try:
            print(f"You have {login_attempts} attempt(s) left.")
            userPin = int(input("Enter PIN: "))

            if userPin == pin:
                print("\nLogin Successful!")
                return True
            else:
                print("Incorrect PIN!")
                login_attempts -= 1
        except ValueError:
            print("Invalid Input! PIN must be numbers only.")
            login_attempts -= 1

    print("\nMaximum attempts reached! Account Blocked.")
    return False


# =====================================================================
# 4. MAIN PROGRAM CONTROLLER (EXECUTION FLOW)
# =====================================================================
def main():
    print("================================")
    print("              ATM               ")
    print("================================")

    # Check system authentication first
    if not verifyLogin():
        sys.exit()  # Stops execution cleanly if login fails

    while True:
        print("""\n1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Change PIN
5. Transaction History
6. Exit""")

        try:
            menuoption = int(input("Enter option from given list: "))

            if menuoption == 1:
                checkBalance()
            elif menuoption == 2:
                depositMoney()
            elif menuoption == 3:
                withdrawMoney()
            elif menuoption == 4:
                # If PIN change fails due to maximum incorrect attempts, block session
                if not changePIN():
                    break
            elif menuoption == 5:
                transactionHistory()
            elif menuoption == 6:
                print("\nThank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid Choice! Please enter an option between 1 and 6.")
        except ValueError:
            print("Invalid Input! Please enter option number only.")


if __name__ == "__main__":
    main()
