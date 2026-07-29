class employee:
    def __init__(self,role,department,salary):
        self.role = role 
        self.department = department 
        self.salary = salary
    def show_details(self):
            print(f"He has a {self.role} role in our company ")
            print(f"He is belongs to {self.department} department ")
            print(f"He get {self.salary} salary per month")

class Engineer(employee):
     def __init__(self, name,age):
          self.name = name
          self.age = age
          super().__init__("Enginner","IT",200000)

a = Engineer("Vinay",21,)
a.show_details()
