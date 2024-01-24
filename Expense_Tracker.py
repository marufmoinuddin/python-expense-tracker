import os
import sqlite3
import csv
from datetime import datetime

#Database Approach (Bonus)
def create_db():
    conn = sqlite3.connect("ET.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, amount REAL, category TEXT, description TEXT)""")
    conn.commit()
    conn.close()


def add():    
    while True:
        try:
            amt = float(input("Enter the amount: "))
            if amt >= 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        cat = input("Enter the category: ")
        if cat.strip(): 
            break
        else:
            print("Category cannot be empty. Please enter a valid category.")

    des = input("Enter the description (optional): ")

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    expense_data = (time, amt, cat, des)
    conn = sqlite3.connect("ET.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO expenses (date, amount, category, description) VALUES (?, ?, ?, ?)""", expense_data)
    conn.commit()
    conn.close()
    print("\nExpense added successfully!\n")

def show():
    print("\nExpense List:")
    print("ID | Date                 | Amount | Category  | Description")
    print("-" * 65)

    conn = sqlite3.connect("ET.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    for cell in cursor.fetchall():
        print("{:2} | {:20} | {:6} | {:9} | {}".format(cell[0], cell[1], cell[2], cell[3], cell[4]))

    print()
    conn.close()


def save_csv(): #Please expand the date column in excel to successfully view the date
    while True:
        csv_name = input("Enter the filename to save: ")

        if not csv_name.strip():  
            print("Filename cannot be empty. Please enter a valid filename.")
            continue

        try:
            line1 = ["ID", "Date", "Amount", "Category", "Description"]

            conn = sqlite3.connect("ET.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM expenses")

            with open(csv_name, "w", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(line1)
                writer.writerows(cursor.fetchall())

            print("Expenses saved successfully to \'{}\'!\n".format(csv_name))
            conn.close()
            break
        except Exception as e:
            print(f"Error: {e}\nPlease enter a valid filename.\n")


if not os.path.exists("ET.db"):
    create_db()

while True:
    print("Expense Tracker Menu:")
    print("1. Add Expense")
    print("2. Display Expenses")
    print("3. Save Expenses to CSV")
    print("4. Exit")

    opt = input("\nEnter your choice (1/2/3/4): ")

    if opt == "1":
        add()
    elif opt == "2":
        show()
    elif opt == "3":
        save_csv()
    elif opt == "4":
        print("Exiting the Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid choice (1/2/3/4).\n")

