from address_book_classes import Birthday, Phone, Email, Name, Record, ab, abi, error_keeper 


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


# Field operations
@error_keeper
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

@error_keeper
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

@error_keeper
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
    
def find_func(inp_split_lst):
    inp = ' '.join(inp_split_lst[1:]).strip()
    ab.find_contact(inp)


# Main function with all input logic
def main():
    while True:
        ask = input('>>> ')
        inp_split_lst = ask.split(' ')
        commands = ['add_contact', 'delete_contact', 'add_number', 'change_number', 'delete_number', 'add_email', 'change_email', 'delete_email', 'add_birthday', 'change_birthday', 'delete_birthday', 'find', 'show', 'show_all', 'close', 'exit']
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

        elif command == 'find':
            find_func(inp_split_lst)

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