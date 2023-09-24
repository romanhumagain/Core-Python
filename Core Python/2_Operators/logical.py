# Logical operators are used to combine conditional statements:

# Logical AND (and):
x = 5
y = 10

if x > 0 and y < 15:
    print("Both conditions are True.")
else:
    print("At least one condition is False.")

# Output: Both conditions are True.

# Logical OR (or):
x = 5
y = 20

if x > 10 or y < 15:
    print("At least one condition is True.")
else:
    print("Both conditions are False.")

# Output: At least one condition is True.

# Logical NOT (not):
x = 5

if not x > 10:
    print("The condition is False.")
else:
    print("The condition is True.")

# Output: The condition is True.