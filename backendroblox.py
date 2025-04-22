import dataroblox as dat


def starter():
    print(f"\nHello, {dat.userName}!")
    moduleSelector()


def login():
    print("\nPlease, enter your name: ")
    dat.init()
    print("\nPlease, enter your password: ")
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
    print("\nPlease choose your Module!\n1. Casual\nL. Log out\n0. Exit\n")
    module = str(input()).lower()
    if module == "1":
        casual()
    if module == "0":
        print("\nThank you for using this app!")
        exit()
    elif module == "m":
        starter()
        # print("tololll")
    if module == "l":
        logout()
    else:
        print("We're working on that, sorry for the inconvenience!")
        moduleSelector()


def casual():
    print(
        "\nWelcome to the casual module solver!\nPlease select your module of choice.\n1. Wires\n2. Buttons\n3. Hexadecimal\n4. Tiles\n5. Keypad\n6. Binary\n7. Mathematics\n8. Color Code\n9. Multi Buttons\n10. Timing\n11. Morse Code\n12. Echo\n13. Counting\n14. Interview\n0. Back"
    )
    moduleSelect = str(input())
    if moduleSelect == "1":
        wires()
    elif moduleSelect == "0":
        moduleSelector()
    elif moduleSelect == "3":
        hexadecimal()
    elif moduleSelect == "4":
        tiles()
    else:
        print("We're working on that, sorry for the inconvenience!")
        casual()


def wires():
    print("Wires")


def buttons():
    print("Buttons")


def hexadecimal():
    sequence = str(input("Please input the hexadecimal sequence!\n")).lower().split()
    solvedSequence = ""
    for i in range(0, len(sequence)):
        solvedSequence += hexadecimalCheck(sequence[i])
    print(f"Solved sequence: {solvedSequence}\n")
    input("Press anything to continue")
    casual()


def hexadecimalCheck(hex: str):
    return chr(int(hex, 16))


def tiles():
    pair = str(input("Please input the color pair!\n")).lower().split()
    numResult = 0
    for i in range(0, len(pair)):
        numResult += tilesChecker(pair[i])
    print(f"Solved pair: {numResult}\n")
    input("Press anything to continue")
    casual()


def tilesChecker(color):
    if color == "r" and "red":
        return 1
    if color == "y" and "yellow":
        return 2
    if color == "g" and "green":
        return 9
    if color == "b" and "blue":
        return 7
    if color == "p" and "pink":
        return 6
    if color == "w" and "white":
        return 5


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
