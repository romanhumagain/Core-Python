# Declare some variables
x = 10
y = 10
z = [1, 2, 3]
w = z

# Identity comparison using 'is'
print(x is y)  # True, as x and y have the same value and refer to the same object in memory

print(z is w)  # True, as z and w refer to the same list object in memory

# Identity comparison using 'is not'
print(x is not y)  # False, as x and y have the same value and refer to the same object in memory

print(z is not w)  # False, as z and w refer to the same list object in memory
