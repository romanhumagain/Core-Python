# Using lamda function, map and the filter
# Program to get the even number first and then square the even numbers

numbers = [2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x : x%2 ==0, numbers))
squared = list(map(lambda x : x**2, even_numbers))

print(squared)
