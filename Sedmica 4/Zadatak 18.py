n = input("Unesite prirodan broj n: ")
broj = int(n)
n.split()

brojac = 0

while True:
    n = [int(x) for x in n]
    n = sorted(n)
    broj = broj - n[-1]
    brojac += 1
    if broj == 0:
        break
    else:
        n = str(broj)
        n.split()

print(f"Broj potrebnih poteza je: {brojac}")
