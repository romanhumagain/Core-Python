# 1-> Write a Python `for` loop that prints the numbers from 1 to 5.
for i in range(1,6):
    print(i)

# 2-> Create a Python `for` loop that calculates the sum of all numbers from 1 to 10.
sum = 0
for i in range(1,11):
    sum += i
print(f"The sum of number from 1 to 10 is {sum}")

# 3-> Write a Python `for` loop to iterate over a list of fruits and print each fruit's name.
fruits_list = ["apple", "banana", "mango"]
for fruit in fruits_list:
    print(fruit)

'''4. Create a Python `for` loop that counts the number of vowels (a, e, i, o, u) in a given string. (Also
use upper()or lower())'''

vowels_letters = ["a", "e", "i", "o", "u" ]
my_str = "Roman Humagain"
count = 0
for vowel in vowels_letters:
    if vowel in my_str:
        count += 1
print(f"There are {count} vowels letter in string: {my_str}")
print(my_str.upper())
print(my_str.lower())

# 5. Write a Python `for` loop to find and print all even numbers between 1 and 20.
for i in range(1,21):
    if i%2 == 0:
        print(i)

# 7. Create a Python `for` loop that prints the squares of numbers from 1 to 5.
for i in range(1,6):
    print(i**2)

# 8. Write a Python `for` loop to find and print the factorial of a given number `n`.
n = int(input("Please enter a number to find its factorial. "))
factorial = 1

for i in range(n,0,-1):
    factorial *= i
print(f"The factorial of {n} is {factorial}")


# 9. Create a Python `for` loop to iterate over a list of names and print a greeting for each name.
names = ["Roman", "Anuj", "Anup", "Pratab"]

for name in names:
    print(f"Hello {name}")



# 11. Create a Python `for` loop to find and print the largest number in a list of integers.
numbers = [3, 56, 22, 10, 90, 87, 44]
largest_number = None

for number in numbers:
    if largest_number == None:
        largest_number = number
    else:
        if number > largest_number:
            largest_number = number

print(f"The lergest number is {largest_number}")