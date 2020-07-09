import Advanced.ADVHW_4_Decorators.ADVHW_4_Decorators as decor


class Contact:
    '''
    :args - дополнительные телефоны
    :kwargs
        Email =
        Social_media =
    '''

    def __init__(self, name, surname, phone, *args, favourite = False, **kwargs):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.favourite = favourite
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Телефон: {self.phone}\n' \
               f'{"В избранном: да" if self.favourite == True else "В избранном: нет"}\n' \
               f'Дополнительная информация: \n' \
               f'\t Email: {self.kwargs["email"]} \n' \
               f'\t Social media: {self.kwargs["social"]}' \


class PhoneBook:
    phonebook = []

    def __init__(self, name):
        self.name = name
        self.phonebook = []
        print(f'Создана телефонная книга "{self.name}"')

    def add_contact(self, contact):
        self.phonebook.append(contact)
        print('Контакт добавлен')
    @decor.function_logger_current_folder
    def print_contacts(self):
        for i in self.phonebook:
            print(i)

    def delete_phone(self, to_delete):
        for contact in self.phonebook:
            if contact.phone == to_delete:
                self.phonebook.remove(contact)
                print('Контакт удален')

    def find_favourites(self):
        favourites = []
        for contact in self.phonebook:
            if contact.favourite == True:
                favourites.append(contact)
        return favourites

    def find_by_name(self, name, surname):
        for contact in self.phonebook:
            if contact.name == name and contact.surname == surname:
                return contact
            else:
                return 'Контакт не найден'

def test():
    john = Contact('John', 'Smith', 1111111111, 78888888888, 654654654654, favourite=True, email='1@email.ru',
                   social='@JohnSmith')
    book = PhoneBook('111')
    book.add_contact(john)
    book.print_contacts()

if __name__ == '__main__':
    test()