charstr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input("Unesite broj n: "))

s = 0

for i in range(n):
    if s == 26:
        s = 0
    if i == 0:
        for j in range(n):
            print(f"{charstr[s]} ", end="")
    else:
        for k in range(i):
            print("  ", end="")
        for k in range(n-i):
            print(f"{charstr[s]} ", end="")
    s += 1
    print()
