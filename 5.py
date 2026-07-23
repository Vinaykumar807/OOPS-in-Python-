# # Menu Driven Method :- 
# # A menu-driven program is a program that allows users to interact by choosing options from a menu.
# # These programs are commonly used in applications such as banking systems, shopping carts, or command-line utilities.
# # Menu-driven programs are typically implemented using loops and conditional statements (if-elif-else).



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


# # Banking system 

# def display_menu():
#     print("***Banking System***")
#     print("1.Check balance")
#     print("2.Deposite Money")
#     print("3.Withdraw Money")
#     print("4.Exit!!")
# balance = 0 

# while True :
#     display_menu()

#     choice = int(input("Enter your Choice(1-4) :"))

#     if choice == 1:
#         print(f"Total Balance = ",balance)
#     elif choice == 2 :
#         amount = int(input("Enter deposite amount = "))
#         balance += amount
      
#     elif choice == 3:
#         amount = int(input("Enter your Withdraw amount = "))
#         balance -= amount
       
#     elif choice == 4:
#         print("Exit!")
#         break
#     else :
#         print("Invalid option Try again!")

# Grocery store menu 

# def store_menu():
#     print("1. Add items to there carts ")
#     print("2.Remove items")
#     print("3.View the total price")
#     print("4.Exit")

# cart = []

# while True :
#     store_menu()

#     choice = int(input("Enter your chioce (1-4) :"))

#     if choice == 1 :
#         item  = input("Enter your items to add : ")
#         price = input ("Enter your price : ")
#         cart.append(item)
        
#     elif choice == 2:
#         item = (input("Enter your remove item : "))
#         if item in cart :
#             cart.remove(item )

#     elif choice == 3 :
#         print("Items : ",cart)
#         print("price : ",price )

#     elif choice == 4:
#         print("Exit!")
#         break
#     else :
#         print("Invalid choice try again !")




def contact_manage():
        print("1. Add Contact ")
        print("2. View Contact  ")
        print("3. Search Contact  ")
        print("4. Delete Contact ")
        print("5. Exit ")  
contacts = []

while True:
        contact_manage()
    
        choice = int(input("Enter Your Chioce (1-5) : "))

        if choice == 1 :
                add = int(input("Add a Contacts  :"))
                contacts.append(add)
        elif choice == 2 :
                print("Contacts are :",contacts)
        elif choice == 3 :
                search = int(input("Enter your Contacts : "))
                if search in contacts :
                        print("The contacts is avialabel!")
                else :
                        print("Sorry this contact is not avialabel")
        elif choice == 4 :
                delete = int(input("Enter you delete contact : "))
                if delete in contacts:
                        contacts.remove(delete)
                        print("Contacts is deleted")
                else :
                        print("Contacts not found !")
                        
        elif choice == 5 :
                print("Exit!")
                break
        else :
                print("Invail choice Try again !")
    