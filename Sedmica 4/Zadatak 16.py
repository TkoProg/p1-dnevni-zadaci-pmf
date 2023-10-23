import random

n = int(input("Unesite prirodan broj: "))

a = int(input("Unesite cijeli broj: "))
b = int(input("Unesite cijeli broj: "))

najm = min(a, b)
najv = max(a, b)
zbir = 0

for i in range(n):
    broj = str(random.randint(najm, najv))
    print(f"{i + 1}. broj je: {broj} ")
    if len(broj) == 1:
        zbir += int(broj)
    else:
        zbir += int(broj[-2])

print(f"{zbir} je zbir svih predzadnjih cifara")
