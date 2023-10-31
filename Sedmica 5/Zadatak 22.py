n = int(input("Unesite broj n: "))

brojac = 0
exp = 1
mjesta = 1
cudan = ""

while True:
    for i in range(2**exp):
        cudan = f'{i:0{mjesta}b}'
        brojac += 1
        if brojac == n:
            break
    if brojac == n:
        break
    mjesta += 1
    exp += 1

cudan = cudan.replace("0", "2")
cudan = cudan.replace("1", "3")

print(f"Vas n-ti cudan broj je: {cudan}")
