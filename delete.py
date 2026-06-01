from storage import load_data, save_data
from models import Book

def delete_book():
    data = load_data()
    book = input('Введите название книги, которую хотите удалить: ')
    for item in data:
        if item['name'] == book:
            data.remove(item)
            save_data(data)
            print('Книга удалена!')
            return
        else:
            print('Книга не найдена.')