# ==== To take input from the user, input() function is used ====

# taking a float number from the user and converting into integer 

num = int(input("Enter a float number !")) # displays error, as in  python integer can not be automatically converted into float and then in integer

# ValueError: invalid literal for int() with base 10: '45.'

print(num)

# Taking a integer value from the user and then converting it to the float
''' It won't display error as float suppport the multi casting like first it takes the integer value as a string, 
and then it convert it into the float.
'''
float_num = float(input("Enter a integer value."))
print(float_num) # 5.0