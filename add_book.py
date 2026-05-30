from storage import save_data, load_data
from models import Book

def add_book():
    data = load_data()
    print('Добавление книги.')
    author = input('Напишите автора книги: ')
    name = input('Введите название книги: ')
    description = input('Опишите книгу: ')
    book = {
        'author': author,
        'name': name,
        'description': description
    }
    data.append(book)
    save_data(data)
    book_object = Book(author, name, description)
    book_object.get_info()