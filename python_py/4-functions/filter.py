#even numbers using filter()

def even(n):
    if n%2 == 0:
        return True
    
lst = list(range(21))

evens = list(filter(even,lst))
print(evens)

#filter with lambda

lst = list(range(21))
z = list(filter(lambda x:x>5,lst))
print(z)

#filter and lambda with multiple conditions

lst = list(range(21))
z = list(filter(lambda x:x>5 and x%2 == 0,lst))
print(z)

## Filter() to check if the age is greate than 25 in dictionaries
people=[
    {'name':'Krish','age':32},
    {'name':'Jack','age':33},
    {'name':'John','age':25}
]

def age_greater_than_25(person):
    return person['age']>25

age = list(filter(age_greater_than_25,people))
print(age)
