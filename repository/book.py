""".

Book Repository
"""

from entities.book import Book
from repository.base import BaseRepository


class BookRepository(BaseRepository):
    """.

    BookRepository
    """

    def find_all(self):
        """.

        Find all book
        """
        books = self.session().query(Book).all()
        return books
