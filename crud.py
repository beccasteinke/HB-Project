"""CRUD operations"""

from model import db, User, Business, Service, Event, UserBus, connect_to_db

def create_user(fname, lname, email, password, tel):
    """Create and return a new user"""

    user = User(fname=fname, 
                lname=lname, 
                email=email, 
                password=password, 
                tel=tel)

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    """Return a user by email"""

    return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    """Return a user by user_id"""

    return User.query.filter(User.user_id == user_id).first()

def check_user_login_info(email, password):
    """check if the users email and password match in the database"""

    return User.query.filter((User.email == email) & (User.password == password)).first()

def create_business(bus_name, url, address, email, tel, description, image, service, bus_passwrd):
    """Create and return a new business"""

    business = Business(bus_name=bus_name, 
                        url=url, 
                        address=address, 
                        email=email, 
                        tel=tel, 
                        description=description,
                        image=image,
                        service=service,
                        bus_passwrd=bus_passwrd)
    
    db.session.add(business)
    db.session.commit()

    return business

# TODO: this is redundant
def add_new_business(bus_name, url, address, email, tel, description, image, service_id, bus_passwrd):

    new_bus = Business(bus_name=bus_name,
                        url=url,
                        address=address,
                        email=email, 
                        tel=tel, 
                        description=description,
                        image=image,
                        service_id=service_id,
                        bus_passwrd=bus_passwrd)

    db.session.add(new_bus)
    db.session.commit()

def check_bus_login_info(email, bus_passwrd):
    """check if the business email and password match in the database"""

    return Business.query.filter((Business.email == email) & (Business.bus_passwrd == bus_passwrd)).first()

def get_businesses():
    """Return all businesses"""

    return Business.query.all()

def get_bus_by_email(email):
    """Return a business by email"""

    return Business.query.filter(Business.email == email).first()

def get_bus_by_id(bus_id):
    """Return a business by primary key"""

    return Business.query.get(bus_id)

def get_bus_evts(bus_id):
    """Return a list of events by business id"""

    return Event.query.filter_by(bus_id=bus_id).all()

def create_service(name_serv, description):
    """Create and return a service category"""

    service = Service(name_serv=name_serv, 
                    description=description)

    db.session.add(service)
    db.session.commit()

    return service

def get_servs():
    """Return all services"""

    return Service.query.all()

def serv_by_name(name_serv):
    """Return service by name_serv"""

# Service.query.distinct(Service.name_serv).all()

    return Service.query.filter(Service.name_serv == name_serv).all()


def create_event(name_evt, start, end, description, service, business):
    """Create and return an event"""

    event = Event(name_evt=name_evt, 
                start=start,
                end=end,
                description=description,
                service=service,
                business=business)
    
    db.session.add(event)
    db.session.commit()

    return event

def get_events():
    """Return all events"""

    return Event.query.all()

def get_evt_by_bus(bus_id):
    """Return all events matching a bus_id"""

    return Event.query.filter_by(bus_id=bus_id).all()

def create_userbus(user, business):
    """add a user's favorite business to their profile"""

    userbus = UserBus(user=user, business=business)

    db.session.add(userbus)
    db.session.commit()

    return userbus

def add_new_userbus(user, business):
    """allow user to add new userbus to db"""

    userbus = UserBus(user=user, business=business)

    db.session.add(userbus)
    db.session.commit()

    return userbus

def check_userbus_info(user_id, business_id):
    """check if the user and business exist in the database"""

    return UserBus.query.filter((UserBus.user_id == user_id) & (UserBus.bus_id == bus_id)).first()

# def add_fav_bus(user_id, bus_id):

    # in server user_id = session.get("user_id")
    # bus_id linked to bus page?
    # fave_bus = UserBus()

def get_bus_by_user_id(user_id):
    """find bus_name from bus_id's connected to user accounts"""

    bus_ids = db.session.query(UserBus.bus_id).filter_by(user_id=user_id)

    faves_list = []
    for bus in bus_ids:
        faves_list.append(db.session.query(Business.bus_name).filter_by(bus_id=bus.bus_id).all())
 
    remove_content = ["[", "(", "]", ")", "',", "'"]
    faves_str = repr(faves_list)

    for content in remove_content:
        faves_str = faves_str.replace(content, '')
    joined_faves = faves_str.split(",")

    return joined_faves
















# def create_event_service(service, event):
    # evtservice = EventService(service=service, event=event)

# def create_bus_serv(service, business):
#     busserv = BusServ(service=service, business=business)

#     db.session.add(busserv)
#     db.session.commit()

# def create_bus_evt(business, event):
#     busevt = BusEvt(business=business, event=event)

#     db.session.add(busevt)
#     db.session.commit()

# search service category - get list of businesses
# get businesses by service

# search business - get list of events and service category
# get events by business
# get service category by business

# search event - get business and service
# get business by event
# get service by event


if __name__ == '__main__':
    from server import app
    connect_to_db(app)