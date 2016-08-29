from flask import render_template
from flask import request

from . import books
from .models import Books


@books.route('/search', methods=['POST'])
def search():
    search_term = request.form.get('search_term')
    filters = request.form.get('filters')
    results = Books.search_by(search_term.lower(), filters=filters)
    context = {
        'search_term': search_term,
        'filter': filters,
        'results': results
    }
    return render_template('search-results.html', context=context)
