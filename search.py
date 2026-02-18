from storage import load_books
from books import display_books
from utils import clear_screen
from validation import get_valid_choice, VALIDATORS, normalise, field_definer, FIELD_TYPES, field_options_menu

books = load_books("books.csv")

RARITY_OPTIONS = {
    "1": ("Rare", "True"),
    "2": ("Common", "False"),
}

def search_menu():
    while True:
        clear_screen()
        print("Select Field\n" + "="*20)
        menu = field_options_menu("searchable")
        for key, field in menu.items():
            if field:
                print(f"{key}. {field.capitalize()}")
            else:
                print(f"{key}. Return to main menu")
        choice = get_valid_choice(menu.keys())
        field = menu[choice]

        if field is None:
            return # Return to main menu
        elif field == "rarity":
            query = rare_books_menu()
        elif field == "publication":
            query = get_valid_choice(range(1000, 2027), prompt="Enter publication year (e.g. 1999): ", error_msg="Please enter a valid year between 1000 and 2024.")
        else:
            query = input(f"Enter search query for {field}: ")
    
        results = search_books(books, field, query)
        clear_screen()

        if not results:
            print("No matches found.")
            input("\nPress Enter to return to search menu...")
        else:
            display_books(results, view="detailed")
            input("\nPress Enter to return to search menu...")

def rare_books_menu():
    while True:
        clear_screen()
        print("Select Rarity\n" + "="*20)
        for key, (label, _) in RARITY_OPTIONS.items():
            print(f"{key}. {label}")

        choice = get_valid_choice(RARITY_OPTIONS.keys())
        _, rarity = RARITY_OPTIONS[choice]
        return rarity

def search_books(books, field, query):
    field_key, field_type = field_definer(field) # Get internal key and type for the selected field

    # Validate input
    validator = VALIDATORS[field_type]
    if not validator(query):
        return []

    query = normalise(query, field_type)
    matches = []

    for book in books:
        book_value = book.get(field_key)

        if book_value is None:
            continue

        # Normalise book value
        book_value_norm = normalise(str(book_value), field_type)

        if field_type == "text":
            if query in book_value_norm:
                matches.append(book)

        else:
            if query == book_value_norm:
                matches.append(book)

    return matches


def view_all_books():
    print("Viewing all books...")


