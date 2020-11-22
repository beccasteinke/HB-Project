from wtforms import Form, StringField, SelectField

class BusSearchForm(Form):
    choices = [('Business', 'Business'),
                ('Service', 'Service')
                ('Address', 'Address')]
    select = SelectField('Search for a business:', choices-choices)
    search = StringField('')