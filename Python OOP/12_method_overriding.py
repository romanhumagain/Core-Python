''''
-> Overriding deals with two methods, one in the parent class and one in the child class,
where the method in the child class override the method in the parent class
'''
# === Basics Example ====

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):  # Overriding the parent class method
        return "Woof"

class Cat(Animal):
    def speak(self):  # Overriding the parent class method
        return "Meow"

animal = Animal()
dog = Dog()
cat = Cat()

print(animal.speak())  # Some sound
print(dog.speak())     # Woof
print(cat.speak())     # Meow


# ==== Working with more method overriding =====

class Shape:
  def area(self):
    print("Calculating area of the generic shape.")

class Rectangle(Shape):
  def __init__(self, length, breadth):
    self.length = length
    self.breadth = breadth
    
  def area(self):
    print(f"The area of rectangle is {self.length * self.breadth}")
    
class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
    
  def area(self):
    print(f"The area of circle is {3.14 * self.radius ** 2}")


# Create instances of the Rectangle and Circle classes
shape_obj = Shape()
rectangle_obj = Rectangle(4,5)
circle_obj = Circle(5)

shape_obj.area()      # Calculating area of the generic shape.
rectangle_obj.area()  # The area of rectangle is 20
circle_obj.area()     # The area of circle is 78.5