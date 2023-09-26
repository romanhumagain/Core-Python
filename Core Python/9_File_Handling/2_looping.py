# Looping line by line through the content in the file

with open('pyfile.txt') as file:
  file_line = file.readlines()
  for line in file_line:
    print(line)