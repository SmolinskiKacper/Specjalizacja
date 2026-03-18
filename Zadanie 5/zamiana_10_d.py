def zmiana_sys(liczba,system):
    wynik = ""

    while liczba !=0:
        reszta = liczba % system
        liczba = liczba // system
        match reszta:
            case 10:
                reszta = "A"
            case 11:
                reszta = "B"
            case 12:
                reszta = "C"
            case 13:
                reszta = "D"
            case 14:
                reszta = "E"
            case 15:
                reszta = "F"
            case 16:
                reszta = "G"
            case 17:
                reszta = "H"
            case 18:
                reszta = "I"
            case 19:
                reszta = "J"
            case 20:
                reszta = "K"


        wynik += str(reszta)

    return wynik[::-1]

print(zmiana_sys(15325320,3))