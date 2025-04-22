passer = open("password.txt", "r")
passVar = passer.read()


def init():
    global userName
    userName = str(input())


def password():
    global userPass
    userPass = str(input())


def passwordCheck():
    global user
    user = None
    if userPass == passVar:
        user = True
        return user
    else:
        user = False
        return user
