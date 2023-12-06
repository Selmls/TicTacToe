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


def ketvirtas(listas):
    o = input("enter number")
    if o in listas:
        listas = listas.replace(o, "0")
        print(listas)
        return listas
    elif o not in listas:
        print(listas)
        print("Wrong value")


def penktas(listas):
    x = input("enter number")
    if x in listas:
        xreiksmes.append(x)
        listas = listas.replace(x, "X")
        print(listas)
        return listas
    elif x not in listas:
        print(listas)
        print("Wrong value")



