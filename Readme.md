# Expense Manager OOP

## **Project Description**

The goal of this project is to implement two classes, Expense and ExpenseDatabase which will be used to model and manage financial expenses 

### Expense Class

Represents an individual financial expense.

#### Attributes
- id: A unique identifier generated as a UUID string.
- title: A string representing the title of the expense.
- amount: A float representing the amount of the expense.
- created_at: A timestamp indicating when the expense was created (UTC).
- updated_at: A timestamp indicating the last time the expense was updated (UTC).

#### Methods
- __init__: Initializes the attributes.
- update: Allows updating the title and/or amount, updating the updated_at timestamp.
- to_dict: Returns a dictionary representation of the expense.

### ExpenseDatabase Class

Manages a collection of Expense objects.

#### Attributes
- expenses: A list storing Expense instances.

#### Methods
- __init__: Initializes the list.
- add_expense: Adds an expense.
- remove_expense: Removes an expense.
- get_expense_by_id: Retrieves an expense by ID.
- get_expenses_by_title: Retrieves expenses by title (returning a list).
- to_dict: Returns a list of dictionaries representing expenses.

### Instructions

For the Expense Database class:
- Implement an __init__ method to initialize the attributes.
- Implement an update method that allows updating the title and/or amount of the expense. The updated_at attribute should be automatically set to the current UTC timestamp whenever an update occurs.
- Implement a to_dict method that returns a dictionary representation of the expense.

For the Expense Database class:
- Implement an __init__ method to initialize the expenses list.
- Implement methods to: a. Add an expense to the database. b. Remove an expense from the database. c. Get an expense by ID. d. Get expenses by title (returning a list).
- Create a to_dict method that returns a list of dictionaries representing each expense in the database. Github


## **How to Clone the Repository**

To clone this project:
- Copy this repository url from the "Code" button in this repository
- Open git bash and Change the current working directory to the location where you want the cloned directory using cd command - ```cd <folder path>```
- Use the git clone command followed by the repository URL you copied earlier. Paste the URL after 'git clone'. For this repository; ```git clone https://github.com/Rodhiyat/Python_expense_oop.git```
- Press Enter to create your local clone. 


## **How to Run the Code**

- Ensure you have python installed (version 3.10 or above) 
- Execute the Python file containing the classes ```expenses_OOP.py```
- The python file ```run_expenses_OOP.py``` contain instances of Expense and ExpenseDatabase alongside their method execution so you can run the file. Alternatively, you can run the code below;

#### Create instances of the expense
```
expense1 = Expense ("groceries", 200.0)
expense2 = Expense ("bag", 60.0)
expense3 = Expense ("bag", 45.5)
expense4 = Expense ("groceries", 100.5)
```
#### Update an expense
```
update_status = expense1.update(title="hair", amount=7500.0)
```
#### Extract expense1 as a dictionary
```
expense1_dict = expense1.to_dict()
print(expense1_dict)
```
#### Creating an ExpenseDB instance and adding expenses
```
expense_db = ExpenseDatabase()
for expense in [expense1, expense2, expense3, expense4]:
    print(expense_db.add_expense(expense))
```
#### Add a new expense to the database
```
expense5 = Expense("Hair", 1000.2)
expense_db.add_expense(expense5)
```
#### Remove an expense by id
```
expense_db.remove_expense(expense3.id)
```
#### Retrieve an expense by ID
```
print(expense_db.get_expense_by_id(expense2.id))
```
#### Retrieve expenses by title
```
print(expense_db.get_expense_by_title("hair"))    
```
#### Retrieve all expenses in the database as a list of dictionary
```
print(expense_db.to_dict())
```


