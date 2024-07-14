import sys
import sqlite3

# Connect to SQLite database.
db = sqlite3.connect('Budget_Tracker_App.db')
cursor = db.cursor()

# Create tables if they do not exist.
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

db.commit()  # Commit changes to the database.


def add_expense_category():
    # Function to add a new expense category or update an existing one.
    try:
        category_name = input("Type in Expense category (e.g., Home, Car, Family, etc.): ").strip().title()
        print("# Note that your amount would automatically update if you type in the name of an existing expense:")
        expense_name = input(
            "What is the name of your expense (e.g., Microwave for Home, car parts for Car, sister/brother for Family): ").strip().title()
        amount = float(input("Input the Amount of the expense: R"))
        cursor.execute('''
        INSERT OR REPLACE INTO expenses(expense_category, expense_name, amount)
        VALUES (?, ?, ?)''', (category_name, expense_name, amount))
        db.commit()  # Commit changes to the database.
        print(f"Total expense of R{amount:.2f} was added to {category_name}.")
    except ValueError as ve:
        print(f"Error: Please enter a number to the amount / {ve}")
    except Exception as e:
        print(f"Error: {e}")


def view_expense():
    # Function to view all expenses.
    try:
        cursor.execute('''
        SELECT id, expense_category, expense_name, amount FROM expenses''')
        print("\nViewing all Expenses:")
        total = 0
        for row in cursor:
            print(f"ID {row[0]}: Category ({row[1]}): Expense ({row[2]}): Amount R{row[3]:.2f}")
            total += row[3]
        print(f"Total Expense is R{total:.2f}")
    except Exception as e:
        print(f"Error: {e}")


def view_expense_category():
    # Function to view expenses by category.
    try:
        cursor.execute('''
        SELECT DISTINCT expense_category FROM expenses''')
        categories = cursor.fetchall()

        if categories:
            print("\nThe following categories of expenses are shown: ")
            for category in categories:
                print(f"- {category[0]}")
            expense_name = input("Type in the category you would like to see: ").strip().title()

            cursor.execute('''
            SELECT expense_category, expense_name, amount FROM expenses WHERE expense_category = ?''', (expense_name,))
            expense_category = cursor.fetchall()
            total = 0

            if expense_category:
                for row in expense_category:
                    print(f"Category ({row[0]}): Expense ({row[1]}): Amount R{row[2]:.2f}.")
                    total += row[2]
                print(f"\nTotal Expense by {expense_name} is R{total:.2f}")
                change = input(f"Would you like to make changes? (Y/N): ").strip().lower()

                if change in ["y", "yes"]:
                    print("Proceeding to changes...")
                    delete = input(f"Would you like to remove this category? (Y/N): ").strip().lower()
                    if delete in ["y", "yes"]:
                        cursor.execute('''
                        DELETE FROM expenses WHERE expense_category = ?''', (expense_name,))
                        db.commit()  # Commit changes to the database.
                        print(f"Deleted category.")
                    else:
                        print("No changes made.")
            else:
                print("Error: Check if your spelling is correct and shown on the above categories!")
        else:
            print("You have no categories yet. Make sure you added one!")
    except Exception as e:
        print(f"Error: {e}")


def add_income_category():
    # Function to add a new income category or update an existing one.
    try:
        category_name = input("Type in Income category (e.g., Work, Salary, etc.): ").strip().title()
        print("# Note that your amount would automatically update if you type in the name of an existing income:")
        income_name = input("What is the name of your income (e.g., Freelance, Hyperiondev, etc.): ").strip().title()
        amount = float(input("Input the Amount of the income: R"))
        cursor.execute('''
        INSERT OR REPLACE INTO income(income_category, income_name, amount)
        VALUES (?, ?, ?)''', (category_name, income_name, amount))
        db.commit()  # Commit changes to the database.
        print(f"Total income of R{amount:.2f} was added to {category_name}.")
    except ValueError as ve:
        print(f"Error: Please enter a number to the amount / {ve}")
    except Exception as e:
        print(f"Error: {e}")


def view_income():
    # Function to view all incomes.
    try:
        cursor.execute('''
        SELECT id, income_category, income_name, amount FROM income''')
        print("\nViewing all Income:")
        total = 0
        for row in cursor:
            print(f"ID {row[0]}: Category ({row[1]}): Income ({row[2]}): Amount R{row[3]:.2f}")
            total += row[3]
        print(f"Total Income is R{total:.2f}")
    except Exception as e:
        print(f"Error: {e}")


def view_income_category():
    # Function to view income by category.
    try:
        cursor.execute('''
        SELECT DISTINCT income_category FROM income''')
        categories = cursor.fetchall()

        if categories:
            print("\nThe following categories of income are shown: ")
            for category in categories:
                print(f"- {category[0]}")
            income_name = input("Type in the category you would like to see: ").strip().title()

            cursor.execute('''
            SELECT income_category, income_name, amount FROM income WHERE income_category = ?''', (income_name,))
            income_category = cursor.fetchall()
            total = 0

            if income_category:
                for row in income_category:
                    print(f"Category ({row[0]}): Income ({row[1]}): Amount R{row[2]:.2f}.")
                    total += row[2]
                print(f"\nTotal Income by {income_name} is R{total:.2f}")
                change = input(f"Would you like to make changes? (Y/N): ").strip().lower()

                if change in ["y", "yes"]:
                    print("Proceeding to changes...")
                    delete = input(f"Would you like to remove this category? (Y/N): ").strip().lower()
                    if delete in ["y", "yes"]:
                        cursor.execute('''
                        DELETE FROM income WHERE income_category = ?''', (income_name,))
                        db.commit()  # Commit changes to the database.
                        print(f"Deleted category.")
                    else:
                        print("No changes made.")
            else:
                print("Error: Check if your spelling is correct and shown on the above categories!")
        else:
            print("You have no categories yet. Make sure you added one!")
    except Exception as e:
        print(f"Error: {e}")


