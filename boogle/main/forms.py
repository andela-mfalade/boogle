from wtforms import Form
from wtforms import StringField
from wtforms import SelectField
from wtforms import validators


class SearchForm(Form):
    CHOICES = [
        ('keyword', 'Search By Keyword'),
        ('name', 'Search By Book Name'),
        ('category', 'Search By Category')
    ]
    search_term = StringField('search_term')
    filters = SelectField(
        'filters',
        choices=CHOICES,
        validators=[validators.optional()]
    )
