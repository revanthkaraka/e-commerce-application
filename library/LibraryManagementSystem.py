class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
class Library:
    def __init__(self):
        self.__books = [] 

    def add_book(self,book):
        for a in self.__books:
            if a.isbn==book.isbn:
                print(f"Book with isbn: {book.isbn} already exists.")
                return
        self.__books.append(book)
        print(f"Book added: {book.title}")

    def remove_book(self, isbn):
        for a in self.__books:
            if a.isbn == isbn:
                self.__books.remove(a)
                print(f"Book removed is : {a.title}")
                return
        print(f"No book found with ibsn number : {isbn}")

    def display_books(self):
        if not self.__books:
            print("No books are available in the library.")
        else:
            print("Available books:")
            for index, book in enumerate(self.__books, start=1):
                print(f"{index}. {book}")

lib = Library()

book1 = Book("Python Basics", "Revanth", "9783161484100")
book2 = Book("Data Science ", "Nikhil", "9781234567897")
book3 = Book("Machine Learning", "Mohan", "9789876543210")

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.add_book(book1) 

lib.display_books()

lib.remove_book("9783161484100")

lib.display_books()
