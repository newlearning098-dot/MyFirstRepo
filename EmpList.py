# Create a list containing 5 employee names
employees = ["Alice", "Bob", "Charlie", "David", "Eve"]


# Use a for loop with enumerate to print each name with a number
print("Employee List:")
for index, name in enumerate(employees, start=1):
    print(f"{index}. {name}")