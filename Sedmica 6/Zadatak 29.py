suma = 0
brojac = 0

while True:
    n = input(f"Brojac {brojac+1}. broj: ")
    if n[0] == "3":
        suma += int(n)
        break
    else:
        brojac += 1
        if brojac == 2:
            suma += int(n)

print(f"Suma drugog i posljednjeg broja je: {suma}")
