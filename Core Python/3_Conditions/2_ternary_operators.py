'''
ternary operators" or "conditional expressions," provide a shorter way to express simple if-else conditions.
'''

'''
# SYNTAX 
[VALUE_IF_TRUE] IF [CONDITION] ELSE [VALUE_IF_FALSE]
'''

a = 10
b = 20
maximum = a if a > b else b
print(maximum)  # This will print 20



# to check odd or even number

def check_number(num):
  return "Even" if num % 2 == 0 else "Odd"

print(check_number(5)) # Odd



