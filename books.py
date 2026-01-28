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

def display_books(books):
    if not books:
        print("No books to display.")
        return

    headers = ["Title", "Author", "Year", "Stock", "Price", "Rare"]
    rows = []

    for book in books:
        rows.append([
            book["title"],
            book["author"],
            book["publication_year"],
            book["quantity_in_stock"],
            book["unit_price"],
            book["is_rare"]
        ])

    print(tabulate(rows, headers=headers, tablefmt="grid"))