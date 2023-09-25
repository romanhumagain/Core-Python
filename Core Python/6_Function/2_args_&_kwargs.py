# Arbitary Arguments (*args) 
'''
-> If you're unsure about the number of arguments, use *args.
'''

def fruits(*args):
  for fruit in args:
    print(fruit)
  
fruits('Apple', 'Banana', 'Orange')

def my_func(arg1, *args):
  print(f"First argument is {arg1}")
  for arg in args:
        print("Next argument through *argv :", arg)
        
my_func('Hello', 'Welcome', 'to', 'Python World')

# Keyword Arguments
'''
-> Allows you to pass arguments using keyword=value syntax.
'''
def student_info(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}:- {value}")
    
student_info(name= "Roman Humagain" , email ="romanhumagain@gmail.com")


def myFun(arg1, **kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))
  
# Driver code
myFun("Hi", first='Python', mid='for', last='Change')
