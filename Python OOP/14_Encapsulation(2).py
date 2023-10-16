'''
-> In python, instead of traditional getter and setter methods, 
we typically use the `property` decorators. This allows us to define 
methods for getting and setting attributes
'''

'''
1. @property: For defining the getter method.
2. @attribute_name.setter: For defining the setter method.

'''

class Computer:
  def __init__(self, brand, price):
    self.__brand = brand
    self.__price = price
    
  # For getter method we use `@property` decorators
  @property
  def brand(self):
    return self.__brand
  
  # For setter methods we use `attributes_name.setter` decorators
  @brand.setter
  def brand(self,brand):
    if not brand:
      raise ValueError("Brand cannot be empty !")
    
  @property
  def price(self):
    return self.__price

  @price.setter
  def price(self, price):
    if price <0 :
      raise ValueError("Price cannot be less than 0.")
    else:
      self.__price = price
      
  def display(self):
     return f"Brand: {self.brand}, Price: {self.price}"
  
laptop = Computer("Dell", 1000)
print(laptop.display())  # Brand: Dell, Price: 1000

# Using properties to change the brand and price
laptop.brand = "HP"
laptop.price = 1200

print(laptop.display())  # Brand: HP, Price: 1200

# The below statement will raise a ValueError due to our setter validation
# laptop.price = -100

print(laptop.price)  # 1200
 
