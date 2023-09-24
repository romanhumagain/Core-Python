# using nested if
x = 10

if x > 0:
    print("x is positive")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
else:
    print("x is non-positive")

# using multiple condition with logic gate
x = 10

if x > 0 and x % 2 == 0:
    print("x is a positive even number")
elif x > 0 and x % 2 != 0:
    print("x is a positive odd number")
else:
    print("x is non-positive")

# using if elif else chain
def switch_case(argument):
    if argument == 1:
        print("Sunday")
    elif argument == 2:
        print("Monday")
    elif argument == 3:
        print("Tuesday")
    elif argument == 4:
        print("Wednesday")
    elif argument == 5:
        print("Thursday")
    elif argument == 6:
        print("Friday")
    elif argument == 7:
        print("Saturday")
    else:
        print("Invalid case")

switch_case(2)  # Output: Monday
