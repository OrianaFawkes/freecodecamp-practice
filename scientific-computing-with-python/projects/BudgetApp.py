# Scientific Computing with Python Project 3
# Made by Oriana Fawkes '24

class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance
    
    def transfer(self, amount, another_category):
        self.withdraw(self, amount, description = f"Transfer to {another_category}")
        self.withdraw(self, amount, description = f"Transfer to {another_category}")
    def check_funds(self, amount):
        balance = self.get_balance(self)
        return False if amount > balance else True 


def create_spend_chart(categories):
    pass



food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))