# ==== Boolean data types in python ====

x = True
y = False

# to check the type of the variable
print(type(x))    # output <class 'bool'>

# === Converting the other datatypes to the boolean types

'''

-> By default, any non zero or non empty will return a boolean value of True
-> Zero, empty strings, empty lists/tuples/dicts/sets, None will be converted to False.

'''

a = "roman humagain"
bool_a = bool(a)
print("bool value of a is" , bool_a)

b = ""
bool_b = bool(b)
print("bool value of b is" , bool_b)

c =[ "roman", "humagain"]
bool_c = bool(c)
print("bool value of c is" , bool_c)

d = []
bool_d = bool(d)
print("bool value of d is" , bool_d)

# ==== to check true or false ====
print(5 == 5)
print(5 != 9)


newString = "Roman Humagain"

if "R" in newString:
  print("Yes there is R in newString ")
else:
  print("Sorry not there !!")