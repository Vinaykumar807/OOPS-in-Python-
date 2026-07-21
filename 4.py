# # Getter and Setter :- 
# # Getters and setters are methods that allow controlled access to an object's attributes.
# # Purpose:-
# # They help in validating data, protecting data from accidental modification, and providing controlled access.

# # Example :- 
# class Student:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age  # Private attribute

#     # Getter for age
#     def get_age(self): 
#         return self.__age

#     # Setter for age
#     def set_age(self, age):
#         if age > 0:  # Validation
#             self.__age = age
#         else:
#             print("Invalid age")

# # Usage
# student = Student("Anita", 20)
# print("Age:", student.get_age())        # Accessing age with getter
# student.set_age(21)                     # Modifying age with setter
# print("Updated Age:", student.get_age())


# Method overloading :-
# It has ability to define multiple methods with the same name but different parameters.
# Note :- 
# Python doesn’t support method overloading directly, 
# but we can achieve it by using default parameters or by handling varying numbers of arguments with *args or **kwargs.

# Example :- 

class calc:
    def add(self,a,b,c=0):  # here we assigning default value c = 0;
        print(a+b+c)

c = calc()
c.add(1,2)   # 2 parameters 
c.add(1,2,3) # 3 parameters 

# Method overriding :- 
# It allows a child class to provide a specific implementation for a method that is already defined in its parent class.
# Purpose: 
# It enables a child class to alter or extend the behavior of a parent class method.

# Example :- 

class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")  # Overrides the parent class method

# Usage
animal = Animal()
animal.sound()
dog = Dog()
dog.sound()  # Calls the overridden method in Dog class

# Super() Class :- 
# The super() function is used in child classes to call a method from the parent class, 
# Enabling access to inherited methods or attributes.

# Example 

class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def __init__(self,name ):
        self.name = name 
    def sound(self):
        super().sound()
        print(f"{self.name} is barking")  # Overrides the parent class method

dog = Dog("Doggyyy")
dog.sound()  
