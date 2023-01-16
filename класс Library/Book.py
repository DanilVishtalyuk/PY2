class Book:
    def __init__(self, book_id: int, name: str, pages: int):
        self.book_id = book_id
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.book_id}, name={self.name!r}, pages={self.pages})'
