class Bank:
    count=0 #class vaiable
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        Bank.count+=1
    @classmethod    
    def customer_count(self):
        return Bank.count  
    def deposit_amount(self,amount):#Instance Method
        self.balance+=amount
        print(f"amount {amount} deposited in {self.owner}")
    def widhdraw(self,amount):#Instance Method
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print(f"current balace is {self.balance}")   
    def __str__(self):
        return f"Student(name={self.owner}, age={self.balance})"
customer_01=Bank("avir",5000)
print(customer_01)
# customer_02=Bank("vir",5000)
# customer_03=Bank("ashutosh",5000)
# customer_04=Bank("ashu",5000)
# print(Bank.customer_count())
# print(customer_01.owner)
# print(customer_01.balance)
# customer_01.deposit_amount(1000)
# print(customer_01.balance)
# customer_01.widhdraw(3000)
# print(customer_01.balance)

# class Math:
#     @staticmethod
#     def is_even(n):
#         if n%2==0:
#             return True
#         else:
#             return False
#     @staticmethod
#     def double(n):
#         return n*2    
# print(Math.is_even(6))
# print(Math.double(6))