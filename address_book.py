from collections import UserDict


class Phone():
    def __init__(self, phone):
        self.phone = phone


class Email():
    def __init__(self, email):
        self.email = email


class Name:
    def __init__(self, name):
        self.name = name


class Record:
    def __init__(self, person_name, phone_num=None, email=None):
        self.name = person_name.name
        if phone_num:
            self.phones = []
            self.phones.append(phone_num)

        if email:
            self.emails = []
            self.emails.append(email)

    def add_phone(self, extra_phone):
        try:
            self.phones.append(extra_phone)
        except AttributeError:
            self.phones = []
            self.phones.append(extra_phone)

        print(f'Phone number {extra_phone.phone} has been successfully added!\n')

    def change_phone(self, some_phone, different_phone):
        flag = False
        for ph in self.phones:
            if ph.phone == some_phone.phone:
                self.phones.remove(ph)
                self.phones.append(different_phone)
                print(f'Phone number {some_phone.phone} has been successfully changed to {different_phone.phone}\n')
                flag = True

        if flag == False:
            print(f'There is no such phone as {some_phone.phone}\n')

    def delete_phone(self, some_phone):
        flag = False
        for ph in self.phones:
            if ph.phone == some_phone.phone:
                self.phones.remove(ph)
                flag = True
                print(f'Phone number {some_phone.phone} has been successfully deleted\n')

        if flag == False:
            print(f'There is no such phone as {some_phone.phone}\n')

    def add_email(self, extra_email):
        try:
            self.emails.append(extra_email)
        except AttributeError:
            self.emails = []
            self.emails.append(extra_email)

        print(f'Email {extra_email.email} has been successfully added!\n')

    def change_email(self, some_email, different_email):
        flag = False
        for em in self.emails:
            if em.email == some_email.email:
                self.emails.remove(em)
                self.emails.append(different_email)
                print(f'Email {some_email.email} has been successfully changed to {different_email.email}\n')
                flag = True

        if flag == False:
            print(f'There is no such email as {some_email.email}\n')

    def delete_email(self, some_email):
        flag = False
        for em in self.emails:
            if em.email == some_email.email:
                self.emails.remove(em)
                flag = True
                print(f'Email {some_email.email} has been successfully deleted\n')

        if flag == False:
            print(f'There is no such email as {some_email.email}\n')

    def __str__(self):
        result = f'\nName: {self.name}\n'
        try:
            p = list(x.phone for x in self.phones)
            result += f'Phones: {p}\n'
        except AttributeError:
            pass

        try:
            e = list(x.email for x in self.emails)
            result += f'Emails: {e}\n'

        except AttributeError:
            pass

        return result


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record
        print(f'One contact ({record.name}) has been successfully added!\n')

    def delete_record(self, name_to_delete):
        for username in self.data.keys():
            if username == name_to_delete:
                del self.data[username]
                print(f'Contact ({username}) has been deleted successfully!\n')
                return None
            
        print(f'There is no such contact as {name_to_delete}\n')

    def __str__(self):
        result = ''
        for person_name, rec in self.data.items():
            result += f'\nName: {person_name}\n'
            try:
                p = list(x.phone for x in rec.phones)
                result += f'Phones: {p}\n'
            except AttributeError:
                pass

            try:
                e = list(x.email for x in rec.emails)
                result += f'Emails: {e}\n'

            except AttributeError:
                pass

        return result

ab = AddressBook()


def add_contact(inp_split_lst):
    if 'phone' in inp_split_lst:
        if 'email' in inp_split_lst:
            ab.add_record(Record(Name(' '.join(inp_split_lst[1:inp_split_lst.index('phone')])), Phone(' '.join(inp_split_lst[inp_split_lst.index('phone')+1:inp_split_lst.index('email')])), Email(' '.join(inp_split_lst[inp_split_lst.index('email')+1:]))))
        else:
            ab.add_record(Record(Name(' '.join(inp_split_lst[1:inp_split_lst.index('phone')])), Phone(' '.join(inp_split_lst[inp_split_lst.index('phone')+1:]))))

    else:
        if 'email' in inp_split_lst:
            ab.add_record(Record(Name(' '.join(inp_split_lst[1:inp_split_lst.index('email')])), email=Email(' '.join(inp_split_lst[inp_split_lst.index('email')+1:]))))
        else:
            ab.add_record(Record(Name(' '.join(inp_split_lst[1:]))))


def input_error(function):
    def inner(*args):
        try:
            function(*args)
        except ValueError:
            print('Something is wrong!\nGo to README.md to check the correctness\n')
        except KeyError:
            print('Name is incorrect!\n')
                  
    return inner

@input_error
def add_number(inp_split_lst):
    ab[' '.join(inp_split_lst[1:inp_split_lst.index('phone')])].add_phone(Phone(' '.join(inp_split_lst[inp_split_lst.index('phone')+1:])))

@input_error
def change_number(inp_split_lst):
    ab[' '.join(inp_split_lst[1:inp_split_lst.index('phone')])].change_phone(Phone(' '.join(inp_split_lst[inp_split_lst.index('phone')+1:inp_split_lst.index('to')])), Phone(' '.join(inp_split_lst[inp_split_lst.index('to')+1:])))

@input_error
def delete_number(inp_split_lst):
    ab[' '.join(inp_split_lst[1:inp_split_lst.index('phone')])].delete_phone(Phone(' '.join(inp_split_lst[inp_split_lst.index('phone')+1:])))


@input_error
def add_email(inp_split_lst):
    ab[' '.join(inp_split_lst[1:inp_split_lst.index('email')])].add_email(Email(' '.join(inp_split_lst[inp_split_lst.index('email')+1:])))

@input_error
def change_email(inp_split_lst):
    ab[' '.join(inp_split_lst[1:inp_split_lst.index('email')])].change_email(Email(' '.join(inp_split_lst[inp_split_lst.index('email')+1:inp_split_lst.index('to')])), Email(' '.join(inp_split_lst[inp_split_lst.index('to')+1:])))

@input_error
def delete_email(inp_split_lst):
    ab[' '.join(inp_split_lst[1:inp_split_lst.index('email')])].delete_email(Email(' '.join(inp_split_lst[inp_split_lst.index('email')+1:])))



def main():
    while True:
        ask = input('>>> ')
        inp_split_lst = ask.split(' ')
        commands = ['add_contact', 'delete_contact', 'add_number', 'change_number', 'delete_number', 'add_email', 'change_email', 'delete_email', 'show_all', 'close', 'exit']
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
            add_number(inp_split_lst)

        elif command == 'change_number':
            change_number(inp_split_lst)

        elif command == 'delete_number':
            delete_number(inp_split_lst)
        
        elif command == 'add_email':
            add_email(inp_split_lst)

        elif command == 'change_email':
            change_email(inp_split_lst)

        elif command == 'delete_email':
            delete_email(inp_split_lst)

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