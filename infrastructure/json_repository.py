import json
from pathlib import Path

from domain.book import Book
from domain.repository import BookRepository


class JsonBookRepository(BookRepository):

    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = Path(__file__).resolve().parent.parent / "books.json"
        else:
            self.file_path = Path(file_path)

        self.books = []
        self.load_books()

    def load_books(self):
        if not self.file_path.exists():
            self.save_books()
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("Файл должен содержать список книг")

            self.books = []

            for item in data:
                book = Book(
                    item["book_id"],
                    item["title"],
                    item["author"],
                    item["price"],
                    item["quantity"]
                )
                self.books.append(book)

        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            raise ValueError(f"Ошибка загрузки книг: {error}")

    def save_books(self):
        data = []

        for book in self.books:
            data.append({
                "book_id": book.book_id,
                "title": book.title,
                "author": book.author,
                "price": book.price,
                "quantity": book.quantity
            })

        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except OSError as error:
            raise OSError(f"Ошибка сохранения книг: {error}")

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Можно добавлять только объекты класса Book")

        if self.get_book_by_id(book.book_id) is not None:
            raise ValueError("Книга с таким ID уже существует")

        self.books.append(book)
        self.save_books()

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
        self.save_books()

    def update_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Можно обновлять только объекты класса Book")

        if self.get_book_by_id(book.book_id) is None:
            raise ValueError("Книга не найдена")

        self.save_books()
