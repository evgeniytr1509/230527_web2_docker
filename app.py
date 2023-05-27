from abc import ABC, abstractmethod
from Bot import Bot


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactAssistant(ABC):
    @abstractmethod
    def handle(self, action):
        pass


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    # Остальные методы класса AddressBook


class MyContactAssistant(ContactAssistant):
    def __init__(self):
        self.bot = Bot()

    def handle(self, action):
        if action == 'add':
            # Обработка логики добавления контакта
            name = input("Введите имя контакта: ")
            phone = input("Введите номер телефона контакта: ")
            email = input("Введите email контакта: ")
            contact = Contact(name, phone, email)  # Создание экземпляра класса Contact
            self.bot.book.add_contact(contact)
            print("Контакт успешно добавлен.")
            self.bot.book.save("auto_save")  # Сохранение изменений в файл
        elif action == 'search':
            # Обработка логики поиска контакта
            pass
        elif action == 'edit':
            # Обработка логики редактирования контакта
            self.bot.book.save("auto_save")
        elif action == 'load':
            # Обработка логики загрузки контактов
            pass
        elif action == 'remove':
            # Обработка логики удаления контакта
            self.bot.book.save("auto_save")
        elif action == 'save':
            # Обработка логики сохранения контактов
            pass
        elif action == 'congratulate':
            # Обработка логики поздравления
            pass
        elif action == 'view':
            # Обработка логики просмотра контактов
            pass
        elif action == 'exit':
            # Обработка логики выхода из программы
            pass
        else:
            print('Неверная команда')

    def run(self):
        print('Привет. Я ваш помощник по контактам. Что мне сделать с вашими контактами?')
        self.bot.book.load("auto_save")
        commands = ['Добавить', 'Поиск', 'Редактировать', 'Загрузить', 'Удалить', 'Сохранить', 'Поздравить', 'Просмотреть', 'Выход']
        while True:
            action = input('Введите "help" для списка команд или введите команду: ').strip().lower()
            if action == 'help':
                format_str = str('{:%s%d}' % ('^', 20))
                for command in commands:
                    print(format_str.format(command))
                action = input().strip().lower()
                self.handle(action)
            else:
                self.handle(action)
            if action in ['add', 'remove', 'edit']:
                self.bot.book.save("auto_save")
            if action == 'exit':
                break


if __name__ == "__main__":
    assistant = Bot()
    assistant.run()