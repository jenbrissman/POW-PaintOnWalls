from sqlalchemy import func
import model
from server import app

def test_user():
    """Creates test user in test database"""

    test_user = User(first_name = 'Jenny', last_name = 'Testman', email = 'test@test.com', password = 'shopify')
    db.session.add(test_user)
    db.session.commit()


