from collections import UserDict
from datetime import datetime


# Custom errors
class BirthdayError(Exception):
    pass


class PhoneError(Exception):
    pass


# Decorator
def error_keeper(function):
    def inner(*args):
        try:
            function(*args)
        except BirthdayError:
            print('That is incorrect birthday!')
        except PhoneError as pe:
            if pe.args:
                print(f'This phone number is too {pe.args[0]}!')
            else:
                print('That is incorrect phone number!')
        except ValueError:
            print('Something is wrong!\nGo to README.md to check the correctness\n')
        except AttributeError:
            print('Something is wrong!\nGo to README.md to check the correctness\n')
        except KeyError:
            print('Name is incorrect!\n')

    return inner


# Classes
class Field:
    def __init__(self, name=None, phone=None, email=None, birthday=None):
        if name:
            self.name = name
        if phone:
            self.__phone = None
            self.phone = phone
        if email:
            self.email = email
        if birthday:
            self.__birthday = None
            self.birthday = birthday


class Birthday(Field):
    @property
    def birthday(self):
        if self.__birthday:
            return self.__birthday

    
    @birthday.setter
    @error_keeper
    def birthday(self, birthday):
        try:
            self.__birthday = datetime.strptime(birthday, "%d %m %Y")
        except ValueError:
            self.__birthday = None
            raise BirthdayError
        except IndexError:
            self.__birthday = None
            raise BirthdayError


class Phone(Field):
    @property
    def phone(self):
        if self.__phone:
            return self.__phone

    @phone.setter
    @error_keeper
    def phone(self, phone):
        try:
            if int(phone.strip()) or (phone.startswith('+') and int(phone[1:])):
                self.__phone = phone
                if 10 > len(phone):
                    self.__phone = None
                    raise PhoneError('short')
                if 13 < len(phone):
                    self.__phone = None
                    raise PhoneError('long')
            else:
                self.__phone = None
        except ValueError:
            self.__phone = None
            raise PhoneError


class Email(Field):
    pass


class Name(Field):
    pass


class Record:
    def __init__(self, person_name, phone_num=None, email=None, birthday=None):
        self.name = person_name
        if phone_num:
            self.phones = []
            self.phones.append(phone_num)

        if email:
            self.emails = []
            self.emails.append(email)
        
        if birthday:
            self.birthday = birthday
    
    # Phone operations
    def add_phone(self, extra_phone, flag=True):
        try:
            try:
                self.phones.append(extra_phone)
                for x in self.phones:
                    x.phone
            except AttributeError:
                self.phones = []
                self.phones.append(extra_phone)

            if flag == True and extra_phone.phone != None:
                print(f'Phone number {extra_phone.phone} has been successfully added!\n')
        except AttributeError:
            pass

    def change_phone(self, some_phone, different_phone):
        try:
            flag = False
            if different_phone.phone != None:
                for ph in self.phones:
                    if ph.phone == some_phone.phone:
                        self.phones.append(different_phone)
                        self.phones.remove(ph)
                        print(f'Phone number {some_phone.phone} has been successfully changed to {different_phone.phone}\n')
                        flag = True
        except AttributeError:
            flag == False
        if flag == False:
            print(f'There is no such phone!')

    def delete_phone(self, some_phone):
        try:
            if some_phone.phone != None:
                flag = False
                for ph in self.phones:
                    if ph.phone == some_phone.phone:
                        self.phones.remove(ph)
                        flag = True
                        print(f'Phone number {some_phone.phone} has been successfully deleted\n')
        except AttributeError:
            flag = False
            
        if flag == False:
            print(f'There is no such phone as {some_phone.phone}\n')

    # Email operations
    def add_email(self, extra_email):
        try:
            self.emails.append(extra_email)
            for x in self.emails:
                x.email
        except AttributeError:
            self.emails = []
            self.emails.append(extra_email)

        print(f'Email {extra_email.email} has been successfully added!\n')

    def change_email(self, some_email, different_email):
        flag = False
        try:
            for em in self.emails:
                if em.email == some_email.email:
                    self.emails.remove(em)
                    self.emails.append(different_email)
                    print(f'Email {some_email.email} has been successfully changed to {different_email.email}\n')
                    flag = True
        except AttributeError:
            flag == False

        if flag == False:
                print(f'There is no such email as {some_email.email}\n')

    def delete_email(self, some_email):
        flag = False
        try:
            for em in self.emails:
                if em.email == some_email.email:
                    self.emails.remove(em)
                    flag = True
                    print(f'Email {some_email.email} has been successfully deleted\n')
        except AttributeError:
            flag == False

        if flag == False:
                print(f'There is no such email as {some_email.email}\n')

    # Birthday operations
    def days_to_birthday(self):
        self.birthday.birthday
        bd = datetime(year=datetime.now().year, month=self.birthday.birthday.month, day=self.birthday.birthday.day)
        delta = bd - datetime.now()
        if delta.days < 0:
            delta = datetime(year=datetime.now().year+1, month=self.birthday.birthday.month, day=self.birthday.birthday.day) - datetime.now()
        return delta.days+1
    
    def add_birthday(self, extra_birthday):
        self.birthday = extra_birthday
        print(f'Birthday {extra_birthday.birthday.date()} has been successfully added!\n')

    def change_birthday(self, some_bd, different_bd):
        flag = False
        try:
            if self.birthday.birthday == some_bd.birthday:
                self.birthday = different_bd
                print(f'Birthday {some_bd.birthday.date()} has been successfully changed to {different_bd.birthday.date()}\n')
                flag = True
        except AttributeError:
            flag == False

        if flag == False:
                print(f'There is no such birthday as {some_bd.birthday.date()}\n')
    
    def delete_birthday(self, some_bd):
        flag = False
        try:
            if self.birthday.birthday == some_bd.birthday:
                self.birthday = None
                flag = True
                print(f'Birthday {some_bd.birthday.date()} has been successfully deleted\n')
        except AttributeError:
            flag == False
        
        if flag == False:
                print(f'There is no such birthday as {some_bd.birthday.date()}\n')

    def __str__(self):
        result = f'\nName: {self.name.name}\n'
        try:
            p = list(x.phone for x in self.phones if x.phone != None)
            if len(p) > 0:
                result += f'Phones: {p}\n'
        except AttributeError:
            pass

        try:
            e = list(x.email for x in self.emails)
            if len(e) > 0:
                result += f'Emails: {e}\n'
        except AttributeError:
            pass

        try:
            result += f'Birthday: {self.birthday.birthday.date()}'
            result += f'\nDays to next birthday: {str(ab[self.name.name].days_to_birthday())}\n'
        except AttributeError:
            pass

        return result


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.name] = record
        print(f'One contact ({record.name.name}) has been successfully added!\n')

    def delete_record(self, name_to_delete):
        for username in self.data.keys():
            if username == name_to_delete:
                del self.data[username]
                print(f'Contact ({username}) has been deleted successfully!\n')
                return None
            
        print(f'There is no such contact as {name_to_delete}\n')
        
    current_index = 0

    def __next__(self):
        records = self.data
        if self.current_index < len(records):
            self.current_index += 1
            result = list(enumerate(self))
            return self.data[result[self.current_index-1][1]]
        print('Here is the end of your address book!\n')
        self.current_index = 0
        raise StopIteration

    def __str__(self):
        result = ''
        for rec in self.data.values():
            result += str(rec)
        return result
    
ab = AddressBook()

# Iterator
class ABIterator:
    def __iter__(self):
        return ab

abi = ABIterator()