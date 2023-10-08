fruits = {"apple", "banana", "cherry"}

# 1. add(element)

fruits.add("orrange") # {'banana', 'apple', 'orrange', 'cherry'}
print(fruits)

# 2. remove(element)
fruits.remove("banana")
print(fruits)   # {'apple', 'cherry', 'orrange'}

#  3. discard(element)
''' Removes the specified element from the set. Does nothing if the element is not found (doesn't raise an error). '''
fruits.discard("hahaha")
print(fruits)

#  5. clear()
fruits.clear()
print(fruits)  # set()

