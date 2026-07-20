# Pillar of OOPS :- 
# There are 4 Pillars 
# 1.Abstraction 2.Encapsulation 3.Inheritance 4.Polymorphism

# 1.Abstraction :- 
# Abstraction hides the complex inner workings of an object, exposing only the essential parts for interaction.
# Real-World Example: 
# Think about driving a car. You use the steering wheel and pedals to control the car, without needing to know the engine mechanics or braking systems.

# Example :- 

class car:
    def start(self):
        print("Car Started")
    def Accelerate(self):
        print("Car Accelerating")
    def brake(self):
        print("Car Stoped")
Car = car()
              # Abstacts complex internal working 
Car.start()
Car.Accelerate()
Car.brake()

# 2.Encapsulation :- 
# Encapsulation involves wrapping (covering) data and methods that operate on that data within one unit, such as a class. 
# This protects the data from external interference and misuse, improving security and maintainability. 
# Real-World Example: Imagine an ATM machine—you interact with a limited interface (e.g., withdraw, deposit, check balance) but do not have access to the inner mechanics or backend functions.

# Example :- 

class Account:
    def __init__(self, __balance):
        # self.balance = balance   # Public 
        # self._balance = balance  # When we write sigle underscore(_)before the var it indicates (Proctected attribute)
        self.__balance = __balance  # When we write double underscore(__)before the var it indicates (Private attribute)

    def display_balance(self):
        print("Total balance =",self.__balance)


    def debit(self, amount):
        self.__balance -= amount
        print(f"Debit = {amount}. New balance = {self.__balance}")

    def credit(self,amount):
        self.__balance += amount
        print(f"credit = {amount}. New balance =  {self.__balance}")

atm = Account(1000)
atm.display_balance()
atm.debit(500)
atm.credit(300)
atm.display_balance()





