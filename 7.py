# class employee:
#     def __init__(self,role,department,salary):
#         self.role = role 
#         self.department = department 
#         self.salary = salary
#     def show_details(self):
#             print(f"He has a {self.role} role in our company ")
#             print(f"He is belongs to {self.department} department ")
#             print(f"He get {self.salary} salary per month")

# class Engineer(employee):
#      def __init__(self, name,age):
#           self.name = name
#           self.age = age
#           super().__init__("Enginner","IT",200000)

# a = Engineer("Vinay",21,)
# a.show_details()


#  E commerce platform 

class Product:
    def __init__(self,item_name,item_id,price,stock,disscount):
        self.item_name = item_name
        self.item_id = item_id
        self.price = price
        self.stock = stock
        self.disscount = disscount

    def display_product(self):

        print("Product Name :- ",self.item_name)
        print("Product ID:- ",self.item_id)
        print("Price :- ",self.price)
        print("Sotocks :- ",self.stock)
        print("Disscount :- ",self.disscount)


class Cart():
    def __init__(self):
        self.products = []
        self.quantity = []

    def add_cart(self,products,quantity):
        self.products.append(products)
   
        self.quantity.append(quantity)
        

    def view_cart(self):

        if len(self.products) == 0:
            print("Empty Cart.")

        print("====CART====")
        for i in range(len(self.products)):
            product = self.products[i]
            quantity = self.quantity[i]

            

            print("Products:",product.item_name)
            print("Quantity:", quantity)
        print("=========")
        
            
class Customer :
    def __init__(self,name,number,id):
        self.name  = name 
        self.number = number
        self.id = id 
    def display_customer(self):
        print("Customer name : ",self.name)
        print("Customer ID : ",self.id)
        print("Customer Number: ",self.number)



product1 = Product()
product2 = Product("Headphone",102,5000,10,15)
product3 = Product("Phone",103,25000,15,8)

customer1 = Customer("Vinay",636615,101)
customer2 = Customer("Raju",997297,102)
customer3 = Customer("Shrusti",807335,103)

cart1 = Cart()


product1.display_product()
customer1.display_customer()
cart1.add_cart(product1)
cart1.view_cart()

print()
product2.display_product()
customer2.display_customer()

print()
product3.display_product()
customer3.display_customer()