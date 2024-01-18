# Scientific Computing with Python Project 3
# Made by Oriana Fawkes '24

import math 

class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        output = self.category.center(30, "*") + "\n"
        for item in self.ledger:
            output += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": f"{description}"})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": f"{description}"})
            return True
        return False
    
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, description = f"Transfer to {other.category}")
            other.deposit(amount, description = f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        balance = self.get_balance()
        return not amount > balance

def create_spend_chart(categories):
    bar_chart = 'Percentage spent by category\n'
    spend_per_category = []
    
    for item in categories:
        proxy = 0
        for item in item.ledger:
            if item["amount"] < 0:
                proxy += item["amount"]
        spend_per_category.append(proxy * -1)

    spend_sum = sum(spend_per_category)
    print(spend_sum, str(spend_per_category))

    for index in range(len(spend_per_category)):
        spend_per_category[index] = math.floor(spend_per_category[index]/spend_sum * 100)
    print(spend_sum, str(spend_per_category))
    
    # Percents and Bars
    for percent in range(100, -1, -10):
        bar_chart += f'{percent:3}|'
        for index in range(len(categories)):
            if spend_per_category[index] >= percent:
                bar_chart += ' o '
            else:
                bar_chart += '   '
        bar_chart += ' \n'
    bar_chart += '    -' + '---'*len(categories) + '\n'
    
    # Categories
    max_height = max([len(str(item.category)) for item in categories])
    for index in range(max_height):
        bar_chart += '    '
        for item in categories:
            if len(item.category) > index:
                bar_chart += f' {item.category[index]} '
            else:
                bar_chart += '   '
        if index < max_height - 1:
            bar_chart += ' \n'
        else:
            bar_chart += ' '

    return bar_chart

# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# print(food)
# print(clothing)

# print(create_spend_chart([food, clothing, auto]))

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))