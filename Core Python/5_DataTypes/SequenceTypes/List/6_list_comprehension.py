# Basics Example of list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [x for x in fruits if "a" in x]
print(new_list)  # ['apple', 'banana', 'mango']

# Without using any conditions

new_list1 = [x for x in fruits]
print(new_list1)

# Using range function to create a iterable
numbers = [x for x in range(1,11)]
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using condition with tha range function
numbers = [x for x in range(1,11) if x>5]
print(numbers)  # [6, 7, 8, 9, 10]

# To create a list of the squares of numbers from 0 to 9:
squares = [ x**2 for x in range(10)]

print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# to create a list of the squares of even number from 1 to 8 
squares1 = [ x**2 for x in range(9) if x%2 == 0 ]
print(squares1)  # [0, 4, 16, 36, 64]

# List Comprehensions with if-else
parity = ["even" if x%2 == 0  else "odd" for x in range(10)  ]
print(parity)