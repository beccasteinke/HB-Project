import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb fake_data')
os.system('createdb fake_data')

model.connect_to_db(server.app)
model.db.create_all()

# Load business data from JSON file
with open('data/fake_data.json') as b:
    business_data = json.loads(b.read())

# Create businessess, store them in a list

buss_in_db = []
for business in business_data:
    bus_name, url, address, email, tel, description = (
        business['bus_name'], business['URL'], business['address'],
        business['email'], business['tel'], business['description'])

    db_business = crud.create_business(bus_name, url,
                                        address, email,
                                        tel, description)#, service)
    buss_in_db.append(db_business)

# b.close()

# Create 10 fake users;
for n in range(10):
    fname = f'first name{n}'
    lname = f'last name{n}'
    email = f'user{n}@test.com'
    password = f'test{n}'
    tel = f'{n}{n}{n}-{n}{n}{n}{n}'

    user = crud.create_user(fname, lname, email, password, tel)


# Create service categories with fake data
with open('data/fake_services.json') as f:
    service_data = json.loads(f.read())

servs_in_db = []
for service in service_data:
    name_serv, description = (service['name_serv'], service['description'])

    db_service = crud.create_service(name_serv, description)

    servs_in_db.append(db_service)

# f.close()

# Create 2 fake events for each business
with open('data/fake_events.json') as e:
    event_data = json.loads(e.read())

evts_in_db = []
for event in event_data:
    name_evt, description = (event['name_evt'], 
    event['description'])
    
    start = datetime.strptime(event['start'], '%Y-%m-%d-%H')
    end = datetime.strptime(event['end'], '%Y-%m-%d-%H')

    print(business)
    print(service)

    db_event = crud.create_event(name_evt, start, end, description)

    evts_in_db.append(db_event)

# e.close()


