import csv  # Import the csv module for handling CSV files
import os  # Import os module to check file existence

class Expense:
    def __init__(self, date, amount, description):
        self.date = date
        self.amount = amount
        self.description = description

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

# Function to add an expense to the list and save it to the file
def add_expense(expenses, date, amount, description):
    expenses.append([date, amount, description])  
    save_expenses(expenses) 

# Function to remove an expense from the list and save changes
def remove_expense(expenses, index):
    if 0 <= index < len(expenses):  
        del expenses[index]  
        save_expenses(expenses)  
        print("Expense removed successfully.")
    else:
        print("Invalid index! Please enter a valid expense number.")

# Function to display all recorded expenses
def view_expenses(expenses):
    print("\nExpense List:")
    print("No. | Date       | Amount | Description")  
    print("-" * 60)  
    for i, expense in enumerate(expenses):
        print(f"{i+1:3} | {expense[0]:10} | ₱{expense[1]:5} | {expense[2]}")  
    print(f"\nTotal Expenses: ₱{sum(int(exp[1]) for exp in expenses):.2f}") 

# Function to save expenses to a CSV file
def save_expenses(expenses, filename="expenses.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)  
        writer.writerow(["Date", "Amount", "Description"])  
        writer.writerows(expenses)  

# Function to load expenses from a CSV file
def load_expenses(filename="expenses.csv"):
    expenses = []
    if os.path.exists(filename):  
        with open(filename, mode='r') as file:
            reader = csv.reader(file)  
            next(reader, None)  
            expenses = [row for row in reader]  
    return expenses  

# Main function to run the expense tracker
def main():
    expenses = load_expenses()  
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':  
            date = input("Enter date (YYYY-MM-DD): ")
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            add_expense(expenses, date, amount, description)  
        elif choice == '2':  
            view_expenses(expenses)  
            try:
                index = int(input("Enter the expense number to remove: ")) - 1  
                remove_expense(expenses, index)  
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == '3':  
            view_expenses(expenses)  
        elif choice == '4':  
            break  
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")  

if __name__ == "__main__":
    main()  