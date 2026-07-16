# Class and objects 

# Class :- It is a blueprint for creating objects. 
# It defines the attributes and behaviors of the objects created from it.

# Objects :- An object is an instance of a class. 
# Each object has its own attributes (data) and can perform actions through methods (functions)

# Example 1 

class mobile:             # This is a class (Buleprint of a mobile) 
    def __init__(self,name):   # This is a name attribute 
        self.name = name        
    
    def charge(self):        # Methods of mobiles 
        print(f"{self.name} this mobile is charging")  

mobile1 = mobile("Redmi note 13 pro")      # These are the objects based on the class 
mobile2 = mobile("Iphone 17 pro max")

mobile1.charge()       # Calling the functions 
mobile2.charge()        # Output of the both obj is (mobiles this mobile is charging)


# Example 2 

# Craeting a class student 

class student :
    def __init__(self,name,marks):   # adding a name and marks (Attributes)
        self.name = name 
        self.marks = marks 
        
    def display_info(self):        # Adding methods (marks , name )
        print("Name :",self.name)
        print("Marks :",self.marks)
        print()


# Creating a objects 

student1 = student("Vinay",90)
student2 = student("Shrusti",98)

student1.display_info()       # Calling a functions
student2.display_info()