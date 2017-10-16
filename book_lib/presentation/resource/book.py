"""Books Controller."""

from flask import jsonify
from flask_restful import Resource
from book_lib.infrastructure.repository.book import BookRepository


class Book(Resource):
    """."""
    def __init__(self, **kwargs):
        self.db = kwargs['db']
        self.book_repo = BookRepository(self.db)

    def get(self):
        """."""
        books = [b.serialize() for b in self.book_repo.find_all()]

        return jsonify(books)
