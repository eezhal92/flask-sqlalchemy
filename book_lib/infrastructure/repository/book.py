""".

Book Repository
"""

from book_lib.domain.entities.book import Book
from book_lib.infrastructure.repository.base import BaseRepository


class BookRepository(BaseRepository):
    """.

    BookRepository
    """

    def create(self, book):
        """`.

        Create new book record
        """
        return super(BookRepository, self).create(book)

    def find_all(self):
        """.

        Find all book
        """
        books = self.session().query(Book).all()
        return books
