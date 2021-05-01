from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

###########################USER#############################################

class User(db.Model):
    """Data model for a user"""
    # TODO: remove nullables below for testing

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        """Display info about user"""

        return f'<User user_id={self.user_id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}, password={self.password}>'

############################IMAGE############################################

class Image(db.Model):
    """Data model for images"""

    __tablename__ = 'image'

    image_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    image_title = db.Column(db.String)
    artist = db.Column(db.String)
    location = db.Column(db.String)
    image_url = db.Column(db.String)
    

    user = db.relationship('User')

    def __repr__(self):
        """Display info about image"""

        return f'<Image image_id={self.image_id}, image_title={self.image_title}, artist={self.artist}, location={self.location}, image_url={self.image_url}>'

########################################################################

def connect_to_db(flask_app, db_uri='postgresql:///pow', echo=False):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all()
    print('Connected to db!')
