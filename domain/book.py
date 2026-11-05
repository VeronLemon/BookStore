class Book:
    def __init__(self, book_id, title, author, price, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (
            f"ID: {self.book_id} | "
            f"Название: {self.title} | "
            f"Автор: {self.author} | "
            f"Цена: {self.price} руб. | "
            f"Количество: {self.quantity}"
        )