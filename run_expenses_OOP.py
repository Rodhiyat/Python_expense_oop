from expenses_OOP import Expense, ExpenseDatabase


# creating sample expenses
expense1 = Expense ("groceries", 200.0)
expense2 = Expense ("bag", 60.0)
expense3 = Expense ("groceries", 45.5)
expense4 = Expense ("groceries", 100.5)


# update an expense
update_status = expense1.update(title="hair", amount=7500.0)
print("="*100)


# extract expense1 as a dictionary
expense1_dict = expense1.to_dict()
print(expense1_dict)
print("="*100)

 
# Creating an ExpenseDB instance and adding expenses
expense_db = ExpenseDatabase()
for expense in [expense1, expense2, expense3, expense4]:
    print(expense_db.add_expense(expense))
print("="*100)

 
# add a new expense to the database
expense5 = Expense("Hair", 1000.2)
expense_db.add_expense(expense5)
print("="*100)


# remove an expense by id
expense_db.remove_expense(expense3.id)
print("="*100)


# retrieve an expense by ID
print(expense_db.get_expense_by_id(expense2.id))
print("="*100)   


# retrieve expenses by title
print(expense_db.get_expense_by_title("hair"))    
print("="*100)


# print all expenses in the database as a list of dictionary
print(expense_db.to_dict())
