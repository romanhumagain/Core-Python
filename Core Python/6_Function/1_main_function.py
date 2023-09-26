'''
-> In Python, a common practice is to define a main() function to encapsulate the main execution code of a script.
You might often see this pattern combined with the if __name__ == '__main__': line at the bottom of scripts.

'''

# ==== What is __name__ in Python? ====
''' __name__ variable is a special built in variable that shows the current name of the module
'''

# Using __name__ function to print the current module name
print(__name__)  # Output : __main__


def main():
  print("This is the statement inside the main function !!")
  
# Using the main function to call the function

if __name__ ==  '__main__':
  main()
  
  