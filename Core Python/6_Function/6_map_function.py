'''
-> The map function is used to apply a function to all the items in an input list,
(or any other iterable)

-> '''

# ==== WORKING FLOW OF MAP() ====
'''
Data: a1, a2, a3
function: f

map(f, data)

returns a iterator over
f(a1), f(a2),.....,  f(an)

'''


# Basic syntax of the map() function
''' map(function, interable,  ....) '''

# Using map with the user defined functions

def square(num):
  return num * num

numbers = [2, 4, 6, 7, 8]
squared_number = list(map(square, numbers))
print(squared_number)   # [4, 16, 36, 49, 64]


# Multiple iterable and using the lamda function

numbers1 = [1, 3, 5, 7, 9]
numbers2 = [2, 4, 6, 8, 10]

result = list(map(lambda x,y: x + y, numbers1, numbers2))
print(result)   # [3, 7, 11, 15, 19]


# List containing the list of tuple , each tuples containing the data of the city with temp in celcious
# Converting the temperature in fehrenheit
temps = [('Kathmandu',20), ('Pokhara',30), ('Birjung',40)]

celcius_to_fehrenheit = lambda data: (data[0], (9/5)*data[1]+32)

temps_details = list(map(celcius_to_fehrenheit,temps))
print(temps_details)