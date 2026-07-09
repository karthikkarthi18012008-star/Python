##calculate the sum of first n natural numbers using for and while loops

#using while loop
n = int(input("Enter a positive integer:"))
sum = 0
count = 1

while count <=n:
    sum += count
    count += 1

print(f"The sum of first {n} natural numbers using while loop is: {sum}")


##using for loop
sum2 = 0
for i in range(1,n+1):
    sum2 +=i
print(f"The sum of first {n} natural numbers using for loop is: {sum}")

#display prime numbers between 1 and 100 using for loop

for num in range(1,101):
    if num > 1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
                    