""".

Something
"""


class Book:
    """.

    Book
    """

    def __init__(self, title=None, author=None):
        """.

        Constructor
        """
        self.title = title
        self.author = author

    def serialize(self):
        return {
            'title': self.title,
            'author': self.author
        }
