# '''
# -> String formatting is the process of inserting a custom string or variable in predefined text
# '''

# # === OLD STYLE '%' FORMATTING ===

# # using the %s for string
# name = "Roman Humagain"
# print("Hello, %s!" % name)

# # using the %d and %f for integer and float respectively
# age = 20
# height = 5.7

# print("I am %d years old and my height is %.2f" % (age, height))

# # controlling the decimal place
# pi = 3.1415926
# print("Pi is approximately %.2f" % pi) # 3.14


# 2.`str.format() method`
# Basics uses

print("Hello {}".format("Roman Humagain"))

# using positional formatting
print("{0} and {1}".format("Apple", "Banana"))

# using name placeholder
print("my name is {fname} {lname}".format(fname = "Roman", lname = "Humagain"))

# formatting the number 
pi = 3.1415926
print("Pi is approximately {:.2f}".format(pi))  # Outputs: Pi is approximately 3.14


# ==== 3. F-Strings (Formatted String Literals):====

name = "Roman"
print(f"Hello, {name}!")

# Expression inside the f-sting
age = 30
print(f"In ten years, I'll be {age + 10} years old.")

# formatting within f-string
pi = 3.1415926
print(f"Pi is approximately {pi:.2f}")

