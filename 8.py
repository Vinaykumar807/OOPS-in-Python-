# Errors and Exception Handling
# Error :- An error is a problem in a program that stops the execution.
# Two types of error :- 1. Syntax Errors 2. Exceptions

# Example os syntax error :- 
 
# if True                   # Missing colon
#     print("Hello")

# Example of Runtime Exception

a = 10
b = 0
print(a / b)       # Output :- ZeroDivisionError: division by zero


# Exception Handling :- 
# Exception Handling is a way to protect your program from crashing when an error occurs.

# Basic Structure :- 


try:                      # Code that may raise an exception (may be raise an error)
    pass
except Exception:    # What to do if error happens (if an error occur what should we do ! )
    pass
else :                    # Run if no error
    pass
finally :                 # Always run (cleanup, close file, etc.)
    pass

# 1.Example :- 
 
a = int(input("a : "))
b = int(input("b : "))

try : 
    print(a/b)
except Exception as e :
    print("Error ! ",e)
else : 
    print("All Good")
finally : 
    print("Program Ended ! ")

# 2. Example :- 

try : 
    bat = input("Bat : ")
    if bat != "MRF" : 
        raise Exception ("You selected wrong bat ! ")  # Here we using "raise" keyword so we can raise a own exception (Error)
except Exception as e: 
    print("Error ! ",e)
else : 
    print("You selected correct bat !!")