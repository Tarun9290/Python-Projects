#Budget Tracker: 
#A program that allows the user to track their income and expenses. 
#The program calculates the current balance and allows the user to view a history of their transactions.

class Transaction:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def view_history(self):
        for transaction in self.transactions:
            print(f"{transaction.description}: {transaction.amount}")

    def get_balance(self):
        balance = 0
        for transaction in self.transactions:
            balance += transaction.amount
        return balance

def main():
    budget_tracker = BudgetTracker()
    while True:
        print("1. Add transaction")
        print("2. View history")
        print("3. Get balance")
        print("4. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            budget_tracker.add_transaction(Transaction(description, amount))
        elif choice == 2:
            budget_tracker.view_history()
        elif choice == 3:
            balance = budget_tracker.get_balance()
            print("Current balance:", balance)
        elif choice == 4:
            break

if __name__ == '__main__':
    main()
