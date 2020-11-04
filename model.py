from flask_sqlalchemy import flask_SQLAlchemy

db = SQLAlchemy()

class User(db.model):
    """Instantiate a user"""

    __tablename__ = 'users'

    user_id
    fname
    lname
    email
    password
    tel

    def __repr__(self):
        return f'<User user_id={self.user_id}, name={self.fname} {self.lname}, email={self.email}'