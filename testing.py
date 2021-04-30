from server import app
from unittest import TestCase
from flask import session
import model
# from test_seed import *

class PowTests(TestCase):
    """Tests Pow site"""

    def setUp(self):
        """Code to run before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_home(self):
        """Tests homepage"""

        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'<p class="message"> Not registered?', result.data)

    # def test_upload(self):
    #     """Tests page that displays upload image form"""

    #     result = self.client.get('/upload')
    #     # self.assertEqual(result.status_code, 200)
    #     self.assertIn(b'name="submit">SUBMIT', result.data)


class TestPowDatabase(TestCase):
    """Tests Pow database"""

    def setUp(self):
        """Code to run before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        connect_to_db(app, db_uri='postgresql:///testdb')

        db.create_all()
        test_data()

    def test_home(self):
        """Tests homepage"""

        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'<p class="message"> Not registered?', result.data)

    def tearDown(self):
        """Code to run after every test"""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()

if __name__ == '__main__': 
    import unittest
    unittest.main()