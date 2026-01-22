MAIN_MENU = {
    "1": ("Book management", "BOOK_MENU"),
    "2": ("Search & view books", "SEARCH_MENU"),
    "3": ("Reports", "REPORTS_MENU"),
    "4": ("Exit", "exit"),
}
'''
BOOK_MENU = {
    "1": ("Add a book", add_book),
    "2": ("Edit a book", edit_book),
    "3": ("Delete a book", delete_book),
    "4": ("Return to main menu", None),
}

SEARCH_MENU = {
    "1": ("Search by field", search_books),
    "2": ("View all books", view_all_books),
    "3": ("View rare books only", view_rare_books),
    "4": ("Return to main menu", None),
}

REPORTS_MENU = {
    "1": ("Full inventory report", full_inventory_report),
    "2": ("Rare book report", rare_book_report),
    "3": ("Low stock report", low_stock_report),
    "4": ("Return to main menu", None),
}
'''

def run_menu(menu):
    while True:
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")

        
        _, action = menu[choice]

        if action is None:
            return
        elif isinstance(action, str):
            return action
        else:
            action()

def main():
    while True:
          run_menu(MAIN_MENU)

main()

