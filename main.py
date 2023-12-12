from models.pirmas import pirmas, lista, antras, trecias, check_win
while True:
    try:
        a = int(input("1 - Žaisti dviems\n2 - Pakaroti žaidimą\n3 - Žaisti prieš kompiuterį\n4 - Baigti\n"))
    except ValueError:
        print("Nėra tokio pasirinkimo")
    match a:
        case 1:
            print(lista)
            b = pirmas()
            while True:
                c = antras(b)
                b = trecias(c)
                if check_win(b) or check_win(c):
                    break
        case 2:
            ...
        case 3:
            ...
        case 4:
            ...


