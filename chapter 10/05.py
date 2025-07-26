
class bankAccount:
    
    def __init__(self,amount):
        self.balance=amount# Use 'balance' to store the current amount

    def deposit(self,d):
        self.balance +=d
        print(f" your deposit your amount : {d}")

    def withdraw(self,w):
        if self.balance>=w:
            self.balance -=w
            print(f"withdraw your amount is : {w}")
        else:
            print("insuficent balance")


    def get_balance(self):
        print(f"your current balance is : {self.balance}")
    @staticmethod
    def thank():
        print("thanks for our service and please be aware for any scam")
b=bankAccount(10000)
# b.name="zaryab"
b.withdraw(1000)
b.deposit(2000)
b.get_balance()
b.thank()