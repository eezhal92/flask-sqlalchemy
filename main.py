"""Main."""

import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from book_lib.infrastructure.mappings import init as init_mappings
from book_lib.presentation.resource import init as init_resources

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['MYSQL_URI']

db = SQLAlchemy(app)
init_mappings(db)

api = Api(app)
init_resources(api, db)
