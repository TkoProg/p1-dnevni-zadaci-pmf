suma = 0
brojac = 0

while True:
    n = input(f"Unesite {brojac+1}. broj: ")
    if n[0] == "3":
        break
    else:
        brojac += 1
        if brojac == 2:
            suma += int(n)

print(f"Suma drugog i posljednjeg broja je: {suma+int(n)}")
