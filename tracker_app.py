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
def initialize_database():

    db = sqlite3.connect('Budget_Tracker.db')
    cursor = db.cursor()

    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Expense_Category''')
