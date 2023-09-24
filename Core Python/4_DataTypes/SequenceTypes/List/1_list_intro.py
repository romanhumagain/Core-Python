''' 
-> List is used to store the multiple value to a single variable
-> List can contain different type of the datatypes
-> List can also contain the dublicate data 
-> List are mutable i.e. their elements can be changed after creations also.

'''

# -- Working with List --
empty_list = []
mixed_list = ["Roman Humagain", 20, True, "69.99", 20]
number_list = [2, 4, 5, 6, 8]

# Accessing the elements from the mixed_list
first_elements = mixed_list[0]  # the first elements is always present in the 0 index
second_elements = mixed_list[1]

# Using negative index 
'''
-> Negative index starts from -1 i.e. to access the last elements
'''
last_elements = mixed_list[-1]
print(f"The last elements is {last_elements}")

second_last_elements = mixed_list[-2]
print(f"The second last elements is {second_last_elements}")

# modifying the list
number_list[0] = "Mr.Roman "
print(number_list)  

# To get the length of the list
print(f"The total length of the string is {len(number_list)}")

# Adding the two list
list1 = [1,2,3,4]
list2 = [5,6,7,8]

merged_list = list1 + list2
print(merged_list)  # output: [1, 2, 3, 4, 5, 6, 7, 8]

# To check if element exists in a list or not

print("Roman" in number_list)  # Output: False