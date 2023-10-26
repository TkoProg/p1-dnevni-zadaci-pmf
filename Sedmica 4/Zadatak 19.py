n = int(input("Unesite prirodan broj n: "))

print()

print("Kvadrat:")
for i in range(n):
    for j in range(n):
        if i != 0 and i != n - 1:
            if j == 0 or j == n - 1:
                print("* ", end="")
            else:
                print("  ", end="")
        else:
            print("* ", end="")
    print()

print("-------------------------------")
print("Piramida:")

mjesta = 0
for i in range(n):
    for j in range(n):
        if i == 0:
            print("* ", end="")
    if 0 < i < n:
        print(" " * i, end="")
        print("*", end="")
        if 0 < i < n - 1:
            print(" " * ((n * 2) - (4 + mjesta + i)), end="")
            mjesta += 1
            print("*", end="")
    print()

print("-------------------------------")
print("Baklava:")

mjesta2 = 1
for i in range(n):
    if i == 0:
        print(" " * (n - 1), end="")
        print("*", end="")
    if i > 0:
        print(" " * (n - 1 - mjesta2), end="")
        print("*", end="")
        print(" " * (i + mjesta2 - 1), end="")
        print("*", end="")
        mjesta2 += 1
    print()

mjesta3 = 0
for i in range(n):
    print(" "*i, end="")
    print("*", end="")
    if i == n - 1:
        break
    print(" " * ((n*2)-(3+mjesta3+i)), end="")
    print("*", end="")
    mjesta3 += 1
    print()
