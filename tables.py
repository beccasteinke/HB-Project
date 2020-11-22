from flask_table import Table, Col

class Results(Table):
    id = Col('Id', show=False)
    bus_name = Col('Business')
    url = Col('Website')
    address = Col('Address')
    tel = Col('Phone')