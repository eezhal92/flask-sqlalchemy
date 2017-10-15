""".

Main
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from mappings import init as init_mappings
from repository.book import BookRepository

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['MYSQL_URI']
db = SQLAlchemy(app)

init_mappings(db)

book_repo = BookRepository(db)


@app.route('/')
def index():
    """.

    Index Page
    """
    books = book_repo.find_all()

    html = ''

    for book in books:
        html += '<p>%s</p>' % book.title

    return html
