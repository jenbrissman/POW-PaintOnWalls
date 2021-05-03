from model import connect_to_db, db, User, Image

###########################USER######################################

def create_user(first_name, last_name, email, password):
    """Creates and returns a new user"""
    user = User(first_name=first_name, last_name=last_name,
                email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def check_email(email):
    """Return database row that matches given email."""
    return User.query.filter(User.email == email).first()

def get_user_by_email(email):
    """Return a user by email"""
    return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    return User.query.get(user_id)

###########################IMAGE#######################################

def create_image(user_id, image_title, artist, location, image_url):
    """Creates and returns image"""
    image = Image(user_id=user_id,
                  image_title=image_title, artist=artist, location=location, image_url=image_url)
    db.session.add(image)
    db.session.commit()
    return image

def get_image_by_user(user_id):
    return Image.query.filter_by(user_id=user_id).all()

def get_all_images():
    return Image.query.all()


##########################RUN##############################################

    connect_to_db(app)
    db.create_all()
    print('Connected to db!')