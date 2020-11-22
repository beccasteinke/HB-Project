from flask_table import Table, Col

class BusResults(Table):
    id = Col('Id', show=False)
    bus_name = Col('Business')
    url = Col('Website')
    address = Col('Address')
    tel = Col('Phone')

class EvtResults(Table):
    id = Col('Id', show=False)
    name_evt = Col('Event')
    start = Col('Start Time')
    end = Col('End Time')
    business = Col('Business')