def set_budget():
    # Function to set or update a budget for a category.
    try:
        while True:
            print("# Note that if the name is found in the Database, it would update automatically.")
            category_name = input("Enter the name for the budget: ").strip().title()
            if category_name:
                break
            print("Category name cannot be empty. Please enter a valid category name.")

        while True:
            try:
                amount = float(input(f"Enter the limited amount for {category_name} (Maximum spend): R"))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the amount.")

        cursor.execute('''
        INSERT OR REPLACE INTO budget (category_name, amount)
        VALUES (?, ?)''', (category_name, amount))
        db.commit()  # Commit changes to the database.
        print(f"Budget of R{amount:.2f} has been set for category '{category_name}'.")
    except Exception as e:
        print(f"Error: {e}")


def calculate_budget():
    # Function to calculate the overall budget.
    try:
        # Calculate total income.
        cursor.execute('SELECT SUM(amount) FROM income')
        income_total = cursor.fetchone()[0]
        if income_total is None:
            income_total = 0

        print(f"Total income is R{income_total:.2f}")

        # Calculate total expenses.
        cursor.execute('SELECT SUM(amount) FROM expenses')
        expenses_total = cursor.fetchone()[0]
        if expenses_total is None:
            expenses_total = 0

        print(f"Total expense is R{expenses_total:.2f}")

        # Calculate remaining budget (profit).
        profit = income_total - expenses_total
        print(f"Your profit in total is R{profit:.2f}")
    except Exception as e:
        print(f"Error: {e}")


def view_budget():
    # Function to view and manage budgets.
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
                    print(f"Category ({row[0]}): Amount R{row[1]:.2f}.")
                    total += row[1]
                print(f"\nTotal Budget for {category_name} is R{total:.2f}")
                calculate_budget()  # Calculate and display the overall budget.

                change = input(f"Would you like to make changes? (Y/N): ").strip().lower()

                if change in ["y", "yes"]:
                    print("Proceeding to changes...")
                    delete = input(f"Would you like to remove this category? (Y/N): ").strip().lower()
                    if delete in ["y", "yes"]:
                        cursor.execute('''
                        DELETE FROM budget WHERE category_name = ?''', (category_name,))
                        db.commit()  # Commit changes to the database.
                        print(f"Deleted category '{category_name}'.")
                    else:
                        print("No changes made.")
            else:
                print("Error: Check if your spelling is correct and shown in the above categories!")
        else:
            print("You have no budget categories yet. Make sure you added one!")
    except Exception as e:
        print(f"Error: {e}")


def set_financial_goal():
    # Function to set a financial goal.
    try:
        while True:
            goal_name = input("Enter the name of your financial goal: ").strip().title()
            if goal_name:
                break
            print("Goal name cannot be empty. Please enter a valid goal name.")

        while True:
            try:
                target_amount = float(input("Enter the target amount for this goal: R"))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the target amount.")

        while True:
            try:
                current_amount = input("Enter the current amount saved towards this goal (or leave blank if none): R")
                if current_amount.strip() == "":
                    current_amount = 0.0
                    break
                current_amount = float(current_amount)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the current amount or leave it blank.")

        cursor.execute('''
            INSERT INTO financial_goals (goal_name, target_amount, current_amount)
            VALUES (?, ?, ?)''', (goal_name, target_amount, current_amount))
        db.commit()  # Commit changes to the database.
        print(
            f"Financial goal '{goal_name}' with a target of R{target_amount:.2f} and current amount of R{current_amount:.2f} has been set.")
    except Exception as e:
        print(f"Error: {e}")


def view_progress_towards_financial_goals():
    # Function to view progress towards financial goals.
    try:
        cursor.execute('''
        SELECT goal_name, target_amount, current_amount FROM financial_goals''')
        goals = cursor.fetchall()

        if goals:
            print("\nFinancial Goals and Progress:")
            for goal in goals:
                goal_name, target_amount, current_amount = goal
                print(f"Goal: {goal_name}")
                print(f"  Target Amount: R{target_amount:.2f}")
                print(f"  Current Amount: R{current_amount:.2f}")
                print(f"  Progress: {current_amount / target_amount * 100:.2f}%")
                print()
        else:
            print("No financial goals found. Set a financial goal to track your progress.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    # Main menu loop.
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

        option = input("Please choose your option: ").strip()

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
                set_financial_goal()
                input("Press Enter to route back to the menu.")
            elif option == "10":
                view_progress_towards_financial_goals()
                input("Press Enter to route back to the menu.")
            elif option == "11":
                print("Quitting Application. Goodbye!")
                db.close()  # Close the database connection
                sys.exit()
            else:
                print(f"\nMake sure you only type in the NUMBER of your option. (e.g., 1 or 2)")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
