# ==== USING FOR LOOP TO ITERITATE THROUGH LIST ====

list_name = ["Roman", "Anup", "Sushant", "Bijen"]

for name in list_name: # name is the iteration variable
  print(f"Happy New Year {name}") 

# Using range() methods for looping
for i in range(len(list_name)):
  print(f"Welcome {list_name[i]} for learning the Core Python")

print()
print()

# Converting the string to list, taking input from the user
new_list = []
for _ in range(2):
  name = input("Enter Your Name.... ")
  new_list.append(name)

print(f"The new list so formed is {new_list}")
print("All Done !!")
  
  
# === Using enumerate() function to get the both index and the value in a list
for index, name in enumerate(list_name):
  print(index, name)

print()

# === to print the name which are only at the even index
for index,name in enumerate(list_name):
  if index % 2 == 0:
    print(index, name)

print()

# loop through the list, starting indexing from 1 
for index, name in enumerate(list_name, start=1):
  print(index, name)

print()

# Converting into the list with indexing using enumerate function
enumerated_list = list(enumerate(list_name))
print(enumerated_list) # Output: [(0, 'Roman'), (1, 'Anup'), (2, 'Sushant'), (3, 'Bijen')]

print()

# Looping through matrix to get the element with row and column
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

for row_index, row in enumerate(matrix):
  for column_index , element in enumerate(row):
    print(f"The element at {row_index} , {column_index} is {element} ")
  
lst_numbers = [2, 4, 5, 7, 8, 10]
# using loop to modify list by squaring a each element in the list
for index, number in enumerate(lst_numbers):
  lst_numbers[index] = number ** 2

print(lst_numbers) # Output: [4, 16, 25, 49, 64, 100]
print("All Done !!")
print()

grades = [20, 100, 30, 40, 50, 80, 90]
# To print the index of the grade which are less than 50

for index, grade in enumerate(grades):
  if grade < 50 :
    print(index)


# ==== WORKNG WITH ADVANCED LOOPING PROBLEM =====
'''1-> To Find the greatest and smallest number from the list. '''
numbers = [34, 57, 32, 10, 22, 99, 14, 67, 90, 34, 89]

greatest_number = 0
smallest_number = None

for number in numbers:
  if number > greatest_number:
    greatest_number = number
    
  if smallest_number is None:
    smallest_number = number
  else:
    if number < smallest_number:
      smallest_number = number
    
    
print(f"The greatest number is  {greatest_number}")
print(f"The smallest number is  {smallest_number}")


# To find the sum of the elements in the list 
sum = 0
for number in numbers:
  sum += number
print(f"The total sum of the elements in the list is {sum}")

# ==== Create a list containing the lengths of each word from a list of words. ====

words = ["Roman","Software Eengineer", 'PCPS College', "Panauti"]
new_list = []
for word in words:
  length_of_word = len(word)
  new_list.append(length_of_word)
print(f"New List with the length of each elements from the words list is {new_list}")

print()

'''
Implement a rotation of a list. Given a list and a number n, "rotate" the list by n positions.
For example, given the list [1, 2, 3, 4, 5] and n = 2, the result should be [4, 5, 1, 2, 3]
'''
new_list1 = [1, 2, 3, 4, 5]
n= 2 
x= len(new_list1) - 2

rotation_of_list = new_list1[x:] + new_list1[:x]
print(rotation_of_list)




  
