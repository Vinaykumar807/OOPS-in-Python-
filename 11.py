# Decorators :- 
# Decorators allow us to modify the behavior of a function without changing its actual code.

# Example :- 

def welcome(func):
    def wrapper():             # This is a special function(we can use any name as a special function )
        print("Namaskara!")
        func()                 # Here we calling fucn function to wrapp
        print("Take care!")
    return wrapper

@welcome                  # Here we calling a welcome function to decorate and using @ to call the function 
def intro():
    print("I am Vinay from Karnataka.")


intro()                  # Output :-  Namaskara! 
                        #             I am Vinay from Karnataka
                        #               Take care!                   

# Decorator with Arguments 

def decorator_result(func):
    def wrapper(a,b):
        print("Result : ",end="")
        func(a,b)
    return wrapper

@decorator_result
def add(a,b):
    print(a+b)

add(3,4)

@decorator_result
def sub(a,b):
    print(a-b)

sub(5,2)