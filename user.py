from dataBase import *

def check(username):
    user = userCol.find_one({"username": username})
    if user:
        return True
    return False


def reg(username, password):
    if check(username):
        print("the user is already exist")
        return False
    userCol.insert_one({USER_username: username, USER_password: password})
    return True

def login(username, password):
    if not check(username):
        print("no such user founded")
        return False
    user = userCol.find_one({USER_username: username, USER_password: password})
    if not user:
        print("wrong password")
        return False
    return True
