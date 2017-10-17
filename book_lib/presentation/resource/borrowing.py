"""Borrowing Controller."""

from flask import jsonify
from flask_restful import Resource
from book_lib.infrastructure.repository.book import BookRepository
from book_lib.application.service import Borrowing as BorrowingService


class Borrowing(Resource):
    """."""

    def __init__(self, **kwargs):
        """."""
        self.db = kwargs['db']

        book_repo = BookRepository(self.db)

        self.borrowing_service = BorrowingService(book_repo)

    def post(self):
        """."""
        # hard coded, it supposed to be retrieved from request
        title = 'Refactoring'

        try:
            borrowed_book = self.borrowing_service.borrow(title)
        except Exception as inst:
            return str(inst)

        return jsonify(borrowed_book.serialize())
