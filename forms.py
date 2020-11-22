from wtforms import Form, StringField, SelectField

class SearchForm(Form):
    choices = [('Business', 'Business'),
                ('Event', 'Event')]
    select = SelectField('Search for a business:', choices=choices)
    search = StringField('')
