from book_lib.presentation.resource.book import Book
from book_lib.presentation.resource.borrowing import Borrowing


def init(api, db):
    api.add_resource(
        Borrowing,
        '/borrowings',
        resource_class_kwargs={'db': db}
    )

    api.add_resource(
        Book,
        '/books',
        resource_class_kwargs={'db': db}
    )
