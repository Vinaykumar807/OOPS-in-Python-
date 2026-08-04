# Inheritance :-
# Inheritance allows a class to inherit attributes and methods from another class, facilitating reuse
# Real-World Example:- 
# Consider human families. Characteristics like surname, traditions, or physical features can be passed down from parents to children.

# Example 1 :- 

class user :
    def __init__ (self,username,):  
        self.username = username 
    def login(self):
        print(f"{self.username} looged in ")
    
class admin(user):            # Here we inherit the attributes and methods from class "user"
    def delete_user(self):    # Also we able to add new attributes and methods for new class 
        print("Admin deleted user ")

user1 = admin("Vinay")
user1.login()   

# Example 2 :- 

class Family:
    def __init__(self, surname):
        self.surname = surname

class Child(Family):
    def __init__(self, surname, name):
        super().__init__(surname)        # Here we using super() basically it is family class insted of using family here we are usign super() keyword 
        self.name = name

child = Child("Vinnu ", "VinayKumar")
print(f"{child.name} {child.surname}")  # Inherits surname from Family


# Polymorphism :- (Many , forms )
# Polymorphism allows objects of different classes to be treated as objects of a common superclass, 
# But they can behave differently depending on the object type.
# Real-World Example: 
# Think of animals making sounds—both dogs and cats make sounds, but each produces a distinct sound. 
# They share a common method make_sound(), but the output varies.

# Example :- 

class Animal:        # Animals is a class 
    def __init__ (self):
        pass

# Dog and Cat is a inheritance of animals and they make sounds diffrent form each other 

class Dog(Animal):        
    def make_sound(self):
        print("Barkssss!")  # This is Polymorphism behaviour 

class Cat(Animal):          
    def make_sound(self):
        print("Meowww!")     # This is Polymorphism behaviour 

animal1 = Dog()     # This is one method 
animal1.make_sound()
animal2 = Cat()
animal2.make_sound()

Animals = [Dog(),Cat()]  # This is another method 
for Animal in Animals:
    Animal.make_sound()
