n = input()
m = int(input())
k = int(input())

zbir = 0

for i in range(k):
    zbir += int(n[i])

for i in range(-1, -m-1, -1):
    zbir += int(n[i])

print(zbir)

# Ponovo mi je bilo mrsko napisati funkciju lol
