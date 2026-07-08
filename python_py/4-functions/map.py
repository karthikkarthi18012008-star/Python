#squaring numbers
def square(n):
    return n**2

n = [1,2,3,4,5,6]
squared = list(map(square,n))
print(squared)

#lambda function with map

square = list(map(lambda x:x*x,n))
print(square)

#mapping multiple iterables

n1 = [1,2,3,4]
n2 = [5,6,7,8]

added_numbers = list(map(lambda x,y:x+y,n1,n2))
print(added_numbers)

#use map to convert string to int

string = ['1','2','3','4']
int_numbers = list(map(int , string))
print(int_numbers)

#converting to uppercase

words = ['apple','banana','mango']

upper_case = list(map(str.upper,words))
print(upper_case)


#dictionay

def get_name(person):
    return person['name']

people=[
    {'name':'Krish','age':32},
    {'name':'Jack','age':33}
]
names = list(map(get_name,people))
print(names)
