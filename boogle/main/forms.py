from wtforms import Form
from wtforms import StringField
from wtforms import SelectField
from wtforms import validators


class SearchForm(Form):
    CHOICES = [
        ('keyword', 'Search By Keyword'),
        ('food_name', 'Search By Food Name'),
        ('category_name', 'Search By Category')
    ]
    search_term = StringField('search_term')
    filters = SelectField(
        'filters',
        choices=CHOICES,
        validators=[validators.optional()]
    )
