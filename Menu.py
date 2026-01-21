def add_books():
    print("Add book")

def delete_book(): 
    print("Delete book")
def exit_programme():
    return False

def generate_reports():
    print("Generate reports")

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
    print("Rare book menu")

def search_books():
    print("Search books")

def update_books():
    print("Update books")

def view_books():
    print("View books")
    
MAIN_MENU = {
    "1": ("Add Books", add_books),
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
        for key, (label, _) in MAIN_MENU.items():
            print(f"{key}. {label}")
        choice = get_menu_choice()