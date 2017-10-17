"""Book Entity."""


class Book:
    """."""

    def __init__(self, title=None, author=None, borrowed=None):
        """."""
        self.title = title
        self.author = author
        self.borrowed = borrowed

    def serialize(self):
        """Serialize model."""
        return {
            '_id': self.id,
            'title': self.title,
            'author': self.author
        }
