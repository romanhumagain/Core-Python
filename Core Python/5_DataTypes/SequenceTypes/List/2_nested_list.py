'''
-> Creating list inside list is said to be the nested list.
'''
nested_list = [['Roman', "Humagain"], [20, 69], ['BSC Hons']]

# to get the first sublist
first_sublist = nested_list[0]
print(first_sublist)  # output: ['Roman', 'Humagain']

# to get the specific element from the first_subset
print(f"Element at the 0 index is {first_sublist[0]}")

# shortcut method for this ^
print(f"Elements at the 0 index is {nested_list[0][0]}")

# to modify the sublist
nested_list[1] = [36, 36.69]
print(nested_list)  # output:- [['Roman', 'Humagain'], [36, 36.69], ['BSC Hons']]

# to modify certain elements at the sublist

nested_list[0][0] = "Mr Roman"
print(nested_list)




