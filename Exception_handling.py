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

#using finally block
try:
    file = open("sample.txt","r")
    print(file.read())
except FileNotFoundError:
    print(f"Error: the file not found.")
finally:
    print("Closing file... (even if error occurred)")

#using try,except
try:
    a = b
except NameError as ex:
    print(ex)

             
try:
    a = int(input("enter a number:"))
    result = 2/a
except ZeroDivisionError as ex:
    print(ex)
    print("enter a valid denomenator:")


try:
    result = 2/1
    a=b
except ZeroDivisionError as ex:
    print(ex)
    print("enter a valid denomenator:")
except Exception as ex1:
    print(ex1)
    print("main exception got caought here")


#multiple exceptions

try:
    num=int(input("Enter a number"))
    result=10/num
except ValueError:
    print("This is not a valid number")
except ZeroDivisionError:
    print("enter denominator greater than 0")
except Exception as ex:
    print(ex)
    
## try,except,else block
try:
    num=int(input("Enter a number:"))
    result=10/num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as ex:
    print(ex)
else:
    print(f"the result is {result}")

## try,except,else and finally
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as ex:
    print(ex)
else:
    print(f"The result is {result}")
finally:
    print("Execution complete.")

### File handling and Exception HAndling

try:
    file=open('example1.txt','r')
    content=file.read()
    a=b
    print(content)

except FileNotFoundError:
    print("The file does not exists")
except Exception as ex:
    print(ex)

finally:
    if 'file' in locals() or not file.closed():
        file.close()
        print('file close')