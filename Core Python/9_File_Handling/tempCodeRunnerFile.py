# ==== 1. Basics Exception Handling 'try', 'except' ====

# try:
#   file = open('file.txt')
#   content = file.read()
#   print(content) 
# except Exception as e:
#   print(f"The error occured {e}") 
  
# # ==== 2. Handling Specific Exceptions ==== 

# try:
#   file = open('file.txt')
#   content = file.read()
#   print(content) 
# except FileNotFoundError:
#   print("The file was not found.") 
# except PermissionError:
#   print("You don't have permission to read the file.")