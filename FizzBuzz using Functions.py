# Define the fizzbuzz function
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(str(i))

# Get user input and call the fizzbuzz function
try:
    user_input = int(input("Enter a positive integer: "))
    if user_input > 0:
        fizzbuzz(user_input)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter an integer.")