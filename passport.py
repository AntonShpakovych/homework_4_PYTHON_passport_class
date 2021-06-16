from random import *
from datetime import *
from datetime import datetime


class Passport:

    """Passport info"""

    def __init__(self, name, surname, patronymic, gen: str, city, birth_date):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.gen = gen
        self.city = city
        self.birth_date = datetime.strptime(
            birth_date, '%d.%m.%Y').date().strftime("%d-%m-%Y")
        self.__number = randint(100000000, 999999999)
        self.create_date = datetime.today().strftime("%d-%m-%Y")

    def __str__(self):
        return f'Passport:{self.name} {self.surname}'

    def _show_info(self):
        print(f"Passport info:\n\
            \tName: {self.name}\n\
            \tSurname: {self.surname}\n\
            \tPatronymic: {self.patronymic}\n\
            \tGender: {self.gen.upper()}\n\
            \tCity: {self.city}\n\
            \tBirth date: {self.birth_date}\n\
            \tNumber: {self.__number}\n\
            \tDate: {self.create_date}")


class ForeignPassport(Passport):
    def __init__(self, name, surname, patronymic, gen: str, city, birth_date):
        super().__init__(name, surname, patronymic, gen, city, birth_date)

        self.__number = randint(100000000, 999999999)
        self.visa = []

    def new_visa(self, country, end):
        self.visa.append({country: datetime.strptime(
            end, '%d.%m.%Y').date().strftime("%d-%m-%Y")})

    def _show_info(self):
        print(f"Passport info:\n\
            \tName: {self.name}\n\
            \tSurname: {self.surname}\n\
            \tPatronymic: {self.patronymic}\n\
            \tGender: {self.gen.upper()}\n\
            \tCity: {self.city}\n\
            \tBirth date: {self.birth_date}\n\
            \tNumber: {self.__number}\n\
            \tDate: {self.create_date}")
        print('Visa info about all countries: ')
        for item in self.visa:
            print('\t', list(item.keys())[0], ':', list(item.values())[0])
        print('Available visa countries')
        for item in self.visa:
            if list(item.values())[0] > datetime.today().strftime("%d-%m-%Y"):
                print('\t',  f'{list(item.keys())[0]}',
                      ':', f'{ list(item.values())[0]}')


user_1 = Passport('Anton', 'Shpakovych', 'Vasylovich',
                  'm', 'Rivne', '30.01.2001')
print(user_1.__str__())
user_1._show_info()

user_2 = ForeignPassport('Anton', 'Shpakovych',
                         'Vasylovich', 'm', 'Rivne', '30.01.2001')
user_2.new_visa('Poland', '16.04.2021')
user_2.new_visa('USA', '16.03.2021')
user_2.new_visa('Ukraine', '16.02.2021')
user_2.new_visa('Russia', '16.09.2021')
user_2.new_visa('turk', '16.10.2021')
user_2._show_info()
