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
    elif moduleSelect == "5":
        keypad()
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
    inputSequence = input(
        "Please input the sequence starting from top left and ending in bottom right!\n"
    ).split()

    sequence = []

    for i in range(0, len(inputSequence)):
        sequence.append(int(inputSequence[i]))

    if len(sequence) > 4:
        print("Please input no more and no less than four")
        keypad()
    x = keypadChecker(sequence)
    y = 0
    for i in range(0, len(sequence)):
        y += sequence[i]

    z = x - y
    print(f"The Z for this keypad is: {z}\nThe sequence is:\n")

    if z < 0.5:
        print("1234")
    elif 0.5 <= z < 20:
        print("1243")
    elif 20 <= z < 50:
        print("4321")
    elif 50 <= z < 90:
        print("3142")
    elif z >= 90:
        print("2314")

    input("Press anything to continue")
    casual()


def keypadChecker(keypSeq):
    result = 0
    for i in range(0, len(keypSeq)):
        if i == 0:
            if keypSeq[i] < 10:
                result = 15
            elif 10 <= keypSeq[i] <= 20:
                result = 20
            elif 20 <= keypSeq[i] <= 80:
                result = 30
            else:
                result = 10
            # print(result)
        if i == 1:
            if keypSeq[i] < 10:
                result += 10
            elif 10 <= keypSeq[i] <= 20:
                result *= 2
            elif 20 <= keypSeq[i] <= 80:
                result *= 3
            else:
                result -= 10
            # print(result)

        if i == 2:
            if keypSeq[i] < 10:
                result *= 2
            elif 10 <= keypSeq[i] <= 20:
                result *= 3
            elif 20 <= keypSeq[i] <= 80:
                result -= 5
            else:
                result
            # print(result)
        if i == 3:
            if keypSeq[i] < 10:
                result *= 2
            elif 10 <= keypSeq[i] <= 20:
                result += 20
            elif 20 <= keypSeq[i] <= 80:
                result += 50
            else:
                result *= 3
            # print(result)

    return result

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
