def posjeceni_gradovi(rute):
    posjeceni = []
    c = 0
    for i in range(len(rute)):
        if i == 0:
            lokacija = rute[0][0]
        elif i != 0:
            lokacija = rute[i][0]
        posjeceni.append(lokacija)
        while True:
            destinacija = rute[c][1]
            if destinacija == rute[c][1]:
                print("ok")



posjeceni_gradovi([["Sarajevo", "Mostar"], ["Tuzla", "Zenica"],
                   ["Mostar", "Konjic"], ["Zenica", "Banja Luka"],
                   ["Konjic", "Tuzla"], ["Zavidovici", "Sarajevo"]])
