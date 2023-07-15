from collections import UserDict
from datetime import datetime


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
    def birthday(self, birthday):
        try:
            date_splt_lst = birthday.split()
            self.__birthday = datetime(day=int(date_splt_lst[0]), month=int(date_splt_lst[1]), year=int(date_splt_lst[2]))
        except ValueError:
            self.__birthday = None
            print("That is incorrect birthday!")
        except IndexError:
            self.__birthday = None
            print("That is incorrect birthday!")


class Phone(Field):
    @property
    def phone(self):
        if self.__phone:
            return self.__phone

    @phone.setter
    def phone(self, phone):
        try:
            if int(phone.strip()) or (phone.startswith('+') and int(phone[1:])):
                self.__phone = phone
                if 10 > len(phone):
                    print('Phone number is too short\n')
                    self.__phone = None
                if 13 < len(phone):
                    print('Phone number is too long\n')
                    self.__phone = None
            else:
                self.__phone = None
        except ValueError:
            self.__phone = None
            print('Incorrect phone!')


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
                    print(x.phone)
            except AttributeError:
                self.phones = []
                self.phones.append(extra_phone)

            if flag == True and extra_phone.phone != None:
                print(f'Phone number {extra_phone.phone} has been successfully added!\n')
        except AttributeError:
            pass

    def change_phone(self, some_phone, different_phone):
        try:
            if different_phone.phone != None:
                flag = False
                for ph in self.phones:
                    if ph.phone == some_phone.phone:
                        self.phones.append(different_phone)
                        self.phones.remove(ph)
                        print(f'Phone number {some_phone.phone} has been successfully changed to {different_phone.phone}\n')
                        flag = True
        except AttributeError:
            flag == False
        if flag == False:
                    print(f'There is no such phone as {some_phone.phone}\n')

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
                    print(x.email)
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
            p = list(x.phone for x in self.phones)
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

def iter():
    ab.current_index = 0
    counter = ab.current_index
    for rec in abi:
        counter += 1
        print(rec)

        if (counter % 2) == 0:
            inp = str(input("type 'next' to see the next page or type enything else to stop\n>>> "))
            if inp == 'next':
                continue
            else:
                print('\n')
                break

# Adding contact function
def add_contact(inp_split_lst):
    if 'phone' not in inp_split_lst:
        input_phone = None
    else:
        input_phone = True
    if 'email' not in inp_split_lst:
        input_email = None
    else:
        input_email = True
    if 'birthday' not in inp_split_lst:
        input_birthday = None
    else:
        input_birthday= True

    input_name = ' '.join(inp_split_lst[1:])
    if input_birthday:
        input_name = ' '.join(inp_split_lst[1:inp_split_lst.index('birthday')])
        try:
            input_phone = ' '.join(inp_split_lst[inp_split_lst.index('phone')+1:inp_split_lst.index('birthday')])
        except ValueError:
            pass
        try:
            input_email = ' '.join(inp_split_lst[inp_split_lst.index('email')+1:inp_split_lst.index('birthday')])
        except ValueError:
            pass
        input_birthday = ' '.join(inp_split_lst[inp_split_lst.index('birthday')+1:])

    if input_email:
        input_name = ' '.join(inp_split_lst[1:inp_split_lst.index('email')])
        input_email = ' '.join(inp_split_lst[inp_split_lst.index('email')+1:])
        try:
            input_email = ' '.join(inp_split_lst[inp_split_lst.index('email')+1:inp_split_lst.index('birthday')])
        except ValueError:
            pass

    if input_phone:
        input_name = ' '.join(inp_split_lst[1:inp_split_lst.index('phone')])
        input_phone = ' '.join(inp_split_lst[inp_split_lst.index('phone')+1:])
        try:
            input_phone = ' '.join(inp_split_lst[inp_split_lst.index('phone')+1:inp_split_lst.index('birthday')])
        except ValueError:
            pass
        try:
            input_phone = ' '.join(inp_split_lst[inp_split_lst.index('phone')+1:inp_split_lst.index('email')])
        except ValueError:
            pass

    ab.add_record(Record(Name(name=input_name), Phone(phone=input_phone), Email(email=input_email), Birthday(birthday=input_birthday)))

# Decorator
def input_error(function):
    def inner(*args):
        try:
            function(*args)
        except ValueError as ve:
            print('Something is wrong!\nGo to README.md to check the correctness\n')
            print(ve)
        except AttributeError as ae:
            print('Something is wrong!\nGo to README.md to check the correctness\n')
            print(ae)
        except KeyError:
            print('Name is incorrect!\n')
    return inner

