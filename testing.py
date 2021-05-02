import os
from flask_sqlalchemy import SQLAlchemy
from server import app
from unittest import TestCase
from flask import session
from model import *
from test_seed import *

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

    # def test_upload(self):
    #     """Tests page that displays upload image form"""

    #     result = self.client.get('/upload')
    #     self.assertEqual(result.status_code, 200)
    #     self.assertIn(b'enctype="multipart/form-data', result.data)


class TestPowDatabase(TestCase):
    """Tests Pow database"""

    def setUp(self):
        """Code to run before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True



if __name__ == '__main__': 
    import unittest
    unittest.main()