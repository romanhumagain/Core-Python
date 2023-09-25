'''
1-> Associativity defines the order in which operators of the same precedence are evaluated.
2-> Exponentiation(**) and assignment(==) are a right-associative i.e evaluated right to left
3-> Other operators are evaluated from left to right
'''

8 - 5 - 3   # It is evaluated as (8 - 5) - 3 = 0

# working with exponentiation
''' Exponentiation(**) is a right-associative i.e right to left '''
x = 2 ** 3 ** 2  # It is evaluated as 2 ** (3 ** 2) = 2 ** 9 = 512
print(x)

# Working with assignment operators
'''assignment operators are also right-associative'''
a = b = c = 5   # This means c = 5, then b = c, then a = b.


# left-to-right associativity
print(5 * 2 // 3) # 3

# Shows the right-left associativity of **
print(2 ** 3 ** 2)   # Output: 512, Since 2**(3**2) = 2**9

# If 2 needs to be exponated fisrt, need to use ()
print((2 ** 3) ** 2)  # Output: 64


'''
---- When in doubt, use parentheses: They make the order of operations explicit. ----
'''