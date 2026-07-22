# # Simple Calculator :- 

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b

# def display_menu():
#     print("***Simple Calculator***")  
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit!")

# while (True) :
#     display_menu()

#     choice = int(input("Enter your choice (1-5): "))

#     if choice in {1,2,3,4}:
#             a = int(input("Enter your first number : "))
#             b = int(input("Enter your second number : "))

#     if choice == 1:
#             print("Result :",add(a,b))
#     elif choice == 2:
#             print("Result :",sub(a,b))
#     elif choice == 3:
#             print("Result :",mul(a,b))
#     elif choice == 4:
#             print("Result :",div(a,b))
#     elif choice == 5 :
#             print("Exit!!")
#             break
#     else :
#             print("Invaild chioce try agian!!!")


# Banking system 



def display_menu():
    print("1.Check balance")
    print("2.Deposite Money")
    print("3.Withdraw Money")
    print("4.Exit!!")
balance = 0 

while True :
    display_menu()

    choice = int(input("Enter your Choice(1-4) :"))

    if choice == 1:
        print(f"Total Balance = ",balance)
    elif choice == 2 :
        amount = int(input("Enter deposite amount = "))
        balance += amount
      
    elif choice == 3:
        amount = int(input("Enter your Withdraw amount = "))
        balance -= amount
       
    elif choice == 4:
        print("Exit!")
        break
    else :
        print("Invalid option Try again!")