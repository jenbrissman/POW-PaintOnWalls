import os
from flask_sqlalchemy import SQLAlchemy
from flask import session
from model import db, connect_to_db
from unittest import *

import testing.postgresql
from sqlalchemy import create_engine
import psycopg2

import os
import tempfile
import pytest


# def setUp(test_client):
#     """Code to run before every test."""

#     client = test_client
#     postgresql = testing.postgresql.Postgresql()
        
#     with testing.postgresql.Postgresql() as postgresql:
#         # connect to PostgreSQL
#         engine = create_engine(postgresql.url())
#         testdb = psycopg2.connect(**postgresql.dsn())

#         app.config['TESTING'] = True
#         connect_to_db(app, db_uri=testdb)
#         # connect_to_db(app, db_uri="postgresql:///testdb")
#         db.create_all()

#     with client as client:
#         with client.session_transaction() as sess:
#             sess['user_id'] = 1

def test_upload(test_client):
    """Tests page that displays upload image form"""

    result = test_client.get('/upload')
    assert(result.status_code, 200)
    assert(b'id="upload-art"', result.data)

def test_logout():
    """Tests if user gets logged out of session"""
    result = test_client.get('/logout')
    assert(result.status_code, 200)
    # assert(b'id="upload-art"', result.data)
#       with client as client:
# #         with client.session_transaction() as sess:
# #             sess['user_id'] = 1


# def tearDown(self):
#     """Code to run after every test"""
    
#     db.session.remove()
#     db.drop_all()
#     db.engine.dispose()

#     self.postgresql.stop()

