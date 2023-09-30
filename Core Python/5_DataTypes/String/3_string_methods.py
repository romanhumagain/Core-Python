# Some common string methods

my_str = "roman humagain"

# 1. capitalize()
'''-> Capitalize the first character of the string'''
print(my_str.capitalize())  # Roman humagain

# 2. upper()
'''-> Converts the all character into upper case'''
print(my_str.upper())  # ROMAN HUMAGAIN

# 3. lower()
'''-> Converts the all character into lower case'''
str1 = "RomAN HuMaGAiN"
print(str1.lower())  # roman humagain

# 4.title()
'''-> Converts the first character of each word into the capital letter'''
print(my_str.title())  # Roman Humagain

# 5. strip()
'''-> Removes any whitespace from the begining or the end of the string'''
str2 = "    Roman     Humagain    "
print(str2) #     Roman Humagain
# to remove the white spaces
print(str2.strip())  # Roman     Humagain

# 6. lstrip() and rstrip()
'''-> Removes the whitespaces from the left or the right side of the string, respectively'''
print("   hello    ".rstrip()) #    hello
print("   hello    ".lstrip()) # hello

# 6. replace(old, new)
'''-> Replaces substring'''
print("hello world".replace("world", "python"))  # hello python

# 7. split()
''' -> Splits string into a list where each word is a list item'''
print("Hello World".split())  # ['Hello', 'World']

#8. join(iterable)
first_str = "12345"
second_str = "abcde"
last_str = "@#$%^"

print("".join([first_str, second_str, last_str])) # 12345abcde@#$%^

# 9. startswith(prefix)
'''-> Determine if the string starts with a certain prefix or not'''
print(my_str.startswith("ro"))  # True

# 10. endswith(prefix)
'''-> Determine if the string ends with a certain prefix or not'''
print(my_str.endswith("an"))  # False

# 11. encode()
'''Returns an encoded version of the string'''
print(my_str.encode())

# 12. find()
'''
Syntax
string.find(value, start, end)
'''
new_str = "my name is roman humagain"
# To find in which index does a lies in between the index 2 and 5
print(new_str.find('a', 2, 5)) # 4

# 13. swapcase()
'''-> Swaps cases, lower case becomes upper case and vice versa '''
new_str1 ="mY namE IS rOman HuMAGAin"
print(new_str1.swapcase())  # My NAMe is RoMAN hUmagaIN

# 14. isalpha()
new_str2 = "CheckingWhetherthestringcontainonlystringornot"
'''Even if there will be any white spaces, it will return false'''
print(new_str2.isalpha())  # True

# 15. isalnum()
new_alnum = "Roman2342523462"
'''-> Returns true if the string contain only alpha numeric value'''
print(new_alnum.isalnum()) # True

# 16. isdigit()
new_digits = "5483939"
'''-> Return true if the string contain only digits '''
print(new_digits.isdigit())  # True 

