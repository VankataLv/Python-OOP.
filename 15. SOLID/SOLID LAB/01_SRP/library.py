class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"{self.title}, {self.author}, {self.location}"


class Library:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, title: str):
        try:
            book = [b for b in self.books if b.title == title]
            return book
        except IndexError:
            return None


book1 = Book("Title1", "Author1", "ukn")
book2 = Book("Title2", "Author2", "ukn")

lib = Library()
lib.add_book(book1)
lib.add_book(book2)

print(book1)