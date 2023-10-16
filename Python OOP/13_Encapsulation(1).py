'''
-> Encapsulation describes the idea of wrapping the data and the methods.
-> This puts restriction on the accessing the variable and methods directly
-> This prevents the additional modification of the data.
-> To prevent accidential change, an object variable can only be changed by an object methods, those type of variable are called private variable

'''
class Computer:
  # Constructor
  def __init__(self, brand, price):
    # making the instance variable private
    self.__brand = brand
    self.__price = price
  
  # Getter method for the brand and the price
  def get_brand(self):
    return self.__brand
  def get_price(self):
    return self.__price
  
  # Setter methods to set the value for the brand and the price
  def set_brand(self, brand):
    self.__brand = brand
    
  def set_price(self,price):
    if price < 0:
      raise ValueError("Price cannot be less than 0.")
    else:
      self.__price = price
    
    
  def display(self):
    return f"Branb {self.get_brand()}, price {self.get_price()}"

laptop = Computer("Dell", 1000)
print(laptop.display())  # Brand: Dell, Price: 1000

print(laptop.get_brand())  # Dell

laptop.set_price(-10)  # ValueError: Price cannot be less than 0.
