import argparse
import json
import os
from datetime import datetime

class Expense:
    def __init__(self, id, description, amount):
        self.id = id
        self.description = description
        self.amount = amount
        self.date = datetime.now().strftime('%Y-%m-%d')
        self.createdAt = datetime.now().isoformat()
        self.updatedAt = self.createdAt

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "date": self.date,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }

def load_expenses(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        return json.load(file)

def save_expenses(filename, expenses):
    with open(filename, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses, description, amount):
    expense_id = len(expenses) + 1
    expense = Expense(expense_id, description, amount)
    expenses.append(expense.to_dict())
    return expense_id

def update_expense(expenses, expense_id, description=None, amount=None):
    for expense in expenses:
        if expense['id'] == expense_id:
            if description:
                expense['description'] = description
            if amount is not None:
                expense['amount'] = amount
            expense['updatedAt'] = datetime.now().isoformat()
            return True
    return False

def delete_expense(expenses, expense_id):
    for i, expense in enumerate(expenses):
        if expense['id'] == expense_id:
            del expenses[i]
            return True
    return False

def update_id(expenses, expense_id):
    for i, expense in enumerate(expenses):
        if expense['id'] > expense_id:
            expense['id'] = expense['id'] - 1

def list_expenses(expenses):
    print('ID  Date       Description          Amount')
    for expense in expenses:
        print(f"{expense['id']}  {expense['date']}  {expense['description']: <20}  ${expense['amount']}")

def summary_expenses(expenses, month=None):
    total_amount = 0
    for expense in expenses:
        if month is None or expense['date'].split('-')[1] == str(month).zfill(2):
            total_amount += expense['amount']
    return total_amount

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Подкоманда 'add'
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('--description', type=str, required=True, help='Description of the expense')
    add_parser.add_argument('--amount', type=float, required=True, help='Amount of the expense')

    # Подкоманда 'update'
    update_parser = subparsers.add_parser('update', help='Update an existing expense')
    update_parser.add_argument('--expense_id', type=int, help='ID of the expense to update')
    update_parser.add_argument('--description', type=str, help='New description of the expense')
    update_parser.add_argument('--amount', type=float, help='New amount of the expense')

    # Подкоманда 'delete'
    delete_parser = subparsers.add_parser('delete', help='Delete an expense')
    delete_parser.add_argument('--expense_id', type=int, help='ID of the expense to delete')

    # Подкоманда 'list'
    subparsers.add_parser('list', help='List all expenses')

    # Подкоманда 'summary'
    summary_parser = subparsers.add_parser('summary', help='Show summary of expenses')
    summary_parser.add_argument('--month', type=int, help='Month for summary (1-12)')

    args = parser.parse_args()
    filename = 'expenses.json'
    expenses = load_expenses(filename)

    if args.command == 'add':
        expense_id = add_expense(expenses, args.description, args.amount)
        save_expenses(filename, expenses)
        print(f"Expense added successfully (ID: {expense_id})")

    elif args.command == 'update':
        if update_expense(expenses, args.expense_id, args.description, args.amount):
            save_expenses(filename, expenses)
            print(f"Expense {args.expense_id} updated successfully.")
        else:
            print(f"Expense {args.expense_id} not found.")

    elif args.command == 'delete':
        expense_id = args.expense_id
        if delete_expense(expenses, expense_id):
            update_id(expenses, expense_id)
            save_expenses(filename, expenses)
            print(f"Expense {expense_id} deleted successfully.")
        else:
            print(f"Expense {expense_id} not found.")

    elif args.command == 'list':
        list_expenses(expenses)

    elif args.command == 'summary':
        months = {1: 'January', 2: 'Fabruary', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
        month = args.month
        total = summary_expenses(expenses, month)
        if month:
            print(f'Total expenses for month {months.get(month)}: ${total:,.2f}')
        else:
            print(f'Total expenses: ${total:,.2f}')

if __name__ == '__main__':
    main()