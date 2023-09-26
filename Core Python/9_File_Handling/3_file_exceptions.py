# ==== 1. Basics Exception Handling 'try', 'except' ====

try:
  file = open('file.txt')
  content = file.read()
  print(content) 
except Exception as e:
  print(f"The error occured {e}") 
  
# ==== 2. Handling Specific Exceptions ==== 

try:
  file = open('file.txt')
  content = file.read()
  print(content) 
except FileNotFoundError:
  print("The file was not found.") 
except PermissionError:
  print("You don't have permission to read the file.")


# ==== 3. else and finally in Exception Handling ====
try:
  my_file = open('pyfile.txt', "r")
  content = my_file.read()
  print(content)
except FileNotFoundError:
  print("The file was not found.") 
else:
  print()
  print("File opened successfully and printed the content.")
finally:
  try:
    my_file.close()
    print("File closed successfully!! ")
  except NameError:
    pass
  
# ==== 4. Raising Exceptions ====
file_name = 'example.txt'

if file_name.endswith(".txt"):
  raise ValueError(".txt file are not supported !!")