import statistics

data = [2, 4, 7,8, 8.8, 9.2]
avg = statistics.mean(data)

# Using the filter function to check the data less than and greater than the avg value

less_than_avg = list(filter(lambda x : x < avg, data))
print(less_than_avg)     # [2, 4]

greater_than_avg = list(filter(lambda x: x > avg, data))
print(greater_than_avg)  # [7, 8, 8.8, 9.2]

# Filtering the even number from the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_num = list(filter(lambda x: x % 2 == 0, numbers))
print(f"The list of the even number is {even_num}")  # [2, 4, 6, 8]

# Filtering a non empty string
strings = ["apple", "banana", "", "cherry", ""]
non_empty = filter(lambda x: x != "", strings)
print(list(non_empty))  # Output: ["apple", "banana", "cherry"]