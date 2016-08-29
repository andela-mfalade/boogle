import shelve
from random import choice

all_books = shelve.open('all_books')

names = [
    'Do Androids Dream of Electric Sheep?',
    'Something Wicked This Way Comes (Green Town, #2)',
    'The Hitchhikers Guide to the Galaxy',
    'Pride and Prejudice and Zombies',
    'I Was Told There would Be Cake',
    'The Curious Incident of the Dog in the Night-Time',
    'The Hollow Chocolate Bunnies of the Apocalypse',
    'To Kill a Mockingbird',
    'The Unbearable Lightness of Being',
    'Are You There, Vodka? Its Me, Chelsea',
    'The Man Without Qualities'
]

categories = [
    'fiction',
    'suspence',
    'action',
    'drama',
    'prose'
]

book_list = []
for idx in range(len(names)):
    book_list.append({
        'name': names[idx],
        'category': choice(categories)
    })
all_books['books'] = book_list
print all_books, 'result'



all_books.close()
