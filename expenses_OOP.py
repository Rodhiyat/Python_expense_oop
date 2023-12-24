import uuid
from datetime import datetime, timezone


class Expense:
    
    def __init__(self, title, amount):
        """
        Initializes an Expense object with a unique ID, title, amount,
        creation time , and last updated time.
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount                
        self.created_at = datetime.now(timezone.utc)  
        self.updated_at = self.created_at    
       

    def update(self, title = None, amount = None):
        """
        This method updates the title and/or amount 
        The updated_at attribute is automatically set to the current UTC timestamp.
        """  
        self.title = title if title is not None else self.title
        self.amount = amount if amount is not None else self.amount
        self.updated_at = datetime.now(timezone.utc)      
        print(f"expense with id {self.id} updated successfully!")


    def to_dict(self):
        """
        This method returns a dictionary representation of the expense object
        """
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        } 

    def __repr__(self): 
        return f"{self.id} {self.title} {self.amount} '{self.created_at}' '{self.updated_at}'"
    

class ExpenseDatabase:
    def __init__(self):
        """
        Initializes an ExpenseDB object with an empty list to store expenses.
        """
        self.expenses = []

    def add_expense(self, expense):
        """
        This method adds an expense to the database and returns a list all the expense id in the database
        """
        self.expenses.append(expense)
        print(f"{expense} added successfully!")
        return [exp.id for exp in self.expenses]


    def remove_expense(self, expense_id):
        """
        This method removes an expense by it's unique identifier (ID) from the database
        """
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]
        print(f"expense with id {expense_id} has been removed")


    def get_expense_by_id(self, expense_id):
        """
        This method retrieves an expense by it's unique identifier (ID)
        returns the expense object with the given ID
        """
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None        

    def get_expense_by_title(self, expense_title):
        """
        This method enables us retrieve expenses by title
        and returns a list of the expense object to the user
        """
        title_match = [expense for expense in self.expenses if expense.title.lower() == expense_title.lower()]
        return title_match if title_match else None

    
    def to_dict(self):
        """
        This method returns a list of dictionaries representing each expense in the database
        """
        return [expense.to_dict() for expense in self.expenses]
    