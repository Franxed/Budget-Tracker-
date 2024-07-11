# add Expense category (e.g. House, Elect & Water bills)
# delete an expense category from the database
# update expense amount
# track their spending
# add income
# add income categories
# delete an income category from the database
# track their income
# View expense or income categories

import sqlite3

db = sqlite3.connect('Budget_Tracker_App.db')
cursor = db.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS expense_category(
    id INTEGER PRIMARY KEY,
    expense_category TEXT NOT NULL UNIQUE)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS expense(
    id INTEGER PRIMARY KEY,
    expense_name TEXT NOT NULL UNIQUE,
    amount INTEGER REAL,
    FOREIGN KEY(id) REFERENCES expense_category(id))''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS income_category(
    id INTEGER PRIMARY KEY,
    income_category TEXT NOT NULL UNIQUE)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS income(
    id INTEGER PRIMARY KEY,
    income_name TEXT NOT NULL UNIQUE,
    amount INTEGER REAL,
    FOREIGN KEY(id) REFERENCES income_category(id))''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS budget(
    id INTEGER PRIMARY KEY,
    category_id INTEGER,
    amount REAL,
    FOREIGN KEY(category_id) REFERENCES expense_category(id))''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS financial_goals(
    id INTEGER PRIMARY KEY,
    goal_name TEXT NOT NULL,
    target_amount REAL,
    current_amount REAL)''')

db.commit()



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


main()
