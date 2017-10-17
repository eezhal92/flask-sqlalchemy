""".

Lending Service
"""


class LendingService:
    """.

    LendingService
    """

    def __init__(self, book_repo):
        self.book_repo = book_repo

    def record_borrowing(self):
        """.

        Cari buku yang available
        """
        self.book_repo.find
        return 'noop'

    def record_returning(self):
        return 'noop'