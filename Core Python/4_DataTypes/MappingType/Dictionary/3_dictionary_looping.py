my_dict =  {'name': "Roman Humagain",
            'age':20, 
            'College':'PCPS College',
            'Course': 'Software Engineering' }

# Looping to get the keys of the dictionary
for key in my_dict:
  print(key)
  
# Looping to get the value from the dictionary
for value in my_dict.values():
  print(value)
  
# Looping to get the both pair of keys and value
for key, value in my_dict.items():
  print(f"{key} :  {value}")
  
# Looping for the nested dictionary

nested_dict = {
    'user1': {'name': 'Roman', 'age': 20},
    'user2': {'name': 'Unknwon', 'age': 25},
}

for outer_key, inner_dict in nested_dict.items():
  print(outer_key)
  for inner_key , inner_value in inner_dict.items():
    print(f"{inner_key}:{inner_value}")
  print()


