n = int(input("Unesite broj n. Program ispisuje matricu velicine n x n: "))

rezervisano = len(str(n * n))

for i in range(1, n + 1):
    if i % 2 == 0:
        for k in range(1, n + 1):
            print(f"{((i * n) + 1) - k:>{rezervisano + 1}}", end="")
    else:
        for j in range(1, n + 1):
            print(f"{((i * n) - n) + j:>{rezervisano + 1}}", end="")
    print()
