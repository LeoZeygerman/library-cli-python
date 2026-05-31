from storage import load_data, save_data
from add_book import add_book
from find import find_book, find_author

while True:
    try:
        print('1.Добавить книгу')
        print('2.Найти книгу')
        print('3.Удалить книгу')
        print('4.Поиск книг автора')
        print('5.Выйти')
        choice = int(input('Ваш выбор: '))
        
        if choice == 1:
            add_book()
            
        if choice == 2:
            find_book()
            
        if choice == 4:
            find_author()
        
        if choice == 5:
            break
        
    except ValueError:
        print('Ошибка при вводе!')
    