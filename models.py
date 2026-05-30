
class Book: 
    def __init__(self, author, name, description):
        self.author = author
        self.name = name
        self.description = description
        
    def get_info(self):
        print(f'Автор книги: {self.author} | Название: {self.name}\nОписание: {self.description}')