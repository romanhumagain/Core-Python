'''
-> Anonymous function is also known as lamda function.
-> Lamda function is that type of function which dont need the function name.
-> It can have any number of arguments but can only have one expression.
'''
expression = None

# Syntax of the lamda function.
lambda arguments : expression

# The expression is executed when the lamda function is called

greet = lambda:print("Hello Roman")
greet()  # Hello Roman


# Basic lamda function
new_func = lambda x : x +5
print(new_func(5))  # 10

# Lamda with multiple arguments
new_func1 =  lambda x,y,z : x + y * z
print(new_func1(2, 4, 4))  # 18

# To find the greatest number between two numbers
lamda_func = lambda num1, num2: num1 if num1>num2 else num2
print(f"The greates number is {lamda_func(5,4)}")


# Using lambda with map() to double each item in a list
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x*2, nums))
print(doubled)  # This will output [2, 4, 6, 8]

# Using lambda with filter() to get even numbers from a list
evens = list(filter(lambda x: x%2 == 0, nums))
print(evens)  # This will output [2, 4]

