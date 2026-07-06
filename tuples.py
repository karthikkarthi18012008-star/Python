tpl = tuple(range(21))
print(tpl)

#accessing tuple elements
print(f"First element: {tpl[0]}")
print(f"Middle element: {tpl[len(tpl) // 2]}")
print(f"Last element: {tpl[-1]}")


#tuple slicing
print(f"First three elements: {tpl[:3]}")
print(f"Last three elements: {tpl[-3:]}")
print(f"Elements from index 2 to 5: {tpl[2:6]}")

#nested tuples

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print("Matrix:")
for row in matrix:
    print(row)
print(f"Element at second row and third column: {matrix[1][2]}")

#tuple concatenation

tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)
concatenated = tpl1 + tpl2
print(concatenated)

#tuple repetation

print(tpl1*3)

#tuple methods

tpl = (1, 2, 2, 3, 4, 4, 4, 5)
print(f"Occurrences of 4: {tpl.count(4)}")
print(f"Index of first occurrence of 2: {tpl.index(2)}")

#tuple unpacking

tpl = (1, 2, 3, 4, 5)
a, b, c, d, e = tpl
print(a, b, c, d, e)

#tuple conversion

lst = [1, 2, 3, 4, 5]
tpl = tuple(lst)
print(tpl)

#tuple of tuples

tpl_of_tpls = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(tpl_of_tpls)

#tuple of list
tpl = (1, 2, 3, 4, 5)
lst = list(tpl)
lst.append(6)
tpl = tuple(lst)
print(tpl)

#tuple and string

string = "hello"
tpl = tuple(string)
joined_string = ''.join(tpl)
print(joined_string)

#tuple dictionary

tpl_dict = {
    (1, 2): 3,
    (4, 5): 6,
    (7, 8): 9
}
print(tpl_dict)

#nested tuple iteration

nested_tpl = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
for tpl in nested_tpl:
    for elem in tpl:
        print(elem)

#set and tuple

tpl = (1, 2, 2, 3, 4, 4, 4, 5)
unique_set = set(tpl)
print(unique_set)

