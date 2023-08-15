# **commands availible:**

['add_contact', 'delete_contact', 'clear_addressbook', 'add_phone', 'change_phone', 'delete_phone', 'add_email', 'change_email', 'delete_email', 'add_birthday', 'change_birthday', 'delete_birthday', 'birthday_within', "add_address", "change_address", "delete_address", 'find', 'show', 'show_all', 'close', 'exit']
# **Operations with contacts:**
# add_contact

add_contact *username* phone *userphone* email *useremail*

*username* is always required, but *userphone* and *useremail*are not
Words phone and email before corresponding data are always required

## examples(add_contact):
	add_contact Sasha Cheburatenko phone +380661111111 email chebusania@gmail.com birthday 10 07 2006 address street Shevchenka building 17 apartment 92
	
    add_contact Sasha Cheburatenko phone +380661111111 email chebusania@gmail.com

    add_contact Sasha Cheburatenko phone +380661111111

    add_contact Sasha Cheburatenko email chebusania@gmail.com
    
    add_contact Sasha Cheburatenko birthday 10 07 2006
    
    add_contact Sasha Cheburatenko

# delete_contact
delete_contact *username*

## example(delete_contact):

    delete_contact Sasha Cheburatenko

# **Operations with phone numbers:**

# add_phone
add_phone *username* phone *another_userphone*

The word phone is required for code to know when the phone number starts

## Example(add_phone):

    add_phone Sasha Cheburatenko phone +380661111112

# change_phone

change_phone *username* phone *some_userphone* to *another_userphone*

Words phone and to are required for code to know the borders of phone numbers

## Example(change_phone):

    change_phone Sasha Cheburatenko phone +380661111112 to +380661111113

# delete_phone
delete_phone *username* phone *some_userphone*

## Example(change_phone):

    delete_phone Sasha Cheburatenko phone +380661111113
# **Operations with emails:**
Work just the same way as operations with phone numbers

## Examples(operations with emails):

    add_email Sasha Cheburatenko email chebusania2@gmail.com
    change_email Sasha Cheburatenko email chebusania2@gmail.com to chebusania3@gmail.com
    delete_email Sasha Cheburatenko email chebusania3@gmail.com

# **Operations with birthday:**
Work just the same way as operations with phone numbers and emails

# **Operations with addresses:**
Work just the same way as operations with phone numbers, etc.
The word street is required for addresses. Building and apartment are optional

# **find**
    find *any info*

# **clear_addressbook**
Removes all the data from your addressbook after you confirm it

# **show**
Displays all information about contacts, dividing it into pages of 2 contacts
## next
Turns the page

# **show_all**
Displays all the information about contacts

# **close and exit**
Simply stop the work of the program
Work in the same way both