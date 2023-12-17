from models.pirmas import *
olaimejimai = 0
xlaimejimai = 0
while True:
    a = int(input("1 - Žaisti dviems\n2 - Rezultatas\n3 - Baigti\n"))
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
                        if check_draw(antrasejimas):
                            print("Draw")
                            break
                        pirmasejimas = trecias(antrasejimas)
                        if check_win(pirmasejimas):
                            xlaimejimai += 1
                            break
                        if check_draw(pirmasejimas):
                            print("Draw")
                            break
                    except AttributeError:
                        print("Wrong Value")
                        print(listas)
            elif e == 2:
                pirmasejimas = pirmasnuliukai()
                while True:
                    try:
                        antrasejimas = trecias(pirmasejimas)
                        if check_win(antrasejimas):
                            break
                        if check_draw(antrasejimas):
                            print("Draw")
                            break
                        pirmasejimas = antras(antrasejimas)
                        if check_win(pirmasejimas):
                            break
                        if check_draw(antrasejimas):
                            print("Draw")
                            break
                    except AttributeError:
                        print("Wrong value")
                        print(listas)
        case 2:
            print(f"X pergales: {xlaimejimai}\n0 pergales: {olaimejimai}")
        case 3:
            break
