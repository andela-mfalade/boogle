import os
import shelve


class Books(object):
    """Book Class to mock DB.

    The current implementation uses the Python shelve module.
    This can be switched to either SQLite, POSTGRES, or MySql db.
    """

    ALL_BOOKS = shelve.open('all_books')

    @classmethod
    def search_by(cls, search_term, filters='keyword'):
        if filters in ('name', 'category'):
            return cls.search_by_filters(search_term, filters)
        else:
            return cls.search_all_fields(search_term)

    @classmethod
    def search_by_filters(cls, search_term, keyword):
        result = []
        for book in cls.ALL_BOOKS['books']:
            if search_term in book.get(keyword):
                result.append(book)
        return result

    @classmethod
    def search_all_fields(cls, search_term):
        result = []

        for book in cls.ALL_BOOKS['books']:
            if search_term in book['category'] or search_term in book['name']:
                result.append(book)
        return result
