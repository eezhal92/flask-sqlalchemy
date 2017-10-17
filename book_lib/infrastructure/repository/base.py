"""Repo."""


class BaseRepository(object):
    """.

    Base Repo
    """

    def __init__(self, db):
        """.

        Constructor
        """
        self.db = db

    def session(self):
        """.

        Get session
        """
        return self.db.session

    def create(self, item):
        """.

        Insert into db
        """
        self.session().add(item)
        self.session().commit()
