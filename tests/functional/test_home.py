import os
from flask_sqlalchemy import SQLAlchemy
from flask import session
import testing.postgresql
from sqlalchemy import create_engine
import psycopg2
import tempfile
import pytest

def test_home(test_client):
    """Tests homepage"""

    result = test_client.get('/')
    assert(result.status_code, 200)
    assert(b'<p class="message"> Not registered?', result.data)