# Field operations
@input_error
def add_field(inp_split_lst, type):
    if type == 'number':
        name = ' '.join(inp_split_lst[1:inp_split_lst.index('phone')])
        add_ph = ' '.join(inp_split_lst[inp_split_lst.index('phone')+1:])
        ab[name].add_phone(Phone(phone=add_ph))

    elif type == 'email':
        name = ' '.join(inp_split_lst[1:inp_split_lst.index('email')])
        add_em = ' '.join(inp_split_lst[inp_split_lst.index('email')+1:])
        ab[name].add_email(Email(email=add_em))

    elif type == 'birthday':
        name = ' '.join(inp_split_lst[1:inp_split_lst.index('birthday')])
        add_bd = ' '.join(inp_split_lst[inp_split_lst.index('birthday')+1:])
        ab[name].add_birthday(Birthday(birthday=add_bd))

@input_error
def change_field(inp_split_lst, type):
    if type == 'number':
        name = ' '.join(inp_split_lst[1:inp_split_lst.index('phone')])
        change_ph_from = ' '.join(inp_split_lst[inp_split_lst.index('phone')+1:inp_split_lst.index('to')])
        change_ph_to = ' '.join(inp_split_lst[inp_split_lst.index('to')+1:])
        ab[name].change_phone(Phone(phone=change_ph_from), Phone(phone=change_ph_to))

    elif type == 'email':
        name = ' '.join(inp_split_lst[1:inp_split_lst.index('email')])
        change_em_from = ' '.join(inp_split_lst[inp_split_lst.index('email')+1:inp_split_lst.index('to')])
        change_em_to = ' '.join(inp_split_lst[inp_split_lst.index('to')+1:])
        ab[name].change_email(Email(email=change_em_from), Email(email=change_em_to))

    elif type == 'birthday':
        name = ' '.join(inp_split_lst[1:inp_split_lst.index('birthday')])
        change_bd_from = ' '.join(inp_split_lst[inp_split_lst.index('birthday')+1:inp_split_lst.index('to')])
        change_bd_to = ' '.join(inp_split_lst[inp_split_lst.index('to')+1:])
        ab[name].change_birthday(Birthday(birthday=change_bd_from), Birthday(birthday=change_bd_to))

@input_error
def delete_field(inp_split_lst, type):
    if type == 'number':
        name = ' '.join(inp_split_lst[1:inp_split_lst.index('phone')])
        del_ph = ' '.join(inp_split_lst[inp_split_lst.index('phone')+1:])
        ab[name].delete_phone(Phone(phone=del_ph))

    elif type == 'email':
        name = ' '.join(inp_split_lst[1:inp_split_lst.index('email')])
        del_em = ' '.join(inp_split_lst[inp_split_lst.index('email')+1:])
        ab[name].delete_email(Email(email=del_em))

    elif type == 'birthday':
        name = ' '.join(inp_split_lst[1:inp_split_lst.index('birthday')])
        del_bd = ' '.join(inp_split_lst[inp_split_lst.index('birthday')+1:])
        ab[name].delete_birthday(Birthday(birthday=del_bd))


# Main function with all input logic
def main():
    while True:
        ask = input('>>> ')
        inp_split_lst = ask.split(' ')
        commands = ['add_contact', 'delete_contact', 'add_number', 'change_number', 'delete_number', 'add_email', 'change_email', 'delete_email', 'add_birthday', 'change_birthday', 'delete_birthday', 'show', 'show_all', 'close', 'exit']
        command = inp_split_lst[0].lower()
        
        if command == 'hello':
            print("How can I help you?\nInput 'commands' to see all the commands avalible!\nFor more information go to README.md\n")

        elif command == 'commands':
            print('\nCommands avalible:\n')
            for com in commands:
                print(com)
            print('For more information go to README.md\n')

        elif command == 'add_contact':
            add_contact(inp_split_lst)

        elif command == 'delete_contact':
            ab.delete_record(' '.join(inp_split_lst[1:]))

        elif command == 'add_number':
            add_field(inp_split_lst, 'number')

        elif command == 'change_number':
            change_field(inp_split_lst, 'number')

        elif command == 'delete_number':
            delete_field(inp_split_lst, 'number')
        
        elif command == 'add_email':
            add_field(inp_split_lst, 'email')

        elif command == 'change_email':
            change_field(inp_split_lst, 'email')

        elif command == 'delete_email':
            delete_field(inp_split_lst, 'email')

        elif command == 'add_birthday':
            add_field(inp_split_lst, 'birthday')

        elif command == 'change_birthday':
            change_field(inp_split_lst, 'birthday')

        elif command == 'delete_birthday':
            delete_field(inp_split_lst, 'birthday')

        elif command == 'show':
            iter()

        elif command == 'show_all':
            if len(ab) > 0:
                print(ab)
            else:
                print('\nYour address book is empty now!\n')

        elif command in commands[-2:]:
            print('\nGood bye!')
            break

        else:
            print(f"\nUnknown command ({command})\nInput 'commands' to see all the commands avalible!\nFor more information go to README.md\n")


if __name__ == "__main__":
    main()