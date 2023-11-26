def neNalaziSe(n):
    n = str(n)
    brojevi = []
    for i in range(0, 10):
        if str(i) in n:
            continue
        else:
            brojevi.append(i)
    return brojevi


def sumaBrojeva(brojevi):
    suma = 0
    for i in range(len(brojevi)):
        suma += brojevi[i]
    return suma


n = int(input())

brojevi = neNalaziSe(n)

print(sumaBrojeva(brojevi))
