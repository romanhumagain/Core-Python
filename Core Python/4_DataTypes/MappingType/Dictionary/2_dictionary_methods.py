'''
copy()--------->	Returns a copy of the dictionary
fromkeys()----->	Returns a dictionary with the specified keys and value
get()---------->	Returns the value of the specified key
items()-------->	Returns a list containing a tuple for each key value pair
keys()--------->	Returns a list containing the dictionary's keys
pop()---------->	Removes the element with the specified key
popitem()------->	Removes the last inserted key-value pair
setdefault()---->	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()------->	Updates the dictionary with the specified key-value pairs
values()------->	Returns a list of all the values in the dictionary
clear()---------> Removes all the elements from the dictionary
'''
# === WORKING WITH THE copy() METHOD ====
original = {'name1':'Apple', 'color1':'Red'}
copied = original.copy()
print(f"The dictionary formed after copying from the dict1 is {copied}")  # Output :{'name1':'Apple', 'color1':'Red'}


# === WORKING WITH THE clear() METHOD ====
dict1 = {'a':2, 'b': 4 , 'c':8}
dict1.clear()
print(dict1) # Output: {}

# === WORKING WITH THE dict.fromkeys(key, value) METHOD ====
keys = ['a','b','c' ]
values = 10
new_dict = dict.fromkeys(keys, values)
print(new_dict) # Output: {'a': 10, 'b': 10, 'c': 10}


my_dict =  {'name': "Roman Humagain",
            'age':20, 
            'College':'PCPS College',
            'Course': 'Software Engineering' }


# === WORKING WITH THE get() METHOD ====
name =my_dict.get('name', 'Unknown')
print(name) # Output: Roman Humagain

address = my_dict.get('address', 'Unknown Address') # no address key in the my_dict dictionary
print(address) # Output: Unknown Address, 


# === WORKING WITH THE items() METHOD ====
''' Returns a view object that displays a list of dictionary's key-value tuple pairs. '''
d = {'name': 'Roman', 'age': 20}
dict_items = d.items()
print(dict_items) # Output: dict_items([('name', 'Roman'), ('age', 20)])


# === WORKING WITH THE keys() METHOD ====
''' Returns a view object displaying keys of the dictionary. '''
print(my_dict.keys()) # Output: dict_keys(['name', 'age', 'College', 'Course'])


# === WORKING WITH THE values() METHOD ====
''' Returns a view object that displays all the values in the dictionary. '''
print(my_dict.values())  # Output: dict_values(['Roman Humagain', 20, 'PCPS College', 'Software Engineering'])


# === WORKING WITH THE pop() METHOD ====
''' Removes the specified key and returns its value. If the key is not found, it returns the default value. '''
print(my_dict.pop('Course', 'N/A'))  # Output: Software Engineering
print(my_dict.pop('Address', 'N/A'))  # Output: N/A


# === WORKING WITH THE popitems() METHOD ====
''' Removes and returns the last key-value pair from the dictionary. '''
print(my_dict.popitem()) # Output: ('Course', 'Software Engineering')


# === WORKING WITH THE update() METHOD ====
''' Updates the dictionary with the key-value pairs from other, overwriting existing keys. '''
update_data = {'Address': 'Panauti', 'Gender':'Male'}
my_dict.update(update_data)
print(my_dict)  # Output:  {'name': 'Roman Humagain', 'age': 20, 'Address': 'Panauti', 'Gender': 'Male'} 


# === WORKING WITH THE setdefault() METHOD ====
''' Returns the value of a key (if the key is in the dictionary). If not, it inserts the key with the specified value. '''
new_dict1 = {'name': 'Roman Humagain'}
print(new_dict.setdefault('name', 'Unknown')) # Unknown
print(new_dict.setdefault('Age', 20))  # 20

# === WORKING WITH THE clear() METHOD ====
''' Clear the existing keys and value pair from the dictionary '''
my_dict.clear()
new_dict.clear()
new_dict1.clear()

print(my_dict, new_dict, new_dict1)  # Output: {} {} {}






