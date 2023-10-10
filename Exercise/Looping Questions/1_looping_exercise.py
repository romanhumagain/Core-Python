# 1-> Basic Looping.
for num in range(1,10):
  print(num)
  
  
# 2-> Table of number.
try:
  num = int(input("Please Enter a number for its multiplication table. "))
  print(f"The multiplication table of {num} is: ")
  for i in range(1,11):
    mul = num * i
    print(mul)
except ValueError:
  print("Please Enter a Valid Integer Number !!")


# 3-> Factorial Calculation
n = int(input("Please enter a number to find its factorial:  "))
fact = 1

for i in range(n, 0, -1):
  fact *= i
print(f"The factorial of {n} is {fact}")


# 4-> Sum of Squares of the number
n = int(input("Enter a number for finding the sum of squares: "))
sum = 0
for i in range(1,n+1):
   square = i**2
   sum += square 
print(f"The sum of squares of a number from 1 to {n} is {sum}")


# 5-> To count the vowel letters 
str = input("Please Enter a string to count and print the vowel letters: ")
vowel_letters = ["a","e","i","o","u"] 
vowel_letters_count = 0

for char in str:
  if char in vowel_letters:
    vowel_letters_count += 1
    print(char)
print(f"The total number of vowel letters in {str} is {vowel_letters_count} ")