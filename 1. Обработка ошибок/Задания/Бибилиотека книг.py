class BookNotFoundError(Exception):
    def __init__(self, title):
        self.title = title
        super().__init__(f'Книга {title} не найдена.')


class BookAlreadyExistsError(Exception):
    def __init__(self, title):
        self.title = title
        super().__init__(f'Книга {title} уже находится в библиотеке.')


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        if title in self.books:
            raise BookAlreadyExistsError(title)
        self.books.append(title)

    def remove_book(self, title):
        if title not in self.books:
            raise BookNotFoundError(title)
        self.books.remove(title)

    def find_book(self, title):
        if title not in self.books:
            raise BookNotFoundError(title)
        print(f'Книга {title} найдена!')


library = Library()