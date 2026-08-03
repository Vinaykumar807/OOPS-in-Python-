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
        print("Stocks :- ",self.stock)
        print("Disscount :- ",self.disscount)

    def update_stock(self,quantity):       
            self.stock =  self.stock - quantity
            print("Stock Updated :",self.stock)

          
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
        

    def remove_cart(self, product):
        
                if product in self.products:

                    index = self.products.index(product)

                    self.products.remove(product)

                    self.quantity.pop(index)

                    print(product.item_name, "removed successfully")

                else:
                     print("Product not found in cart")


    def update_quantity(self,product,new_quantity):
         
         if product in self.products:
              
              index = self.products.index(product)

              self.quantity[index] = new_quantity

              print("Quantity Updated : ",new_quantity)

            
class Customer :
    def __init__(self,name,number,id):
        self.name  = name 
        self.number = number
        self.id = id 

    def display_customer(self):
        print("Customer name : ",self.name)
        print("Customer ID : ",self.id)
        print("Customer Number: ",self.number)

class Order() :
    def __init__(self,customer,cart,order_id,status = "Pending"):
        self.customer = customer
        self.cart = cart    
        self.order_id = order_id
        self.status = status
        
    def place_order(self):

       print("=====ORDER=======")
         
       print("Order ID : ",self.order_id)
       print("Customer Name : ",self.customer.name)
       print("Customer id : ",self.customer.id)
       print("Status : ",self.status )

    def calculate_total(self):
        total = 0 

        for i in range(len(self.cart.products)):
            product = self.cart.products[i]
            quantity = self.cart.quantity[i]

            subtotal =  product.price * quantity 
            total = total + subtotal

        print("Total : ", total)

        print("==============")



    def order_status(self):
        print("====== ORDER STATUS ======")
        print("Order ID :", self.order_id)
        print("Customer :", self.customer.name)
        print("Status   :", self.status)
        print("==========================")

    def change_status(self, new_status):
        self.status = new_status
        print("Status Updated Successfully!")
        print("Status: ", self.status)

    def final_bill(self):

        print("===== FINAL BILL =====")

        print("Order ID :", self.order_id)
        print("Customer :", self.customer.name)
        print("Status :", self.status)

        total = 0

        for i in range(len(self.cart.products)):

            product = self.cart.products[i]
            quantity = self.cart.quantity[i]

            subtotal = product.price * quantity
            total = total + subtotal

            print("Product :", product.item_name)
            print("Quantity :", quantity)
            print("Subtotal :", subtotal)
            print("----------------")

        print("Grand Total :", total)

        print("======================")
               


product1 = Product("Laptop",101,55000,10,10)


customer1 = Customer("Vinay",636615,1)


cart1 = Cart()
cart2 = Cart()
order1 = Order(customer1,cart1,1001,)


product1.display_product()
product1.update_stock(3)
customer1.display_customer()
cart1.add_cart(product1,2)

cart2.view_cart
cart1.view_cart()
cart1.update_quantity(product1,5)

order1.place_order()
order1.calculate_total()
order1.change_status("Shipped")
order1.order_status
order1.final_bill()
