import random

matrica = []

n = int(input("Unesite prirodan broj: "))

for i in range(n):
    red = []
    for j in range(n):
        broj = f"{str(random.randint(1, n ** 2)):>{len(str(n**2))}}"
        red.append(broj)
    matrica.append(red)

for i in range(n):
    for j in range(n):
        print(matrica[i][j], end=" ")
    print()
