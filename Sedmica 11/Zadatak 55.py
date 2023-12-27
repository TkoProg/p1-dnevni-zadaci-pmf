def matematicke_operacije(izraz):
    while True:
        if izraz.isnumeric():
            return izraz
        if "*" in izraz:
            operacija = izraz.find("*")
            oblik = izraz[operacija - 1] + "*" + izraz[operacija + 1]
            proizvod = str(int(izraz[operacija - 1]) * int(izraz[operacija + 1]))
            izraz = izraz.replace(oblik, proizvod)
            print(izraz, oblik, proizvod)
        if "/" in izraz:
            operacija = izraz.find("/")
            oblik = izraz[operacija - 1] + "/" + izraz[operacija + 1]
            kolicnik = str(int(izraz[operacija - 1]) / int(izraz[operacija + 1]))
            izraz = izraz.replace(oblik, kolicnik)
            print(izraz, oblik, kolicnik)
        if "+" in izraz:
            operacija = izraz.find("+")
            oblik = izraz[operacija - 1] + "+" + izraz[operacija + 1]
            zbir = str(int(izraz[operacija - 1]) + int(izraz[operacija + 1]))
            izraz = izraz.replace(oblik, zbir)
            print(izraz, oblik, zbir)
        if "-" in izraz:
            operacija = izraz.find("-")
            oblik = izraz[operacija - 1] + "-" + izraz[operacija + 1]
            razlika = str(int(izraz[operacija - 1]) / int(izraz[operacija + 1]))
            izraz = izraz.replace(oblik, razlika)
            print(izraz, oblik, razlika)


print(matematicke_operacije("3+4*5"))
