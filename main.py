from validation import get_valid_choice
from books import add_book, edit_book, delete_book, display_books
from search import search_books, view_all_books, view_rare_books
from reports import full_inventory_report, rare_book_report, low_stock_report
from utils import clear_screen, show_logo
from storage import load_books

books = load_books("books.csv")

def display_detailed_books():
    clear_screen()
    display_books(books, view="detailed")
# Detailed books display function - must be delared before use in MAIN_MENU

MAIN_MENU = {
    "1": ("Book management", "book_menu"),
    "2": ("Search books", search_menu),
    "3": ("View all records", display_detailed_books),
    "4": ("Exit", "exit"),
} # Main menu options

BOOK_MENU = {
    "1": ("Add a book", add_book),
    "2": ("Edit a book", edit_book),
    "3": ("Delete a book", delete_book),
    "4": ("Return to main menu", None),
} # Book management menu options

SEARCH_FIELDS = {
    "1": ("Title", "Title"),
    "2": ("Author", "Author"),
    "3": ("ISBN", "ISBN"),
    "4": ("Return", None),
}

VIEW_BOOKS_MENU = {
    "1": ("View books sorted by title", view_all_books),
    "2": ("View books sorted by author", view_all_books),
    "3": ("View books sorted by publication year", view_all_books),
    "4": ("Return to search menu", None),
} # View books menu options
    
def run_menu(menu, view = "default"):
    while True:
        clear_screen()
        display_books(books, view) # Display current books in inventory (default view, includes title, author, isbn)
        print("\n" + "="*35 + "\n") # Menu header separator

        for key, (label, _) in menu.items():
            print(f"{key}. {label}")   # Display menu options

        choice = get_valid_choice(menu.keys())
        _, action = menu[choice]

        if action is None:
            return # Return to previous menu
        elif isinstance(action, str):
            return action # Navigate to another menu
        else:
            action() # Execute the function associated with the choice
            input("\nPress Enter to return to menu...")


def main():
    show_logo()
    current_menu = "main"
    while True: # Main loop to handle menu navigation
        if current_menu == "main":
            next_menu = run_menu(MAIN_MENU)
        elif current_menu == "book_menu":
            run_menu(BOOK_MENU)
            next_menu = "main"
        elif current_menu == "search_menu":
            run_menu(SEARCH_MENU)
            next_menu = "main"
        elif current_menu == "exit":
            break
        current_menu = next_menu
main()

