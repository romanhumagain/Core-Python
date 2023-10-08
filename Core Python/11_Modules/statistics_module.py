import statistics

# Mean: The average of all numbers.
data = [1, 2, 3, 4, 5]
avg = statistics.mean(data)
print(avg)  # Output: 3.0


data = [1, 3, 3, 5, 7]
med = statistics.median(data)
print(med)  # Output: 3

# Mode: The value that appears most frequently.
data = [1, 2, 2, 3, 3, 3, 4]
mode_value = statistics.mode(data)
print(mode_value)  # Output: 3

# Variance: A measure of the spread between numbers in a data set.
data = [1, 2, 3, 4, 5]
var = statistics.variance(data)
print(var) 


data = [1, 2, 3, 4, 5]
h_mean = statistics.harmonic_mean(data)
print(h_mean)
