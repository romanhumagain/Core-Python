'''
1-> Variable is a container to hold the data.
2-> Variables do not need to be declared with any datatypes in python

'''

#  Some basics examples of the variables

num1 = 69               #  num1 is a type of int
str1 = "Roman Humagain" # str1 is a type of string
float1 = 36.6           # float1 is s type of float number 


# ==== To get the type of the variable =====

print(type(num1))   # output <class 'int'>
print(type(str1))   # output <class 'str'>
print(type(float1)) # output <class 'float'>

# ==== Variable names are case-sensitive ====
numbers = 45
Numbers = 69
# Numbers will not overwrite numbers 


# ==== LEGAL MULTI WORD VARIABLE NAMING METHOD IN PYTHON =====

#  1.Camel Case
myVariablesName = "Roman Humagain"
# Pascal Case
MySiteName = "romanhumagain.com.np"
# Snake Case
my_course_name = "Software Enigneering"


# Assigning same value to the multiple variables
my_site = "romanhumagain.com.np"
site1 = site2 = my_site
print(site1, site2)

# == Variable overwrite ==
my_site = "roman.com.np"
print(my_site)

# ==== Unpack a Collection ====
new_list = ['Roman', 'Humagain']
list1 = list2 = new_list
print(list1)
print(list2)

#









