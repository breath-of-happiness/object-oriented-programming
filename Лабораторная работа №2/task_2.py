class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'


class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books
    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, id_: int) -> int:
        for i, b in enumerate(self.books):
            if b.id == id_:
                return i
            else:
                raise ValueError("Книги с запрашиваемым  id не существует")
