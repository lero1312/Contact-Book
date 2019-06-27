import user
import contact


def addNewContactMain():
    newCon = contact.Contact()
    newCon.name = input("name : ")
    newCon.phone = input("phone : ")
    newCon.address = input("address : ")
    newCon.email = input("email : ")
    contact.addNewContact(newCon, username)


print("welcome to CONTACT BOOK")
choice = input("to login enter 1 / to register enter 2\n")
username = input("username : \n")
if choice == '1':
    while not user.login(username, input("pass : \n")): pass
else:
    while not user.reg(username, input("pass : \n")): pass

s = int(input("1 for add new contact / 2 for search for contact"))
if s == 1:
    addNewContactMain()
else:
    contact.showAllContacts(username)
