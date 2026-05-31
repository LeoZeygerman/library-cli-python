from storage import save_data, load_data
from models import Book

def find_book():
    find = input('Введите название книги: ')
    data = load_data()
    found = False
    for item in data:
        if item['name'] == find:
            found = True
            book_item = Book(item['author'], item['name'], item['description'])
            book_item.get_info()
    if not found:
        print('Книги нет.')
        

def find_author():
    find = input('Введите автора: ')
    data = load_data()
    found = False
    for item in data:
        if item['author'] == find:
            found = True
            book_item = Book(item['author'], item['name'], item['description'])
            book_item.get_info()
    if not found:
        print('Книг данного автора нет.')