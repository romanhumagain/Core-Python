'''
-> Slicing means extracting a part of the string'''

'''
# SYNTAX
string_name[starting:ending:jump]
'''

myStr = "Lets Start Learning Python"
print(myStr[2:7])  # ts St

num_str = "123456789"
'''By Default starting and ending will be 0 '''
print(num_str[::2])  # 13579

# Using reverse slicing
print(num_str[::-1])  # 987654321