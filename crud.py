"""CRUD operations"""

from model import db, User, Business, Service, Event, connect_to_db

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

def create_business(bus_name, url, address, email, tel, description, service_id):
    """Create and return a new business"""

    business = Business(bus_name=bus_name, 
                        url=url, 
                        address=address, 
                        email=email, 
                        tel=tel, 
                        description=description,
                        service=service)
    
    db.session.add(business)
    db.session.commit()

    return business

def create_service(name_serv, description, event_id):
    """Create and return a service category"""

    service = Service(name_serv=name_serv, 
                    description=description, 
                    event=event)

    db.session.add(service)
    db.session.commit()

    return service

def create_event(name_evt, start, end, description, service_id):
    """Create and return an event"""

    event = Event(name_evt=name_evt, 
                start=start, 
                end=end, 
                description=description, 
                service=service)
    
    db.session.add(event)
    db.session.commit()

    return event

def create_user_bus(user, business):
    userbus = (user=user, business=business)

if __name__ == '__main__':
    from server import app
    connect_to_db(app)