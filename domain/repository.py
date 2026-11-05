from domain.book import Book


class BookRepository:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Можно добавлять только объекты класса Book")

        if self.get_book_by_id(book.book_id) is not None:
            raise ValueError("Книга с таким ID уже существует")

        self.books.append(book)

    def get_all_books(self):
        return self.books

    def get_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def remove_book(self, book_id):
        book = self.get_book_by_id(book_id)

        if book is None:
            raise ValueError("Книга не найдена")

        self.books.remove(book)

    def update_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Можно обновлять только объекты класса Book")

        if self.get_book_by_id(book.book_id) is None:
            raise ValueError("Книга не найдена")