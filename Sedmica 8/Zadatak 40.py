def brojUKolonu(broj):
    kolona = ""
    while broj > 0:
        ostatak = (broj - 1) % 26
        kolona = chr(65 + ostatak) + kolona
        broj = (broj - 1) // 26
    return kolona


n = int(input("Unesite broj kolone: "))
naziv = brojUKolonu(n)
print(f"Broj {n} predstavlja kolonu {naziv} u Excel-u.")
