def validna_lozinka(s):
    validna = True
    malo = False
    veliko = False
    cifra = False
    nije_alnum = False
    spejs = False
    if len(s) < 10:
        return not validna
    else:
        for i in range(len(s)):
            if s[i].islower():
                malo = True
            elif s[i].isupper():
                veliko = True
            elif s[i].isnumeric():
                cifra = True
            elif not s[i].isalnum():
                nije_alnum = True
            elif s[i] == " ":
                spejs = True
        if malo and veliko and cifra and nije_alnum and (not spejs):
            return validna
        else:
            return not validna


file = open("Zadatak 57.in", "r")

matrica = []

while True:
    red = file.readline()
    if red == "":
        break
    red = red.rstrip("\n")
    red = red.split()
    matrica.append(red)

file.close()

for i in range(len(matrica)):
    if not validna_lozinka(matrica[i][1]):
        print(matrica[i][0])
