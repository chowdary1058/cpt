'''class a:
    def __init__(self,name,age,gender):#constructor
        self.__name=name#its a private varible 
        self.age=age#proteced varile
        self.gender=gender#public variable 
a1=a("sai",21,"male")
a2=a("kishore",22,"male")

print(a1.age)
print(a2.name)'''
class bankaccount:
    def __init__(self,account_number,account_holder_name,balance):
        self.account_number=account_number
        self.account_holder_name=account_holder_name
        self.__balance=balance#private variable

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance