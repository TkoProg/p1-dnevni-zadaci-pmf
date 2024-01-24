file = open("Zadatak 63.in", "r")

lista = []

while True:
    red = file.readline()
    if red == "":
        break
    red = red.rstrip("\n")
    lista.append(red)

file.close()

brojac = 0

nadjeno = False

for i in range(len(lista)):
    for j in range(brojac, len(lista)):
        if abs(float(lista[i]) - float(lista[j])) == 2:
            nadjeno = True
    brojac += 1
    if nadjeno:
        break

if nadjeno:
    print("DA")
else:
    print("NE")

# Mrsko mi bilo pisati funkciju ali eto kako se radi, lahko je implementirati u funkciju
