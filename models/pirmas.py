c = []
xreiksmes = []
lista = "9|8|7\n6|5|4\n3|2|1\n"


def pirmas():
    x = input("enter number")
    listas = "9|8|7\n6|5|4\n3|2|1\n"
    if x in listas:
        xreiksmes.append(x)
        listas = listas.replace(x, "X")
        print(listas)
        return listas
    elif x not in listas:
        print(listas)
        print("Wrong value")


def antras(listas):
    o = input("enter number")
    if o in listas:
        listas = listas.replace(o, "0")
        print(listas)
        return listas
    elif o not in listas:
        print(listas)
        print("Wrong value")


def trecias(listas):
    x = input("enter number")
    if x in listas:
        xreiksmes.append(x)
        listas = listas.replace(x, "X")
        print(listas)
        return listas
    elif x not in listas:
        print(listas)
        print("Wrong value")


def check_win(listas):
    lines = listas.split('\n')

    # Check rows
    for line in lines:
        if 'XXX' in line:
            return print('X won')
        elif '000' in line:
            return print('0 won')

    # Check columns
    for col in range(len(lines[0])):
        column = ''.join(row[col] for row in lines if col < len(row))
        if 'XXX' in column:
            return print('X won')
        elif '000' in column:
            return print('0 won')

    # Check diagonals
    diagonal1 = ''.join(lines[i][i] for i in range(len(lines)) if i < len(lines[i]))
    diagonal2 = ''.join(lines[i][len(lines) - 1 - i] for i in range(len(lines)) if len(lines[i]) > len(lines) - 1 - i)

    if 'XXX' in diagonal1 or 'XXX' in diagonal2:
        return print('X won')
    elif '000' in diagonal1 or '000' in diagonal2:
        return print('0 won')




