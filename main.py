from application.book_service import BookService
from infrastructure.json_repository import JsonBookRepository
from presentation.console import Console


def main():
    try:
        repository = JsonBookRepository()
        service = BookService(repository)
        console = Console(service)

        console.run()

    except (ValueError, OSError, TypeError) as error:
        print(f"Не удалось запустить программу: {error}")


if __name__ == "__main__":
    main()