import random

lista = []

while True:
    n = int(input())
    if n == 0:
        break
    lista.append(n)

k = int(input("Unesite broj: "))

pojavio_se = []

for i in range(k):
    broj = random.randint(0, len(lista) - 1)
    if broj in pojavio_se:
        continue
    else:
        pojavio_se.append(broj)
        print(lista[broj])
