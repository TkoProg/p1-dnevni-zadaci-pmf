def broj_bodova(m):
    for i in range(len(m)):
        print("Ime studenta: ", matrica[i][0], " ", matrica[i][1], ". Broj osvojenih bodova: ", float(matrica[i][2]) + float(matrica[i][3]) + float(matrica[i][4]), sep='')


n = input()

file = open(f"{n}", "r")

matrica = []

while True:
    red = file.readline()
    if red == "":
        break
    red = red.rstrip("\n")
    red = red.split()
    matrica.append(red)

file.close()

print(matrica)

broj_bodova(matrica)
