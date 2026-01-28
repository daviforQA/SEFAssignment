from tabulate import tabulate
from storage import load_books

def add_book():
    print("Adding a book...")
    # Implementation for adding a book goes here

def edit_book(): 
    print("Editing a book...")
    # Implementation for editing a book goes here

def delete_book(): 
    print("Deleting a book...")
    # Implementation for deleting a book goes here

def display_books(books, view = "default", specific_fields = None):
    if not books:
        print("No books to display.")
        return

    DEFAULT_FIELDS = ["title", "author", "isbn"]
    ALL_FIELDS = ["title", "author", "genre", "isbn", "publication_year", "quantity_in_stock", "unit_price", "is_rare", "env_conditions", "additional_info"]


    if view == "default":
        fields_to_display = DEFAULT_FIELDS
    elif view == "detailed":
        fields_to_display = ALL_FIELDS
    elif view == "custom" and specific_fields:
        fields_to_display = ["title"] + specific_fields
    else:
        fields_to_display = DEFAULT_FIELDS

    rows = []
    for book in books:
        row = [book.get(field, "") for field in fields_to_display]
        rows.append(row)
        headers = [field.replace("_", " ").title() for field in fields_to_display]


    print(tabulate(rows, headers=headers, tablefmt="grid"))