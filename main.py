from validation import get_valid_choice
from books import add_book, edit_book, delete_book, display_books
from search import search_books, view_all_books, view_rare_books
from reports import full_inventory_report, rare_book_report, low_stock_report
from utils import clear_screen, show_logo
from storage import load_books

books = load_books("books.csv")

MAIN_MENU = {
    "1": ("Book management", "book_menu"),
    "2": ("Search & view books", "search_menu"),
    "3": ("Reports", "reports_menu"),
    "4": ("Exit", "exit"),
}

BOOK_MENU = {
    "1": ("Add a book", add_book),
    "2": ("Edit a book", edit_book),
    "3": ("Delete a book", delete_book),
    "4": ("Return to main menu", None),
}

SEARCH_MENU = {
    "1": ("Search by field", search_books),
    "2": ("Detailed Book View", view_all_books),
    "3": ("Detailed Rare Book View", view_rare_books),
    "4": ("Return to main menu", None),
}

VIEW_BOOKS_MENU = {
    "1": ("View all books (unsorted)", view_all_books),
    "2": ("View books sorted by title", view_all_books),
    "3": ("View books sorted by author", view_all_books),
    "4": ("View books sorted by publication year", view_all_books),
    "5": ("Return to search menu", None),
}

VIEW_RARE_BOOKS_MENU = {
    "1": ("View rare books (unsorted)", view_rare_books(books)),
    "2": ("View rare books sorted by title", view_rare_books),
    "3": ("View rare books sorted by author", view_rare_books),
    "4": ("View rare books sorted by publication year", view_rare_books),
    "5": ("Return to search menu", None),
}


REPORTS_MENU = {
    "1": ("Full inventory report", full_inventory_report),
    "2": ("Rare book report", rare_book_report),
    "3": ("Low stock report", low_stock_report),
    "4": ("Return to main menu", None),
}
    
def run_menu(menu):
    while True:
        clear_screen()
        display_books(books) # Display current books in inventory (default view, includes title, author, isbn)
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
        elif current_menu == "view_books_menu":
            run_menu(VIEW_BOOKS_MENU)
            next_menu = "search_menu"
        elif current_menu == "view_rare_books_menu":
            run_menu(VIEW_RARE_BOOKS_MENU)
            next_menu = "search_menu"
        elif current_menu == "reports_menu":
            run_menu(REPORTS_MENU)
            next_menu = "main"
        elif current_menu == "exit":
            break
        current_menu = next_menu

main()

