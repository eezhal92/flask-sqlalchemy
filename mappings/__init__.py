""".

Mapping
"""

from entities.book import Book


def init(db):
    """.

    Init
    """
    db.mapper(Book, db.Table(
        'books',
        db.Column('id', db.Integer, primary_key=True),
        db.Column('title', db.Unicode),
        db.Column('author', db.Unicode)
    ))
