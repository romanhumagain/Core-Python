# === Polymorphism with Class methods ====

'''
-> The below code shows how Python can use two different class types, in the same way. 
'''
class Nepal:
  def capital(self):
        print("Kathmandu is the capital of Nepal.")
 
  def language(self):
        print("Nepali is the most widely spoken language of Nepal.")
 
  def type(self):
        print("Nepal is a developing country.")
    
    
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")
        
obj_nepal = Nepal()
obj_usa = USA()

for country in (obj_nepal, obj_usa):
  country.capital()
  country.language()
  country.type()
  
# Output
'''
Kathmandu is the capital of Nepal.
Nepali is the most widely spoken language of Nepal.
Nepal is a developing country.
Washington, D.C. is the capital of USA.
English is the primary language of USA.
USA is a developed country.
'''