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

class Cart ():
    def __init__(self,product,quntity):
        self.product = product
        self.quntity = quntity

    def add_cart(self):
        self.product + self.quntity
        print("Cart has : ",self.product)

    def view_cart(self):
        print("Cart has : ",self.product)

    def remove_cart(self):
        self.product - self.quntity
        print("Cart removed : ",self.product)

class Customer :
    def __init__(self,name,number,id):
        self.name  = name 
        self.number = number
        self.id = id 
    def display_customer(self):
        print("Customer name : ",self.name)
        print("Customer ID : ",self.id)
        print("Customer Number: ",self.number)



product1 = Product("Laptop",101,55000,10,10)
product2 = Product("Headphone",102,5000,10,15)
product3 = Product("Phone",103,25000,15,8)
cart1 = Cart("Laptop","10")
customer1 = Customer("Vinay",636615,101)
customer2 = Customer("Raju",997297,102)
customer3 = Customer("Shrusti",807335,103)
product1.display_product()
cart1.add_cart()
cart1.remove_cart()
customer1.display_customer()
print()
product2.display_product()
customer2.display_customer()
print()
product3.display_product()
customer3.display_customer()