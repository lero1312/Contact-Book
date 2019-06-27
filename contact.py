from dataBase import *

class Contact:
    name = ''
    phone = ''
    address = ''
    email = ''


def check(name):
    contact = contactCol.find_one({CONTACT_name: name})
    if contact:
        return True
    return False


def addNewContact(contact, username):
    if check(contact.name):
        print("this name is already exist")
        return False
    contactCol.insert_one({CONTACT_name: contact.name, CONTACT_phone: contact.phone,
                           CONTACT_address: contact.address, CONTACT_email: contact.email,
                           CONTACT_username: username})


def getAllContact(username):
    return contactCol.find({CONTACT_username: username})

def showAllContacts(username):
    listOfContacts = list(getAllContact(username))
    for ind, x in enumerate(listOfContacts):
        print(str(ind) + ' ' + x["name"])
    indx = -1
    while not (0 <= indx < len(listOfContacts)):
        indx = int(input("enter the number : "))
    print('name : ' + listOfContacts[indx]["name"])
    print('phone : ' + listOfContacts[indx]["phone"])
    print('addr : ' + listOfContacts[indx]["address"])
    print('mail : ' + listOfContacts[indx]["email"])