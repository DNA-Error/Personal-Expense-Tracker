
import  csv



def add_expense():
    #Asking an input data from user
    date = input("Enter a date (YYYY-MM-DD): ")
    item_category = input("Enter a category(eg., food, transport): ")
    amount = input("Enter a amount: ")
    #It's an optional
    descrption = input("Enter a description(optional): ")

    #appending into CSV file
    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, item_category, amount, descrption])

    print("Expenses added successfully")



def view_expenses():
    try:
        with open("expenses.csv", mode="r", newline="") as file:
            expenses = list(csv.reader(file))
            if not expenses:
                print("🚫 No expenses recorded yet. Please add an expense first.")
                return
            # For dynamic length
            max_desc_len = max(len(row[3])for row in expenses)
            max_line_length = 15+15+15+10+max_desc_len+10

            print("\nAll Expenses:")
            print(f"{'Date':<15} {'Category':<15} {'Amount($)':<10} {'Description'}")
            print("-" * max_line_length)

            for row in expenses:
                date,item_category, amount, description,= row
                print(f"{date:<15} {item_category:<15} {amount:<10} {description}")

            print("-" * max_line_length)
            print("\n")
    except FileNotFoundError:
        print("Error: Skipping invalid row (missing data")
    except Exception as e:
        print(f"❗ An error occurred: {e}")




def guide_user():
    while True:
        print("Welcome to Expense Tracker \n ")
        print("1.Add a Expenses")
        print("2.View all Expenses")
        print("3.View expense by category")
        print("4.View Total Spending")
        print("5.Quit")
        choice = input("Choose an Option:")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "5":
            print("Exited Successfully")
            break
        else:
            print("Invalid choice!!")

#making guide_user as a default function where it start like main() in C++
if __name__ == "__main__":
    guide_user()