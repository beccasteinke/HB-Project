from wtforms import Form, StringField, SelectField

class SearchForm(Form):
    choices = [('Business', 'Business'),
                ('Event', 'Event')]
    select = SelectField('Search:', choices=choices)
    search = StringField('')
