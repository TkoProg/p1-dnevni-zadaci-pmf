def fibonaci(x):
    broj = 1
    prethodni = 0
    lista = []
    for i in range(x):
        lista.append(broj)
        broj = prethodni + broj
        prethodni = broj - prethodni
    return lista


n = int(input())
niz = fibonaci(n)
[print(x, end=" ") for x in niz]
