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