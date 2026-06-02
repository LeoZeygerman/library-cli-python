from storage import save_data, load_data
from models import Book

def edit():
    data = load_data()
    name = input('Введите название книги, которую хотите редактировать: ')
    found = False
    for item in data:
        if item['name'] == name:
            found = True
            print('Что хотите редактировать? \n 1.Название \n 2.Автора \n 3.Описание \n 4.Вернуться')
            choice = int(input('Ваш выбор: '))
            
            if choice == 1:
                new_name = input('Введите новое название: ')
                item['name'] = new_name
                save_data(data)
                print('Название успешно изменено.')
                
            if choice == 2:
                new_author = input('Введите новое имя автора: ')
                item['author'] = new_author
                save_data(data)
                print('Имя автора успешно изменено.')
                
            if choice == 3:
                new_description = input('Введите новое описание книги: ')
                item['description'] = new_description
                save_data(data)
                print('Описание успешно изменено.')
                
            if choice == 4:
                return
            
    if not found:
        print('Книга не найдена.')
            
    