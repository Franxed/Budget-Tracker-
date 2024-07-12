'''Create a program that allows the user to:
○ add new expense categories to the database (check)---------------------
○ update an expense amount (check)---------------------------------------
○ delete an expense category from the database
○ track their spending
○ add income
○ add income categories
○ delete an income category from the database
○ track their income
○ View expense or income categories
○ The program should be able to calculate the user’s budget based on
the income and expenses that they have provided
● Install the SQLite library. This will allow your app to communicate with the
SQLite database.
● Connect to the SQLite database. You can do this by using the "connect"
function from the sqlite3 library.
● Next, you will need to create your database tables to store your data. You
can use the "execute" function to execute SQL commands to create tables.
● Insert data: After creating tables, ensure that users are able to insert data
into them. You can use the "execute" function to execute SQL commands to
insert data.
● Ensure that users can retrieve data from the database using SQL queries.
● Close the connection to the database using the "close" function.
● The program should present the user with the following menu:
1. Add expense
2. View expenses
3. View expenses by category
4. Add income
5. View income
6. View income by category
7. Set budget for a category
8. View budget for a category
9. Set financial goals
10. View progress towards financial goals
11. Quit
The program should perform the function that the user selects. The
implementation of these functions is left up to you.'''


import sqlite3

db = sqlite3.connect('Budget_Tracker_App.db')
cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY,
    expense_category TEXT NOT NULL,
    expense_name TEXT NOT NULL,
    amount REAL,
    UNIQUE(expense_category, expense_name))''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS income_category(
    id INTEGER PRIMARY KEY,
    income_category TEXT NOT NULL UNIQUE)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS income(
    id INTEGER PRIMARY KEY,
    income_name TEXT NOT NULL UNIQUE,
    amount REAL,
    FOREIGN KEY(id) REFERENCES income_category(id))''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS budget(
    id INTEGER PRIMARY KEY,
    category_name TEXT,
    amount REAL,
    FOREIGN KEY(id) REFERENCES expense_category(id))''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS financial_goals(
    id INTEGER PRIMARY KEY,
    goal_name TEXT NOT NULL,
    target_amount REAL,
    current_amount REAL)''')

db.commit()

def add_expense_category():
      try:
            category_name = input("Type in head category (e.g. Home, Car, Family etc) : ").strip().title()
            print("# Note that your amount would automatically update if the name of your expenses are the same:")
            expense_name = input("What is the name of your expense (e.g. Microwave for Home, car parts for Car, sister/brother for Family) : ").strip().title()
            amount = float(input("Input the Amount of the expense : R"))
            cursor.execute('''
            INSERT OR REPLACE INTO expenses(expense_category, expense_name, amount)
            VALUES (?, ?, ?)''',(category_name, expense_name, amount))
            print(f"Total expense of R{amount:.2f} was added to {category_name}.")
            db.commit()
      except ValueError as ve:
            print(f"Error: Please enter a number to the amount / {ve}")
      except Exception as e:
            print(f"Error: {e}")


def view_expense():
      try:
            cursor.execute('''
            SELECT id, expense_category, expense_name, amount FROM expenses''')
            print("\nViewing all Expenses:")
            for row in cursor:
                  print(f"ID {row[0]} : {row[1]} ({row[2]}): R{row[3]:.2f}")

      except Exception as e:
            print(f"Error : {e}")
      finally:
            db.close()

def view_expense_category():
      try:
            cursor.execute('''
            SELECT DISTINCT expense_category FROM expenses''')
            categories = cursor.fetchall()

            if categories:
                  print("\nThe following categories are shown: ")
                  for category in categories:
                        print(f"- {category[0]}")
                  expense_name = input("Type in the category you would like to see! : ").strip().title()

                  cursor.execute('''
                  SELECT expense_category, expense_name, amount FROM expenses WHERE expense_category = ?''', (expense_name,))
                  expense_category = cursor.fetchall()

                  if expense_category:
                        print(f"- {expense_category}:\n")   # hier moet for loop kom.


                  else:
                        print("Error : Check if your spelling is correct and on shown on the above categories!")
            else:
                  print("You have no categories yet, make sure you added one!")




      except Exception as e:
            print(f"Error : {e}")


def main():
    print("\n1. Add expense\n"
          "2. View expenses\n"
          "3. View expenses by category\n"
          "4. Add income\n"
          "5. View income\n"
          "6. View income by category\n"
          "7. Set budget for a category\n"
          "8. View budget for a category\n"
          "9. Set financial goals\n"
          "10. View progress towards financial goals\n"
          "11. Quit")

view_expense_category()

