from abc import ABC, abstractmethod


class BookRepository(ABC):

    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def get_all_books(self):
        pass

    @abstractmethod
    def get_book_by_id(self, book_id):
        pass

    @abstractmethod
    def remove_book(self, book_id):
        pass

    @abstractmethod
    def update_book(self, book):
        pass
