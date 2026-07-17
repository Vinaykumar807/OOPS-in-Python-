# # Constructor and self keyword 

# # Constructor :- The __init__() method in Python is a special method that initializes an object when it’s created. 
# # It’s called automatically when you create a new instance of a class.
# # Basically in a class creating a object using constructor 

# # Example 

# class name:
#     def __init__(self,name1,name2):     # Constructor 
#         self.name1 = name1
#         self.name2 = name2


# class Body:
#     def __init__ (self,parts):        # This is a constructor part 
#         self.parts = parts            
#     def mouth(self):
#         print(f"{self.parts} is used to eating and talking")

# mouth1 = Body("Mouth")

# mouth1.mouth()

# Self Keyword :- 
# self: Refers to the instance of the class itself, allowing you to access attributes and methods within a class

class person:
    def __init__ (self,name,age):   # This is a self keyword 
        self.name= name
        self.age = age 
    def eat(self):           # It is a mandatory to write self keyword in a method 
        print(f"{self.name} {self.age} years old and eating a pizza")
    

v = person("Vinay",20)

v.eat()
