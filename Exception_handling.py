try:
    a = int(input("enter a number:"))
    result = 10/a
    print("Result:",result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#handling multiple exceptions
try:
    a = int(input("enter a number:"))
    result = 10/a
    print("Result:",result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

#using finallu block
try:
    file = open("sample.txt","r")
    print(file.read())
except FileNotFoundError:
    print(f"Error: the file not found.")
finally:
    print("Closing file... (even if error occurred)")

             
        
    

