#Functions to deal with reading/writing to books.csv file
import csv

def load_books(filename="books.csv"):
    books = []
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                books.append(row)
        return books
    except FileNotFoundError:
        return []

        