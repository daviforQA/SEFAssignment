def add_books():
    print("Add book")

def delete_book(): 

def exit_programme():
    return False

def generate_reports():

def get_menu_choice():
    while True:
        choice = input("Select an option: ").strip()

        if not choice.isdigit():
            print("Please enter a number.")
            continue

        choice = int(choice)

        if 1 <= choice <= 8:
            return choice
        else:
            print("Choice must be between 1 and 8.")

def rare_book_menu():

def search_books():

def update_books():

def view_books():
    
MAIN_MENU = {
    "1": ("Add Books", add_book),
    "2": ("View Books", view_books),
    "3": ("Search Books", search_books),
    "4": ("Update Books", update_books),
    "5": ("Delete Book", delete_book),
    "6": ("Rare Book Menu", rare_book_menu),
    "7": ("Generate Reports", generate_reports),
    "8": ("Exit", exit_programme)
}

def main():
    running = True
    while running:
        clear_screen()
        print("\n==== Bookstore Managment Systems ====\nMenu:\n")
        for key, (label, _) in MAIN_MENU:
            print(f"{key}. {label}")
        get_menu_choice
    main()