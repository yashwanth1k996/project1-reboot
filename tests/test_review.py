import os
import unittest

from config import basedir
from app import app, db
from app.models import User
from user import given_review

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

    def test_given_recordreview(self):
        flag = given_review("yashwanth", "Love, Stargirl")
        self.assertTrue(flag)

    def test_not_given_recordreview(self):
        flag = given_review("yashwanth", "The Tenth Circle")
        self.assertFalse(flag)


if __name__ == '__main__':
    unittest.main()