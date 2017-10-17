"""."""


class Borrowing:
    """."""

    def __init__(self, book_repo):
        """."""
        self.book_repo = book_repo

    def borrow(self, book_title):
        """."""
        available_copies = self.find_available_copies(book_title)

        if (len(available_copies) == 0):
            raise Exception(
                "No copies of title `{}` are available".format(book_title)
            )

        to_be_borrowed_book = available_copies[0]
        self.book_repo.mark_borrowed(to_be_borrowed_book)

        return to_be_borrowed_book

    def find_available_copies(self, book_title):
        """."""
        return self.book_repo.find_available_copies(book_title)
