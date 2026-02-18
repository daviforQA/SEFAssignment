from validation import get_valid_choice
from books import add_book, edit_book_menu, delete_book, display_books
from search import search_menu
from utils import clear_screen, show_logo
from storage import load_books

books = load_books("books.csv")

def display_detailed_books():
    clear_screen()
    display_books(books, view="detailed")
    input("\nPress Enter to return to menu...")
# Detailed books display function - must be delared before use in MAIN_MENU

MAIN_MENU = {
    "1": ("Book management", "book_menu"),
    "2": ("Search books", search_menu),
    "3": ("View all records", display_detailed_books),
    "4": ("Exit", "exit"),
} # Main menu options

BOOK_MENU = {
    "1": ("Add a book", add_book),
    "2": ("Edit a book", edit_book_menu),
    "3": ("Delete a book", delete_book),
    "4": ("Return to main menu", None),
} # Book management menu options
    
def run_menu(menu, view = None, menu_header = None):
    while True:
        clear_screen()
        if view != None:
            display_books(books) # Display current books in inventory (default view, includes isbn, title, author)
        if menu_header:
            print(menu_header)
        print("="*35 + "\n") # Menu header separator

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

def main():
    show_logo()
    current_menu = "main"
    while True: # Main loop to handle menu navigation
        if current_menu == "main":
            next_menu = run_menu(MAIN_MENU, view = "default", menu_header = "Main Menu")
        elif current_menu == "book_menu":
            run_menu(BOOK_MENU, menu_header = "Book Management Menu")
            next_menu = "main"
        elif current_menu == "exit":
            break
        current_menu = next_menu
main()

