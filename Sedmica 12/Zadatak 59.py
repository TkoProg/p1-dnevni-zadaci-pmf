korisnici = []
prije_korisnici = []

file = open("lozinke.txt", "r")

while True:
    red = file.readline()
    if red == "":
        break
    red = red.rstrip("/n")
    red = red.split()
    prije_korisnici.append(red)

file.close()

while True:
    n = input()
    if n == "":
        break
    if n in prije_korisnici:
        break
    korisnici.append(n)
