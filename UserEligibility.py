# Ask for user's age and convert to integer
age = int(input("Please enter your age: "))

# Ask for user's IT experience and convert to integer
experience = int(input("Please enter your years of IT experience: "))

# Check conditions using if-else statement
if age >= 22 and experience >= 2:
    print("Access Granted")
else:
    print("Access Denied")
