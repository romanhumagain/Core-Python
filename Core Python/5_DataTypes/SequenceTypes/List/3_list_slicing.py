'''
-> The slicing in list move from the left to right '''

# ==== WORKING WITH LIST SLICING ==== !important

numbers_list = [4, 6, 12, 20, 40, 50, 60, 100]
mixed_list = ["Roman", "Humagain", 20, "Panauti", "PCPS College"]

# To get the first three number from the numbers_list
first_three = numbers_list[:3]
print(f"first three numbers from the number_list are {first_three}")  # output [4, 6, 12]

# using negative slicing to get the last two numbers
last_two = numbers_list[-2:]
print(f"last two numbers from the number_list are {last_two}")  # output [60, 100]

print(f"Printing all the element in the list {numbers_list[:]}") # output [4, 6, 12, 20, 40, 50, 60, 100]

# accessing the elements from the list with one element gap
print(f"Elements at the even number indexing are: {numbers_list[::2]}")

# accessing only three elements from the list with one element gap
print(f"Three elements at the even number indexing are {numbers_list[:6:2]}")



# ==== WORKING WITH NEGATIVE INDEX SLICING ==== !important
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# to print all the elements from last
print(f"The elements from the last of the list are {numbers_list[::-1]}")

# to print the 5,6 and 7 from the above numbers_list
print(numbers_list[-4:-1])  # output [5, 6, 7]


# === OVERSHOOTING === 
'''
-> If start and stop overshoot the list boundaries, Python will not raise an error.
'''
print(numbers_list[100:200])  # ! no error, output: []


# ==== MODIFYING LIST WITH SLICING ==== !important
numbers_list[::2] = ['R', 'O', 'M', 'A', 'N']
print(f"Modified list using the slicing:  {numbers_list}")  # output- ['R', 1, 'O', 3, 'M', 5, 'A', 7, 'N']


# ===== Advanced Slicing Questions: ===== ! important
lst = [0, 1, 2, 3, 4, 5]

'''
1.->  If lst = [0, 1, 2, 3, 4, 5], what would lst[-2:1:-1] produce? '''
# Answer of question number one ...
'''
Ans description:
here, the list element starts from the -2 index stop at the 1 index with negative indexing
so, it will produce [4, 3, 2] 
'''

'''
2. How can you use slicing to get the last three elements of a list?

Ans---> 
To get the last three elements of the list, we should use the negative indinxing 
as it should starts from the -1 index and stop at the -4 index
i.e lst[-3:]
'''

# === Swaping list to seperate the first half and the second half === 
mid_len = len(lst) / 2
swapped_list = lst[3:] + lst[:3]
print(swapped_list)   # [3, 4, 5, 0, 1, 2]




