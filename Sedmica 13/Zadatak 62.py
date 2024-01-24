n = input()
m = input()

najmanji = str(min(int(n), int(m)))
najveci = str(max(int(n), int(m)))

broj_nula = len(najveci) - len(najmanji)
najmanji = "0"*broj_nula + najmanji

brojac = 0
broj = ""

for i in range(len(najmanji)-1, -1, -1):
    zbir = str(int(najmanji[i]) + int(najveci[i]))
    cifra = zbir[-1]
    broj += cifra

print(broj[::-1])
