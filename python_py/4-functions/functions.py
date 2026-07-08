#temperature conversion

def temperature(temp,unit):
    if unit == "C":
        return temp*9/5+32
    if unit == "F":
        return (temp-32)*5/9
    else:
        return None
    
print("temperature in Farheniet:",temperature(25,"C"))
print("temperature in celcius:",temperature(77,"F"))
print("="*30)

#checking password strength
def is_strong_password(password):
    """This function checks if the password is strong or not"""
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+' for char in password):
        return False
    return True

## calling the function
print(is_strong_password("WeakPwd"))
print(is_strong_password("Str0ngPwd!"))

#calculating the total cost of the items in a shopping cart
def calculate_total_cost(cart):
    total_cost=0
    for item in cart:
        total_cost+=item['price']* item['quantity']

    return total_cost


## Example cart data

cart=[
    {'name':'Apple','price':0.5,'quantity':4},
    {'name':'Banana','price':0.3,'quantity':6},
    {'name':'Orange','price':0.7,'quantity':3}

]

## calling the function
total_cost=calculate_total_cost(cart)
print(total_cost)

#checks if a string is a palindrome

def is_palindrome(s):
    s=s.lower().replace(" ","")
    return s==s[::-1]

print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Hello"))