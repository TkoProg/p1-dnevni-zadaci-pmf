n = int(input("Unesite dimenzije kvadrata: "))
a = int(input("Unesite broj reda: "))
b = int(input("Unesite broj kolone: "))
m = int(input("Unesite dimenzije unutrasnjeg kvadrata: "))

matrica = []
brojaca = 0
brojacb = 0
brojacm = 0

for i in range(n):
    red = []
    for j in range(n):
        red.append("-")
    matrica.append(red)

for i in range(a-1, m+a-1):
    for j in range(b-1, m+b-1):
        matrica[i][j] = " "

for i in range(len(matrica)):
    for j in range(len(matrica[i])):
        print(matrica[i][j], end=" ")
    print()
