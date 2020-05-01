import unittest
from BaseTest import BaseTestURLs

class TestLoginUrls(BaseTestURLs):
    def test_login_sucess(self):
        response = self.app.post("/login", data=dict(name="yashwanth", password="1234"), follow_redirect=True)
        self.assertIn("signed in as yashwanth", response.data.decode())
        self.assertEquels(response.status_code, 200)

