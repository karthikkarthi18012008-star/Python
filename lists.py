lst = list(range(20))

print(lst)
print("="*30)
#accessing elements
print(lst[0])
print(lst[5])
print("="*30)

#list slicing
print(lst[:5])
print(lst[-5:])
print(lst[5:16])
print("="*30)

#list comprehension

new_lst = [x**2 for x in lst]
print(new_lst)
print("="*30)


#filtering lists

evens = [x for x in lst if x%2 == 0]
print(evens)
print("="*30)

#list methods

#creating a list of random numbers and sorting it in ascending and descending order,remove the duplicates and print the modified list
import random
n = [random.randint(1,20) for _ in range(15)]
print(f"the random numbers are:{n}")
print("="*30)

asc = sorted(n)
print(f"the numbers in ascending order:{asc}")
print("="*30)

desc = sorted(asc,reverse = True)
print(f"the numbers in descending order:{desc}")
print("="*30)

uniques = list(set(n))
print(f"the unique numbets in list is:{uniques}")
print("="*30)

print("count of random numbers is:",len(n))
print("count of uniques numbers is:",len(uniques))

#nested list creating 3x3 matrix and accessing elements

matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
]

print(f"original matrix is:{matrix}")

print(f"the element at 1st row and second column of matrix is:{matrix[0][1]}")
print("="*30)

#transpose of the matrix

def transpose_matrix(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = transpose_matrix(matrix)
print("Original matrix:")
for row in matrix:
    print(row)
print("Transposed matrix:")
for row in transposed:
    print(row)

#flattenig a nested list

def flatten(nested_list):
    flattened = [item for sublist in nested_list for item in sublist]
    return flattened

nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = flatten(nested_list)
print("original list\n")
print(nested_list)
print("="*30)

print("falttened list\n")
print(flattened)
print("="*30)

#list manipulation
lst = list(range(1, 11))
print(f"Original list: {lst}")
del lst[6]
del lst[4]
del lst[2]
lst.insert(5, 99)
print(f"Modified list: {lst}")
print("="*30)

#list zipping
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
zipped = list(zip(list1, list2))
print(zipped)
print("=*30")

#list reversal
def reverse_list(lst):
    return lst[::-1]

original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(f"Original list: {original_list}")
print(f"Reversed list: {reversed_list}")
print("=*30")

#list rotation
def rotate_list(lst, n):
    return lst[n:] + lst[:n]

original_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list(original_list, 2)
print(f"Original list: {original_list}")
print(f"Rotated list: {rotated_list}")
print("=*30")

#list intersection
def list_intersection(lst1, lst2):
    return [x for x in lst1 if x in lst2]

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection = list_intersection(list1, list2)
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Intersection: {intersection}")
print("=*30")
