import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def init_file():
    try:
        with open(FILE_NAME, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Type", "Category", "Amount"])
    except FileExistsError:
        pass

def add_entry(entry_type):
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, entry_type, category, amount])

    print("Entry added successfully!\n")

def show_summary():
    income = 0
    expense = 0

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Type"] == "income":
                income += float(row["Amount"])
            else:
                expense += float(row["Amount"])

    print("\n----- Summary -----")
    print("Total Income :", income)
    print("Total Expense:", expense)
    print("Balance      :", income - expense)
    print("-------------------\n")

def main():
    init_file()

    while True:
        print("Expense Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_entry("income")
        elif choice == "2":
            add_entry("expense")
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()