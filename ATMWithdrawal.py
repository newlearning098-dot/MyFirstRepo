# Ask the user to enter a withdrawal amount
try:
    amount = int(input("Enter withdrawal amount: "))

    # Check if the amount is a multiple of 100
    if amount % 100 == 0:
        print(f"Dispensing {amount}")
    else:
        print("Invalid amount")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    

