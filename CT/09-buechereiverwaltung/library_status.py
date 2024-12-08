import csv

def store_library_status(books:list[dict[str:str,str,str,str,str,int]],borrowed_books:list[dict[str:str,str,str,str,str,int]])->None:
    with open("data.csv","w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["title","author","isbn","status"])
        for book in books:
            status = "borrowed" if book in borrowed_books else "available"
            writer.writerow(list(book.values())+[status])

def load_library_status()->list[dict[str:str,str,str,str,str,int]]:
    with open("data.csv","r", newline='') as file:
        reader = csv.reader(file)
        data=[]
        for idx,row in enumerate(reader):
                if idx > 0:
                    data.append(dict(title=row[0],author=row[1],isbn=row[2]))
    return data

def load_borrowed_books()->list[dict[str:str,str,str,str,str,int]]:
    with open("data.csv","r", newline='') as file:
        reader = csv.reader(file)
        data=[]
        for idx,row in enumerate(reader):
                if idx > 0:
                    data.append(dict(title=row[0],author=row[1],isbn=row[2],status=row[3]))
    return data

if __name__ == "__main__":
    # code to reset the csv
    from main import books, borrowed_books
    books_new=load_library_status()
    store_library_status(books_new,borrowed_books)
    print(load_library_status())
    store_library_status(books,borrowed_books)
    load_borrowed_books()