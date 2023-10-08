# using random module to get the random value
import random

# To returns a random number between 0 to 1
print(random.random())  

# Using a randint(a,b) to return a random value from 'a' to 'b'
print(random.randint(1,10))

# Using the randrange(start, stop, step)
print(random.randrange(0,11,2))

# To return a random float number using uniform()
print(random.uniform(3,5))

# ==== Random Sequences =====

name_choices = ['roman', 'bijen', 'anup', 'anuj', 'pratab']
# to print a random name from the above choices
print(random.choice(name_choices))

# To pring the random 3 name from the above choices
print(random.choices(name_choices, k = 3))

# To suffle the sequence in-place
numbers = [4,5,3,5,7,8]
random.shuffle(numbers)
print(numbers)

# Using the sample(population, k): Returns a k length list of unique elements chosen from the population.
print(random.sample(name_choices, 4))
