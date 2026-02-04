from tabulate import tabulate
from storage import load_books
from utils import clear_screen

def add_book():
    print("Adding a book...")

    # Implementation for adding a book goes here

def edit_book(): 
    print("Editing a book...")

    # Implementation for editing a book goes here

def delete_book(): 
    print("Deleting a book...")
    
    # Implementation for deleting a book goes here

def display_books(books, view = "default", specific_fields = None, orientation = "horizontal"):
    if not books:
        print("No books to display.")
        return

    DEFAULT_FIELDS = ["isbn", "title", "author"]
    ALL_FIELDS = ["isbn", "title", "author", "genre", "publication", "stock", "unit_price", "is_rare", "additional_info"]


    if view == "default":
        fields_to_display = DEFAULT_FIELDS
    elif view == "detailed":
        fields_to_display = ALL_FIELDS
    elif view == "custom" and specific_fields:
        fields_to_display = ["isbn", "title"] + specific_fields
    else:
        fields_to_display = DEFAULT_FIELDS
    
    if orientation == "horizontal":
        rows = []
        for book in books:
            row = [book.get(field, "") for field in fields_to_display]
            rows.append(row)
            headers = [field.replace("_", " ").title() for field in fields_to_display]
        print(tabulate(rows, headers=headers, tablefmt="grid"))

