'''
-> A decorator in python is a design pattern that allows you to add new functionality to an existing object
'''


# Working with basic decorators
def my_decorators(func):
  def wrappers():
    print("Something is happening before the function is called.")
    func()
    print("Something is happening after the function is called. ")
    
  return wrappers

# using decorator here
@my_decorators
def say_hello():
  print("Hello !!")

# Calling the function 
say_hello()


# Let's create a decorator called repeat that will repeat the execution of a function based on a provided number:

def repeat(times):
  def decorators_repeat(func):
    def wrappers(*args, **kwargs):
      for _ in range(times):
        result = func(*args, **kwargs)
      return result
    return wrappers
  return decorators_repeat


@repeat(3)  
def say_hello(name):
  print(f"Hello {name}")
  
say_hello("Roman")


# Decorators using args and kwargs

def simple_decorators(func):
  def wrappers(*args, **kwargs):
    print(f"Function {func}() is called with arguments {args} and keywords arguments {kwargs} ")
    return func(*args, **kwargs)
  return wrappers

@simple_decorators
def greet(name, greeting = "Hello"):
  print(f"{greeting}, {name}")
  
greet("Roman")