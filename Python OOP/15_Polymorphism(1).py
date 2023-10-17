'''
-> The Word polymerphism means having many forms
-> Polymerphism means the same function name (but different signatures) being used for different types.
'''
# Python program to demonstrate the built-in polymorphic function

# len() being used for the string
print(len("Roman")) # 5

# len() being used for a list
print(len([20, 10, 30, 80])) # 4


# A simple Python function to demonstrate 
# Polymorphism
 
def add(x, y, z = 0): 
    return x + y+z
 
# Driver code 
print(add(2, 3))
print(add(2, 3, 4))


