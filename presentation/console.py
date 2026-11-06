from domain.book import Book


class Console:
    def __init__(self, book_service):
        self.book_service = book_service

    def run(self):
        while True:
            print("\n=== Книжный магазин ===")
            print("1. Показать все книги")
            print("2. Добавить книгу")
            print("3. Найти книгу по ID")
            print("4. Продать книгу")
            print("5. Удалить книгу")
            print("0. Выход")

            choice = input("Выберите действие: ")

            try:
                if choice == "1":
                    self.show_books()
                elif choice == "2":
                    self.add_book()
                elif choice == "3":
                    self.find_book()
                elif choice == "4":
                    self.sell_book()
                elif choice == "5":
                    self.remove_book()
                elif choice == "0":
                    print("Программа остановлена")
                    break
                else:
                    print("Неверный пункт меню")

            except (ValueError, OSError, TypeError) as error:
                print(f"Ошибка: {error}")

    def show_books(self):
        books = self.book_service.get_all_books()

        if not books:
            print("В магазине пока нет книг")
            return

        for book in books:
            print(book)

    def add_book(self):
        book_id = int(input("Введите ID книги: "))
        title = input("Введите название: ")
        author = input("Введите автора: ")
        price = float(input("Введите цену: "))
        quantity = int(input("Введите количество: "))

        book = Book(book_id, title, author, price, quantity)

        self.book_service.add_book(book)

        print("Книга успешно добавлена")

    def find_book(self):
        book_id = int(input("Введите ID книги: "))

        book = self.book_service.get_book_by_id(book_id)

        if book is None:
            print("Книга не найдена")
        else:
            print(book)

    def sell_book(self):
        book_id = int(input("Введите ID книги: "))
        quantity = int(input("Введите количество для продажи: "))

        total = self.book_service.sell_book(book_id, quantity)

        print(f"Продажа оформлена. Сумма: {total} руб.")

    def remove_book(self):
        book_id = int(input("Введите ID книги: "))

        self.book_service.remove_book(book_id)

        print("Книга успешно удалена")