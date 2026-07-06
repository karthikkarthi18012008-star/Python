#adding two numbers
sum = lambda a,b:a+b

print(type(sum))
print(sum(1,2))

#checking for even number
even = lambda a:a%2==0
print(even(23))

# adding 3 numbers
addition = lambda a,b,c:a+b+c
print(addition(1,2,3))

#lambda function with map()
n = [1,2,3,4,5]
square = list(map(lambda x:x**2,n))
print(square)


