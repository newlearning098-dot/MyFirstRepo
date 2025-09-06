# Store the correct password
correct_password = "openAI123"

# Allow the user up to 3 attempts
for attempt in range(3):
    entered_password = input("Enter your password: ")

    if entered_password == correct_password:
        print("Login Successful")
        break  # Exit the loop if password is correct
    else:
        print("Incorrect password.")

# If loop completes without a successful login
else:
    print("Account Locked")