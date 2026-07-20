# Getter and Setter :- 
# Getters and setters are methods that allow controlled access to an object's attributes.
# Purpose:-
# They help in validating data, protecting data from accidental modification, and providing controlled access.

# Example :- 
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age  # Private attribute

    # Getter for age
    def get_age(self): 
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:  # Validation
            self.__age = age
        else:
            print("Invalid age")

# Usage
student = Student("Anita", 20)
print("Age:", student.get_age())        # Accessing age with getter
student.set_age(21)                     # Modifying age with setter
print("Updated Age:", student.get_age())