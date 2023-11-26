import math


def brojNulaUFaktorijelu(n):
    suma = 0
    for i in range(1, n+1):
        suma += math.floor((n/5**i))
    return suma


n = int(input("Unesite broj n: "))

print(brojNulaUFaktorijelu(n))
