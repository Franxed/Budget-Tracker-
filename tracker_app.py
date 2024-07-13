'''Create a program that allows the user to:
○ add new expense categories to the database (check)---------------------
○ update an expense amount (check)---------------------------------------
○ delete an expense category from the database (check)-------------------
○ track their spending (check)-------------------------------------------
○ add income (check)-----------------------------------------------------
○ add income categories (check)------------------------------------------
○ delete an income category from the database (check)--------------------
○ track their income (check)---------------------------------------------
○ View expense or income categories (check)------------------------------
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

import sys
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
CREATE TABLE IF NOT EXISTS income(
    id INTEGER PRIMARY KEY,
    income_category TEXT NOT NULL,
    income_name TEXT NOT NULL,
    amount REAL,
    UNIQUE(income_category, income_name))''')

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
            category_name = input("Type in Expense category (e.g. Home, Car, Family etc) : ").strip().title()
            print("# Note that your amount would automatically update if you type in the name of an existing expense:")
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

      db.commit()


def view_expense():
      try:
            cursor.execute('''
            SELECT id, expense_category, expense_name, amount FROM expenses''')
            print("\nViewing all Expenses:")
            total = 0
            for row in cursor:
                  print(f"ID {row[0]} : Category ({row[1]}) : Expense ({row[2]}): Amount R{row[3]:.2f}")
                  total += row[3]
            print(f"Total Expense is R{total:.2f}")

      except Exception as e:
            print(f"Error : {e}")

      db.commit()


def view_expense_category():
      try:
            cursor.execute('''
            SELECT DISTINCT expense_category FROM expenses''')
            categories = cursor.fetchall()

            if categories:
                  print("\nThe following categories of expenses are shown: ")
                  for category in categories:
                        print(f"- {category[0]}")
                  expense_name = input("Type in the category you would like to see! : ").strip().title()

                  cursor.execute('''
                  SELECT expense_category, expense_name, amount FROM expenses WHERE expense_category = ?''', (expense_name,))
                  expense_category = cursor.fetchall()
                  total = 0

                  if expense_category:
                        for row in expense_category:
                              print(f"Category ({row[0]}) : Expense ({row[1]}) : Amount R{row[2]:.2f}.")
                              total += row[2]
                        print(f"\nTotal Expense by {expense_name} is R{total}")
                        change = input(f"Would you like to make changes? (Y/N): ").strip().lower()

                        if change in ["y", "yes"]:
                              print("Proceeding to changes...")
                              delete = input(f"Would you like to remove this category? (Y/N): ").strip().lower()
                              if delete in ["y", "yes"]:
                                    cursor.execute('''
                                    DELETE FROM expenses WHERE expense_category = ?''', (expense_name,))
                                    db.commit()
                                    print(f"Deleted category.")
                              else:
                                    print("No changes made.")
                  else:
                        print("Error : Check if your spelling is correct and shown on the above categories!")
            else:
                  print("You have no categories yet, make sure you added one!")

      except Exception as e:
            print(f"Error : {e}")

      db.commit()


def add_income_category():
      try:
            category_name = input("Type in Income category (e.g. Work, Salary, etc.) : ").strip().title()
            print("# Note that your amount would automatically update if you type in the name of an existing income:")
            income_name = input("What is the name of your income (e.g. Freelance, Hyperiondev, etc.) : ").strip().title()
            amount = float(input("Input the Amount of the income : R"))
            cursor.execute('''
            INSERT OR REPLACE INTO income(income_category, income_name, amount)
            VALUES (?, ?, ?)''',(category_name, income_name, amount))
            print(f"Total income of R{amount:.2f} was added to {category_name}.")
            db.commit()
      except ValueError as ve:
            print(f"Error: Please enter a number to the amount / {ve}")
      except Exception as e:
            print(f"Error: {e}")

      db.commit()


def view_income():
      try:
            cursor.execute('''
            SELECT id, income_category, income_name, amount FROM income''')
            print("\nViewing all Income:")
            total = 0
            for row in cursor:
                  print(f"ID {row[0]} : Category ({row[1]}) : Income ({row[2]}): Amount R{row[3]:.2f}")
                  total += row[3]
            print(f"Total Income is R{total:.2f}")

      except Exception as e:
            print(f"Error : {e}")

      db.commit()


