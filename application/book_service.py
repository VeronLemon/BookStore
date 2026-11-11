from domain.repository import BookRepository


class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def add_book(self, book):
        self.repository.add_book(book)

    def get_all_books(self):
        return self.repository.get_all_books()

    def get_book_by_id(self, book_id):
        return self.repository.get_book_by_id(book_id)

    def sell_book(self, book_id, quantity):
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise ValueError("Количество должно быть целым числом")

        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")

        book = self.repository.get_book_by_id(book_id)

        if book is None:
            raise ValueError("Книга не найдена")

        if book.quantity < quantity:
            raise ValueError("Недостаточно книг в наличии")

        book.quantity -= quantity
        self.repository.update_book(book)

        return book.price * quantity

    def remove_book(self, book_id):
        self.repository.remove_book(book_id)
