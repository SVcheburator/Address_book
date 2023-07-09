# **commands availible:**

['add_contact', 'delete_contact', 'add_number', 'change_number', 'delete_number', 'add_email', 'change_email', 'delete_email', 'show_all', 'close', 'exit']
# **Operations with contacts:**
# add_contact

add_contact *username* phone *userphone* email *useremail*

*username* is always required, but *userphone* and *useremail*are not
Words phone and email before corresponding data are always required

## examples(add_contact):

    add_contact Sasha Cheburatenko phone +380661111111 email chebusania@gmail.com

    add_contact Sasha Cheburatenko phone +380661111111

    add_contact Sasha Cheburatenko email chebusania@gmail.com
    
    add_contact Sasha Cheburatenko

# delete_contact
delete_contact *username*

## example(delete_contact):

    delete_contact Sasha Cheburatenko

# **Operations with phone numbers:**

# add_number
add_number *username* phone *another_userphone*

The word phone is required for code to know when the phone number starts

## Example(add_number):

    add_number Sasha Cheburatenko phone +380661111112

# change_number

change_number *username* phone *some_userphone* to *another_userphone*

Words phone and to are required for code to know the borders of phone numbers

## Example(change_number):

    change_number Sasha Cheburatenko phone +380661111112 to +380661111113

# delete_number
delete_number *username* phone *some_userphone*

## Example(change_number):

    delete_number Sasha Cheburatenko phone +380661111113
# **Operations with emails:**
Work just the same way as operations with phone numbers

## Examples(operations with emails):

    add_email Sasha Cheburatenko email chebusania2@gmail.com
    change_email Sasha Cheburatenko email chebusania2@gmail.com to chebusania3@gmail.com
    delete_email Sasha Cheburatenko email chebusania3@gmail.com
# **show_all**
Displays all the information about contacts

# **close and exit**
Simply stop the work of the program
Work in the same way both

