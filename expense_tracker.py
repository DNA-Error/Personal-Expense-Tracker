
import csv

def add_expense():
    # Asking input data from user
    date = input("Enter a date (YYYY-MM-DD): ")
    item_category = input("Enter a category (e.g., food, transport): ")
    amount = input("Enter an amount: ")
    # It's optional
    description = input("Enter a description (optional): ")

    # Appending into CSV file
    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, item_category, amount, description])

    print("Expense added successfully.")

def view_expenses():
    try:
        with open("expenses.csv", mode="r", newline="") as file:
            expenses = list(csv.reader(file))
            if not expenses:
                print("🚫 No expenses recorded yet. Please add an expense first.")
                return
            # For dynamic length
            max_desc_len = max(len(row[3]) for row in expenses if len(row) > 3)
            max_line_length = 15 + 15 + 15 + 10 + max_desc_len + 10

            print("\nAll Expenses:")
            print(f"{'Date':<15} {'Category':<15} {'Amount($)':<10} {'Description'}")
            print("-" * max_line_length)

            for row in expenses:
                if len(row) < 4:
                    print("Skipping invalid row (missing data).")
                    continue
                date, item_category, amount, description = row
                print(f"{date:<15} {item_category:<15} {amount:<10} {description}")

            print("-" * max_line_length)
            print("\n")
    except FileNotFoundError:
        print("No expenses recorded yet.")
    except Exception as e:
        print(f"❗ An error occurred: {e}")

def view_by_category():
    category_input = input("Enter the category to filter by: ").strip().lower()
    found = False
    try:
        with open("expenses.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            print(f"\n--- Expenses in Category: {category_input} ---")
            for row in reader:
                if len(row) < 4:
                    continue
                date, item_category, amount, description = row
                if item_category.strip().lower() == category_input:
                    print(f"Date: {date}, Amount: {amount}, Description: {description}")
                    found = True
            if not found:
                print("No expenses found in that category.")
            print("--------------------------------------------------------\n")
    except FileNotFoundError:
        print("No expenses recorded yet.")

def total_spending():
    total = 0.0
    try:
        with open("expenses.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 3:
                    continue
                amount = row[2]
                try:
                    total += float(amount)
                except ValueError:
                    print(f"Skipping invalid amount: {amount}")
        print(f"\nTotal spending: ${total:.2f}\n")
    except FileNotFoundError:
        print("No expenses recorded yet.")

def monthly_report():
    month_input = input("Enter the month (YYYY-MM): ").strip()
    total = 0.0
    found = False

    try:
        with open("expenses.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 3:
                    continue
                date = row[0]
                if date.startswith(month_input):
                    total += float(row[2])
                    found = True
            if found:
                print(f"\nTotal Spending for {month_input}: ${total:.2f}\n")
            else:
                print("No expenses found for that month.")
    except FileNotFoundError:
        print("No expenses recorded yet.")
    except ValueError:
        print("There was an error processing the amounts.")

def delete_expense():
    try:
        with open("expenses.csv", mode="r", newline="") as file:
            reader = list(csv.reader(file))

        if not reader:
            print("No expenses to delete.")
            return
        print("\nExpenses:")
        for i, row in enumerate(reader):
            if len(row) < 4:
                continue
            print(f"{i+1}. Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Description: {row[3]}")

        choice = input("Enter the number of the expense to delete: ")
        if not choice.isdigit():
            print("Invalid input. Please enter a valid number.")
            return

        choice = int(choice)
        if 1 <= choice <= len(reader):
            removed = reader.pop(choice-1)
            print(f"Deleted: {removed}")

            with open("expenses.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(reader)
        else:
            print("Invalid choice.")
    except FileNotFoundError:
        print("No expenses recorded yet.")
    except ValueError:
        print("Please enter a valid number.")

def edit_expense():
    try:
        with open("expenses.csv", mode="r", newline="") as file:
            reader = list(csv.reader(file))

        if not reader:
            print("No expenses to edit.")
            return

        print("\nExpenses:")
        for i, row in enumerate(reader):
            if len(row) < 4:
                continue
            print(f"{i+1}. Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Description: {row[3]}")

        choice = input("Enter the number of the expense to edit: ")
        if not choice.isdigit():
            print("Invalid input. Please enter a valid number.")
            return

        choice = int(choice)
        if 1 <= choice <= len(reader):
            old = reader[choice - 1]
            print("Leave blank to keep the current value:")

            new_date = input(f"New Date (current: {old[0]}): ") or old[0]
            new_category = input(f"New Category (current: {old[1]}): ") or old[1]
            new_amount = input(f"New Amount (current: {old[2]}): ") or old[2]
            new_desc = input(f"New Description (current: {old[3]}): ") or old[3]

            reader[choice-1] = [new_date, new_category, new_amount, new_desc]
            with open("expenses.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(reader)

            print("Expense updated successfully.")
        else:
            print("Invalid choice.")
    except FileNotFoundError:
        print("No expenses recorded yet.")
    except ValueError:
        print("Please enter a valid number.")

def guide_user():
    while True:
        print("Welcome to Expense Tracker\n")
        print("1. Add an Expense")
        print("2. View all Expenses")
        print("3. View expense by category")
        print("4. View Total Spending")
        print("5. Modify Existing Data")
        print("6. Quit")
        choice = input("Choose an Option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            print("\nTotal Spending Options:")
            print("1. Total Report")
            print("2. Monthly Report")
            sub_choice = input("Choose an Option: ")
            if sub_choice == "1":
                total_spending()
            elif sub_choice == "2":
                monthly_report()
        elif choice == "5":
            print("\nModify Expense Options:")
            print("1. Delete an Expense")
            print("2. Edit an Expense")
            modify_choice = input("Choose an Option: ")
            if modify_choice == "1":
                delete_expense()
            elif modify_choice == "2":
                edit_expense()
            else:
                print("Invalid Option.")
        elif choice == "6":
            print("Exited Successfully.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    guide_user()
