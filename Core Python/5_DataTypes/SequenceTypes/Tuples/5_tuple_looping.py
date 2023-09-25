# === BASIC TUPLE LOOPING ====
my_tuple = (1, 2, 3, 4, 5)
 
for i in my_tuple:
  print(i, end=" ") # Output: 1 2 3 4 5 
  
# Using range() function
for i in range(len(my_tuple)): 
  print(my_tuple[i], end=" ")  # Output: 1 2 3 4 5 
  
  
# ==== Advanced Tuple Looping: ==== !important

# Using enumerate() function to loop
for index, value in enumerate(my_tuple):
  print(f"Index {index} has value {value}")

# Iteration over a nested loop  
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
for outer_element in nested_tuple:
  for inner_element in outer_element:
    print(inner_element, end=" ")
  print()  
  
# Using zip() function to loop through multiple tuples simultaneously
tuple1 = (2, 4, 6, 8)
tuple2 = ('Two', 'Four', 'Six', 'Eight')

for num, name in zip(tuple1, tuple2):
  print(num, name)
  
# Using while loop 
i = 0
while i < len(my_tuple):
  print(my_tuple[i], end=" ")
  i += 1