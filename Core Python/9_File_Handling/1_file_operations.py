import os
'''
-> When we want to read or write to a file, we need to open a file first and
when we are done we need to close the file so that the resourses tied with the file will be freed.
'''

'''
# --- In Python file operations take place in the following order ---
1->. Open a file
2->. Read or Write 
3->. close a file
'''

# ==== Different Modes to Open a File in Python ====
'''
-------------------------------------------------
Mode                        Description
-----------------------------------------------
r                           open a file for reading. (default)
w                           open a file for writing. Create a file if not exist, else overwrite a file if exists.
x                           open a file for exclusive creation. If file exists, the operation fails
a                           append (creates a file if not exists or add to a end of the file.)

'''

# ==== OPENING A FILE ====
# Method 1
file1 = open("pyfile.txt", "r")  # open a file
 
read_file = file1.read()  # read a file 
print(read_file)          # print a content in a file
file1.close()             # closing a file after completing a file operations

# # Method 2
# # Using a with keyword to open a file so that it autometically closes a file

with open('pyfile.txt', "r") as file1:
  content = file1.read()
  print(content)
  
# Writing on a file
with open('newfile.txt', "w") as newfile:
  content = newfile.write("This is the new file created by using the file command to write.")
  
# Overwrite the existing content using the "w" mode, if the file exists and the content is there
with open('newfile.txt', "w") as newfile:
  content = newfile.write("New content after overwriting a previous text.")

# Using append
with open("pyfile.txt", 'a') as pyfile:
  content = pyfile.write("This is the appended text in this file.")


# === CHECKING IF A FILE EXISTS OR NOT ===

if os.path.exists('pyfile.txt'):
  print("Yes Exists")
else:
  print("Sorry! The file didn't exists.")

# # === DELETING A FILE IF EXISTS ===

if os.path.exists('deletefile.txt'):
  os.remove('deletefile.txt')
  print("file deleted")
else:
    print("Sorry! The file didn't exists.")


# # === DELETING A FOLDER  ===
os.rmdir("my_folder_name")




