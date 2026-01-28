from storage import load_books
from books import display_books

def search_books(): 
    print("Searching books...")
    # Implementation for searching books goes here

def view_all_books():
    print("Viewing all books...")
    

def view_rare_books(books):
    print("Viewing rare books...")
    rare_books = [book for book in books if book.get("is_rare", "No") == "Yes"]
    display_books(rare_books, view="detailed")


