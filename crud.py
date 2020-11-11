"""CRUD operations"""

from model import db, User, Business, Service, Event, BusServ, BusEvt, connect_to_db

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

    return User.query.filter(User.email == email).all()

def create_business(bus_name, url, address, email, tel, description, image):
    """Create and return a new business"""

    business = Business(bus_name=bus_name, 
                        url=url, 
                        address=address, 
                        email=email, 
                        tel=tel, 
                        description=description,
                        image=image)
    
    db.session.add(business)
    db.session.commit()

    return business

def get_businesses():
    """Return all businesses"""

    return Business.query.all()

def create_service(name_serv, description):
    """Create and return a service category"""

    service = Service(name_serv=name_serv, 
                    description=description)

    db.session.add(service)
    db.session.commit()

    return service

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

# def create_user_bus(user, business):
    # userbus = UserBus(user=user, business=business)

# def create_event_service(service, event):
    # evtservice = EventService(service=service, event=event)

def create_bus_serv(service, business):
    busserv = BusServ(service=service, business=business)

    db.session.add(busserv)
    db.session.commit()

def create_bus_evt(business, event):
    busevt = BusEvt(business=business, event=event)

    db.session.add(busevt)
    db.session.commit()

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