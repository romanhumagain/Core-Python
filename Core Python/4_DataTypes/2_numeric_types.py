'''
there are three numeric data types in python i.e
int,
float,
complex

'''
x = 36      # int types represent the whole number
y = 45.6    # float types represent the real number
z = 3 + 4j  # complex types represent the complex number

# ==== WORKING WITH NUMERIC DATATYPES IN PYTHON =====

# changing int to float and vice-versa
newFloat = float(x)
newInt = int(y)

print("Integer to float :", newFloat)  # output: 36.0
print("Float to integer :", newInt)    # output: 45


# ==== Working with complex datatypes ==== 
complex1 = 4 + 6j 
complex2 = 5 + 7j

print("The sum of two complex number is", complex1 + complex2)  # output :- (9+13j)

print(complex1.real) # to get only the real number of the complex number excluding the imaginary part

# Convert the integer to the complex number
integer_value = 6
complex_value = complex(integer_value)
print("The value after converting the integer to the complex number is", complex_value) # output :- (6+0j)

# To provide the custom imaginary value 
complex_value = complex(integer_value, 9)
print("Converting the integer to the complex number including the imaginary part is", complex_value) # output :- (6+9j)



