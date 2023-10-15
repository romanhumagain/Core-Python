# 1. Write a Python program to sum all the items in a list.
list1 = [2, 4, 6, 8, 10]
sum = 0
for num in list1:
  sum += num
print(f"The sum of elements in the list is {sum}")

# 2. Write a Python program to get the largest and smallest number from a list.
list2 = [22, 44, 67, 80, 100]

smallest_number = None
greatest_number = None

for num in list2:
  if smallest_number is None and greatest_number is None:
    smallest_number = num
    greatest_number = num
  elif num > greatest_number:
    greatest_number = num
  elif num < smallest_number:
    smallest_number = num
  else:
    pass

print(f"The greatest number is {greatest_number} and smallest number is {smallest_number}")

# list comprehension

lst = [x for x in range(5)]
print(lst)