"""
DAILY EXPENSE TRACKER
Python Beginner Project
"""

import json
from datetime import date


# Load saved expenses
def load_expenses():
    try:
        with open("expenses.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save expenses
def save_expenses():
    with open("expenses.json", "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


# Store expenses
expenses = load_expenses()


# 1. Add an expense
def add_expense():
    description = input("Enter expense description: ").strip()

    if not description:
        print("Description cannot be empty.")
        return

    print("\nSelect expense category:")
    print("1. Food")
    print("2. Travel")
    print("3. Shopping")
    print("4. Education")
    print("5. Other")

    category_choice = input("Choose category (1-5): ")

    categories = {
        "1": "Food",
        "2": "Travel",
        "3": "Shopping",
        "4": "Education",
        "5": "Other"
    }

    category = categories.get(category_choice)

    if category is None:
        print("Invalid category.")
        return

    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    expense = {
        "description": description,
        "amount": amount,
        "category": category,
        "date": date.today().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully!")


# 2. View all expenses
def view_expenses():
    if not expenses:
        print("No expenses available.")
        return

    print("\n===== YOUR EXPENSES =====")

    for number, expense in enumerate(expenses, start=1):
        print(f"\nExpense {number}")
        print(f"Description: {expense['description']}")
        print(f"Amount: Rs. {expense['amount']:.2f}")
        print(f"Category: {expense.get('category', 'Uncategorized')}")
        print(f"Date: {expense.get('date', 'Not recorded')}")


# 3. Calculate total expenses
def calculate_total():
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expenses: Rs. {total:.2f}")


# 4. Category-wise expense summary
def category_summary():
    if not expenses:
        print("No expenses available.")
        return

    summary = {}

    for expense in expenses:
        category = expense.get("category", "Uncategorized")
        amount = expense["amount"]

        summary[category] = summary.get(category, 0) + amount

    print("\n===== CATEGORY-WISE SUMMARY =====")

    for category, total in summary.items():
        print(f"{category}: Rs. {total:.2f}")


# 5. Monthly expense summary
def monthly_summary():
    if not expenses:
        print("No expenses available.")
        return

    summary = {}

    for expense in expenses:
        expense_date = expense.get("date")

        if expense_date and len(expense_date) >= 7:
            month = expense_date[:7]
            amount = expense["amount"]

            summary[month] = summary.get(month, 0) + amount

    print("\n===== MONTHLY EXPENSE SUMMARY =====")

    if not summary:
        print("No dated expenses available.")
        return

    for month, total in sorted(summary.items()):
        print(f"{month}: Rs. {total:.2f}")


# 6. Delete an expense
def delete_expense():
    if not expenses:
        print("No expenses available to delete.")
        return

    view_expenses()

    try:
        number = int(input("\nEnter expense number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if 1 <= number <= len(expenses):
        deleted = expenses.pop(number - 1)
        save_expenses()

        print(f"Successfully deleted: {deleted['description']}")
    else:
        print("Invalid expense number.")


# 7. Search expenses
def search_expenses():
    keyword = input("Enter description to search: ").lower().strip()

    if not keyword:
        print("Please enter a search keyword.")
        return

    found = False

    print("\n===== SEARCH RESULTS =====")

    for expense in expenses:
        description = expense.get("description", "")

        if keyword in description.lower():
            print(f"\nDescription: {description}")
            print(f"Amount: Rs. {expense['amount']:.2f}")
            print(f"Category: {expense.get('category', 'Uncategorized')}")
            print(f"Date: {expense.get('date', 'Not recorded')}")
            found = True

    if not found:
        print("No matching expenses found.")


# 8. Monthly budget
def monthly_budget():
    try:
        budget = float(input("Enter your monthly budget (Rs.): "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if budget <= 0:
        print("Budget must be greater than zero.")
        return

    current_month = date.today().strftime("%Y-%m")

    total = sum(
        expense["amount"]
        for expense in expenses
        if expense.get("date", "").startswith(current_month)
    )

    remaining = budget - total

    print("\n===== MONTHLY BUDGET REPORT =====")
    print(f"Monthly Budget: Rs. {budget:.2f}")
    print(f"Amount Spent: Rs. {total:.2f}")
    print(f"Remaining Budget: Rs. {remaining:.2f}")

    if total > budget:
        print("Warning! You have exceeded your monthly budget.")
    elif total == budget:
        print("You have reached your monthly budget.")
    else:
        print("You are within your monthly budget.")


# 9. Main menu
while True:
    print("\n================================")
    print("      DAILY EXPENSE TRACKER")
    print("================================")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Calculate total expenses")
    print("4. Category-wise expense summary")
    print("5. Monthly expense summary")
    print("6. Delete an expense")
    print("7. Search expenses")
    print("8. Monthly budget")
    print("9. Exit")

    choice = input("\nChoose an option (1-9): ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        calculate_total()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        monthly_summary()

    elif choice == "6":
        delete_expense()

    elif choice == "7":
        search_expenses()

    elif choice == "8":
        monthly_budget()

    elif choice == "9":
        print("\nThank you for using Daily Expense Tracker!")
        break

    else:
        print("Invalid choice. Please select an option from 1 to 9.")