def view_income_category():
      try:
            cursor.execute('''
            SELECT DISTINCT income_category FROM income''')
            categories = cursor.fetchall()

            if categories:
                  print("\nThe following categories of income are shown: ")
                  for category in categories:
                        print(f"- {category[0]}")
                  income_name = input("Type in the category you would like to see! : ").strip().title()

                  cursor.execute('''
                  SELECT income_category, income_name, amount FROM income WHERE income_category = ?''', (income_name,))
                  income_category = cursor.fetchall()
                  total = 0

                  if income_category:
                        for row in income_category:
                              print(f"Category ({row[0]}) : Income ({row[1]}) : Amount R{row[2]:.2f}.")
                              total += row[2]
                        print(f"\nTotal Income by {income_name} is R{total}")
                        change = input(f"Would you like to make changes? (Y/N): ").strip().lower()

                        if change in ["y", "yes"]:
                              print("Proceeding to changes...")
                              delete = input(f"Would you like to remove this category? (Y/N): ").strip().lower()
                              if delete in ["y", "yes"]:
                                    cursor.execute('''
                                    DELETE FROM income WHERE income_category = ?''', (income_name,))
                                    db.commit()
                                    print(f"Deleted category.")
                              else:
                                    print("No changes made.")
                  else:
                        print("Error : Check if your spelling is correct and shown on the above categories!")
            else:
                  print("You have no categories yet, make sure you added one!")

      except Exception as e:
            print(f"Error : {e}")

      db.commit()


def set_budget():
      try:
            while True:
                  print("# Note that if the name is found in the Database, it would update automatically.")
                  category_name = input("Enter the category name for the budget: ").strip().title()
                  if category_name:
                        break
                  print("Category name cannot be empty. Please enter a valid category name.")

            while True:
                  try:
                        amount = float(input("Enter the budget amount: R"))
                        break
                  except ValueError:
                        print("Invalid input. Please enter a numeric value for the amount.")

            cursor.execute('''
            INSERT OR REPLACE INTO budget (category_name, amount)
            VALUES (?, ?)''', (category_name, amount))
            db.commit()
            print(f"Budget of R{amount:.2f} has been set for category '{category_name}'.")
      except Exception as e:
            print(f"Error: {e}")

def view_budget(): # Moet nog laat dit BUDGET uitwerk. Wins = Inkomste - Uitgawes
    try:
        cursor.execute('''
        SELECT DISTINCT category_name FROM budget''')
        categories = cursor.fetchall()

        if categories:
            print("\nThe following budget categories are shown: ")
            for category in categories:
                print(f"- {category[0]}")
            category_name = input("Type in the category you would like to see: ").strip().title()

            cursor.execute('''
            SELECT category_name, amount FROM budget WHERE category_name = ?''', (category_name,))
            budget_category = cursor.fetchall()
            total = 0

            if budget_category:
                for row in budget_category:
                    print(f"Category ({row[0]}) : Amount R{row[1]:.2f}.")
                    total += row[1]
                print(f"\nTotal Budget for {category_name} is R{total:.2f}")
                change = input(f"Would you like to make changes? (Y/N): ").strip().lower()

                if change in ["y", "yes"]:
                    print("Proceeding to changes...")
                    delete = input(f"Would you like to remove this category? (Y/N): ").strip().lower()
                    if delete in ["y", "yes"]:
                        cursor.execute('''
                        DELETE FROM budget WHERE category_name = ?''', (category_name,))
                        db.commit()
                        print(f"Deleted category '{category_name}'.")
                    else:
                        print("No changes made.")
            else:
                print("Error: Check if your spelling is correct and shown in the above categories!")
        else:
            print("You have no budget categories yet, make sure you added one!")
    except Exception as e:
        print(f"Error: {e}")

    db.commit()


def main():
      while True:
            print("\nWelcome to your budget planner Menu! Please pick only the number of the option to proceed:")
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

            option = input("Please choose your option : ").strip()

            try:
                  if option == "1":
                        add_expense_category()
                        input("Press Enter to route back to the menu.")
                  elif option == "2":
                        view_expense()
                        input("Press Enter to route back to the menu.")
                  elif option == "3":
                        view_expense_category()
                        input("Press Enter to route back to the menu.")
                  elif option == "4":
                        add_income_category()
                        input("Press Enter to route back to the menu.")
                  elif option == "5":
                        view_income()
                        input("Press Enter to route back to the menu.")
                  elif option == "6":
                        view_income_category()
                        input("Press Enter to route back to the menu.")
                  elif option == "7":
                        set_budget()
                        input("Press Enter to route back to the menu.")
                  elif option == "8":
                        view_budget()
                        input("Press Enter to route back to the menu.")
                  elif option == "9":
                        pass

                  elif option == "10":
                        pass

                  elif option == "11":
                        print("Quiting Application. Goodbye!")
                        sys.exit()
                  else:
                        print(f"\nMake sure you only type in the NUMBER of your option. (e.g. 1 or 2)")
            except Exception as e:
                  print(f"Error : {e}")


main()

