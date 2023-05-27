from AddressBook import *
from abc import ABC, abstractmethod

class ContactAssistant(ABC):
    @abstractmethod
    def handle(self, action):
        pass


class Bot(ContactAssistant):
    def __init__(self):
        self.book = AddressBook()

    def handle(self, action):
        if action == 'add':
            name = Name(input("Name: ")).value.strip()
            phones = Phone().value
            birth = Birthday().value
            email = Email().value.strip()
            status = Status().value.strip()
            note = Note(input("Note: ")).value
            record = Record(name, phones, birth, email, status, note)
            return self.book.add(record)
        elif action == 'search':
            print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
            category = input('Search category: ')
            pattern = input('Search pattern: ')
            result = (self.book.search(pattern, category))
            for account in result:
                if account['birthday']:
                    birth = account['birthday'].strftime("%d/%m/%Y")
                    result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                    print(result)
        elif action == 'edit':
            contact_name = input('Contact name: ')
            parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
            new_value = input("New Value: ")
            return self.book.edit(contact_name, parameter, new_value)
        elif action == 'remove':
            pattern = input("Remove (contact name or phone): ")
            return self.book.remove(pattern)
        elif action == 'save':
            file_name = input("File name: ")
            return self.book.save(file_name)
        elif action == 'load':
            file_name = input("File name: ")
            return self.book.load(file_name)
        elif action == 'congratulate':
            print(self.book.congratulate())
        elif action == 'view':
            print(self.book)
        elif action == 'exit':
            pass
        else:
            print("There is no such command!")

    def run(self):
        print('Привет. Я ваш помощник по контактам. Что мне сделать с вашими контактами?')
        self.book.load("auto_save")
        commands = ['Добавить', 'Поиск', 'Редактировать', 'Загрузить', 'Удалить', 'Сохранить', 'Поздравить',
                    'Просмотреть', 'Выход']
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
                self.book.save("auto_save")
            if action == 'exit':
                break