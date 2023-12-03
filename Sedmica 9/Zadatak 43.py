n = int(input())
lista = []

for i in range(n):
    m = int(input())
    lista.append(m)

dominantni = 0
flag = False

for i in range(len(lista)):
    broj = lista.count(lista[i])
    if broj >= n / 2:
        flag = True
        dominantni = lista[i]

if flag:
    print(f"Dominantni broj je: {dominantni}")
else:
    print("Nema dominantnog broja!")
