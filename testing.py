import os
from flask_sqlalchemy import SQLAlchemy
from server import app
from unittest import TestCase
from flask import session
from model import db, connect_to_db
from test_seed import test_user, test_image
import unittest
import testing.postgresql
from sqlalchemy import create_engine
import psycopg2

import os
import tempfile
import pytest

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


class TestPowLoggedIn(TestCase):
    """Tests if a user is logged in correctly"""

    def setUp(self):
            """Code to run before every test."""

            self.client = app.test_client()
            self.postgresql = testing.postgresql.Postgresql()
            
    with testing.postgresql.Postgresql() as postgresql:
        # connect to PostgreSQL
        engine = create_engine(postgresql.url())
        testdb = psycopg2.connect(**postgresql.dsn())

        app.config['TESTING'] = True
        connect_to_db(app, db_uri=testdb)
        # connect_to_db(app, db_uri="postgresql:///testdb")
        db.create_all()
        test_user()
        test_image()

        with self.client as client:
                    with client.session_transaction() as sess:
                        sess['user_id'] = 1

    def test_upload(self):
            """Tests page that displays upload image form"""

            result = self.client.get('/upload')
            self.assertEqual(result.status_code, 200)
            self.assertIn(b'id="upload-art"', result.data)

    def test_logout(self):
        """Tests if user gets logged out of session"""

    def tearDown(self):
            """Code to run after every test"""
            
            db.session.remove()
            db.drop_all()
            db.engine.dispose()

            self.postgresql.stop()


if __name__ == '__main__': 
    import unittest
    unittest.main()