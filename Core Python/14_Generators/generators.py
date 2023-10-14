'''
-> Generators are a type of iterable like lists or tuple.
-> They do not store all the values in memory
'''

# Creating generators
'''-> Generators function uses the 'yield' keyword to return value. '''

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

number = count_up_to(5)
for num in number:
  print(num, end=" ")
  
# we can also use the next() function to get the next value from the generator
'''
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
'''

print()

# Chaining Generators: You can chain generators together.

def check_even_numbers(nums):
  for n in nums:
    if n%2 == 0:
      yield n
      
      
number = count_up_to(5)
even_number = check_even_numbers(number)

for num in even_number:
  print(num, end=" ")
