import math

n = int(input())

lista = []

# lista = [14,5,3,45,43,9,11]
nova = []
bez = []
indeksi = []

for i in range(n):
    m = int(input())
    lista.append(m)

prime = True

for i in range(len(lista)):
    prime = True
    broj = lista[i]
    for j in range(2, math.ceil(math.sqrt(broj)) + 1):
        if broj % j == 0:
            prime = False
    if not prime:
        indeksi.append(i)
        bez.append(broj)
        continue
    else:
        nova.append(broj)

nova.sort()

j = 0
zadnja = []

for i in range(len(lista)):
    if lista[i] in nova:
        zadnja.append(nova[j])
        j += 1
    else:
        zadnja.append(lista[i])

print(zadnja)
