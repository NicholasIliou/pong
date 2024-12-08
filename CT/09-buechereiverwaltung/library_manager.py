import library_status as libs 
books=libs.load_library_status()

def add_book(title: str, author: str, isbn: str) -> None:
    borrowed_books=libs.load_borrowed_books()
    books.append({"title": title, "author": author, "isbn": isbn})
    libs.store_library_status(books,borrowed_books)

def print_book(book: dict[str, str]) -> None:
    print(f" * {book['title']} by {book['author']} (isbn: {book['isbn']})")

def borrow_book(isbn: str) -> None:
    borrowed_books=libs.load_borrowed_books()
    for book in books:
        if book["isbn"] == isbn and book not in borrowed_books:
            borrowed_books.append(book)
            print(f"Book '{book['title']}' borrowed out successfully.")
            libs.store_library_status(books,borrowed_books)
            return
    print("Book is not available for borrow.")

def return_book(isbn: str) -> None:
    borrowed_books=libs.load_borrowed_books()
    for book in borrowed_books:
        if book["isbn"] == isbn:
            borrowed_books.remove(book)
            for b in books:
                if b["isbn"] == isbn:
                    print(f"Book '{b['title']}' returned successfully.")
                    libs.store_library_status(books,borrowed_books)
                    return
    print("Book not found in borrowed list.")

def list_all_books() -> None:
    list_available_books()
    print("")
    list_borrowed_books()

def list_available_books() -> None:
    borrowed_books=libs.load_borrowed_books()
    print("Books Available:")
    for book in borrowed_books:
        for value in book.values():
            if value == "available":
                print_book(book)
    
def list_borrowed_books() -> None:
    borrowed_books=libs.load_borrowed_books()
    print("Borrowed Books:")
    for book in borrowed_books:
        for value in book.values():
            if value == "borrowed":
                print_book(book)