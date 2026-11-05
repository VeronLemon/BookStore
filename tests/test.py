from pathlib import Path

from domain.book import Book
from infrastructure.json_repository import JsonBookRepository


file_path = Path(__file__).resolve().parent / "Test.json"

file_path.write_text("[]", encoding="utf-8")

repository = JsonBookRepository(file_path)

book = Book(1, "Книга", "Автор", 1, 1)
repository.add_book(book)