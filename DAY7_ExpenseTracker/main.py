from dataclasses import dataclass

@dataclass
class Expense:
    id:int
    amount:float
    category: str
    description: str

class ExpenseTracker:
    def __init__(self):

        self.expenses: list[Expense] = []
        self.nextid: int = 1

    def add_expense(self):
        print("----- ADD EXPENSE -----")
        try:
            amount = float(input("Enter Amount : "))
            if amount <= 0:
                print("The amount should be greater than zero.")
                return
        except ValueError:
            print("Invalid input. Enter a numeric amount.")
            return

        category = input("Enter category of the expense (Eg. Food , Transport , Movies , etc) : ").strip().title()
        description = input("Enter a description of the expense : ").strip()

        expense = Expense(
            id = self.nextid,
            amount = amount,
            category = category,
            description = description,
        )
        self.expenses.append(expense)
        print(f"Expense added successfully with ID: {self.nextid}")
        self.nextid += 1

    def view_expenses(self , expense_list=None):
        print("----- All Expenses -----\n")
        target_list = self.expenses if expense_list is None else expense_list

        if not target_list:
            print("No expenses found.")
            return
        for e in target_list:
            print(f"{e.id}. ₹ {e.amount}   {e.category}   {e.description}")

    def search(self):
        print("----- Search Expenses -----")
        print("1. Filter by Category\n2. Search by Description\n")
        choice = int(input("Choose an option from 1-2"))

        if choice == 1:
            cat = input("Enter category to filter: ").strip().lower()
            result = [e for e in self.expenses if e.category.lower() == cat]
        elif choice == 2:
            query = input("Enter keyword to search in description: ").strip().lower()
            result = [e for e in self.expenses if query in e.description.lower()]
        else:
            print("I'll take that as a no.")
            return

        self.view_expenses(result)

    def summary(self):
        print("----- Summary -----")
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        total_spent = sum(e.amount for e in self.expenses)
        avg_expense = total_spent/len(self.expenses)

        category_totals: dict[str , float] = {}
        for e in self.expenses:
            category_totals[e.category] = (category_totals.get(e.category , 0.0) + e.amount)

        highest_category = max(category_totals , key=category_totals.get)

        print(f"Total spent: {total_spent}\nAverage Expense : {avg_expense}\nBy category: ")
        for cat , amt in category_totals.items():
            print(f"{cat} :  ₹{amt}")

        print(f"Highest spending category: {highest_category} : ₹{category_totals[highest_category]}")

    def delete_expense(self):
        print("----- Delete Expense -----")
        try:
            target_id = int(input("Enter Expense ID to delete: "))
        except ValueError:
            print("I'll consider that as a no.")
            return
        for i , e in enumerate(self.expenses):
            if e.id == target_id:
                deleted = self.expenses.pop(i)
                print(f"Deleted expense ID {target_id}")
                return
        print(f"No expense ID found with ID {target_id}")

    def sort_expenses(self):
        print("----- Sort Expenses -----\n")
        print("1. Highest amount first\n2. Lowest amount first\n")
        choice = int(input("Select sorting order (1/2) : "))

        if choice == 1:
            sorted_list = sorted(self.expenses , key=lambda x: x.amount , reverse=True)
        elif choice == 2:
            sorted_list = sorted(self.expenses , key=lambda x:x.amount)
        else:
            print("Invalid input.")
            return
        self.view_expenses(sorted_list)

    def run(self):
        while True:
            print("+=+=+= Expense Tracker =+=+=+\n")
            print("1. Add Expense\n2. View Expenses\n3. Search / Filter Expenses\n4. Show Summary\n5. Delete Expenses\n6. Sort Expenses\n7. Exit")
            choice = int(input("Choose an option from 1-7 : "))
            if choice == 1:
                self.add_expense()
            elif choice == 2:
                self.view_expenses()
            elif choice == 3:
                self.search()
            elif choice == 4:
                self.summary()
            elif choice == 5:
                self.delete_expense()
            elif choice == 6:
                self.sort_expenses()
            elif choice == 7:
                print("Sayonara ~ ~")
                break
            else:
                print("Invalid input! Please enter a NUMBER between 1 to 7.")

tracker = ExpenseTracker()
tracker.run()