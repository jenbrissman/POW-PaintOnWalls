from sqlalchemy import func
from model import User, Image, db
from server import app


def test_user():
    """Creates test user in test database"""

    test_user = User(first_name = 'Jennifer', last_name = 'Testman', email = 'testing@testing.com', password = 'jenny')
    db.session.add(test_user)
    db.session.commit()


def test_image():
    """Creates test image in test database"""

    test_image = Image(user_id=1, image_title = "Sailor's Kiss", artist = "Kobra", location = "The High Line, West 30th Street, New York, NY, USA", image_url="http://res.cloudinary.com/jenbrissman/image/upload/v1619933391/meq168zr4pglkskc8oge.jpg")
    db.session.add(test_image)
    db.session.commit()
    
