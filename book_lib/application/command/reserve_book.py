"""Something."""


class ReserveBook:
    """Ini."""

    def __init__(self, book_id):
        """."""
        self._book_id = book_id

    def get_request(self):
        """."""
        return {
            "book_id": self._book_id
        }

    def get_book_id(self):
        """Get book's id.

        This is description
        """
        return self._book_id
