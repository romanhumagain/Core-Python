# Looping through a list...
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)
  
# Looping through a string...
my_str = "Roman"
for char in my_str:
  print(char)
 
# Using the range() function

for i in range(5):  # prints numbers 0 through 4
    print(i)

for i in range(2, 5):  # prints numbers 2 through 4
    print(i)
    
# Using range function with start, stop, and step
for i in range(0, 10, 2):
  print(i)
  

# Using break and continue
for i in range(5):
  if i == 3:
    break
  print(i)


for i in range(5):
  if i == 3:
    continue
  print(i)
  

# ==== Using nested loop ====
for i in range(3):
  for j in range(3):
    print(i, j)