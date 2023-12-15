from models.pirmas import *
olaimejimai = 0
xlaimejimai = 0
while True:
    a = int(input("1 - Žaisti dviems\n2 - Rezultatas\n3 - Žaisti prieš kompiuterį\n4 - Baigti\n"))
    if a == 1:
        e = int(input("1 - pradėti kryžiukais\n2 - pradėti nuliukais\n"))
    else:
        e = 0
    match a:
        case 1:
            if e == 1:
                pirmasejimas = pirmaskryziukai()
                while True:
                    try:
                        antrasejimas = antras(pirmasejimas)
                        if check_win(antrasejimas):
                            olaimejimai += 1
                            break
                        pirmasejimas = trecias(antrasejimas)
                        if check_win(pirmasejimas):
                            xlaimejimai += 1
                            break
                    except AttributeError:
                        print("Wrong Value")
                        print(listas)
            elif e == 2:
                pirmasejimas = pirmasnuliukai()
                while True:
                    antrasejimas = trecias(pirmasejimas)
                    if check_win(antrasejimas):
                        break
                    pirmasejimas = antras(antrasejimas)
                    if check_win(pirmasejimas):
                        break
        case 2:
            print(f"X pergales: {xlaimejimai}\n0 pergales: {olaimejimai}")
        case 3:
            ...
        case 4:
            break
