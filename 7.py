# SOLID Principles :- The SOLID principles are five guidelines that help us write clean, maintainable, and scalable object-oriented code. 
#    These are best practices followed by experienced developers to make code better.
# S = Single Responsibility Principle(SRP)
# O = Open/Closed Principle
# L = Liskov Substitution Principle
# I = Interface Segregation Principle 
# D = Dependency Inversion Principle

# 1. S = Single Responsibility Principle(SRP) :- 
# A class should have only one reason to change. That means, a class should do only one job.
# Example :- 

class Student :
    def __init__(self,name,marks):    # Giving one responsibility for one class 
        self.name = name 
        self.marks = marks

class SaveDatabase : 
    def save(self,student):
        print(f"Saving {student.name} database ")

class ReportCard:
    def repo(self,student):
        print(f"Genrating Report Card for {student.name} obtained marks {student.marks}")


# 2. O = Open/Closed Principle(OCP) :- 
# Software entities (classes, functions, etc.) should be open for extension but closed for modification.
# Example :- 

class Discount:
    def get_discount(self):
        return 0

class RegularCustomer(Discount):    # Here we did't modifing for new class or function 
    def get_discount(self):
        return 10

class PremiumCustomer(Discount): 
    def get_discount(self):
        return 20


# 3. L = Liskov Substitution Principle (LSP) :- 
# Subclasses should be able to replace their parent class without breaking the program.
# Example :- 

class Bird:
    def move(self):
        pass

class Sparrow(Bird):     # Here we using move keyword to get a correct output 
    def move(self):      # The program will be execute correctly without crashing 
        print("Flying...")

class Penguin(Bird):
    def move(self):
        print("Swimming...")


# 4. I = Interface Segregation Principle (ISP):- 
# Don’t force a class to implement methods it does not use.
# Python doesn’t have interfaces like Java/C#, but we can still follow this idea using base classes.
# Example :- 
class Workable:
    def work(self):  
        pass

class Eatable:   
    def eat(self):
        pass

class Human(Workable, Eatable):   
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class Robot(Workable):
    def work(self):
        print("Robot working")


# 5. D = Dependency Inversion Principle(DIP):- 
# High-level modules should not depend on low-level modules. Both should depend on abstractions.
# Example :- 

class InputDevice:
    def input(self):
        pass

class Keyboard(InputDevice):
    def input(self):
        return "User typing..."

class Mouse(InputDevice):
    def input(self):
        return "Mouse clicked"

class Computer:
    def __init__(self, device: InputDevice):
        self.device = device

    def get_input(self):
        return self.device.input()