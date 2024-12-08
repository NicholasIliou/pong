books = [
    {"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "isbn": "9781593275990"},
    {"title": "Python Crash Course", "author": "Eric Matthes", "isbn": "9781593279288"},
    {"title": "Fluent Python", "author": "Luciano Ramalho", "isbn": "9781491946008"},
    {"title": "Learning Python", "author": "Mark Lutz", "isbn": "9781449355739"},
    {"title": "Python for Data Analysis", "author": "Wes McKinney", "isbn": "9781491957660"},
    {"title": "Effective Python", "author": "Brett Slatkin", "isbn": "9780134034287"},
]

borrowed_books = []

import library_manager as libm
import library_status as libs

def main() -> None:
    libs.load_library_status()
    while True:
        print("\nLibrary System Menu:")
        print("1. Add a book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. List available books")
        print("5. List borrowed books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter ISBN: ")
            libm.add_book(title, author, isbn)
        elif choice == "2":
            isbn = input("Enter ISBN of the book to checkout: ")
            libm.borrow_book(isbn)
        elif choice == "3":
            isbn = input("Enter ISBN of the book to return: ")
            libm.return_book(isbn)
        elif choice == "4":
            libm.list_available_books()
        elif choice == "5":
            libm.list_borrowed_books()
        elif choice == "6":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
