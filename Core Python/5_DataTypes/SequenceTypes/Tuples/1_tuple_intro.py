'''
-> Tuples are used to store the multple items in a single variable.
-> Tuples is a collection which is ordered and unchangable.
-> Tuples are witten in small/round brackets.
-> Tuples allow the dublicate value.
-> Tuple items are indexed.
'''

# Creating a tuple
my_tuple = ("Roman", 20, "Software Engineer", "PCPS College")
print(my_tuple)

# Tuples allow the dublicate value inside it
new_tuple1 = (1, 2, 3, 4, 2 ,1) 
print(new_tuple1)  # Output: (1, 2, 3, 4, 2, 1)

# Using len() function to find the length of the tuple
print(f"The length of the tuple is {len(my_tuple)}")

# To creating a tuple with one items, we have to add comma after the value
tuple1 = ("Roman",)
print(type(tuple1)) #Output: <class 'tuple'>


# Creating a tuple without comma, it will print its as a string.
tuple2 = ("roman") 
print(type(tuple2)) # Output: <class 'str'>

# To access the value of the tuple using the index value
print(f"The element at first index is {my_tuple[1]}")

# Tuple are immutable but their content can be mutable
tuple3 = (1, 2, 3, [4,5])
tuple3[3][0] = 9

print(f"Tuple after modifying is {tuple3}")

# Tuple unpacking
a,b,c = (1, 2, 4)

print(a) # 1 
print(b) # 2
print(c) # 3 

# Tuples Concatination : 
tuple1 = (2, 4, 6, 8, 10)
tuple2 = (1, 3, 5, 7, 9)

merged_tuple = (tuple1 + tuple2)
print(merged_tuple)  # Output: (2, 4, 6, 8, 10, 1, 3, 5, 7, 9)


# Tuple Repetition:
original_tuple = (2, 4, 6)
repeated_tuple =  original_tuple*2 # to repeat the original tuple two times
print(f"The repeated tuples is  {repeated_tuple}") # Output: (2, 4, 6, 2, 4, 6)

# To check whether the element is there in the tuple or not
print("Roman" in original_tuple) # Output: False