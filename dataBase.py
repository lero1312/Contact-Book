import pymongo

host = 'localhost'
port = 27017

clint =pymongo.MongoClient(host, port)
db = clint["ContactBook"]
userCol = db["users"]
contactCol = db["contact"]

# users vars
USER_username = "username"
USER_password = "password"

# contact vars
CONTACT_name = "name"
CONTACT_phone = "phone"
CONTACT_address = "address"
CONTACT_email = "email"
CONTACT_username = 'username'