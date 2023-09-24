'''
-> A dictionary is an unordered collection of the values, used to store data value like a map

-> A dictionary store the data in the key:value pair
'''

# SYNTAX
dictionary = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

# Creating a dictionary
my_dict =  {'name': "Roman Humagain",
            'age':20, 
            'College':'PCPS College',
            'Course': 'Software Engineering' }

# Accessing the value from the my_dict
print(f"My name is {my_dict['name']}. I am {my_dict['age']} years old. I am currently pursuing my studies in {my_dict['College']}.")

# values can be accessed in two ways.
print(my_dict['name'])
print(my_dict.get('name'))

# Modifying a dictionary

my_dict['name'] =  "Mr Roman"
print(f"Modified dicionary is {my_dict}")

# Dublicate data is not allowed in dictionary
dict1 = {
  'name' : 'Roman',
  'age': 20,
  'name':'roman'
}    # It only print the value of the name which occured at first        
print(dict1)   # Output: {'name': 'roman', 'age': 20}

# The values in the dictionary can be of any datatypes 
new_dict ={
  'name': "Roman Humagain",
  'age': 20,
  'married': False,
  'education': ['LNA', 'Khwopa', 'PCPS']
}

# We can also make this dictionary using the dict keyword as: 
this_dict = dict(name = "Mr Roman Humagain", address  = "Panauti", age = 20)
print(f"The dict made using dict function is {this_dict}")

# Merging two dictionary
dict2 = {'a':2, 'b':4}
dict3 = {'c':6, 'e':9}

merged_dict = {**dict2 ,  **dict3}
print(merged_dict)  # Output: {'a': 2, 'b': 4, 'c': 6, 'e': 9}

# Nested Dictionary
nested_dict = {
  'name':'Roman Humagain',
  'age': 20,
  'sports': {'outdoor':'football', 'indoor':'TT'}
}

# to get the value of the sports
print(nested_dict.get('sports', 'N/A'))