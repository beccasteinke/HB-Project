from faker import Faker
import json             # to create a json file
import numpy as np
from random import randint
import pandas as pd
from pprint import pprint

fake = Faker()

def create_data(x):

    # create a dictionary

    business_data = {}

    for i in range(0, x):
        business_data[i] = {}
        business_data[i]['business_name'] = fake.company()
        business_data[i]['URL'] = fake.url()
        business_data[i]['address'] = fake.address()
        business_data[i]['email'] = fake.email()
        business_data[i]['tel'] = fake.pyint(1000000000, 9999999999)
        business_data[i]['description'] = fake.text()

    return business_data

businesses = create_data(10)
pd.DataFrame.from_dict(businesses)

with open('fake_data.json', 'wt') as out:
    pprint(businesses, stream=out)




