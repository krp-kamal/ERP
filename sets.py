'''
Author: Ms Rya
Version: 3.10
'''
def manage_Books():
    book_collection = set()
    
    book_collection.add('Initialize an empty set for books')
    book_collection.add('1984')
    book_collection.add('Add individual books to the collection')
    print("Book collection after adding books:", book_collection)

    book_collection.update({'The Great Gatsby', 'Moby Dick', 'War and Peace'})
    print("Book collection after updating with more books:", book_collection)

    book_collection.remove('1984')
    print("Book collection after removing a book:", book_collection)

manage_Books()
