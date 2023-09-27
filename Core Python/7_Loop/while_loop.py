# program to display numbers from 1 to 5

# initialize the variable
i = 1
n = 5

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1
    
    
# Programm to calculate the sum of numbers until the used write 0
total = 0
number = int(input("Enter a number: "))

while number != 0:
  total += number
  
  number = int(input("Enter a number: "))

print("Now Done !!")
print(f"The sum of total number is {total}")


# Python While loop with else
counter = 0

while counter < 3:
  print("Inside Loop!! ")
  counter += 1
  
else:
  print('Inside Else !!')
  
  
# Using the break keywords
counter = 0

while counter < 3:
    # loop ends because of break
    # the else part is not executed 
    if counter == 1:
        break

    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')
    
    
# Using the continue keywords
count = 0
while count <= 8:
  count += 1
  if count == 5:
    # if count is 5 skip the rest of the iteration below this
    continue
  
   # If count reaches 7, exit the loop
  if count ==7:
    break
  print(count)

  


