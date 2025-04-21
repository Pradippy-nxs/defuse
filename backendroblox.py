import dataroblox as dat


def starter():
    print(f"\nHello, {dat.userName}!")
    moduleSelector()


def login():
    print("Please, enter your name: ")
    dat.init()
    print("Please, enter your password: ")
    dat.password()
    loginSuccess()


def loginSuccess():
    dat.passwordCheck()
    if dat.user == True:
        print(f"\nWelcome to the Roblox Defusal Solver!")
        starter()
    else:
        print("who r u gang?")


def logout():
    # print("jalan kok")
    print(f"Goodbye, {dat.userName}\n!")
    del (dat.userName, dat.userPass)
    login()


def moduleSelector():
    print("\nPlease choose your Module!\n1. Casual\nL. Log out")
    module = str(input())
    if module == "1":
        casual()
    elif module == "m" and "M":
        starter()
        # print("tololll")
    if module == "l" and "L":
        logout()
    else:
        print("We're working on that, sorry for the inconvenience!")


def casual():
    print(
        "\nWelcome to the casual module solver!\nPlease select your module of choice.\n1. Wires\n2. Buttons\n3. Hexadecimal\n4. Tiles\n5. Keypad\n6. Binary\n7. Mathematics\n8. Color Code\n9. Multi Buttons\n10. Timing\n11. Morse Code\n12. Echo\n13. Counting\n14. Interview\n0. Back"
    )
    moduleSelect = str(input())
    if moduleSelect == "1":
        wires()
    elif moduleSelect == "0":
        moduleSelector()
    else:
        print("We're working on that, sorry for the inconvenience!")


def wires():
    print("Wires")


def buttons():
    print("Buttons")


def hexadecimal():
    print("Hexadecimal")


def tiles():
    print("tiles")


def keypad():
    print("keypad")


def binary():
    print("binary")


def mathematics():
    print("Mathematics")


def colorCode():
    print("colorCode")


def multiButtons():
    print("multiButtons")


def timing():
    print("timing")


def morseCode():
    print("morseCode")


def echo():
    print("echo")


def counting():
    print("counting")


def interview():
    print("interview")
