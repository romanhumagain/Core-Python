# using the min() and max() methods to find the lowest and highest value in an iterable

my_list = [4,5,34,76,34]
greatest_num = max(my_list)
smallest_num = min(my_list)

print(f"The greatest number in {my_list} is {greatest_num} ") # 76
print(f"The smallest number in {my_list} is {smallest_num}")  # 4

# using the abs value to find the absolute value (positive)

print(abs(-34.34))  # 34.34


# Using the pow() function to find the power of the certain value
my_pow = pow(3, 4)
print(my_pow)   # 81

# === To extends more python function ===
import math

x = math.sqrt(4)
print(x)   # 2.0

# using the math ceil() methods to round the number upwards to its nearest integer number
print(math.ceil(2.2))  # 3

# using the floor() methods to round the number downwards to its nearest value
print(math.floor(3.9))  # 3

# to get the value of the pi
print(math.pi)   # 3.141592653589793


angle = math.radians(90)  # Convert 90 degrees to radians
print(math.sin(angle))  # Outputs: 1.0 because sin(90°) = 1

