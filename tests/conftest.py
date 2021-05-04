
from model import User, Image, db
from project import create_app
import pytest

@pytest.fixture(scope='module')
def test_client():
    """Code to run before every test."""

    flask_app = create_app('test.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            return testing_client  # this is where the testing happens!

    
@pytest.fixture(scope='module')
def test_user():
    """Creates test user in test database"""

    test_user = User(first_name = 'Jenny', last_name = 'Testman', email = 'test@test.com', password = 'shopify')
    db.session.add(test_user)
    db.session.commit()

@pytest.fixture(scope='module')
def test_image():
    """Creates test image in test database"""

    test_image = Image(user_id=1, image_title = "Sailor's Kiss", artist = "Kobra", location = "The High Line, West 30th Street, New York, NY, USA", image_url="http://res.cloudinary.com/jenbrissman/image/upload/v1619933391/meq168zr4pglkskc8oge.jpg")
    db.session.add(test_image)
    db.session.commit()
    
