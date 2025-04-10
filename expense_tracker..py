
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
        elif choice == "5":
            print("Exited Successfully")
            break
        else:
            print("Invalid choice!!")


if __name__ == "__main__":
    guide_user()