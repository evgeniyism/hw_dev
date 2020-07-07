import self as self


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
    ivan = Contact('Ivan', 'Ivanov', 2222222222, favourite=False, email='2@email.ru', social='@IvanIvanov')
    petr = Contact('Petr', 'Petrov', 3333333333, 78888888888, favourite=False, email='3@email2.ru',
                   social='@PetrPetrov')

    book = PhoneBook('111')
    print('_____________')
    book.add_contact(john)
    book.add_contact(ivan)
    book.add_contact(petr)
    book.print_contacts()
    book.delete_phone(3333333333)
    print('_____________')
    book.print_contacts()
    print('_____________')
    fav = book.find_favourites()
    for i in fav:
        print(i)
    print('_____________')
    print(book.find_by_name('John', 'Smith'))
    print(book.find_by_name('Petr', 'Petrov'))



test()