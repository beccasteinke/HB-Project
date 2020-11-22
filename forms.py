from wtforms import Form, StringField, SelectField

class BusSearchForm(Form):
    choices = [('Business', 'Business'),
                ('Event', 'Event')]
    select = SelectField('Search for a business:', choices=choices)
    search = StringField('')