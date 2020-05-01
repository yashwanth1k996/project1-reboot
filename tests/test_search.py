import os
import unittest

from config import basedir
from app import app, db
from models import Books
from application import get_books


class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        # db.session.remove()
        # db.drop_all()
        pass

    def test_search_true(self):

        totalbooks = get_books("The Secret Keeper")
        self.assertEquals(totalbooks, ["The Secret Keeper"])
        totalbooks1 = get_books("A Touch of Dead")
        self.assertEquals(totalbooks, ["A Touch of Dead"])
        totalbooks2 = get_books("The Brothers K")
        self.assertEquals(totalbooks, ["The Brothers K"])
        totalbooks3 = get_books("The Lightning Thief")
        self.assertEquals(totalbooks, ["The Lightning Thief"])



if __name__ == '__main__':
    unittest.main()
