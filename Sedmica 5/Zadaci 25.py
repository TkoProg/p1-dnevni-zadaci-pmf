def prost(x):
    for j in range(2, x // 2 + 1):
        if x % j == 0:
            return False
    return True


n = int(input("Unesite prost broj: "))

svi = True

for i in range(len(str(n))):
    broj = str(n)[i:]
    if prost(int(broj)):
        continue
    else:
        svi = False

if svi:
    print("Jesu")
else:
    print("Nisu")
