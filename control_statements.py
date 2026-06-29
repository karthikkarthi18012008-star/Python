#determine if a year is a leap year using nested conditional statements
year = int(input("Enter a year:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

##select the operation to perform using if-elif-else statements
n1 = float(input("Enter first number:"))
n2 = float(input("Enter second number:"))
operation = input("Enter operation (+, -, *, /):")

if operation == "+":
    result = n1 + n2
    print(f"The result of {n1} + {n2} is {result}.")
elif operation == "-":
    result = n1 - n2
    print(f"The result of {n1} - {n2} is {result}.")
elif operation == "*":
    result = n1 * n2
    print(f"The result of {n1} * {n2} is {result}.")
elif operation == "/":
    if n2 != 0:
        result = n1 / n2
        print(f"The result of {n1} / {n2} is {result}.")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation.")



###Determine the ticket price based on age  and student status using nested if-else statements
age = int(input("Enter your age:"))
is_student = input("Are you a student? (yes/no):").strip().lower()

if age < 5:
    price = "Free"
elif age <=12:
    price = "$10"
elif age <= 17:
    if is_student == "yes":
        price = "$12"
    else:
        price = "$15"
elif age <= 64:
    if is_student == "yes":
        price = "$18"
    else:
        price = "$20"
else:
    price = "$25"

print(f"The ticket price is {price}.")