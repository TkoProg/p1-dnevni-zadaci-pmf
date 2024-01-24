n = int(input())

lista = [n]

while True:
    n = input()
    if n == "":
        break
    lista.append(int(n))

print(lista[2]*lista[-2])
