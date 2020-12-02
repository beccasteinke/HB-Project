from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:////fake_data'
db = SQLAlchemy()


class User(db.Model):
    """Instantiate a user"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)
    tel = db.Column(db.String, unique=True)

    def __repr__(self):
        return f'<User user_id={self.user_id}, name={self.fname} {self.lname}, email={self.email}>'

class Business(db.Model):
    """Instantiate a business"""

    __tablename__ = 'businesses'

    bus_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    bus_name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True)
    address = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True, nullable=False)
    bus_passwrd = db.Column(db.String, nullable=False)
    tel = db.Column(db.String, unique=True)
    description = db.Column(db.Text)
    image = db.Column(db.String)
    service_id = db.Column(db.Integer, db.ForeignKey('services.service_id'))

    users = db.relationship("User", secondary="users_buss", backref="businesses")
 
    service = db.relationship('Service', backref='businesses')
    event = db.relationship('Event', backref='businesses')

    def __repr__(self):
        return f'<Business bus_id={self.bus_id}, bus_name={self.bus_name}>'

class Service(db.Model):
    """A service a business provides"""

    __tablename__ = 'services'

    service_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name_serv = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)


    def __repr__(self):
        return f'Service service_id={self.service_id}, name={self.name_serv}>'

class Event(db.Model):
    """An event"""
# TODO: import datetime, research datetime

    __tablename__ = 'events'

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name_evt = db.Column(db.String, nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String)
    service_id = db.Column(db.Integer, db.ForeignKey('services.service_id'))
    bus_id = db.Column(db.Integer, db.ForeignKey('businesses.bus_id'))

    service = db.relationship('Service', backref='events') # can call service.events
    business = db.relationship('Business', backref='events') # can call business.events

    def __repr__(self):
        return f'<Event event_id={self.event_id}, event name={self.name_evt}, bus_id={self.business}>'

class UserBus(db.Model):
    """Connecting Users with businessess they favorite"""

    __tablename__ = 'users_buss'

    user_bus_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    bus_id = db.Column(db.Integer, db.ForeignKey('businesses.bus_id'), nullable=False)

    user = db.relationship('User', backref='users_buss')
    business = db.relationship('Business', backref='users_buss')

    def __repr__(self):
        return f'<business={self.business}>'

# class BusServ(db.Model):
#     """Connecting businesses with types of services they offer"""

#     __tablename__ = 'business_services'

#     bus_serv_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     bus_id = db.Column(db.Integer, db.ForeignKey('businesses.bus_id'))
#     service_id = db.Column(db.Integer, db.ForeignKey('services.service_id'))

#     service = db.relationship('Service', backref='business_services')
#     business = db.relationship('Business', backref='business_services')

#     def __repr__(self):
#         return f'<BusServ bus_serv_id={self.bus_serv_id}>'

# class BusEvt(db.Model):
#     """Connecting businesses with the events they are offering"""

#     __tablename__ = 'business_events'

#     bus_evt_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     bus_id = db.Column(db.Integer, db.ForeignKey('businesses.bus_id'))
#     event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))

#     business = db.relationship('Business')#, backref='business_events')
#     event = db.relationship('Event')#, backref='business_events')

#     def __repr__(self):
#         return f'<BusEvt bus_evt_id={self.bus_evt_id}>'

def connect_to_db(flask_app, db_uri='postgresql:///fake_data', echo=True):
#  TODO: db_uri???? also not sure how exactly this function works
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db')

if __name__ == '__main__':
    from server import app

    connect_to_db(app)