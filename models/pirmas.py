c = []
listas = "9|8|7\n6|5|4\n3|2|1\n"


def pirmaskryziukai():
    listas = "9|8|7\n6|5|4\n3|2|1\n"
    print(listas)
    x = input("Enter number: ")
    if x in listas:
        listas = listas.replace(x, "X")
        print(listas)
        return listas
    if x not in listas:
        print(listas)
        print("Wrong value")
        pirmaskryziukai()


def pirmasnuliukai():
    listas = "9|8|7\n6|5|4\n3|2|1\n"
    print(listas)
    x = input("Enter number: ")
    if x in listas:
        listas = listas.replace(x, "0")
        print(listas)
        return listas
    if x not in listas:
        print(listas)
        print("Wrong value")
        pirmasnuliukai()


def antras(listas):
    try:
        o = input("Enter number: ")
        if o in listas:
            listas = listas.replace(o, "0")
            print(listas)
            return listas
    except o not in listas:
        print(listas)
        print("Wrong value")



def trecias(listas):
    x = input("Enter number: ")
    if x in listas:
        listas = listas.replace(x, "X")
        print(listas)
        return listas
    if x not in listas:
        print(listas)
        print("Wrong value")
        trecias(listas)


def check_win(listas):
    lines = listas.split('\n')
    for line in lines:
        if line == "X|X|X":
            print('X won')
            return True
        elif line == "0|0|0":
            print('0 won')
            return True

    for col in range(len(lines[0])):
        column = ''.join(row[col] for row in lines if col < len(row))
        if 'XXX' in column:
            print("X Won")
            return True
        elif '000' in column:
            print("O Won")
            return True

    if listas[0] == "X" and listas[8] == "X" and listas[16] == "X" or listas[4] == "X" and listas[8] == "X" and listas[12] == "X":
        print("X won")
        return True

    if listas[0] == "0" and listas[8] == "0" and listas[16] == "0" or listas[4] == "0" and listas[8] == "0" and listas[12] == "0":
        print("0 won")
        return True

    else:
        print("Draw")
