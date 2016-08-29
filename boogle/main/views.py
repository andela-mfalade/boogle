from flask import render_template

from . import main
from .forms import SearchForm


@main.route('/')
def home():
    form = SearchForm()
    return render_template('home.html', form=form)
