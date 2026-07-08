people=[
    {'name':'Krish','age':32},
    {'name':'Jack','age':33},
    {'name':'John','age':25}
]

def age_greater_than_25(person):
    return person['age']>25

age = list(filter(age_greater_than_25,people))
print(age)