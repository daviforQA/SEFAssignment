from tabulate import tabulate
from storage import load_books
from utils import clear_screen
from validation import get_valid_choice, VALIDATORS, normalise, field_definer, field_options_menu, FIELD_TYPES

books = load_books("books.csv")


def add_book():
    while True:
        display_books(books)
        print("Add a New Book\n" + "="*35 + "\n") # Header separator
        new_book = [{}]
        input("Press Enter to continue...")


def edit_book_menu(): 
    while True:
        clear_screen
        display_books(books)
        print("Edit a Book\n" + "="*35 + "\n") # Header separator
        isbn = input("Enter the ISBN of the book you want to edit: ").strip()
        book_to_edit = next((book for book in books if book.get("isbn") == isbn), None)

        if not book_to_edit:
            print("Book not found.")
            input("\nPress Enter to continue...")
            break
        
        
        display_books([book_to_edit], view="detailed")
        print("\nSelect field to edit:")
        menu = field_options_menu("editable")
        for key, field in menu.items():
            if field:
                print(f"{key}. {field.capitalize()}")
            else:
                print(f"{key}. Return to edit menu")
        choice = get_valid_choice(menu.keys())
        field = menu[choice]

        if field is None:
            continue # Return to edit menu
        
       
        print("\nBook updated successfully!")
        input("\nPress Enter to return to menu...")
        break

def fill_book_field(book, field, include_isbn = True):
    for field in FIELD_TYPES:
        if not include_isbn and field == "isbn":
            continue

        current_value = book.get(field, "")

        while True:
            if current_value:
                prompt = f"Enter value for {field} (current: {current_value}): "
            else:
                prompt = f"Enter value for {field}: "

            new_value = input(prompt).strip()
            if not new_value and current_value:
                book[field] = current_value
                break
            elif new_value:
                field_config = FIELD_TYPES[field]
                field_type = field_config["type"]
                validator = VALIDATORS[field_type]
                if validator(new_value):
                    book[field] = normalise(new_value, field_type)
                    break
                else:
                    print(f"Invalid input for {field}. Please try again.")

def delete_book(): 
    print("Deleting a book...")
    
    # Implementation for deleting a book goes here

def display_books(books, view = "default", specific_fields = None):
    if not books:
        print("No books to display.")
        return

    if view == "default":
        fields_to_display = [
            key for key, config in FIELD_TYPES.items()
            if config.get("view") == "default"
        ]
    elif view == "detailed":
        fields_to_display = list(FIELD_TYPES.keys())
    elif view == "custom" and specific_fields:
        fields_to_display = ["isbn", "title"] + specific_fields
    else:
        fields_to_display = [
            key for key, config in FIELD_TYPES.items()
            if config.get("view") == "default"]

    rows = []
    for book in books:
        row = [book.get(field, "") for field in fields_to_display]
        rows.append(row)
        headers = [field.replace("_", " ").title() for field in fields_to_display]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

