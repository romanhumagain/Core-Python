# Tuples can contain other tuple in itself

# my_tuple = (2, 4, (1, 3), (0, 9))

# # Accessing the elements in from the nested_tuples
# print(my_tuple[2][0]) # 1

# === Iteration Over Nested Tuples === !important

nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
for outer_element in nested_tuple:
  for inner_element in outer_element:
    print(inner_element, end=" ")
  print()


# === Unpacking Nested Tuples ===
nested_tuple = (1, (2, 3, 4), (5, 6))
a, (b, c, d), (e, f) = nested_tuple

print(b) # 2
print(f) # 6
print(d) # 4
print(e) # 5


