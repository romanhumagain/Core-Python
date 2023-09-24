'''

->  append():----------------Adds an element at the end.
->  insert(index, element):--Inserts the element at the given index.
->  extend(iterable):--------Extend the list with elements from another iterable.
->  remove(value):-----------Removes the first occurrence of the value.
->  pop(index):--------------Removes and returns the element at the index.
->  index(value):------------Returns the index of the first occurrence of the value.
->  count(value):------------Counts the occurrences of a value.
->  sort():------------------Sorts the list in-place.
->  reverse():---------------Reverses the list in-place.
->  copy():------------------Returns a copy of the list.

'''
my_list = ['Roman', 'Humagain', 20, 5.6, 'Software Engineer']

# ==== EXAMPLE FOR THE append() method ====
'''
append() method will add the new element at the last of the list. 
'''
my_list.append('PCPS College')
print(f'New list after using the append method is {my_list}') # output: ['Roman', 'Humagain', 20, 5.6, 'Software Engineer', 'PCPS College']


# ==== Example FOR THE insert() METHOD ====
my_list.insert(6,"Male")
print(my_list)

# ==== Example FOR THE index() METHOD ====
index = my_list.index('Roman')   # index method is used to find the index of the certain element from the list.
print(f"The index for the value 'Roman' is {index}")


# ==== Example FOR THE extend() method ====
list1 = [1,2,3,4]
list2 = ['Roman', 'Humagain', 'Male']

list1.extend(list2)  # It will extend the element in the list1 from the list2
print(list1)


# ==== EXAMPLE FOR THE remove() METHOD ====
list2 = ['Roman', 'Humagain', 'Male', 'Roman', 'Roman']
list2.remove('Roman') # It will remove only the String 'Roman' which come first.
print(f"Example of remove method {list2}")  # ['Humagain', 'Male', 'Roman', 'Roman']


# ==== EXAMPLE FOR THE pop() METHOD ====
my_list.pop(3)  # It will remove the element which is at the 3 index value
print(my_list)


# ==== EXAMPLE FOR THE count() METHOD ====
count_list = [1, 2, 3, 1, 3, 1, 1, 4, 5, 6]
count_one = count_list.count(1)   # To count the element 1 from the list
print(f"The total count for the element 1 is {count_one}")  # output: 4

my_numb_list = [4, 7, 1, 3, 9, 2, 2]

# ==== EXAMPLE FOR THE reverse() METHOD ====
my_numb_list.reverse()
print(f"The reverced list is {my_numb_list}") # output: [2, 2, 9, 3, 1, 7, 4]


# ==== EXAMPLE FOR THE sort() METHOD ====
my_numb_list.sort() 
print(f"The sorted list is {my_numb_list}")  # output: [1, 2, 2, 3, 4, 7, 9]


# ==== EXAMPLE FOR THE copy() METHOD ====
original_list = [1, 4, 5, 7, 4, 3]
copied = original_list.copy()  # Copy method will copy the entire list from the original list
copied.append(10)
print(f"The copied list is {copied}")












