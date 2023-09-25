'''
-> Differrent operator have different precedence levels.
-> Operator with higher presedence value are evaluated first.
'''
# === LIST OF THE OPERATOR PRECEDENCE, STARTING FROM HIGHEST PRECEDENCE

'''
1. Parentheses (), 
2. Exponentiation **,
3. Unary Operators: '+', '-'. i.e. (-x, +x )
4. Multiplication, Division, Floor Division, Modulus: i.e *, /, //, %
5. Addition, Subtraction: '+', '-'
6. Bitwise Shift Operators: '<<', '>>'
7. Comparison operators: ==, !=, <, <=, >, >=
8. Identity operators: is, is not
9. Membership operators: in, not in
10. Logical NOT: not
11. Logical AND: and
12. Logical OR: or
13. Conditional operator: if – else (ternary)
14. Assignment and compound assignment operators: =, +=, -=, *=, /=, etc.
'''

# === WORKING WITH EXAMPLE ===

x = 10 - 4 * 2  # Multiplication has higher precedence than subtraction
print(x)  # 2 

# Parentheses () has higher precedence
y = (10 - 4) * 2
print(y) # 12


# Precedence of or & and
meal = "vegetable"

money = 0

if meal == "vegetable" or meal == "sandwich" and money >= 2:
    print("Lunch being delivered")
else:
    print("Can't deliver lunch")

'''
This programms run if blocl even when the money is 0. 
It does not give the desired output since the precedence of and is higher than or
'''   


# We can get the desired output by using the ()
meal = "Fruit"
money = 0

if (meal == "Fruit" or meal == "Pizza") and money >= 2:
  print("Lunch being delivered !")
else:
  print("Can't deliver lunch")
