from collections import deque
n = int(input())

lista = []

for i in range(n):
    neka = []
    for j in range(n):
        m = int(input())
        neka.append(m)
    lista.append(neka)

nova = []

for i in range(n):
    for j in range(n):
        nova.append(lista[i][j])

k = int(input())

nova = deque(nova)
nova.rotate(k)
nova = list(nova)

zadnja = []
opa = []
m = 0

for i in range(n):
    opa = []
    for j in range(n):
        opa.append(nova[m])
        m += 1
    zadnja.append(opa)

print(zadnja)
