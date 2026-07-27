
print("***Bank System Simulation***")

class Account:
    def __init__(self,id,name):
        self.name = name 
        self.id = id 
        self._balance = 0 

    def check_balance(self):
        print(f"Balance : {self._balance}")

    def deposite(self,amount):
        self._balance += amount
        print(f"Deposit Successfull . Updated balance :  {self._balance}")

    def withdraw(self,amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdraw sucessfull . Updated balance : {self._balance}")
        else :
            print("Insufficient balance !")

class SavingAccount(Account):
    def cal_intrest(self):
        INTREST = 0.02
        intrest = self._balance * INTREST
        print(f"Intrest : {intrest}")


class CurrentAccount(Account):
    def withdraw(self,amount):
            OVERDRAFT_LIMIT = 1000
            if self._balance  + OVERDRAFT_LIMIT >= amount:
                self._balance -= amount
                print(f"Withdraw sucessfull . Updated balance {self._balance}")
            else :
                print("Insufficient balance !")
   

class Bank:
    def __init__(self,name,city):
        self.city = city
        self.name = name 
        self.__account = {}
    def create_account(self,id,holder_name,type):
        if type == "savings":
            new_account = SavingAccount(id,holder_name)
            print("Account craeted! ")
        elif type == "current":
            new_account = CurrentAccount(id,holder_name)
            print("Account Craeted! ")
        self.__account[id] = new_account
        return new_account

acc1 = Bank("SBI","Raichur")
s1 = acc1.create_account(1,"Vinay","savings")
c1 = acc1.create_account(2,"Shrusti","current")
s1.deposite(1000)
s1.withdraw(300)
s1.check_balance()
c1.deposite(300)
c1.withdraw(500)
c1.check_balance()

s1.cal_intrest()




    

    

