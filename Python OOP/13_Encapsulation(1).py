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



class Car:
  def __init__(self, windows, price, engine_type):
    self.__window = windows
    self.__price = price
    self.__engine_type = engine_type
    
  # Using getter methods for the windows, price and engine_type
  @property
  def window(self):
    return self.__window
  
  @property
  def price(self):
    return self.__price
  
  @property
  def engine_type(self):
    return self.__engine_type
  
  # Using setter methods for the windows, price and engine_type
  @window.setter
  def window(self, window):
    self.__window = window
    
  @price.setter
  def price(self, price):
    if price < 0:
      raise ValueError("Price Should Be Greater Than 0. ")
    else:
      self.__price = price
      
  @engine_type.setter   
  def engine_type(self, engine_type):
    self.__engine_type = engine_type
  
  
  def display_details(self):
    return f"Windows: {self.__window}, Price: {self.__price}, engine type: {self.__engine_type}"
  
car_obj = Car(4, 4000000, "EV")
print(car_obj.engine_type)  # EV

car_obj.price = 20000
car_obj.engine_type = "Diesel"

print(car_obj.display_details())
# car_obj.set_engineType("Diesel")
# print(car_obj.get_engine_type())  # Diesel

# car_obj.set_price(-2)
  
  

  
    